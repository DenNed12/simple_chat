from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','desription','members')