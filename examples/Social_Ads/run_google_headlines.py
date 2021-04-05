##updated api path, engine, top p, updated temp 
##Runs as expected 
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.59,
          top_p=1,
          max_tokens=100)


##Generate Google headlines for website.

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Let CopyAi Automate Your Content"""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Your words, written by artificial intelligence."""))

gpt.add_example(Example("""CopyAi, An AI powered copywriter for small businesses and entrepreneurs.""",
"""Generate content for your business."""))


# Define UI configuration
config = UIConfig(description="Create Google headlines for your social ads.",
                  button_text="Create",
                  placeholder="Enter a product (optional) and a description of the product.")

id = "google-headlines"