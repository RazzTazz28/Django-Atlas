from django.urls import path
from . import views
from Atlas import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('logout/', views.logoutUser, name='logout'),
]

