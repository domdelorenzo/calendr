from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
  path('users/', views.UserList.as_view(), name='user_list'),
  path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
  path('events/', views.EventList.as_view(), name='event_list'),
  path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
]