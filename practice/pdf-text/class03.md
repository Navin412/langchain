# Class 3: searchable PDF text

Source: [original PDF](../../sources/pdfs/class3-langchain.pdf)

This is raw text from the PDF's text layer, kept by page for searching and copying. It is not a checked Python program. For runnable exercises, use the [practice guide](../README.md). Consult the PDF for layout, images and exact code.

## Page 1

~~~~text
    LangChain & Agentic AI – From Basics to Advanced
                            demo- 3 Notes


Without LangChain:
-----------------
We can develop AI based applications.


But we (Our Application) are responsible for



    Application
1. Prompt Management
2. Model Management

3. Conversation History and State Management
4. Handling our own private data
5. Tool Management like Caluclator, Search, Database

6. Agentic Activities
~~~~

## Page 2

~~~~text
With LangChain:
--------------
Application

  |
LangChain
  |

1. Prompt Management
2. Model Management
3. Conversation History and State Management
4. Handling our own private data

5. Tool Management like Caluclator, Search, Database
6. Agentic Activities



LangChain provides useful building blocks, abstractions and
Integrations for creating LLM applications.

import os # os is module
~~~~

## Page 3

~~~~text
from langchain_openai import ChatOpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #function


llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

question = input("Enter the question: ")


response = llm.invoke(question)

print(response.content)


import os
from langchain_google_genai import ChatGoogleGenerativeAI


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
~~~~

## Page 4

~~~~text
    model="gemini-3.6-flash",
    google_api_key=GOOGLE_API_KEY
)


question = input("Enter the question: ")

response = llm.invoke(question)


#print(response.content)
print(response.content[0]["text"])
~~~~
