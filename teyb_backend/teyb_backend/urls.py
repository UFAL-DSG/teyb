from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers

from teyb_service.models import (
    Task,
    Team
)
from teyb_service.serializers import TaskSerializer

from django.contrib import admin
admin.autodiscover()


class TeamViewSet(viewsets.ModelViewSet):
    model = Team


class TaskViewSet(viewsets.ModelViewSet):
    model = Task
    serializer_class = TaskSerializer


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teyb_backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^register', 'teyb_service.views.register_team'),
    url(r'^create_task', 'teyb_service.views.create_task'),
    url(r'^hookup_simulator', 'teyb_service.views.hookup_simulator'),
)
