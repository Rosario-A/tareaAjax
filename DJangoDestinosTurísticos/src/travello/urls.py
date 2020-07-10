from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('destinationCreateView', views.destinationCreateView, name='destinationCreateView'),
    path('destinationListView', views.destinationListView, name='destinationListView'),
    path('delete/<id>/', views.destinationDeleteView, name='deleting'),
]



