from django.conf.urls import url
from apps.authentication.views import RegistrationAPIView, LoginAPIView, AutoLoginView

urlpatterns = [
   url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
   url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
   url(r'^users/autologin/$', AutoLoginView.as_view(), name='autologin')
]