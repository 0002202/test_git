"""
URL configuration for test_git project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from testAPP.views import index, show_question, save_question, question_image, is_correct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('question/<int:pk>/image/', question_image, name='question_image'),
    path('question/', show_question),
    path('save_question/', save_question),

    path('is_correct/', is_correct),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       # 能够在目录中正确的找到工作目录
