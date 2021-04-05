##updated api path, engine, top p 
##Runs as expected 
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


##Generate feature-advantage-benefit for product

gpt.add_example(Example("""heated blanket, stay warm with an electric heated blanket""",
"""Features: 1500 Watt, the best electric heated blanket on the market.
Benefits: Stay warm when you need it"""))

gpt.add_example(Example("""heated blanket, stay warm with an electric heated blanket""",
"""Features: Heated electric blanket
Advantages: Perfect for the chilly nights
Benefits: Stay warm and watch a movie"""))

gpt.add_example(Example("""heated blanket, stay warm with an electric heated blanket""",
"""Features: Heated blankets work on any existing blanket
Advantages: Turn your favorite blanket warm and cozy for those cold nights
Benefits: Stay warm while you sleep – Night after night."""))

gpt.add_example(Example("""heated blanket, stay warm with an electric heated blanket""",
"""Features: Can be used all year to keep you warm
Advantages: heating wire controls the amount of heat given off
Benefits: Allows users to adjust heat levels"""))

gpt.add_example(Example("""laptop case, protect laptop from scratches with high quality leather case""",
"""Features: High quality leather case for your Macbook 13" with 14" cover.
Advantages: Flexible 360 degree rotatable stand for multi-viewing. Elegant and stylish design, easy to carry.
Benefits: Prevent scratches and bumpers will protect your Macbook against dust and damage. 
It feels good on your fingers while operating, no fatigue in long time using."""))

gpt.add_example(Example("""laptop case, protect laptop from scratches with high quality leather case""",
"""Features: Beautiful laptop sleeve with custom fit, you can choose leather style from classic black to brown and custom made style
Advantages: Extremely durable exterior
Benefits: Protect your laptop effectively"""))






# Define UI configuration
config = UIConfig(description="Create features and benefits for your product",
                  button_text="Create",
                  placeholder="Enter product description and name")

id = "feature-adv-bene"