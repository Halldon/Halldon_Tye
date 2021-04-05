##updated api path, engine, top p 
##Runs as expected so long as iunput has enough detail.
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=1,
          max_tokens=100)

##Generate marketing angles for product

gpt.add_example(Example("""Bento Lunch Box Container, slim design but it is also more than enough space, 
sometimes too much. The biggest plus is that it is BPA free and FDA approved. A huge win when trying to eat clean!""",
"""Spacious. Yet Slim."""))

gpt.add_example(Example("""Bento Lunch Box Container, slim design but it is also more than enough space, 
sometimes too much. The biggest plus is that it is BPA free and FDA approved. A huge win when trying to eat clean!""",
"""Our bento lunch box containers are perfect for meals on the go. Wherever your kids are going this school year, 
we’ve got you covered for more than just a sandwich."""))

gpt.add_example(Example("""Inflatable Lounger Air Sofa Hammock, Portable Anti-Air Leaking & Waterproof Pouch Couch 
and Beach Chair Camping Accessories for Parties, Travel, Camping, Picnics, Pool""",
"""Lets be honest. Portable lounge chairs are great. We all know it. Here, have everything you need to make your portable lounge even better."""))

gpt.add_example(Example("""Inflatable Lounger Air Sofa Hammock, Portable Anti-Air Leaking & Waterproof Pouch Couch 
and Beach Chair Camping Accessories for Parties, Travel, Camping, Picnics, Pool""",
"""Inflates in seconds and goes from flat to comfy. Take a load off without having to lift a finger."""))

gpt.add_example(Example("""Inflatable Lounger Air Sofa Hammock, Portable Anti-Air Leaking & Waterproof Pouch Couch 
and Beach Chair Camping Accessories for Parties, Travel, Camping, Picnics, Pool""",
"""It’s a couch that comes in a pouch."""))

gpt.add_example(Example("""LED Ring Light, 6" Selfie Lamp 3 Light Modes & 10 Adjustable Brightness with 
Tripod Stand & Cell Phone Holder for YouTube, Facebook, Live Stream, Makeup and More""",
"""Light up your world with this selfie ring light that is guaranteed to attract attention."""))

gpt.add_example(Example("""LED Ring Light, 6" Selfie Lamp 3 Light Modes & 10 Adjustable Brightness with 
Tripod Stand & Cell Phone Holder for YouTube, Facebook, Live Stream, Makeup and More""",
"""- The ring-shaped light provides a softer, more natural lighting than regular bulbs. Perfect for all your make-up 
selfies; - Works great with any phone or camera to provide a perfect lighting for any photo and video; - Saves you 
money as it is energy efficient and Long lasting lifespan of 10,000 hours."""))


# Define UI configuration
config = UIConfig(description="Create marketing angles for your product",
                  button_text="Create",
                  placeholder="Enter product description and name")

id = "marketing-angles"