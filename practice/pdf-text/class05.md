# Class 5: searchable PDF text

Source: [original PDF](../../sources/pdfs/class5-langchain.pdf)

This is raw text from the PDF's text layer, kept by page for searching and copying. It is not a checked Python program. For runnable exercises, use the [practice guide](../README.md). Consult the PDF for layout, images and exact code.

## Page 1

~~~~text
    LangChain & Agentic AI – From Basics to Advanced
                             demo- 5 Notes


Understanding Messages and Message Types:
-----------------------------------------

Message: It is a structured unit of communication in a
conversation with a chat model.


3 types of Messages:

1. SystemMessage--->Instructions/context that guide the
model. It decides behaviour of the Model.

2. HumanMessage--->Message from human/user
3. AIMessage--->Response from Model

Message Object vs content:

----------------------------
print(message)  -->It prints message object representation |
Complete Message object
~~~~

## Page 2

~~~~text
print(message.content)  -->It prints specific content of the
message | Actual Message content


from langchain_core.messages import SystemMessage,
HumanMessage, AIMessage
system_message = SystemMessage(content = "You are
experienced Python Teacher")

human_message = HumanMessage(content = "What is
Python?")
ai_message = AIMessage(content = "Python is a wonderful
prorgamming language")

#print(system_message)
#print(system_message.content)
#print(human_message)

#print(human_message.content)
print(ai_message)
print(ai_message.content)
~~~~

## Page 3

~~~~text
[
   system message,

   human message,
   ai message,
   human message,
   ai message,

   human message
   ....
]



import os # os is module
from langchain_openai import ChatOpenAI

from langchain_core.messages import
SystemMessage,HumanMessage

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") #function
~~~~

## Page 4

~~~~text
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

system_message = SystemMessage(content="You are
Experienced Python Trainer")
human_message = HumanMessage(content="Explain about
Python in a single line")
ai_msg = llm.invoke([system_message,human_message])

#print(type(ai_msg))
print(ai_msg)
#print(ai_msg.content)



system_message = SystemMessage(content="You are
Experienced Life Skills Coach")

human_message = HumanMessage(content="Explain about
Law of Attraction")
#ai_msg = llm.invoke([system_message,human_message])
#print(type(ai_msg))

#print(ai_msg)
~~~~

## Page 5

~~~~text
#print(ai_msg.content)
~~~~
