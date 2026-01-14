from django.urls import path
from .views import (
    categorias,
)

urlpatterns = [
    path('categorias/', categorias, name='categorias'),
]