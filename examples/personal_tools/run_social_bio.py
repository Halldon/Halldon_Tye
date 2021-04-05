##updated engine, updated API path, added top p 
##Model works 2/9/21

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig



# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=0.5,
          max_tokens=80)

#Create a social bio

gpt.add_example(Example("""I am the founder and CEO of a tech start up.""",
"""“I'm the Founder and CEO of a fast growing tech start up in Austin. Previous experience 
includes over 10 years in aerospace engineering, 3 years as a startup co-founder 
and 2 years of angel investing."""))

gpt.add_example(Example("""I am the founder and CEO of a tech start up.""",
"""“💻Founder & CEO of a Tech Start Up aiming to help FinTechs & many more. We're looking into many areas, 
including Blockchain, Artificial Intelligence, Cybersecurity and Augmented Reality. We are well 
connected in the digital industry & ready to solve any problems you have. Don't hesitate to contact us!
💰 🛠️ www.dominicmclaughlin.com
📲 dmclaug@gmail.com (215) 559"""))

gpt.add_example(Example("""I am a UX designer at Apple""",
"""“I am a UX designer at Apple. Obsessed with technology, design, and identity. I've led product 
design efforts for YouTube Music since the beginning of 2018 and was previously a designer at 
Airbnb and Facebook."""))

gpt.add_example(Example("""I am a UX designer at Apple""",
"""“Hi, I'm a UX designer at Apple. I'm currently working with different teams on watchOS, macOS, tvOS and iOS. 
Have released 2 major Mac apps which are top 100 in Utilities and Education categories respectively.
I'm also working on a website to teach people how to code. Right now it's geared towards beginners, 
but eventually I'd like it to be a helpful resource for anyone interested in learning how to code"""))



# Define UI configuration
config = UIConfig(description="Create a bio for your social handles",
                  button_text="Create",
                  placeholder="A little bit about who you are.")

id = "social-bio"