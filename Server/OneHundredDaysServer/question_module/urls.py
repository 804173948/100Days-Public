"""SignLanguageTranslationServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include

from question_module import views

urlpatterns = [
    path('query/id', views.query_id),
    path('query/ids', views.query_ids),
    path('query/all', views.query_all),
    path('query/filter', views.query_filter),
    path('query/count', views.query_count),
    path('generate/all', views.generate_all),
    path('generate/type', views.generate_type),
    path('generate/level', views.generate_level),
    path('generate/exam', views.generate_exam),
]
if settings.HTML_TEST:
    urlpatterns.extend([
        path('test/load', views.test_load),
        path('test/randomly', views.test_randomly),
        path('test/delete', views.test_delete)
    ])
"""
    path('admin/push', views.admin_push),
    path('admin/update', views.admin_update),
"""
