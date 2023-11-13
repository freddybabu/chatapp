from django.urls import path
from rooms import views


urlpatterns = [
    path('', views.room, name='room'),
    path('<slug:slug>/', views.rooms, name="rooms"),
]
