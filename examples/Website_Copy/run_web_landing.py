##updated api path, engine, top p, updated top p, temp, and tokens. 
##Runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=.5,
          max_tokens=100)


##Generate Landing Page Hero Text

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Your AI-Powered Copywriter"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""AI-powered copywriter for business"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Get professional copy for your website, sales page and social media messages in less"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Create sales generating content in minutes."""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""We write your content in less than 60 seconds."""))

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""The Internet Needs a New Kind of Website"""))

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""Good Websites Make Money"""))

# Define UI configuration
config = UIConfig(description="Create Landing Page Hero Text.",
                  button_text="Create",
                  placeholder="Enter a product (optional) and a description of the product.")

id = "web-landing-app"