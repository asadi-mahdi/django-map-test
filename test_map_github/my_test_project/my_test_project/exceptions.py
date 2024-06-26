

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            'error': str(exc),
        }
        response.data = custom_response
        # # stack trace
        # import traceback
        # file = open(os.path.join(os.path.dirname(__file__), 'exceptions.txt'), 'a')
        # file.write(traceback.format_exc())
        # file.close()

    return response
