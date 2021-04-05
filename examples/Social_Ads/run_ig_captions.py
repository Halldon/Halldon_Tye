##updated api path, engine, top p, updated temp 
##Runs as expected 
##Users can enter a sentence, key words, and even a person, book, or movie if they're looking for a quote
##i.e.: nelson mandela quotes 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.8,
          top_p=1,
          max_tokens=100)

##Create instagram captions 

gpt.add_example(Example("""Mountains, adventure, backpacking, watching the sunrise, mount rainier""",
"""Glorious morning vista. The sun slowly peaks through the clouds, illuminating Mount Rainier’s snow-capped peaks. 
The lake below glistens and sparkles in the early morning light as we pack up our backpacks and"""))

gpt.add_example(Example("""Mountains, adventure, backpacking, watching the sunrise, mount rainier""",
"""Hello, Puget Sound! We’re in awe of your beauty and are having a blast spending a week @mountrainiernps. 
Who else has visited the park recently?"""))


gpt.add_example(Example("""Mountains, adventure, backpacking, watching the sunrise, mount rainier""",
"""Now that fall is finally here, we’re itching to get outside and embrace the new season. 
The weather is gorgeous, so why not have a weekend campout and hike Mt. Rainier?"""))

gpt.add_example(Example("""Mountains, adventure, backpacking, watching the sunrise, mount rainier""",
"""The mountains are calling and I must go"""))

gpt.add_example(Example("""new plants just arrived, monstera, pothos, fiddle leaf fig, planters, local plant shop""",
"""Wake up to beautifully tended plants waiting for you to fill your home or office with greenery. Want something specific?
 Let us know! Come by our spot in San Bruno today to check out our tanks! #plantsofinstagram"""))


gpt.add_example(Example("""new plants just arrived, monstera, pothos, fiddle leaf fig, planters, local plant shop""",
"""Enjoy the view, it’s all green in da hood! These new succulent babies just got planted in our planters 🌱🍃
 #succulove #newplants #plantsofinstagram #succ"""))


gpt.add_example(Example("""new plants just arrived, monstera, pothos, fiddle leaf fig, planters, local plant shop""",
"""Planting plants is like filling your home with big, beautiful dreams. 🌿☀🌱"""))



gpt.add_example(Example("""coffee, coffee shop""",
"""So I can't imagine life without coffee. If it were up to me, we'd be drinking it all day, every day. 
And you know why? Because there's absolutely nothing else like that warm and bright feeling you get when a fresh cup"""))

gpt.add_example(Example("""coffee, coffee shop""",
"""We live for that cozy feeling of warmth and belonging when we walk into a homey cafe with our best buds. 
That's the idea behind our new Cold Brew. It's cold-brewed & blended with creamy milk, giving it an extra smooth"""))

gpt.add_example(Example("""coffee, coffee shop""",
"""Some days you need a caffeine pick-me-up. Other days you need an everything pick-me-up. 
Just make sure you Bring Goodness to your day every day. #bringeverygoodnesstoday"""))

gpt.add_example(Example("""travel, wanderlust, adventure""",
"""If you don't chase what you're passionate about, you'll have nothing. #keepgoing #travelmore"""))

gpt.add_example(Example("""travel, wanderlust, adventure""",
"""We’re Dreamers. Pioneers. Explorers of the unknown and seekers of all things gold."""))


gpt.add_example(Example("""travel, wanderlust, adventure""",
"""Off the beaten path in Bali."""))


gpt.add_example(Example("""travel, wanderlust, adventure""",
"""Daydreaming about that new adventure awaiting. 🍃"""))




# Define UI configuration
config = UIConfig(description="Write your next instagram caption",
                  button_text="Give me captions!",
                  placeholder="What do you want your post to be about?")
id = "ig-captions"
