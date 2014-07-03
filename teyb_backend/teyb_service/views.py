import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import (
    Simulator,
    Task,
    Team
)
from serializers import TeamSerializer


# Create your views here.
def json_response(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


@api_view(['POST'])
def register_team(request):
    serialized = TeamSerializer(data=request.DATA)

    team = Team()
    team.name = serialized.init_data['name']
    team.email = serialized.init_data['email']
    team.key = "something"
    team.save()

    return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)


@csrf_exempt
def create_task(request):
    if request.method == "POST":
        try:
            team = Team.objects.get(key=request.POST["key"])
        except Exception, e:
            return json_response({'status': 0, 'error': "Unknown API key, please check it again."})

        try:
            task = Task()
            task.team = team
            task.name = request.POST["name"]
            task.description = request.POST["description"]
            task.save()

            return json_response({'status': 1})
        except Exception, e:
            print e
            return json_response({'status': 0, 'error': "Unknown error."})


@csrf_exempt
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