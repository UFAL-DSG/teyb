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