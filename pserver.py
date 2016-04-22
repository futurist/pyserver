#!/usr/bin/env python2

import posixpath
import urlparse
import BaseHTTPServer
import CGIHTTPServer
# import cgitb; cgitb.enable()  ## This line enables CGI error reporting

class TypeHandler(CGIHTTPServer.CGIHTTPRequestHandler, object):
    """Route based on file type of request."""

    def is_cgi(self):
        """Determine whether to execute as CGI based on extension."""
        ext = posixpath.splitext(urlparse.urlsplit(self.path).path)[-1]
        check = super(TypeHandler, self).is_cgi() if ext.lower() in ('.py','.pyw') else False
        # print "sdf", self.path,ext , check
        return check

server = BaseHTTPServer.HTTPServer
handler = TypeHandler
server_address = ("", 8000)
handler.cgi_directories = ["/", '/cgi-bin']

httpd = server(server_address, handler)
httpd.serve_forever()
