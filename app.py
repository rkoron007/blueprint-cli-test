import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"Hello from a Blueprint created with the Render CLI! ({os.environ.get('GREETING', 'no greeting set')})\n"
            f"APP_VERSION: {os.environ.get('APP_VERSION', 'unset')}\n"
            f"SECRET_TOKEN set: {bool(os.environ.get('SECRET_TOKEN'))} (length {len(os.environ.get('SECRET_TOKEN', ''))})\n"
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    print(f"Listening on 0.0.0.0:{port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
