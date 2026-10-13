from django.urls import path
from . import views

urlpatterns = [
    # path('', views.lab_view, name="labView"),
    # path('labmodel/', views.lab_model_view, name="lab_model_view"),
    path('api/auth/register/', views.api_register_view, name='api_register_url'),
    path('api/auth/login/', views.api_login_view, name='api_register_url'),
    path('api/assets/create/', views.api_asset_create, name='api_create_asset_url'),
    path('api/assets/all/', views.api_list_assets, name='api_list_assets_url'),
]