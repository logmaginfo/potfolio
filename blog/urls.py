from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.all_blog, name = 'blog'),
    path('<int:id_blog>/',views.detais, name = 'detais'),
]
