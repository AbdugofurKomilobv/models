from django.urls import path
from .views import *


urlpatterns = [
    path('home/',home_page,name='home'),
    path('batafsil/<post_id>',batafsi,name='batafsil')
]