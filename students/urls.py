from django.urls import path
from .views import StudentRetrieveUpdateDeleteView, login, StudentListView, register, student_page

urlpatterns = [
    path('register/', register, name='register'),  
    path('profile/', StudentRetrieveUpdateDeleteView.as_view(), name='profile'),
    path('login/', login, name='login'),
    path('students/', StudentListView.as_view(), name='students-list'),
    path('students/page/', student_page, name='students-page'),
]