from django.urls import path, re_path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.ListGroups.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('post/in/(?P<slug>[^/]+)/', views.SingleGroup.as_view(), name='single'),
    path('join/(?P<slug>[^/]+)/', views.JoinGroup.as_view(), name='join'),
    path('leave/(?P<slug>[^/]+)/', views.LeaveGroup.as_view(), name='leave'),
]
