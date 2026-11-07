"""Class 48: five Document exercises from the source PDF, adapted for practice.

Run: python practice/class48_documents.py
"""

from langchain_core.documents import Document


def program_1_first_document() -> Document:
    return Document(page_content="Python is a popular programming language.")


def program_2_content_and_metadata() -> Document:
    return Document(
        page_content="Students must carry ID cards.",
        metadata={"source": "student_rules.txt", "category": "school"},
    )


def program_3_missing_metadata() -> Document:
    document = Document(page_content="No source was given.")
    print("Source if present:", document.metadata.get("source", "unknown"))
    return document


def program_4_multiple_documents() -> list[Document]:
    return [
        Document(page_content="Rule 1: arrive on time", metadata={"source": "rules.txt"}),
        Document(page_content="Rule 2: bring a notebook", metadata={"source": "rules.txt"}),
    ]


def program_5_master() -> list[Document]:
    documents = [program_1_first_document(), program_2_content_and_metadata()]
    documents.extend(program_4_multiple_documents())
    for index, document in enumerate(documents, 1):
        print(index, repr(document.page_content), document.metadata)
    return documents


if __name__ == "__main__":
    program_3_missing_metadata()
    assert len(program_5_master()) == 4
