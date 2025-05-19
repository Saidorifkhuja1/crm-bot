from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Haridor
from .serializers import ClientSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ClientCreateView(generics.CreateAPIView):
    queryset = Haridor.objects.all()
    serializer_class = ClientSerializer
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientListView(generics.ListAPIView):
    queryset = Haridor.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientDetailView(generics.RetrieveAPIView):
    queryset = Haridor.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientUpdateView(generics.UpdateAPIView):
    queryset = Haridor.objects.all()
    serializer_class = ClientSerializer
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientDeleteView(generics.DestroyAPIView):
    queryset = Haridor.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]
