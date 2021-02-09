from django.urls import path

from . import views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('chats/', views.chats_list),
    path('chats/<int:pk>/', views.chat_details),
]
