"""petfamily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from petfamily.core import views
# from petfamily.core.forms import UserLoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/favourite/<int:petID>/', views.home_favourite_pet, name='home_favourite_pet'),
    path('favourites', views.favourites, name='favourites'),
    path('favourites/remove_favourite/<int:petID>/', views.remove_favourite, name='remove_favourite'),
    path('register/', views.register, name='register'),
    path('upload/',views.upload, name='upload'),
    path('secret/', views.secret_page, name='secret'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/',views.search, name='search'),
    path('about/',views.about, name='about'),
    path('login/',views.login,name='login'),
    # path('login/',views.login, name='login'),
    # path('captcha/', include('captcha.urls')),
    path('contact/',views.contact, name='contact'),
    path('success/',views.success, name='success'),
    path('donate/',views.donate, name='donate'),
    path('pet/<int:pet_id>/',views.detail, name='detail'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
admin.site.index_title = ""
admin.site.site_header = "The PetFamily"
admin.site.site_title = "The PetFamily Administration"
