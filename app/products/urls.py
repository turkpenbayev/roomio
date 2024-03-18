from django.urls import path
from .views import home, SignUpView, edit

urlpatterns = [
    path('', home, name='home'),
    path('edit/', edit, name='edit'),
    path('signup/', SignUpView.as_view(), name="signup"),
]
