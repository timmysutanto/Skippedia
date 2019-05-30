from django.urls import path
from . import views

app_name = 'mahasiswa'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nim>/', views.profil, name='profil'),
    path('<int:nim>/rate/', views.rate, name='rate'),
    path('<int:nim>/comment/', views.comment, name='comment'),
]