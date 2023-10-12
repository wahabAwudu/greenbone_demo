from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Computer
from .serializers import ComputerSerializer


class ComputerViewSet(ModelViewSet):
    model = Computer
    serializer_class = ComputerSerializer
    permission_classes = [AllowAny]
    queryset = Computer.objects.all()
    filterset_fields = ["employee_abbrev",]

