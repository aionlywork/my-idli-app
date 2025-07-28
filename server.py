from http.server import BaseHTTPRequestHandler, HTTPServer
import os

HOST = "localhost"
PORT = 8080

class IdliHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        file_path = "." + self.path
        ext = os.path.splitext(self.path)[1]

        if ext == ".html":
            content_type = "text/html"
        elif ext == ".css":
            content_type = "text/css"
        elif ext == ".js":
            content_type = "application/javascript"
        elif ext == ".mp3":
            content_type = "audio/mpeg"
        else:
            content_type = "application/octet-stream"

        try:
            with open(file_path, "rb") as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, f"File not found: {self.path}")

if __name__ == "__main__":
    print(f"Serving Idli Timer at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), IdliHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
