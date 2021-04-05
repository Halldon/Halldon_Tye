##updated api path, engine, top p, updated top p, temp, and tokens. 
##Runs as expected 

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



#Create a blog outline


gpt.add_example(Example("""Pandas for python, 3 reasons to use the Pandas package in python""",
"""1. It makes data analysis and manipulation easy
2. It allows you to quickly create charts
3. Enables data exchange between programs in Python"""))

gpt.add_example(Example("""Pandas for python, 3 reasons to use the Pandas package in python""",
"""1. It is faster
2. It is easier to use
3. It makes data manipulation easier and more fun"""))

gpt.add_example(Example("""Pandas for python, 3 reasons to use the Pandas package in python""",
"""1. Working with numbers
2. Get data out of the spreadsheet
3. Visualize data"""))

gpt.add_example(Example("""Houseplants for beginners, 5 houseplants for beginners""",
"""
1.Philodendron  
2. Jade plant  
3. Devils ivy  
4. Snake plant  
5. English ivy """))

gpt.add_example(Example("""Houseplants for beginners, 5 houseplants for beginners""",
"""
1. Snake plant
2. Geranium
3. Fern
4. Aloe Vera
5. Begonia """))


# Define UI configuration
config = UIConfig(description="Create a Listicle",
                  button_text="Create",
                  placeholder="Enter your Topic, What are you making a list for? (i.e.: 3 reasons why AI is changing the marketing game.")

id = "listicle-app"