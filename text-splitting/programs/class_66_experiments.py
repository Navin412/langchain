"""Class 66: inspect the effects of chunk size and overlap, offline."""

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def main() -> None:
    alphabet = "ABCDEFGHIJKLMNOPQRST"

    # Programs 1–2: vary size, then overlap, while holding the other setting fixed.
    for size in (20, 10, 5):
        chunks = RecursiveCharacterTextSplitter(
            separators=[""], chunk_size=size, chunk_overlap=0
        ).split_text(alphabet)
        print(f"size={size}: {chunks}")
    for overlap in (0, 2, 4):
        chunks = RecursiveCharacterTextSplitter(
            separators=[""], chunk_size=6, chunk_overlap=overlap
        ).split_text(alphabet)
        print(f"overlap={overlap}: {chunks}")

    # The policy experiment keeps document metadata while comparing settings.
    policy = Document(
        page_content=(
            "ATTENDANCE POLICY\nEmployees report by 9 AM.\n\n"
            "LEAVE POLICY\nEmployees receive 12 casual leaves each year.\n\n"
            "WORK FROM HOME\nManager approval is required."
        ),
        metadata={"source": "company_policy.txt", "department": "HR"},
    )
    for size, overlap in ((40, 0), (80, 10), (200, 0)):
        chunks = RecursiveCharacterTextSplitter(
            chunk_size=size, chunk_overlap=overlap
        ).split_documents([policy])
        assert all(c.metadata["source"] == "company_policy.txt" for c in chunks)
        print(f"policy size={size}, overlap={overlap}: {[c.page_content for c in chunks]}")

    # FAQ and educational-note experiments: inspect whether answers stay near questions.
    faqs = (
        "Q1: What is Python? A1: Python is a programming language.\n\n"
        "Q2: What is Java? A2: Java runs on a virtual machine.\n\n"
        "Q3: What is SQL? A3: SQL queries relational databases."
    )
    for size, overlap in ((60, 0), (100, 15), (250, 0)):
        chunks = RecursiveCharacterTextSplitter(
            chunk_size=size, chunk_overlap=overlap
        ).split_text(faqs)
        print(f"FAQ size={size}, overlap={overlap}: {chunks}")
    print("Inspect chunk boundaries; chunk count alone does not measure retrieval quality.")


if __name__ == "__main__":
    main()
