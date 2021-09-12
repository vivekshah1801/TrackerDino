from django.http import JsonResponse
from django.utils import timezone

def health(request):
    return JsonResponse({
        "status": "healthy",
        "timestamp": timezone.now(),
    })
