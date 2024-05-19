"""
URL configuration for company project.

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
from django.urls import path

import main.views
import services.views

urlpatterns = [
    # Admin site path
    path("admin/", admin.site.urls),

    # Website paths: main app
    path("", main.views.HomeView.as_view(), name="home"),
    path("feedbacks", main.views.FeedbacksView.as_view(), name="feedbacks"),
    path("services_particulars/lawyer", main.views.lawyer_info, name="services-lawyer-info"),
    path("services_particulars/licenses", main.views.licenses_info, name="services-licenses-info"),
    path("services_particulars/registration", main.views.registration_info, name="services-registration-info"),
    path("about", main.views.about_page, name="about-page"),

    # Website paths: services app
    path("services", services.views.services_list, name="services"),
]
