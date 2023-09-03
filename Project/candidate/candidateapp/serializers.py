from django.db.models import fields
from rest_framework import serializers
from .models import *
from rest_framework import status


class CandidatedirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatedirectory
        fields = '__all__'

