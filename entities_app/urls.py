from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'register', views.user_register, name='register'),
    url(r'login', views.user_login, name='login'),
    url(r'logout', views.user_logout, name='logout'),
    url(r'entities', views.entities_view, name='entities'),
    url(r'engagements', views.engagements_view, name='engagements')
]
