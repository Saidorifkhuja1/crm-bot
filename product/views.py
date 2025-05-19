from rest_framework import generics
from .models import Maxsulot
from .serializers import MaxsulotSerializer
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

class MaxsulotCreateView(generics.CreateAPIView):
    queryset = Maxsulot.objects.all()
    serializer_class = MaxsulotSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class MaxsulotListView(generics.ListAPIView):
    queryset = Maxsulot.objects.all()
    serializer_class = MaxsulotSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]

class MaxsulotDetailView(generics.RetrieveAPIView):
    queryset = Maxsulot.objects.all()
    serializer_class = MaxsulotSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class MaxsulotUpdateView(generics.UpdateAPIView):
    queryset = Maxsulot.objects.all()
    serializer_class = MaxsulotSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]

class MaxsulotDeleteView(generics.DestroyAPIView):
    queryset = Maxsulot.objects.all()
    serializer_class = MaxsulotSerializer
    lookup_field = 'uid'
    # permission_classes = [IsAuthenticated, IsAdminUser]
