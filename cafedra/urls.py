from django.urls import path
from . import views 

urlpatterns = [
    path('', views.main_page, name='main'),
    path('cafedra', views.cafedra_page, name='cafedra'),
    path('articles/<slug:slug>', views.regular, name='regular'),
    path('employes/<slug:slug>', views.employee_page, name='employee_page'),
    path('files/<slug:slug>', views.index_page, name="custom_file_page"),
]