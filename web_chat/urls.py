from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import HomePageView, DialogsView, CreateChatView

urlpatterns = [
    path('', DialogsView.as_view(), name='home'),
    path('chats/', views.ChatListAPI.as_view()),
    path('chats/<int:pk>/', views.ChatDetailAPI.as_view()),
    path('chats/<int:pk>/messages/', views.ChatMessagesAPI.as_view()),
    path(r'create/<int:user_id>/', views.CreateDialogView.as_view(), name='create_dialog'),
    url(r'(?P<chat_id>\d+)/$', login_required(views.MessagesView.as_view()), name='messages'),
    path('create/', CreateChatView.as_view(), name='create_chat'),

]

# urlpatterns = format_suffix_patterns(urlpatterns)
