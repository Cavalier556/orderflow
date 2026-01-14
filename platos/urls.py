from django.urls import path
from .views import (
    platos,
)

urlpatterns = [
    path('platos/', platos, name='platos'),
]