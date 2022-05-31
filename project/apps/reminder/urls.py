from django.urls import path
from . import views

urlpatterns = [
    path('', views.LembreteListView.as_view(), name='index'),
    path('edit/<slug:pk>/', views.LembreteUpdateView.as_view(), name='edit'),
    path('delete/<slug:pk>/', views.LembreteDeleteView.as_view(), name='delete'),
    path('adicionar', views.LembreteCreateView.as_view(), name='adicionar')
]
