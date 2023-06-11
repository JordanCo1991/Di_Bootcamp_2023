from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = ('first_name', 'last_name', 'email', 'date_joined')