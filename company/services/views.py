from django.shortcuts import render
from .models import ServiceCategory, Service

# Create your views here.


def services_list(request):
    services = {}
    for category in ServiceCategory.objects.all():
        services_items = []
        for service in Service.objects.filter(category=category):
            services_items.append(service)

        services[category.name] = services_items

    return render(
        request,
        "services/services_list.html",
        context={
            "services": services
        }
    )
