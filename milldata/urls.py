from django.urls import path, include
# from django.contrib.auth import views as auth_views
from .views import home_page_view, device_data, CompanyDashboardView, EditFeedingView, MilldataListCreateAPIView, DashboardView, CompanyDetailView, DeviceDetailView, DeviceDataAPI, CompanyListCreateAPIView, DeviceListCreateAPIView  #,  login_view, signup, profile, CompanyListAPIView, DeviceListAPIView, DeviceDetailAPIView,  DeviceDataRangeAPIView
from . import views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', signup, name='signup'),
    # path('profile/', profile, name='profile'),

    # path('mill', home_page_view, name='home'),
    path('dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard'),
    path('company/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('device/<int:company_id>/<int:pk>/', DeviceDetailView.as_view(), name='device_detail'),
    path('device/<int:pk>/edit_feeding/', EditFeedingView.as_view(), name='edit_feeding'),
    path('export_pdf/<int:device_id>/', views.export_pdf, name='export_pdf'),
    path('export_excel/<int:device_id>/', views.export_excel, name='export_excel'),
    # path('companies/<int:company_pk>/', CompanyDashboardView.as_view(), name='company_dashboard'),
    path('device/<int:device_id>/data/', device_data, name='device_data'),
    # path('companies/<int:company_id>/devices/<int:device_id>/', device_data, name='device_data'),

    path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
    path('devices/', DeviceListCreateAPIView.as_view(), name='device-list-create'),
    # path('companies/', CompanyListAPIView.as_view(), name='company_list'),
    # path('devices/', DeviceListAPIView.as_view(), name='device_list'),
    # path('devices/<int:pk>/', DeviceDetailAPIView.as_view(), name='device_detail'),
    # path('devices/<int:device_id>/data_range/', DeviceDataRangeAPIView.as_view(), name='device_data_range'),
    path('device/<int:device_id>/', DeviceDataAPI.as_view(), name='device-data-api'),
    path('devices/<int:device_id>/timestamps/', MilldataListCreateAPIView.as_view(), name='milldata-list-create'),
]
