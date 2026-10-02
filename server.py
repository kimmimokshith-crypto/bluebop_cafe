"""
THE BLUEBOP CAFE & BAR — LOCAL DEVELOPMENT SERVER
Supports HTTP 206 Partial Content (Range Requests) for smooth video scrubbing.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

class RangeRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RangeRequestHandler)
    print(f"===========================================================")
    print(f" THE BLUEBOP CAFE & BAR — WEB SERVER RUNNING")
    print(f" URL: http://localhost:{port}/")
    print(f" Serving directory: {os.getcwd()}")
    print(f" Video scrub Range requests enabled.")
    print(f"===========================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server.")
        httpd.server_close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
