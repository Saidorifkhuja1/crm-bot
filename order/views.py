from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Buyurtma
from .serializers import BuyurtmaSerializer

class BuyurtmaCreateView(generics.CreateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    parser_classes = [MultiPartParser, FormParser]
    # permission_classes = [IsAuthenticated, IsAdminUser]

class BuyurtmaListView(generics.ListAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class BuyurtmaDetailView(generics.RetrieveAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class BuyurtmaUpdateView(generics.UpdateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class BuyurtmaDeleteView(generics.DestroyAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]
