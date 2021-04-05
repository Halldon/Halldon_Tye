##resolved errors 
#adding in top_p 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig

# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.9,
          top_p = .36,
          max_tokens=40)

#Create a growth ideas generator

gpt.add_example(Example('leather camera strap',
'New idea: promote prints with a group of people you\'re partnered with as a collaborative promotion'))

gpt.add_example(Example('plant pot',
'New idea: offer to include a free cutting of a plant when customers purchases the pot'))

gpt.add_example(Example('leather sunglasses case',
'New idea: offer small container of leather cleaner with purchase.'))

gpt.add_example(Example('candles made from soy wax and essential oils',
'New idea: include a small sized candle of a new scent when customer purchases a regular sized candle.'))

gpt.add_example(Example('dog walking services',
'New idea: market to certain age-group of people who may need this service.'))

gpt.add_example(Example('custom website design',
'New idea: start a referall program for customers who refer their friends.'))

gpt.add_example(Example('running shoes',
'New idea: Customer gets a free pair of socks with running shoes purchase.'))

gpt.add_example(Example('1978 35mm film camera',
'New idea: include a roll of film with the camera.'))

gpt.add_example(Example('coffee bean grinder',
'New idea: host a workshop about the different brewing methods of coffee.'))

# Define UI configuration
config = UIConfig(description="Generate new ideas for the growth of your product",
                  button_text="Generate",
                  placeholder="Product (optional), description of product")

id = "growth-ideas"
