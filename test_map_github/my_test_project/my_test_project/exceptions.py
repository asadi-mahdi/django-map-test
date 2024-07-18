from rest_framework.response import Response


def custom_exception_handler(exc, context):
    # #for one way to handle errors
    # response = exception_handler(exc, context)
    #
    # if response is not None:
    #     custom_response = {
    #         "status": "conflict",
    #         "message": str(exc),
    #     }
    #     response.data = custom_response
    #
    # return response

    # for handle errors with both middleware for 500 errors and this for 409
    custom_response = {
        "status": "conflict",
        "message": str(exc),
    }

    return Response(custom_response, status=409)
