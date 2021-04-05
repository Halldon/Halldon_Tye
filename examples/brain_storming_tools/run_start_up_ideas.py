##Triple quotes work fine here
##outputs are normal 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig

# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=1,
          max_tokens=80)

#Generate new ideas for a start up based off of pasions. 

gpt.add_example(Example("""ai powered plant care""",
"""An ai powered plant care concierge service that helps manage your indoor garden. 
The service would: + Collect data on every aspect of every plant and use it to continually
 personalize each plant's environment + Generate products for wholesale (domes/lights/etc), 
 including an online web store + Make recommendations for certain plants (succulents, 
 plants that clean the air, etc), and offer a subscription service to provide each of 
 them with the perfect environment in exchange for a cut of"""))

gpt.add_example(Example("""ai powered plant care""",
"""Bot powered plant care. AI can do a pretty good job at automated gardening. Whether one 
is tracking growth rate/light, or anticipating number of waterings needed, etc. Tesla has 
already released a couple of their nature-inspired patents in this area (one for hydroponics 
and one for aeroponics).
iota will be the backbone of the new data economy"""))

gpt.add_example(Example("""ai powered plant care""",
"""Using computer vision, machine learning, and natural language understanding 
to provide an AI powered plant care assistant. The startup could automate monitoring 
conditions, and suggest what to do next. A recommendation system coupled with a chatbot 
interface could help the user see what is wrong when a plant is not doing well, and offer 
suggestions for how to fix it. I feel this startup can be used at any scale from a small 
garden up to a commercial greenhouse."""))

gpt.add_example(Example("""ai powered plant care""",
"""Plant care AI will alert us when plants need water, sun, etc. It will tell when 
they are thirsty and remind us to water or transplant them."""))



# Define UI configuration
config = UIConfig(description="Generate new ideas for the next great start up.",
                  button_text="Generate",
                  placeholder="What are you passions, hobbies, or inspirations?")

id = "start-up-ideas"