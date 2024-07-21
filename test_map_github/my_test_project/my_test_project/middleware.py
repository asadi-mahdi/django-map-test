import os

from django.db import transaction
from django.http import HttpResponseForbidden, JsonResponse
from django.utils.deprecation import MiddlewareMixin
from jdatetime import datetime

from test_map_github.my_test_project.my_test_project.settings import ERRORS_PATH


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
        import traceback
        time_now = datetime.now()
        error_time = str(int(time_now.timestamp()))
        full_error_path = os.path.join(ERRORS_PATH, str(time_now.year), str(time_now.month), str(time_now.day))
        if not os.path.exists(full_error_path):
            os.makedirs(full_error_path)
        # file = open(os.path.join(os.path.dirname(__file__), (error_time + '.txt')), 'a')
        file = open(os.path.join(full_error_path, (error_time + '.txt')), 'a')
        file.write(traceback.format_exc())
        file.close()
        custom_response = {
            "status": "server error",
            "message": "error code is " + error_time
        }

        return JsonResponse(custom_response, status=500)
