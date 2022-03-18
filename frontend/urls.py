from . import views
from django.urls import path, include

app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='home'),
    path('works/', views.works, name='works'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('hobby/', views.hobby, name='hobby'),
    path('about-me/', views.about, name='about'),
    path('hire-me/', views.hireMe, name='hire-me'),
    path('ww/', views.ww, name='ww'),
]
