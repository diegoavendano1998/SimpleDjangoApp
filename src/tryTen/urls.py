"""tryTen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django import urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Para mostrar la vista home con views del proyecto profiles
    # $ significa que sera llamada cada vez que el usuairio navegue a la home page
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^profile/$', profiles_views.userProfile, name='profile'),
    # Del proyecto contact
    url(r'^contact/$', contact_views.contact, name='contact'),
    # Auth
    url(r'^accounts/', include('allauth.urls')),
    # Stripe
    url(r'^checkout/$', checkout_views.checkout, name='checkout'),
]

# Si la configuracion esta en debug usara los archivos estaticos correspondientes 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
