from django.urls import path
from .views import current_user, SignUp, SignIn

urlpatterns = [
    path('current_user/', current_user),
    path('sign_up/', SignUp.as_view()),
    path('sign_in/', SignIn.as_view()),
]
