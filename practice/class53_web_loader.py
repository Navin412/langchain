"""Class 53: four WebBaseLoader examples using a tiny local website.

Run: python practice/class53_web_loader.py
"""

from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from threading import Thread

os.environ.setdefault("USER_AGENT", "LangChainPractice/1.0")
from langchain_community.document_loaders import WebBaseLoader


PAGES = {
    "/one": b"<html><title>First</title><body><h1>Python</h1><p>Learn text loaders.</p></body></html>",
    "/two": b"<html><title>Second</title><body><h1>LangChain</h1><p>Load two pages.</p></body></html>",
}


@contextmanager
def demo_website():
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            body = PAGES.get(self.path)
            if body is None:
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *_args):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join()
        server.server_close()


def program_1_basic(url: str):
    return WebBaseLoader(web_path=url, show_progress=False).load()


def program_2_parameters(url: str):
    return WebBaseLoader(
        web_path=url,
        requests_kwargs={"timeout": 5},
        bs_get_text_kwargs={"separator": " ", "strip": True},
        show_progress=False,
    ).load()


def program_3_multiple_urls(base: str):
    return WebBaseLoader(web_paths=(base + "/one", base + "/two"), show_progress=False).load()


def program_4_local_demo():
    with demo_website() as base:
        basic = program_1_basic(base + "/one")
        tuned = program_2_parameters(base + "/one")
        many = program_3_multiple_urls(base)
        assert len(basic) == len(tuned) == 1 and len(many) == 2
        assert "Python" in basic[0].page_content
        assert "LangChain" in many[1].page_content
        return basic, tuned, many


if __name__ == "__main__":
    one, tuned, many = program_4_local_demo()
    print("Basic:", one[0].page_content.strip())
    print("With parameters:", tuned[0].page_content.strip())
    print("Two page sources:", [document.metadata["source"] for document in many])
