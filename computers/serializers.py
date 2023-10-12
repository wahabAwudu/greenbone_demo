from rest_framework.serializers import ModelSerializer
from .models import Computer


class ComputerSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at",)
