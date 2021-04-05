##updated api path, engine, top p
##Runs as expected 
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.7,
          top_p=1,
          max_tokens=100)

#Create a high converting sales copy for websites


gpt.add_example(Example("""Buffer, Social Media management platform""",
"""“Tell your brand’s story and grow your audience with a publishing, analytics, and engagement platform you can trust."""))


gpt.add_example(Example("""WK Leads, Lead generation software to find qualified leads in your market.""",
"""“Get direct access to decision makers from 30M+ companies in less than 5 minutes with WK Leads."""))

gpt.add_example(Example("""Tye, An AI helping users make more creative sales copy""",
"""“A chatbot that helps you create better, more engaging sales pages and email campaigns in minutes."""))



# Define UI configuration
config = UIConfig(description="Create high converting sales copy for your website.",
                  button_text="Create",
                  placeholder="Product, Product description")

id = "sales_copy"