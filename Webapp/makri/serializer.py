from rest_framework import serializers

class MakriClassifier(serializers.Serializer):
    data = serializers.CharField()
