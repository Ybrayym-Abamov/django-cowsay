from django.urls import path
from cowsayapp import views

urlpatterns = [
    path('', views.main),
    path('history/', views.recents)
]
