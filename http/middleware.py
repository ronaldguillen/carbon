"""
The following is Runtime Code and is subject to all restrictions on
such code as contained in the End User License Agreement accompanying
this product.
"""
__author__ = "Ronald Guillen"
__copyright__ = "Copyright (C) 2015 Spark. All Rights Reserved."
__license__ = "Spark Core License"
__version__ = "0.9"

from carbon.http.headers import HTTP_HEADER_CONTENT_TYPE, HTTP_HEADER_ACCEPT

class ContentTypeMiddleware(object):
    def process_request(self, request):
        # Get content-type from request and add shorcuts.
        if HTTP_HEADER_CONTENT_TYPE in request.META:
            request.content_type = request.META['CONTENT_TYPE']
        else:
            request.content_type = None

class AcceptMiddleware(object):
    def process_request(self, request):
        if HTTP_HEADER_ACCEPT in request.META:
            request.http_accept = request.META['HTTP_ACCEPT']
        else:
            request.http_accept = None