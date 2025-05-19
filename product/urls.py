from django.urls import path
from .views import (
    MaxsulotCreateView,
    MaxsulotListView,
    MaxsulotDetailView,
    MaxsulotUpdateView,
    MaxsulotDeleteView
)

urlpatterns = [
    path('maxsulot/', MaxsulotListView.as_view()),
    path('maxsulot/create/', MaxsulotCreateView.as_view()),
    path('maxsulot/<uuid:uid>/', MaxsulotDetailView.as_view()),
    path('maxsulot/<uuid:uid>/update/', MaxsulotUpdateView.as_view()),
    path('maxsulot/<uuid:uid>/delete/', MaxsulotDeleteView.as_view()),
]




