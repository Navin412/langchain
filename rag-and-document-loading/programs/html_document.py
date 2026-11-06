"""Class 57: parse supplied HTML into a Document without fetching a URL."""

from html.parser import HTMLParser

from langchain_core.documents import Document


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip_depth = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth and data.strip():
            self.parts.append(data.strip())


def html_to_document(html: str, source: str) -> Document:
    parser = VisibleText()
    parser.feed(html)
    return Document(
        page_content="\n".join(parser.parts),
        metadata={"source": source, "source_type": "html"},
    )


if __name__ == "__main__":
    sample = "<html><body><h1>Courses</h1><script>ignore()</script><p>Python at 8 AM.</p></body></html>"
    document = html_to_document(sample, "https://example.invalid/courses")
    print(document.page_content)
    assert "ignore" not in document.page_content
