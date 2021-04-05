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

##Create subheader

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""Get a website that brings you clients. Halldon enables businesses to build and grow their online presence 
by providing smart and affordable websites with nationwide support."""))

gpt.add_example(Example("""Halldon, We create websites that make you money.""",
"""Our web design specialists can craft a stunning looking website for your business that will grow your revenue and boost your profits."""))

gpt.add_example(Example("""root your plants faster with this rooting hormone""",
"""Root enhancer for cuttings and strong growth when rooting plants"""))

gpt.add_example(Example("""root your plants faster with this rooting hormone""",
"""Get more root depth and diameter with easy to use liquid hormones."""))




# Define UI configuration
config = UIConfig(description="Create subheaders for your website",
                  button_text="Create",
                  placeholder="Enter a product (optional), describe your product.")

id = "subheader-app"
