"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from mysite.views import *
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', index, name='index'),
    path('cabinet/', cabinet, name='cabinet'),
    path('workers/', employ, name='workers'),
    path('workers/delete/<int:pk>/', delete_employ, name='delete_employ'),
    path('store/', store, name='store'),
    path('store/edit/<int:pk>/', store_edit, name='store_edit'),
    path('store/delete/<int:pk>/', delete_store, name='delete_store'),
    path('promotions/', promotions, name='promotions'),
    path('products/', products, name='products'),
    path('products/delete/<int:pk>/', delete_products, name='delete_products'),
    path('worker/edit/<int:pk>/', employ_update, name='workers_edit'),
    path('schedule/', schedule, name='schedule'),
    path('store/<int:store_id>/schedule/', store_schedule, name='store_schedule'),
    path('products/', products, name='products'),
    path('clients/', clients, name='clients'),
    path('clients/delete/<int:pk>/', delete_clients, name='delete_clients'),
    path('brand/', brand, name='brand'),
    path('brand/delete/<int:pk>/', delete_brand, name='delete_brand'),
    path('producers/', producers, name='producers'),
    path('producers/delete/<int:pk>/', delete_producers, name='delete_producers'),
    path('category/', category, name='category'),
    path('category/delete/<int:pk>/', delete_category, name='delete_category'),
    path('partner/', partner, name='partner'),
    path('partner/delete/<int:pk>/', delete_partner, name='delete_partner'),
    path('deal/', deal, name='deal'),
    path('decrease/', decrease, name='decrease'),
    path('chat/', chat, name='chat'),
    path('support/', support, name='support'),
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {
                "document_root": settings.MEDIA_ROOT,
            },
        ),
    ]