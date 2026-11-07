# Class 4: searchable PDF text

Source: [original PDF](../../sources/pdfs/class4-langchain.pdf)

This is raw text from the PDF's text layer, kept by page for searching and copying. It is not a checked Python program. For runnable exercises, use the [practice guide](../README.md). Consult the PDF for layout, images and exact code.

## Page 1

~~~~text
    LangChain & Agentic AI – From Basics to Advanced
                             demo- 4 Notes


LangChain is a framework for building applications using Large
Language Models.


company chatbot:

   take user's question
   create a proper prompt
   communicate with LLM

   search company documents
   remember conversation history
   call some external tools

   retrieve information
   process the result
   finally give answer

Many components are involved in this application.
~~~~

## Page 2

~~~~text
Lang ---> refers Language Models
Chain --->Connect mult      iple components together


Question --->Retriever -->Documents -->Prompt --->Model --->
Answer


LangChain as an Orchestration Layer:
------------------------------------
LangChain help us connect and coordinate the components of
LLM application. Hence LC consider as Orchestration Layer for
LLM Applications. The components can be:
  Model
  prompt

  Memory/Histroy
  Documents
  Vector Database

  Tools
  Agents
~~~~

## Page 3

~~~~text
  etc



LLM = Engine
LangChain = System connecting and coordinating the parts
around that engine.



LangChain as abstraction layer:
LangChain can provide an abstraction layer between our
application and differet underlying services


Abstraction vs Orchestration:

-----------------------------
Abstraction: Hide or simplify complexity
   Give an easy/common way to interact with different
components
~~~~

## Page 4

~~~~text
Orchestration : Coordinate multiple components
   First prepare the prompt, then call the model, then parse the
output


Abstraction simplifies. Orchestration coordinates.


LangChain can help us with both.


LangChain EcoSystem:

--------------------
1. LangChain-->provides building blocks for developing LLM
based applications
2. LangGraph-->Controlled and stateful workflows/agents

3. LangSmith-->Trace,debug and observability, monitoring and
Evaluate LLM applic     ations
~~~~
