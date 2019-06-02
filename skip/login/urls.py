from django.urls import path
from . import views

# app_name = 'login'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:nim>/', views.profil, name='profil'),
#     path('<int:nim>/rate/', views.rate, name='rate'),
#     path('<int:nim>/comment/', views.comment, name='comment'),
# ]

app_name = 'login'
urlpatterns = [
    path('', views.register, name='register'),
    path('logout/',views.logout_request, name='logout'),
    path('login/',views.login_request, name='login'),
]