from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import HomePageView, DialogsView

urlpatterns = [
    path('', DialogsView.as_view(), name='home'),
    path('chats/', views.ChatListAPI.as_view()),
    path('chats/<int:pk>/', views.ChatDetail.as_view()),
    url(r'(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
