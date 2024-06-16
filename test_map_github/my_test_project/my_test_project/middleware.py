from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # This method is called before the view
        # You can modify the request here
        if request.headers.get('Authorization') == 'Bearer 123':
            request.META['sso'] = "true"
            return None
        else:
            return HttpResponseForbidden("Not Access")

    def process_response(self, request, response):
        # This method is called after the view
        # You can modify the response here
        return response
