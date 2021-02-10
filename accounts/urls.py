from django.urls import path
from .views import SignUpView, RegisterView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('register/', RegisterView.as_view(), name='accounts_register'),
]
