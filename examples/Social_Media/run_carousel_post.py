##updated api path, engine, top p 
##Runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.6,
          top_p=.5,
          max_tokens=100)

#Create a Carousel post for attention grabbing

gpt.add_example(Example("""5 easy ways to attract new customers""",
"""Hook: Start attracting new customers
1: Make a blog for your business
3: Create an ad with your price and go get it
4: Take attractive photos of your work
5: Repost other people's content and add your voice to it
CTA: Share this post  for more tips"""))

gpt.add_example(Example("""5 easy ways to attract new customers""",
"""Hook: Here's how you can attract new customers through your instagram feed
1: Schedule posts so they're posted once per day
2: Share a story about your customers success stories
3: Take and share lots of pictures of your customers using your product or service in real life
4: Post pictures of people doing your service or product in real life situations
5: Engage with people who inquire about your service or product or who connect because they already get it. Reply to"""))

gpt.add_example(Example("""3 ways to boost engagement on instagram""",
"""Hook: Follow these 3 tips to boost engagement on instagram
1: Reply to every comment
2: Tag your top followers and customers with more than 5K followers
3: Use quotes to increase engagement
CTA: Click here for 3 more tips!"""))

gpt.add_example(Example("""3 ways to boost engagement on instagram""",
"""Hook: This is how to boost engagement on instagram
1: Reply to all comments
2: Use hashtags with your niche keywords in them
3: Treat your followers like friends
CTA: Comment your thoughts on the article"""))

gpt.add_example(Example("""3 ways to boost engagement on instagram""",
"""Hook: This is the number 1 mistake you're making on Instagram
1: You aren't posting regularly– Post at least 3 times a day
2: You aren't saying personal things – People want to hear from individual brands, not huge corporations
3: You aren't creating unique content
4: Your photos are boring – Only take boring pictures if you really really have to.
CTA: Check out this post for more tips on how to boost engagement at [x] """))


# Define UI configuration
config = UIConfig(description="Create a Carousel Post for your topic",
                  button_text="Create",
                  placeholder="What is your topic? (i.e.: 5 easy ways to attract new customers.)")

id = "carousel-post"