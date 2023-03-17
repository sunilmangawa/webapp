# accounts/urls.py
from django.urls import path
from .views import SignUpView, login_view, Login_View


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    # path('login/', login_view, name='login'),
    path('login/', Login_View.as_view(), name='login'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)