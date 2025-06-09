#!/usr/bin/python3
"""Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer


PORT = 8000

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        res_message = "Hello, this is a simple API!"
        self.wfile.write(bytes(res_message, "utf-8"))


server_add = ('', 8000)
httpd = HTTPServer(server_add, myHandler)
httpd.serve_forever()