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


gpt.add_example(Example("""Handcrafted plant pots handcrafted, wood, customizable, unique, beautiful""",
"""Top 5 Tips for Making Your Gardens Look Professional: A blog about how to make your garden look professional."""))

gpt.add_example(Example("""Handcrafted plant pots handcrafted, wood, customizable, unique, beautiful""",
"""How to Select the Perfect Indoor Plant for Your Home: A blog about how to select indoor plants"""))

gpt.add_example(Example("""Handcrafted plant pots handcrafted, wood, customizable, unique, beautiful""",
"""How to design your own plant pot: A blog on how to use your imagination and make your own pots. Lots of simple, step-by-step project tutorials."""))

gpt.add_example(Example("""blogging, how to make money and generate sales with your blog """,
"""Do You Have an Effective Blogging Strategy in Place? 3 Ways to Improve Your Blog: a blog with tips for blogging and ways you can make money from it."""))


gpt.add_example(Example("""blogging, how to make money and generate sales with your blog """,
"""Does Blogging Really Pay? 3 Ways To Earn Steady Income With Your Blog: a blog about different methods for earning money with your blog, with examples."""))

gpt.add_example(Example("""blogging, how to make money and generate sales with your blog """,
"""Making Money Blogging? Everything You Need To Know: A blog about making money with your blog."""))

gpt.add_example(Example("""blogging, how to make money and generate sales with your blog """,
"""10 Amazing Ways to Monetize Your Blog: A blog about different methods of generating revenue from a blog."""))


# Define UI configuration
config = UIConfig(description="Get some ideas for your next great blog post",
                  button_text="Brainstorm away",
                  placeholder="Type some ideas here")

id = "blog-ideas-app"
