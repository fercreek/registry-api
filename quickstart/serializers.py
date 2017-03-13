from rest_framework import serializers
from quickstart.models import Record

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        exclude = ()