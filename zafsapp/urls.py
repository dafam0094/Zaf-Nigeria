from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('publication_api', views.publication_api, name='publication_api'),
    path('gallery/', views.gallery, name='gallery'),
    path('donate/', views.Donate, name= 'donate'),
    path('about/', views.team_information, name='about'),
    path('joinus/', views.Join, name= 'joinus'),
    path('contact/', views.Contact, name= 'contact'),
    path('member/', views.Member, name= 'member'),
] 
