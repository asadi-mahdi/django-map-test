import os

from django.http import HttpResponseForbidden, JsonResponse
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


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        custom_response = {
            "status": "server error",
            "message": exception.__str__()
        }
        import traceback
        file = open(os.path.join(os.path.dirname(__file__), 'exceptions.txt'), 'a')
        file.write(traceback.format_exc())
        file.close()

        return JsonResponse(custom_response, status=500)
