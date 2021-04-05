##updated api path, engine, top p , deleted lingering quotation mark, updated temp and top_p 
##Runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.6,
          top_p=.5,
          max_tokens=100)

#Create a call to action for product

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""Sign up now and use CopyAi to automate your company blog!"""))

gpt.add_example(Example("""CopyAi, an AI powered copywriter for small businesses and entrepreneurs""",
"""Try CopyAi risk-free for 10 days"""))


gpt.add_example(Example("""rooting hormone that will build stronger roots faster.""",
"""Get 3X faster plant growth today (CLICK HERE)."""))


gpt.add_example(Example("""rooting hormone that will build stronger roots faster.""",
"""Go check out the best rooting hormone"""))

# Define UI configuration
config = UIConfig(description="Create a Call-To-Action for your product.",
                  button_text="Create",
                  placeholder="Product (optional), description of product")

id = "call-to-action"