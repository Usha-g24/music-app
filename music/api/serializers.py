from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'votes_to_skip','code','guest_can_pause']  # Make sure 'name' exists in the Room model

 