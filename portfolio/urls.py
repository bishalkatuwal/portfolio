from django.urls import path
from .views import home_view, ContactView, about_view, portfolio_view

urlpatterns = [

path('', home_view, name='home'),
path('contact/', ContactView.as_view(), name='contact'),
path('about/', about_view, name='about'),
path('portfolio/', portfolio_view, name='portfolio')

]