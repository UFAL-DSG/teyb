import json
import logging
import random
import string

import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

import requests

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import (
    Dialog,
    Simulator,
    Task,
    Team,
    Turn,
)
from serializers import TeamSerializer


# Create your views here.
def json_response(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


def index(request):
    return redirect('/static/index.html')


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@api_view(['POST'])
def register_team(request):
    serialized = TeamSerializer(data=request.DATA)

    team = Team()
    team.name = serialized.init_data['name']
    team.email = serialized.init_data['email']
    team.key = "something"
    team.save()

    return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)


def create_task(request):
    if request.method == "POST":
        try:
            team = Team.objects.get(key=request.POST["key"])
        except Team.DoesNotExist:
            return json_response({'status': 0, 'error': "Unknown API key, please check it again."})
        except Exception, e:
            logging.exception(e)
            return json_response({'status': 0, 'error': "Unknown error. Please contact the tech support."})

        try:
            task = Task()
            task.team = team
            task.name = request.POST["name"]
            task.description = request.POST["description"]
            task.save()

            return json_response({'status': 1})
        except Exception, e:
            logging.exception(e)
            return json_response({'status': 0, 'error': "Unknown error. Please contact the tech support."})


def hookup_simulator(request):
    if request.method == "POST":
        try:
            team = Team.objects.get(key=request.POST["key"])
        except Exception, e:
            return json_response({'status': 0, 'error': "Unknown API key, please check it again."})

        try:
            task = Task.objects.get(id=request.POST["task_id"])
        except Exception, e:
            return json_response({'status': 0, 'error': "Unknown task. Please try later."})

        try:
            sim = Simulator()
            sim.task = task
            sim.team = team
            sim.name = request.POST["name"]
            sim.url = request.POST["url"]
            sim.save()

            return json_response({'status': 1})
        except Exception, e:
            print e
            return json_response({'status': 0, 'error': "Unknown error."})

@csrf_exempt
def run(request):
    dialog_key = request.POST.get("dialog_key", None)
    if dialog_key is None:
        task_id = request.POST.get("task_id", None)  # If dialog key is None.

        # Check API key.
        try:
            team = Team.objects.get(key=request.POST["key"])
        except Exception, e:
            return json_response({'status': 0, 'error': "Unknown API key, please check it again."})

        # Initialize the dialog.
        dlg = Dialog()
        dlg.task_id = task_id
        dlg.team = team
        dlg.dialog_key = id_generator(16)
        dlg.dialog_key2 = id_generator(16)
        dlg.system_id = request.POST.get("system_id", None)
        dlg.save()
    else:
        dlg = Dialog.objects.get(dialog_key=dialog_key)

    # Get random simulator of the task.
    sim = random.choice(list(dlg.task.simulator_set.all()))

    # Make the request.
    data = {
        'data': request.POST.get("data", None),
        'dialog_key': dlg.dialog_key2
    }

    try:
        resp = requests.post(url=sim.url, data=json.dumps(data))
        print resp.text
        resp_data = resp.json()
        resp_text = resp_data['data']
        success = True
    except Exception, e:
        resp_text = e
        success = False

    turn = Turn()
    turn.request = data
    turn.reply = resp_text
    turn.dialog = dlg
    turn.success = success
    turn.save()

    if success:
        return json_response({'status': 1, 'data': resp_text, 'dialog_key': dlg.dialog_key})
    else:
        return json_response({'status': 0, 'data': str(e)})
