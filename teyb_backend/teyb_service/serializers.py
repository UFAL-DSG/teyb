from rest_framework import serializers

from models import (Task, Team)


class TaskSerializer(serializers.ModelSerializer):
    simulators = serializers.SerializerMethodField('get_simulators')

    def get_simulators(self, obj):
        return obj.simulator_set.count()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'simulators')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team