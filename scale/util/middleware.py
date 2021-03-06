'''Common middleware classes used in the web server configuration.'''


class MultipleProxyMiddleware(object):
    '''Rewrites the proxy headers so that only the first the proxy forwarded host is used.

    By default Django, does not support forwarding the server host name when sitting behind multiple proxy servers.
    Without this middleware the host name returned to the client will contain both proxy names delimited by a comma,
    which will not redirect properly. The original example code this class was based on used the host header value from
    the most recent proxy server. Since the first proxy server in our infrastructure is the host name used by external
    users however, we want to always take that name instead.

    Code derived from the Django documentation for "Request and response objects", HttpRequest.get_host() method.
    '''
    FORWARDED_FOR_FIELDS = [
        'HTTP_X_FORWARDED_FOR',
        'HTTP_X_FORWARDED_HOST',
        'HTTP_X_FORWARDED_SERVER',
    ]

    def process_request(self, request):
        '''Rewrite forwarded host headers to support multiple proxy servers.'''
        for field in self.FORWARDED_FOR_FIELDS:
            if field in request.META:
                if ',' in request.META[field]:
                    parts = request.META[field].split(',')
                    request.META[field] = parts[0].strip()
