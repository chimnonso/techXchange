from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'technology'

urlpatterns = [
    # path('create/', views.create_technology, name="create"),
    path('<int:tech_id>/', views.detail, name="detail"),
    path('<int:tech_id>/contacts', views.contacts, name="contacts"),
    path('technologies/', views.get_technologies, name="technologies")
]