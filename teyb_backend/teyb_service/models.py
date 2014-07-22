from django.db import models




class Team(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    key = models.TextField()


class Task(models.Model):
    team = models.ForeignKey(Team)
    name = models.CharField(max_length=200)
    description = models.TextField()


class Simulator(models.Model):
    task = models.ForeignKey(Task)
    team = models.ForeignKey(Team)
    name = models.TextField()
    url = models.TextField()


class Dialog(models.Model):
    dialog_key = models.TextField()
    dialog_key2 = models.TextField()
    task = models.ForeignKey(Task)
    team = models.ForeignKey(Team)
    system_id = models.CharField(max_length=1000)


class Turn(models.Model):
    request = models.TextField()
    reply = models.TextField()
    dialog = models.ForeignKey(Dialog)
    success = models.BooleanField()
