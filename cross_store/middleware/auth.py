from django.shortcuts import redirect


def login_requested(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('customer'))
        return_url = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
            return redirect(f'login?return_url={return_url}')

        response = get_response(request)
        return response

    return middleware
