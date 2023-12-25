from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lugares', views.lugares, name='lugares'),
    path('socios/', views.socios, name='socios'),
    path('usuario/<str:nombre_usuario>/', views.usuario, name='usuario'),
    # OJO, ESTO NO SE TIENE QUE PISAR CON /USUARIO
    # path('socios/<str:nombre_usuario>', views.usuario, name='usuario'),
    re_path(r'lugares/(?P<id>[0-9]{4})/$', views.lugar_detalle)
]