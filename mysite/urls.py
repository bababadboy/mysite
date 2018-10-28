"""mysite URL Configuration

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
from django.urls import path,include,re_path
from polls import views
from django.views.generic.base import TemplateView

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('api/', include('todo.urls')),
    
    re_path(r'^$',TemplateView.as_view(template_name="index.html"))
    # path('', admin.site.urls),
]

# 自定义错误页面
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.page_error