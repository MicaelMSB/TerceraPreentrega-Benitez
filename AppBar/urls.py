from django.urls import path
from AppBar.views import inicio, productos

urlpatterns = [

    path('', inicio),
    path('productos/', productos),
    path('', inicio, name='inicio'),

]
