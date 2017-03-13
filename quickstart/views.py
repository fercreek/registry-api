from django.shortcuts import render
from rest_framework import viewsets
from quickstart.models import Record
from quickstart.serializers import RecordSerializer

class RecordViewSet(viewsets.ModelViewSet):
	queryset = Record.objects.all()
	serializer_class = RecordSerializer