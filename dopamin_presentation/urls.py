"""conanizator_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='dopamin_presentation/index.html'), name='index'),
    url(r'^src/my-icons$', TemplateView.as_view(template_name='dopamin_presentation/my-app.html'), name='icons'),
    url(r'^src/my-app$', TemplateView.as_view(template_name='dopamin_presentation/my-app.html'), name='application'),
]