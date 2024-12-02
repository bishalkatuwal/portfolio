from django.urls import path
from .views import home_view, about_view, contact_view, ProjectView, ProjectDetailView

urlpatterns = [

path('', home_view, name='home'),
path('about/', about_view, name='about'),
path('contact/', contact_view, name='contact'),

path('project/', ProjectView.as_view(), name='project'),
path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail')

]