##working as expected. 

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
        

##Generate ideas for more "viral" content that could lead to more sales, increased traffic, etc. Effectively a brainstorming bot. 

gpt.add_example(Example("""Wooden cutting board, Handmade from highest quality wood""",
"""Offer a companion pack of personalized bottle-openers, like this. People like receiving gifts and wooden cutting boards make for great gifts."""))

gpt.add_example(Example("""Wooden cutting board, Handmade from highest quality wood""",
"""Challenge customers to post a photo of them using the cutting boards to work or cook off-the-ground."""))

gpt.add_example(Example("""Vegan cookbook, Over 100 plant based recipes""",
"""Include pictures of celebrities, athletes, and other influencers looking sexy and showing 
off their bodies while eating a healthy plant based diet"""))

gpt.add_example(Example("""Vegan cookbook, Over 100 plant based recipes""",
"""Create a fun and interactive campaign for a print book. There could be recipes to try, 
cooking tutorials and interviews with the creator. Along with hashtags, a vegan recipe 
card game to share on social media."""))

gpt.add_example(Example("""Running shoe, Neutral support running shoe with plenty of cushion for a smooth run.""",
"""For the rebranding of the running show: 'You are going to love it. No matter how fast or slow you go."""))


# Define UI configuration
config = UIConfig(description="Think up some viral ideas to promote your product",
                  button_text="Let's go viral",
                  placeholder="Enter your product (optional) and a brief description")

id = "viral-ideas"
