##bad. getting stuck on first prompt. 
##spits input back out rather than an output 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig

# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.35,
          top_p=0.36,
          max_tokens=80)

#Create new ideas for products

gpt.add_example(Example('CopyAi an AI powered copywriter for small businesses and entrepreneurs',
                        'New idea: Create an AI virtual assistant to help with scheduling meetings'))

gpt.add_example(Example('Peak design clip keep your camera securely attached to your bag',
                        'New idea: A camera case that works wih the clip'))

gpt.add_example(Example('Plant pots store your plants in beautiful pots that will liven up any room.',
                        'New idea: a self-watering plant pot'))

gpt.add_example(Example('Candle sweeet scents for your home.',
                        'New idea: a candle warmer to enjoy the candle.'))

gpt.add_example(Example('Portrait photography sessions.',
                        'New idea: create a photobook for clients.'))

gpt.add_example(Example('dog walking services.',
                        'New idea: offer overnight care.'))

gpt.add_example(Example('leather camera bag',
                        'New idea: special leather cleaning product just for this bag.'))

# Define UI configuration
config = UIConfig(description="Generate new ideas for products",
                  button_text="Generate",
                  placeholder="Product (optional), description of product")

id = "next-product"
