"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

##File has passed checks 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig



# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('Neural networks are like',
                        'genetic algorithms in that both are systems that learn from experience.'))
gpt.add_example(Example('Social media is like',
                        'a market in that both are systems that coordinate the actions of many individuals.'))
gpt.add_example(Example(
    'A2E is like', 'lipofuscin in that both are byproducts of the normal operation of a system.'))
gpt.add_example(Example('Haskell is like',
                        'LISP in that both are functional languages.'))
gpt.add_example(Example('Quaternions are like',
                        'matrices in that both are used to represent rotations in three dimensions.'))
gpt.add_example(Example('Quaternions are like',
                        'octonions in that both are examples of non-commutative algebra.'))

# Define UI configuration
config = UIConfig(description="Analogies generator",
                  button_text="Generate",
                  placeholder="Memes are like")

id = "analogies-application"
