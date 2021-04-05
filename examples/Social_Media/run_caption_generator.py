##updated api path, engine, top p 
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

#Create a caption for post 

gpt.add_example(Example("""the mountains""",
"""It’s a reflection of how I live my life. Every day is an adventure, and to me, being in the mountains is as exciting as it gets."""))

gpt.add_example(Example("""the mountains""",
"""It’s not the mountain we conquer, but ourselves. – Sir Edmund Hillary”⁣ .⁣"""))

gpt.add_example(Example("""the mountains""",
"""Getting back to the roots, rejuvenating in nature. 🌲🏔⁣"""))

gpt.add_example(Example("""tips for writing better code""",
"""Now that you’ve spent some time learning Python, it’s time to try writing some code. 
You’ll learn more from planning out your code before writing it than any other method. 
Develop an approach to coding that works for⁣ you"""))

gpt.add_example(Example("""tips for writing better code""",
"""Work smarter, not harder, to speed up the development cycle. Write better code."""))

# Define UI configuration
config = UIConfig(description="Create a caption for your social media post",
                  button_text="Create",
                  placeholder="What is your post about?")

id = "caption-generator"