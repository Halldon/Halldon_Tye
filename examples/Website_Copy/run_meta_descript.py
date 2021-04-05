##updated api path, engine, top p, updated top p, temp, and tokens. 
##Runs as expected 
##must enter product and a descript. 

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



#Create a meta description 


gpt.add_example(Example("""Rooting hormone, promotes root development.""",
"""These natural rooting hormones will promote the development of roots on most popular home, garden and greenhouse plants."""))

gpt.add_example(Example("""Rooting hormone, promotes root development.""",
"""Rooting hormone aids the development of roots on most popular home, garden and greenhouse plants."""))

gpt.add_example(Example("""Rooting hormone, promotes root development.""",
"""Root-A-Hormone™ is an all natural plant rooting hormone with bio-stimulants formulated to promote new root growth on most popular home and 
greenhouse plant varieties."""))

gpt.add_example(Example("""Rooting hormone, promotes root development.""",
"""Rooting hormone helps you start seeds and cuttings easily by helping them develop roots faster. Also helps plant transplants 
become established more quickly, so they can get growing."""))

gpt.add_example(Example("""Rooting hormone, promotes root development.""",
"""Our quality, trusted rooting products provide home gardeners with new ways to create more green."""))

gpt.add_example(Example("""Rooting hormone, promotes root development.""",
"""Rooting hormone is also used to make cuttings of rooted plants and in general to stimulate root growth."""))

gpt.add_example(Example("""Detangle Spray, softens and detangles hair.""",
"""Detangle spray prevents tangles and leaves hair moisturized. This special detangler spray lubricates 
hair strands to make styling easier. Hair feels soft and lightly nourished. Smells great! For all hair types."""))

gpt.add_example(Example("""Detangle Spray, softens and detangles hair.""",
"""Detangle Hair Milk Spray helps you eliminate all tangles without the need for a comb or brush. 
This special milky spray lubricates hair strands to make styling easier and more manageable. Hair feels soft, smooth and lightly nourished."""))

gpt.add_example(Example("""Detangle Spray,softens and detangles hair.""",
"""Detangle and deters breakage with this lightweight spritz that helps to smooth hair"""))







# Define UI configuration
config = UIConfig(description="Create a Meta Description",
                  button_text="Create",
                  placeholder="Product, Description of product.")

id = "meta-description"