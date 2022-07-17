from django.urls import path
from .views import *
urlpatterns = [
    path('', homeView, name='home'),
    path('homiy/', homiyView, name='homiy'),
    path('singlehomiy/<int:id>/', singleHomiyView, name='singlehomiy'),
    path('students/', studentsView, name='students'),
    path('add-student/', addStudentView, name='add-student'),
    path('single-student/<int:id>/',singleStudentView, name='single-student'),
    path('checkbalance/', checkBalanceView, name='checkbalance'),
    path('homiysearch/', homiySearchView, name='homiysearch'),
    path('talabasearch/', talabaSearchView, name='talabasearch')
]