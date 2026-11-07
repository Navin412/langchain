"""Class 57: HTML Document, web fetch, and a custom web BaseLoader.

Run: python practice/class57_web_documents.py
The demo serves a tiny page on localhost; pass a URL to inspect another page.
"""

import argparse
from typing import Iterator

import requests
from bs4 import BeautifulSoup
from langchain_core.document_loaders import BaseLoader
from langchain_core.documents import Document

from class53_web_loader import demo_website


def program_1_local_html(html: str, source: str) -> Document:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return Document(
        page_content=soup.get_text(" ", strip=True),
        metadata={"source": source, "source_type": "html"},
    )


def program_2_web_page(url: str) -> Document:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return program_1_local_html(response.text, url)


class CustomWebPageLoader(BaseLoader):
    def __init__(self, urls: list[str]):
        self.urls = urls

    def lazy_load(self) -> Iterator[Document]:
        for url in self.urls:
            yield program_2_web_page(url)


def program_3_custom_loader(urls: list[str]) -> list[Document]:
    return CustomWebPageLoader(urls).load()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", nargs="?")
    args = parser.parse_args()
    local = program_1_local_html("<h1>Python</h1><script>hide()</script>", "local.html")
    assert "hide" not in local.page_content
    with demo_website() as base:
        url = args.url or base + "/one"
        fetched = program_2_web_page(url)
        many = program_3_custom_loader([url, base + "/two"])
        assert len(many) == 2
        print("Local:", local)
        print("Fetched:", fetched)
        print("Custom loader:", [document.metadata for document in many])
