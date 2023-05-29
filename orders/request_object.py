from . import models

def RequestObjectMiddleware(get_response):
    # one time configuration and initialization


    def middleware(request):
        # code to be executed for each request befor
        # the view (and later middlware) are called
        models.request_object = request

        response = get_response(request)

        # code to be executed for each request/response after
        #  the view is called

        return response
    
    return middleware