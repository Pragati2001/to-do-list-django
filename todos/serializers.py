# serializers.py
from rest_framework import serializers
from .models import TaskList

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = ['name', 'desc', 'completionStatus', 'deadline']

# from rest_framework import serializers
# from .models import Todo

# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['id', 'title', 'description', 'status']