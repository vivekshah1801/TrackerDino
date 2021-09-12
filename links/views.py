from django.http import JsonResponse
from django.shortcuts import render
from .models import Link
from django.core import serializers
from django.forms.models import model_to_dict
from uuid import uuid4

# Create your views here.
def view(request):
    # TODO provide better serialization method
    return JsonResponse([model_to_dict(x) for x in Link.objects.all()], safe=False)

def create(request):
    userid = request.POST.get("userid", None)
    link = Link(creator=userid)
    link.save()
    return JsonResponse({
        "status": True,
        "tracker": "http://" + request.get_host() + "/tracker/" + str(link.uuid),
        "data": model_to_dict(link),
    })

def details(request, tracker):
    link = Link.objects.get(pk=tracker)
    return JsonResponse(model_to_dict(link), safe=False)

def delete(request, tracker):
    link = Link.objects.get(pk=tracker)
    link.delete()
    return JsonResponse(model_to_dict(link), safe=False)

def toggle(request, tracker):
    link = Link.objects.get(pk=tracker)
    link.is_enabled = not link.is_enabled
    link.save()
    return JsonResponse(model_to_dict(link), safe=False)

def toggle_notif(request, tracker):
    link = Link.objects.get(pk=tracker)
    link.notifications_enabled = not link.notifications_enabled
    link.save()
    return JsonResponse(model_to_dict(link), safe=False)
