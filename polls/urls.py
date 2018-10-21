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
from django.urls import path
from . import views

# 加上 app_name 设置命名空间：
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    # the 'name' value as called by the {% url %} template tag
    # 如果你想改变投票详情视图的 URL，比如想改成 polls/specifics/12/ ，
    # 你不用在模板里修改任何东西（包括其它模板），只要在 polls/urls.py 里稍微修改一下就行：
    path('<int:pk>/',views.DetailView.as_view(),name = 'detail'),
    # path('specifics/<int:question_id>/',views.detail,name = 'detail'),

    path('<int:pk>/result/',views.ResultView.as_view(),name = 'result'),
    path('<int:question_id>/vote/',views.vote,name = 'vote'),

]
