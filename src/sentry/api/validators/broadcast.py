from __future__ import absolute_import

from rest_framework import serializers


class BroadcastValidator(serializers.Serializer):
    hasSeen = serializers.BooleanField(required=False)


class AdminBroadcastValidator(BroadcastValidator):
    title = serializers.CharField(max_length=32, required=True)
    message = serializers.CharField(max_length=32, required=True)
    link = serializers.URLField(required=True)
    isActive = serializers.BooleanField(required=False)
    dateExpires = serializers.DateTimeField(required=False)
