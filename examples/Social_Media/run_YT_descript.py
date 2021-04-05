##updated api path, engine, top p, updated top p, temp, and tokens. 
##Runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.65,
          top_p=1,
          max_tokens=100)

#Create a YouTube description for the video.

gpt.add_example(Example("""Business Growth Hacks for 2021, the best ways to grow your business in 2021""",
"""“If you're wondering what the best, most modern ways are to grow your business in 2021 then this is the 
video for you. I talk about why these growth hacks will work and how to implement them."""))

gpt.add_example(Example("""Business Growth Hacks for 2021, the best ways to grow your business in 2021""",
"""“Advice on how to grow your business = there's no secret recipe. In this video, I give you my best 
advice on some of the best ways to grow your business in 2021."""))

gpt.add_example(Example("""Business Growth Hacks for 2021, the best ways to grow your business in 2021""",
"""“Business Growth Hacks For 2021: In this video, I share my thoughts about what the top growth hacks 
for the next few years will be in business. How do you get more customers? How do you profit from your 
ideas? How do you grow a profitable business? These are some of the answers I give"""))

gpt.add_example(Example("""top plant picks for 2020, the most popular plants viewers chose for 2020, 
and what I think the most popular plants will be in 2021.""",
"""“In my 2020 gardening video I identified the top 20 plants that viewers chose in 2018. 
Now, here's the list of popular plants for 2020. Watch to see which plants are trending and 
don't miss my expectation of what will be hot in the future."""))

gpt.add_example(Example("""top plant picks for 2020, the most popular plants viewers chose for 2020, 
and what I think the most popular plants will be in 2021.""",
"""“Neptunia's back with another top 5 video! This time we check out the top 5 plants for 2020. 
I discuss why some of these plants are going to be popular and if they're going to remain popular 
in 2021 (and beyond). Please note that this video doesn't focus on whether or not these plants will 
produce well, but rather, my thoughts on how popular these plants will be over the next few years. 
And even though trends often change, what's popular in one year is often"""))

# Define UI configuration
config = UIConfig(description="Create a description for your YouTube video.",
                  button_text="Create",
                  placeholder="Title, What is the video about?")

id = "youtube-descript-creator"