from django.urls import path
from .views import signup

urlpatterns = [
    path('', signup, name='signup'),
    # Add other views as needed
]
