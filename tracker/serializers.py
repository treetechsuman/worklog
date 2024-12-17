from rest_framework import serializers
from .models import Project, TimeEntry

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at', 'user']

class TimeEntrySerializer(serializers.ModelSerializer):
    #duration = serializers.ReadOnlyField(source='duration')  # Add calculated field

    class Meta:
        model = TimeEntry
        fields = ['id', 'user', 'project', 'date', 'start_time', 'end_time']