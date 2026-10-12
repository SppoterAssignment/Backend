from django.http import JsonResponse
from django.urls import include, path


def index(request):
    return JsonResponse({
        'service': 'Safe Route Planner API',
        'endpoints': {
            'GET /api/health': 'liveness check',
            'POST /api/plan': 'plan a trip: origin, destination, departure, load_lb, interval_mi',
        },
    })


def not_found(request, exception=None):
    # JSON (not an HTML page) since this is an API; echoing the path helps debug routing.
    return JsonResponse({'detail': 'Not found', 'path': request.path}, status=404)


handler404 = not_found

urlpatterns = [
    path('', index),
    path('api/', include('routeplanner.urls')),
]
