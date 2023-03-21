from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear
from django.utils import timezone

from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics, permissions
from django.views import generic
# from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Company, Device, Milldata
from .serializers import CompanySerializer, DeviceSerializer, MilldataSerializer
from .forms import CustomUserCreationForm, EditFeedingForm

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

# class DashboardView(generic.TemplateView):
#     template_name = 'dashboard.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         companies = Company.objects.filter(owner=user)
#         context['companies'] = companies
#         context['user'] = user

#         today = timezone.now()
#         company_devices_data = []

#         for company in companies:
#             devices = Device.objects.filter(company=company)
#             devices_data = []
#             for device in devices:
#                 device_data = {}
#                 #milldata_today = Milldata.objects.filter(device=device,katta_time__day=today.day,katta_time__month=today.month,katta_time__year=today.year)
#                 milldata_today = Milldata.objects.filter(device=device, katta_time__date=today.date())
#                 print(f"Milldata today is {milldata_today}")
#                 total_bags = milldata_today.count()
#                 print("Total bags: %d" % total_bags)
#                 adjusted_duration = 0
#                 # Apply the 300-second condition
#                 for i in range(1, total_bags):
#                     time_diff = (milldata_today[i].katta_time - milldata_today[i - 1].katta_time).total_seconds()
#                     if time_diff <= 300:
#                         adjusted_duration += time_diff

#                 avg_time = adjusted_duration / total_bags if total_bags > 0 else 0

#                 device_data['device'] = device
#                 device_data['total_bags'] = total_bags
#                 device_data['average_time'] = avg_time
#                 devices_data.append(device_data)

#             company_devices_data.append({'company': company, 'devices_data': devices_data})

#         context['company_devices_data'] = company_devices_data
#         return context

class DashboardView(generic.TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        companies = Company.objects.filter(owner=user)
        context['companies'] = companies
        context['user'] = user

        # today = timezone.now()
        today = timezone.localtime(timezone.now())
        company_devices_data = []

        for company in companies:
            devices = Device.objects.filter(company=company)
            devices_data = []
            for device in devices:
                device_data = {}
                milldata_today = Milldata.objects.filter(device=device, katta_time__date=today.date())

                print(f"Device: {device.name}")
                print(f"Today: {today.date()}")
                print(f"Milldata count: {milldata_today.count()}")
                print("Milldata items:")
                for item in milldata_today:
                    print(f"  {item.katta_time}")

                total_bags = milldata_today.count()

                adjusted_duration = 0
                # Apply the 300-second condition
                for i in range(1, total_bags):
                    time_diff = (milldata_today[i].katta_time - milldata_today[i - 1].katta_time).total_seconds()
                    if time_diff <= 300:
                        adjusted_duration += time_diff

                avg_time = adjusted_duration / total_bags if total_bags > 0 else 0

                device_data['device'] = device
                device_data['total_bags'] = total_bags
                device_data['average_time'] = avg_time
                devices_data.append(device_data)

            company_devices_data.append({'company': company, 'devices_data': devices_data})

        context['company_devices_data'] = company_devices_data
        return context

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

# class EditFeedingView(LoginRequiredMixin, generic.UpdateView):
#     model = Device
#     fields = ['circle', 'feed_time', 'circle_hold', 'actual_hold']
#     template_name = 'edit_feeding.html'
#     success_url = reverse_lazy('milldata/dashboard')  # Replace this with the URL you want to redirect to after a successful update

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         company_pk = self.object.company.pk
#         super().form_valid(form)
#         return HttpResponseRedirect(reverse('milldata/dashboard', args=[company_pk]))

class EditFeedingView(LoginRequiredMixin, generic.UpdateView):
    model = Device
    form_class = EditFeedingForm
    template_name = "edit_feeding.html"

    def get_queryset(self):
        # Ensure the user can only edit devices that belong to their company
        # return Device.objects.filter(company=self.request.user.company)
        return Device.objects.filter(company__owner=self.request.user)  
        # return Device.objects.filter(company=Company.owner==self.request.user)
        # return Device.objects.filter(Company.owner==self.request.user)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        # Get the company's primary key from the device instance
        company_pk = self.object.company.pk

        # Redirect to the dashboard view with the primary key
        return HttpResponseRedirect(reverse('dashboard', args=[company_pk]))

class DeviceDetailView(generic.DetailView):
    model = Device
    template_name = 'device_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        device = self.object

        # Get today's date in local timezone
        today = timezone.localtime(timezone.now())

        # Get Milldata for today
        milldata_today = Milldata.objects.filter(device=device,katta_time__day=today.day,katta_time__month=today.month,katta_time__year=today.year)

        # Calculate total bags and average time
        # ... (Reuse the logic from your DashboardView)
        print(f"Device: {device.name}")
        print(f"Today: {today.date()}")
        print(f"Milldata count: {milldata_today.count()}")
        print("Milldata items:")
        for item in milldata_today:
            print(f"  {item.katta_time}")

        total_bags = milldata_today.count()

        adjusted_duration = 0
        runned_duration = 0
        # Apply the 300-second condition
        for i in range(1, total_bags):
            time_diff = (milldata_today[i].katta_time - milldata_today[i - 1].katta_time).total_seconds()
            # time_avg = (milldata_today[i].katta_time - milldata_today[i - 1].katta_time)
            if time_diff >= 300:
                adjusted_duration += time_diff
            # else:
            #     runned_duration += time_diff

        avg_time = adjusted_duration / total_bags if total_bags > 0 else 0
        # avg_time = ((milldata_today.first().katta_time - milldata_today.last().katta_time) - runned_duration) / total_bags if total_bags > 0 else 0
        # katta_average = (3600.00/avg_time) if avg_time > 0 else 0
        # print(katta_average)
        # expectedBagToday = 24*katta_average if katta_average > 0 else 0
        # print(expectedBagToday)

        context['total_bags'] = total_bags
        context['average_time'] = avg_time
        # context['average_katta'] = katta_average
        # context['expectedBagToday'] = expectedBagToday
        return context

def export_pdf(request, device_id):
    # Implement your PDF exporting logic here
    return HttpResponse("PDF exporting not yet implemented")

def export_excel(request, device_id):
    # Implement your Excel exporting logic here
    return HttpResponse("Excel exporting not yet implemented")


# class DeviceDetailView(generic.DetailView):
#     model = Device
#     template_name = 'device_detail.html'

#     def get_queryset(self):
#         print(self.kwargs)  # Add this line to check the kwargs
#         queryset = super().get_queryset()
#         user = self.request.user
#         company = get_object_or_404(Company, pk=self.kwargs['company_pk'])
#         device = get_object_or_404(queryset, company=company, pk=self.kwargs['pk'])
#         if user.is_superuser or company.owner == user:
#             return queryset.filter(company=company, device=device)
#         else:
#             return queryset.none()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         device = self.get_object()
#         milldata = Milldata.objects.filter(device=device).order_by('-id').first()
#         context['milldata'] = milldata
#         return context
    
