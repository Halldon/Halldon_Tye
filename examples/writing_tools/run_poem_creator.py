##updated api path, engine, top p, updated top p, temp, and tokens. 
##Very buggy, needs work. 

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

#Create a rhyming poem based off a topic



gpt.add_example(Example("""I miss you""",
"""I miss you in the morning; I miss you late at night. Just to think about you, Is my joy and my delight. I can't wait to see you; Please hurry and come back. You always make me happy; You have that special knack!"""))

gpt.add_example(Example("""Life Madness""",
"""Life gets faster every day, No time to think, no time to play. Hurry, chaos, lots of stress, Tension leads to sleeplessness. When will all this madness cease? Where is free time? Where is peace? I'm running, doing, till I drop. Give me buttons: Pause, Mute, STOP!"""))

gpt.add_example(Example("""Love""",
"""Loving him is like driving a new Maserati down a dead end street, Faster than the wind, passionate as sin, ending so suddenly;  Loving him is like trying to change your mind Once you're already flying through the free fall, Like the colors in autumn, so bright, just before they lose it all."""))

gpt.add_example(Example("""Love""",
"""Losing him was blue, like I'd never known, Missing him was dark gray, all alone, Forgetting him was like trying to know Somebody you never met. But loving him was red"""))




# Define UI configuration
config = UIConfig(description="Create a rhyming poem",
                  button_text="Create",
                  placeholder="Topic (i.e.: Cocoon)")

id = "poem-creator"