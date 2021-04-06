from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': request.user.id,  # `django.contrib.auth.User` instance.
            "some": "response"
        }
        return Response(content)

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetDetailSerializer

    def list(self, request):
        serializer = DatasetListSerializer(self.queryset, many=True)
        return Response(serializer.data)