from django.urls import path
from . import views

urlpatterns = [
        path('', views.research, name = "research"),
        path('publications/', views.publications, name = "publications"),
]
