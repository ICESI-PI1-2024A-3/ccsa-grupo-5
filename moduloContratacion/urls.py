"""
URL configuration for moduloContratacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('petition.urls')),
    path('resetPassword/', authViews.PasswordResetView.as_view(template_name='passwordResetForm.html'), name='password_reset'),
    path('resetPassword/done/', authViews.PasswordResetDoneView.as_view(template_name='passwordResetDone.html'), name='password_reset_done'),
    path('resetPassword/confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(template_name='passwordResetConfirm.html'), name='password_reset_confirm'),
    path('resetPassword/complete/', authViews.PasswordResetCompleteView.as_view(template_name='passwordResetComplete.html'), name='password_reset_complete')
]
