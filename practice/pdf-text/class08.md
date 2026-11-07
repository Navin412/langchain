# Class 8: searchable PDF text

Source: [original PDF](../../sources/pdfs/class8-langchain.pdf)

This is raw text from the PDF's text layer, kept by page for searching and copying. It is not a checked Python program. For runnable exercises, use the [practice guide](../README.md). Consult the PDF for layout, images and exact code.

## Page 1

~~~~text
     LangChain & Agentic AI – From Basics to Advanced
                              demo- 8 Notes


static prompt vs Dynamic Prompt:
--------------------------------
static prompt:

   Explain Python in simple english
 It is fixed and non changeable

Dynamic Prompt:

    It is not fixed and changeable based user requirement

    Explain { Topic} in simple english



{ Topic} --->input variable or placeholder
~~~~

## Page 2

~~~~text
Final prompt = Template (Dynamic Prompt) + Variable values

PromptTemplate class:
--------------------

It is used to create reusable text prompts with variables

---------------

from langchain_core.prompts import PromptTemplate
prompt_template = PromptTemplate.from_template("Explain
{topic} in Simple English")
#print(type(prompt_template))

#print(prompt_template)
#print(prompt_template.input_variables)



result = prompt_template.invoke(
  {
     "topic":"Python"
  }
~~~~

## Page 3

~~~~text
)
print(type(result))
print(result)
print(result.text)

print(result.to_string())

=====================

import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")

)

prompt_template = PromptTemplate.from_template("Explain
{topic} in Simple English")
~~~~

## Page 4

~~~~text
topic = input('Enter Topic:')
result = prompt_template.invoke(
  {
     "topic":topic

  }
)
ai_message = llm.invoke(result)

print(ai_message.content)


User ---> PromptTemplate --->Final Prompt -->LLM ---
>AIMessage -->Response

===================

PromptTemplate  invoke() ===>To format the prompt ie to
replace variables with original values

ChatModel invoke() ==>To submit prompt to llm and to get the
response
~~~~

## Page 5

~~~~text
=========================================
# Recipe Assistant
import os


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")

)

template = PromptTemplate.from_template(
    "Give me a simple recipe for {dish}. Explain it step by step."

)
dish = input("Enter dish name: ")
~~~~

## Page 6

~~~~text
prompt = template.invoke(
    {
        "dish": dish
    }

)
response = llm.invoke(prompt)


print(response.content)

============
# Topic Explainer

import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


llm = ChatOpenAI(
    model="gpt-4o-mini",
~~~~

## Page 7

~~~~text
    api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(

    """
    Explain {topic} to a beginner.



  Use:
    - Very simple English
    - 5 important points

    - One real-life example
    """
)


topic = input("Enter topic: ")

prompt = template.invoke(
~~~~

## Page 8

~~~~text
    {
        "topic": topic
    }
)


response = llm.invoke(prompt)
print(response.content)


========================
# Topic Explainer
import os


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
~~~~

## Page 9

~~~~text
)

template = PromptTemplate.from_template(
    """

    Explain {topic} to a beginner.



  Use:
    - Very simple English
    - 5 important points
    - One real-life example

    """
)

topic = input("Enter topic: ")


prompt = template.invoke(
    {
~~~~

## Page 10

~~~~text
        "topic": topic
    }
)


response = llm.invoke(prompt)
print(response.content)
~~~~
