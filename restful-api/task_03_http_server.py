"""
Simple API using Python's http.server module.

This module sets up a basic HTTP server that handles GET requests
and serves different responses based on the requested endpoint:
    - /       : Returns a plain text greeting message.
    - /data   : Returns a sample JSON dataset.
    - /status : Returns the API status ("OK").
    - /info   : Returns API version and description as JSON.
    - Any other endpoint returns a 404 Not Found error.
"""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """A custom HTTP request handler for a simple REST API."""

    def do_GET(self):
        """Handle GET requests and route them to the appropriate endpoint."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8000), SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    server.serve_forever()
