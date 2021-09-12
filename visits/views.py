from django.shortcuts import render
from django.http import FileResponse
from .models import Visit
from links.models import Link

# Create your views here.
def track(request, uuid):
    link = Link.objects.get(pk=uuid)
    if link.is_enabled:
        visit = Visit(link=link)
        visit.save()
        if link.visit_count == 0:
            link.first_opened = visit.timestamp
        link.visit_count = link.visit_count + 1
        link.last_opened = visit.timestamp
        link.save()
    response = FileResponse(open("links/trackerDino.png", "rb"))
    response['Cache-Control'] = 'no-store'
    return response