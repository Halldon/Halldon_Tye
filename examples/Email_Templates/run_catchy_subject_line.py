##updated api path, engine, top p
##Works best if given a proper description, otherwise it will just spit out same input.

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


#Create a catchy e-mail subject line

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""SOFT HAIR!"""))

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""The best hairspray to ever walk the earth!?"""))

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""Your hair can look this good, too."""))

gpt.add_example(Example("""Detangle Spray, This special milky detangler spray. A few spritzes lubricates hair strands to make styling easier. 
Hair feels soft and lightly nourished. For all hair types.""",
"""How Your Hair Will Love You"""))

gpt.add_example(Example("""diamond ring, This lovely promise ring for her shimmers with a diamond accent set in a pretty sterling silver band.""",
"""It's about to get real between you two. #engagement"""))

gpt.add_example(Example("""diamond ring, A cluster of round diamonds is flanked by rows of additional round diamonds in this elegant 
engagement ring for her, crafted in 10K white gold. More diamonds grace the profile for a touch of sparkle from every angle. 
The ring totals 1/3 carat in diamond weight.""",
"""Her dazzling smile is only outshone by her new ring!"""))

gpt.add_example(Example("""diamond ring, A cluster of round diamonds is flanked by rows of additional round diamonds in this elegant 
engagement ring for her, crafted in 10K white gold. More diamonds grace the profile for a touch of sparkle from every angle. 
The ring totals 1/3 carat in diamond weight.""",
"""Sheer sparkle in a traditional style"""))

gpt.add_example(Example("""diamond ring, A cluster of round diamonds is flanked by rows of additional round diamonds in this elegant 
engagement ring for her, crafted in 10K white gold. More diamonds grace the profile for a touch of sparkle from every angle. 
The ring totals 1/3 carat in diamond weight.""",
"""Diamonds found in nature are 100% natural and conflict-free."""))




# Define UI configuration
config = UIConfig(description="Create a catchy e-mail subject line",
                  button_text="Create",
                  placeholder="Product (optional), Description of product.")
id = "catchy-subject-line"