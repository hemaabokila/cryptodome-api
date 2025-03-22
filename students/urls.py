from django.urls import path
from .views import StudentRetrieveUpdateDeleteView, login, StudentListView, register

urlpatterns = [
    path('register/', register, name='register'),  
    path('profile/', StudentRetrieveUpdateDeleteView.as_view(), name='profile'),
    path('login/', login, name='login'),
    path('students/', StudentListView.as_view(), name='students-list'),
]