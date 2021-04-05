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



##Generate Microcopy

gpt.add_example(Example("""Thank you for signing up!""",
"""Thanks for signing up to The Hustle."""))


gpt.add_example(Example("""Thank you for signing up!""",
"""Thanks for joining us."""))

gpt.add_example(Example("""Thank you for signing up!""",
"""We have sent a confirmation email to your inbox."""))

gpt.add_example(Example("""Thank you for signing up!""",
"""Thank you! We'll start sending your daily email soon."""))

gpt.add_example(Example("""items in cart""",
"""Don't forget about the items in your cart!"""))

gpt.add_example(Example("""favorited item""",
"""This item you favorited is on sale!"""))


# Define UI configuration
config = UIConfig(description="Create Microcopies for your website.",
                  button_text="Create",
                  placeholder="What is the microcopy for? (e.g.: thanks for signing up!")

id = "microcopy-app"