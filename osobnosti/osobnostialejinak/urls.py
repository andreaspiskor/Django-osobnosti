from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.OsobnostiListView.as_view(), name='list'),
    path('detail/<int:pk>', views.OsobnostiDetailView.as_view(), name='detail'),
]