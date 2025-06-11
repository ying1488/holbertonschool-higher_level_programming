#!/usr/bin/python3
"""Set up a basic web server using the http.server module.
Handle different types of HTTP requests (GET, POST, etc.).
Serve JSON data in response to specific endpoints.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = 8000

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        res_data = {
            "name": "John", 
            "age": 30, 
            "city": "New York"
        }

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            res_message = "Hello, this is a simple API!"
            self.wfile.write(bytes(res_message, "utf-8"))

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(res_data).encode('utf-8'))

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            res_info = {
            "version": "1.0", 
            "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(res_info).encode('utf-8')) 

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            res_message = "OK"
            self.wfile.write(bytes(res_message, "utf-8"))

        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            res_message = "Endpoint not found"
            self.wfile.write(bytes(res_message, "utf-8"))

server_add = ('', 8000)
httpd = HTTPServer(server_add, myHandler)
httpd.serve_forever()