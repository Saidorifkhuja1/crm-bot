from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Client
from .serializers import ClientSerializer

class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]
