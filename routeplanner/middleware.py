BUILD = 'django-mw-1'  # bump to confirm which version is deployed


class BuildHeaderMiddleware:
    """Tags every response with the deployed build, to verify deploys from outside."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-App-Build'] = BUILD
        return response
