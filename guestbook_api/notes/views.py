from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes
from .serializers import NotesSerializers


class NotesViewset(viewsets.ModelViewSet):
    serializer_class = NotesSerializers
    queryset = Notes.objects.all()