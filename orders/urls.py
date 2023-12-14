from django.urls import path
from .views import OrderListCreateView

urlpatterns = [
    path('', OrderListCreateView.as_view()),
    path('<int:pk>/', OrderListCreateView.as_view()),
]
