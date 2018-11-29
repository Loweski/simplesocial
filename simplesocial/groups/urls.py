from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('post/in/<slug:title>/', views.SingleGroup.as_view(), name='single'),
    path('join/<slug:title>/', views.JoinGroup.as_view(), name='join'),
    path('join/<slug:title>/', views.LeaveGroup.as_view(), name='leave'),
]
