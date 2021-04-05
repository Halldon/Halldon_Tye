#updated api route, top p, engine
#works as expected 

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


#Create thank you notes


gpt.add_example(Example("""Customer, for their purchase""",
"""Thank you so much for your purchase. Having your business will help us expand our customer base which will have a huge impact on us."""))

gpt.add_example(Example("""Customer, for their purchase""",
"""Thank you so much for your purchase. I hope you love this new product!"""))

gpt.add_example(Example("""Customer, for their purchase""",
"""Thank you so much for your purchase. I hope you love this new product!"""))

gpt.add_example(Example("""Customer, for their feedback""",
"""Thank you for their feedback for our new product. This feedback is an important part of the process to create a great product that people use."""))

gpt.add_example(Example("""Customer, for their feedback""",
"""Thank you for your feedback. Your post helps me to know what parts of my business I need to improve on and where I am doing well. 
I care about your success as much as my own. Please reach out to me if you have any questions about [my company]."""))


# Define UI configuration
config = UIConfig(description="Create a Thank You Note",
                  button_text="Create",
                  placeholder="Who are we thanking, what are we thanking them for? (I.e.: Customer, for their purchase.")

id = "thank-you-note"