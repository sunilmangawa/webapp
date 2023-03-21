from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from milldata.models import Device


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


class EditFeedingForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['circle', 'feed_time', 'circle_hold', 'actual_hold']
        labels = {
            'circle': 'Circle',
            'feed_time': 'Feed Time',
            'circle_hold': 'Circle Hold',
            'actual_hold': 'Actual Hold',
        }
