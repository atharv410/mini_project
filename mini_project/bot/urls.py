from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('collect/data/', views.collect_data, name='collect_data'),
    path('view/data/', views.view_data, name='view_data'),
    path('export', views.export_data, name='export_data'),
]

