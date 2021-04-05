##updated api path, engine, top p , deleted lingering quotation mark 
##Runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.8,
          top_p=1,
          max_tokens=100)

          
#Create bullet points for product description 

gpt.add_example(Example("""an AI powered copywriter for small businesses and entrepreneurs """,
"""-Small businesses and startups find it hard to create content for their unique voice
-An AI powered copywriter solves this issue
-Create engaging written content in minutes, instead of hours or days"""))

gpt.add_example(Example("""an AI powered copywriter for small businesses and entrepreneurs """,
"""-AI powered copywriter
-Write better ads, social media posts, and website content that converts
-Use it to improve all aspects of your ecosystem--ads, social and website content"""))

gpt.add_example(Example("""an AI powered copywriter for small businesses and entrepreneurs """,
"""-AI powered copywriter
-Work faster and smarter not harder
-Save time and money with a copywriter who can write better than you ever could."""))

gpt.add_example(Example("""an AI powered copywriter for small businesses and entrepreneurs """,
"""-Check out how AI is used in Copywriter.io
-Read about why you should use an AI copywriter
-Discover how to get a 25% discount"""))

# Define UI configuration
config = UIConfig(description="Create bullet points for your product description",
                  button_text="Create",
                  placeholder="Please describe the product")

id = "bullet-point-ads"