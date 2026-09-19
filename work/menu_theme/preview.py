"""Serve the retired theme preview notice on localhost."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit
import argparse

ASSETS = {
    "/": Path(__file__).with_suffix(".html"),
}
RETIRED_IMAGES = {"/a.png", "/b.png", "/c.png", "/face.png", "/outfit.png"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urlsplit(self.path).path
        if route in RETIRED_IMAGES:
            self.send_error(410, "This preview has been retired")
            return
        path = ASSETS.get(route)
        if path is None or not path.is_file():
            self.send_error(404)
            return
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8" if path.suffix == ".html" else "image/png")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *_args):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8796)
    options = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", options.port), Handler)
    print(f"Theme preview: http://127.0.0.1:{options.port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
