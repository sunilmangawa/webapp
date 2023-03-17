from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics, permissions
from django.views import generic
# from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Company, Device, Milldata
from .serializers import CompanySerializer, DeviceSerializer, MilldataSerializer
from .forms import CustomUserCreationForm

def home_page_view(request):
    return render(request, 'home.html')

class MilldataListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MilldataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        return Milldata.objects.filter(device_id=device_id)

    def perform_create(self, serializer):
        device_id = self.kwargs['device_id']
        device = Device.objects.get(id=device_id)
        serializer.save(device=device)

class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        #user = get_object_or_404(User, pk=self.kwargs['pk'])
        companies = Company.objects.filter(owner=user)
        context['companies'] = companies
        context['user'] = user
        if companies.count() >= 1:
            devices = Device.objects.filter(company=companies.first())
            latest_data = []
            for device in devices:
                milldata = Milldata.objects.filter(device=1).order_by('-id').first()
                latest_data.append(milldata)
            context['devices'] = zip(devices, latest_data)
        return context
        # return render('dashboard.html', context)
        # return render(request, 'dashboard.html', context)

class CompanyDashboardView(generic.TemplateView):
    template_name = 'company_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company_id = self.kwargs['company_id']
        company = Company.objects.get(pk=company_id)
        context['company'] = company
        devices = Device.objects.filter(company__id=company_id)
        latest_data = []
        for device in devices:
            milldata = Milldata.objects.filter(device=device).order_by('-id').first()
            latest_data.append(milldata)
        context['devices'] = zip(devices, latest_data)
        return context

@login_required
def device_data(request, company_id, device_id):
    device_data  = Milldata.objects.filter(company_id=company_id, device_id=device_id)
    # perform calculations to get average by shift time
    # render the data in a template
    return render(request, 'dashboard.html', {'device_data ': device_data })

# class CompanyListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     permission_classes = [permissions.IsAuthenticated]


# class DeviceListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer
#     permission_classes = [permissions.IsAuthenticated]
@login_required
def profile(request):
    user = request.user
    companies = Company.objects.filter(owner=user)
    context = {'user': user, 'companies': companies}
    return render(request, 'profile.html', context)

class CompanyDetailView(generic.DetailView):
    model = Company
    template_name = 'company_detail.html'

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.get_object()
        devices = Device.objects.filter(company=2)
        latest_data = []
        
        milldata = Milldata.objects.filter(device=3).order_by('-id').first()
        #latest_data.append(milldata)
        
        latest_data.append(milldata)
        context['devices'] = zip(devices, latest_data)
        return context


class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'device_detail.html'

    def get_queryset(self):
        print(self.kwargs)  # Add this line to check the kwargs
        queryset = super().get_queryset()
        user = self.request.user
        company = get_object_or_404(Company, pk=self.kwargs['company_pk'])
        device = get_object_or_404(queryset, company=company, pk=self.kwargs['pk'])
        if user.is_superuser or company.owner == user:
            return queryset.filter(company=company, device=device)
        else:
            return queryset.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.get_object()
        milldata = Milldata.objects.filter(device=device).order_by('-id').first()
        context['milldata'] = milldata
        return context