from django.urls import path
from . import views

urlpatters = [
        path('', views.research, name = "research"),
        path('publications/', views.publications, name = "publications"),
]
