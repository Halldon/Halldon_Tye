##updated api path, engine, top p, updated top p, temp, and tokens. 
##Runs as expected 
##Needs more detail to get an output, otherwise it continues to spit out what was put in. 
##Will return to this particular model for more refinement. 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.4,
          top_p=0.5,
          max_tokens=70)

#Create a short text hook for product


gpt.add_example(Example('CopyAi, AI powered copywriter for small businesses and entrepreneurs',
'If youre any kind of businessperson then youve probably written an ad Theres an alternative to expensive marketing firms.A thread 👇👇'))

gpt.add_example(Example('CopyAi, AI powered copywriter for small businesses and entrepreneurs',
'The founder of CopyAi turned a $6,000 investment into a multi-million dollar business. Lets explore the model in this thread.'))

gpt.add_example(Example('CopyAi, AI powered copywriter for small businesses and entrepreneurs',
'Ill go into what makes this AI copywriter different to many others, explain the market it serves, give my review of its services so far,and show you what you can achieve with it.'))

gpt.add_example(Example('self watering plant pot',
'A plant pot that waters the plant for you so you wont forget!'))

gpt.add_example(Example('leather camera strap',
'A stylish camera strap that will keep your camera secure.'))

gpt.add_example(Example('a candle with soy wax',
'Soy wax candle means no added chemicals!'))


gpt.add_example(Example('organic dog treats',
'Stop treating your dog to fillers and additives! Your dog deserves better. Check out our selection of organic dog treats!'))

gpt.add_example(Example('inventory sale',
'SO many items marked down and ready to save you money! Check out our sale.'))

gpt.add_example(Example('ice cube mold',
'Create perfect ice cubes with this new ice cube mold!'))

gpt.add_example(Example('kitty litter',
'Litter that clumps for easy clean up and stays smelling fresh.'))



# Define UI configuration
config = UIConfig(description="Create an attention grabbing hook for your products or blog posts.",
                  button_text="Create",
                  placeholder="Product (optional), description of product")

id = "short-text-hook"