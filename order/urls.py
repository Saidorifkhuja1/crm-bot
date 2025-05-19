from django.urls import path
from .views import (
    BuyurtmaCreateView,
    BuyurtmaListView,
    BuyurtmaDetailView,
    BuyurtmaUpdateView,
    BuyurtmaDeleteView,
)

urlpatterns = [
    path('buyurtma/', BuyurtmaListView.as_view(), name='buyurtma-list'),
    path('buyurtma/create/', BuyurtmaCreateView.as_view(), name='buyurtma-create'),
    path('buyurtma/<uuid:uid>/', BuyurtmaDetailView.as_view(), name='buyurtma-detail'),
    path('buyurtma/<uuid:uid>/update/', BuyurtmaUpdateView.as_view(), name='buyurtma-update'),
    path('buyurtma/<uuid:uid>/delete/', BuyurtmaDeleteView.as_view(), name='buyurtma-delete'),
]
