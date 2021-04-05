##updated api path, engine, top p, updated top p, temp, and tokens. 


import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.65,
          top_p=1,
          max_tokens=100)

##Generate feature to benefit for product


gpt.add_example(Example("""The girl took the dog for a very long walk""",
"""The girl took the dog for a long walk."""))

gpt.add_example(Example("""The girl took the dog for a very long walk""",
"""The girl took the dog on a long walk"""))

gpt.add_example(Example("""If a robot can have rights it should have rights""",
"""If a robot can have rights, then it should have rights"""))


# Define UI configuration
config = UIConfig(description="Simplify your sentences",
                  button_text="Create",
                  placeholder="Enter your sentence here")

id = "simplify-sentences"