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


#Create a blog outline

gpt.add_example(Example("""The best plants for north facing windows, A list of plants that can survive in rooms with north facing windows""",
"""Section: 6 house plants that do well in north facing windows
Section: How to keep them alive (8 tips)
Section: Common sense tips and advice for north-facing window dwellers
Takeaway: This will help you pare down the list of plants you can't live without"""))

gpt.add_example(Example("""The best plants for north facing windows, A list of plants that can survive in rooms with north facing windows""",
"""Section: Cool-light loving plants (aka the plants that do well in north facing windows)
Section: What you can grow in the winter - great for apartments!
Section: Plants that should not go in the window sill - aka which plants will not survive the sunny windows
Takeaway: A great guide that tells you what to grow and what to avoid. It has over 2,000 words, 300px image 
and custom graphics about each plant on a north facing windowsill."""))

gpt.add_example(Example("""The best plants for north facing windows, A list of plants that can survive in rooms with north facing windows""",
"""Section: Plants that prefer some sun but not direct
Section: Shade loving plants
Takeaway: Get the most out of your indoor plant without much needed light"""))


gpt.add_example(Example("""Pandas for python, The features of pandas and how to use them.""",
"""Section: The Background of Pandas
Section: Installing Pandas
Takeaway: How to work with the pandas library and some cool things you can do with it!
Section: Comparing the Range Type to other Pandas Types
Section: The difference between comparing values within the same column and comparing values within different columns
Takeaway: A deeper look into the difference between the frame comparison in Pandas."""))

gpt.add_example(Example("""Pandas for python, The features of pandas and how to use them.""",
"""Section: When to use Pandas
Section: How to use Pandas
Takeaway: Getting started with Pandas is easier than you may think.
Section: Dataframes and Series
Takeaway: You can have quite a bit of fun with the different series and dataframe methods. 
Put some time into playing around with them and see what you come up with!"""))

gpt.add_example(Example("""Pandas for python, The features of pandas and how to use them.""",
"""Section: Getting ready to start
Section: Understanding Pandas Dataframes & Series
Section: How to read, write and process data in Pandas
Section: Explore and manipulate your dataframe
Section: How to import data into Pandas and format it correctly
Takeaway: By finishing this blog you will be able to use pandas for manipulating and processing datasets"""))

gpt.add_example(Example("""Pandas for python, The features of pandas and how to use them.""",
"""Section: Fundamentals
Sections: Get familiar with the Pandas DataFrame object
Section: Basics of Intro Stats
Takeaway: Use Pandas to do advanced data analysis and data wrangling tasks, and make your data science life easier.
Section: After dinner relaxation drinks made easy with this one simple trick (where the author 
shows that there's no need for hard liquor when it comes to making a great mixed drink)"""))




# Define UI configuration
config = UIConfig(description="Create blog outlines",
                  button_text="Create",
                  placeholder="Enter your blog title, enter what it is about")
id = "blog-outline-app"