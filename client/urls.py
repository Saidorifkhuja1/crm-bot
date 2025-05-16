from django.urls import path
from .views import (
    ClientCreateView, ClientListView,
    ClientDetailView, ClientUpdateView,
    ClientDeleteView
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<uuid:uid>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/<uuid:uid>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<uuid:uid>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]
