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

#Create confirmation e-mails

gpt.add_example(Example("""Order has been placed""",
"""Thank you for your order! We'll get right on it! YOUR ORDER HAS BEEN PLACED. 
A confirmation email has been sent to you. If you do not receive this email, 
please try resending it to confirmmyorder@theproductfeedback.com"""))

gpt.add_example(Example("""Order has been placed""",
"""Your order has been placed! We’re hard at work processing it now. If you haven’t 
heard from us by X, please call (insert phone number). Thanks again for making us part of your day."""))

gpt.add_example(Example("""Order has been placed""",
"""Thank you for your order! We'll get right on it!"""))

gpt.add_example(Example("""Order has been placed""",
"""Hello, __________! We just received your order and have already begun processing it. You should expect 
to receive your items shortly. If we don't hear from you within 72 hours, we'll follow up with an email 
and call you for a delivery date confirmation."""))

gpt.add_example(Example("""Signing up""",
"""Thanks for signing up to our mailing list! Check your email inbox for a confirmation email, 
and please add "support@ support.com" to your address book to help us deliver emails to your inbox."""))

gpt.add_example(Example("""Signing up""",
"""You've signed up! Thank you for joining our mailing list. You’ll start receiving tips, guides and updates in the next few days."""))



# Define UI configuration
config = UIConfig(description="Create a confirmation e-mail",
                  button_text="Create",
                  placeholder="What are we confirming? e.g.: Order placed.")

id = "confirmation-email"