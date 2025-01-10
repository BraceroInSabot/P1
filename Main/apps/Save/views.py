# Project
from .models import Save
from .serializers import SaveSerializer

# Libs
from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class SaveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows saves to be viewed or edited.
    """
    queryset = Save.objects.all().order_by('-created_at')
    print(queryset, type(queryset))
    serializer_class = SaveSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        print(queryset, type(queryset))
        return Response(serializer.data)