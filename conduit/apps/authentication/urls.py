from django.conf.urls import url

from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, PasswordAPIView, ChangePasswordAPIView, ActiveUserEmailAPIView
)

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
    url(r'^users/sendPasswordRecover/?$', PasswordAPIView.as_view()),
    url(r'^users/changePasswordRecover/?$', ChangePasswordAPIView.as_view()),
    url(r'^users/activation/?$', ActiveUserEmailAPIView.as_view()),
]
