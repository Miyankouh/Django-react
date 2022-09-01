from dataclasses import fields
from xml.parsers.expat import model
from .models import Notes
from rest_framework import serializers


class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
    