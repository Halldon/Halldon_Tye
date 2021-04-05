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

##create an intro for your blog post

gpt.add_example(Example("""Backpacking Essentials, backpacking, mountaineering, gear, safety, mountains, camping, ultralight """,
"""If you plan on going backpacking, mountaineering, or traveling in the mountains, it is essential to have backpacking essentials. 
While some people like to carry heavy equipment out in the wilderness, I prefer traveling ultralight with just the essentials. 
All you need are a few backpacking essentials to ensure your safety and comfort so you can spend more time enjoying yourself 
and less time being frustrated by heavy equipment. Also by traveling ultralight, you will have more opportunities to take 
that amazing Instagram photo or reach that summit without having to turn around for lack of strength and energy."""))

gpt.add_example(Example("""Backpacking Essentials, backpacking, mountaineering, gear, safety, mountains, camping, ultralight """,
"""The most important tips and recommendations on backpacking, mountaineering, and ultralight hiking."""))

gpt.add_example(Example("""Backpacking Essentials, backpacking, mountaineering, gear, safety, mountains, camping, ultralight """,
"""I’m just going to get right into this post because there is a lot to cover and the clock is ticking on my free time. 
I will be honest, I’m not an expert — but I’ve done enough backcountry camping to know how to be safe, comfortable and smart 
in the mountains. Knowledge can be empowering so I hope this guide helps you on your next adventure, or teaches you 
something new that you didn’t know before."""))

gpt.add_example(Example("""Solo Female Travel, backpacking, My experiences as a solo female traveler exploring the world""",
"""I am a solo female traveler and I’ve been bitten by the travel bug. Since discovering the joy of traveling alone, 
I have been completely hooked! Over the last two years, I’ve travelled to countries, amongst others, in Asia, Europe 
and South America. These travels were truly life-changing for me. I learned more about myself and saw parts of the 
world that sparked my interest in different cultures and societies."""))

gpt.add_example(Example("""Solo Female Travel, backpacking, My experiences as a solo female traveler exploring the world""",
"""Solo travel has become increasingly popular in recent years for people around the world. There have been solo travel books,
 shows, and movies creating an immense interest for people to do it. Solo female travel is an even more specialized form 
 of solo travel as women tend to be more hesitant or less comfortable traveling alone because of safety risks or 
 cultural differences. It’s also an incredibly exciting experience because you don’t have any friends to drag you down. 
 It’s you – the whole adventure is yours!"""))

gpt.add_example(Example("""Solo Female Travel, backpacking, My experiences as a solo female traveler exploring the world""",
"""Have you ever wondered what it would be like to travel the world alone? I was terrified to even 
think about this question. When I was a little girl, I could never imagine traveling by myself without 
family or friends around me. It took me years to finally take the plunge into solo travel and learn first hand 
how amazing it is. No limitations, no worries about making plans with friends or families, 
just you and a few months – well spent traveling the world."""))

gpt.add_example(Example("""Solo Female Travel, backpacking, My experiences as a solo female traveler exploring the world""",
"""Maybe it was my thirst for adventure, the desire to discover something new and alluring or even a 
craving for the unfamiliar. I don’t know exactly what drove me but I do know that it worked it’s 
magic and this is how it all began: one fateful day in late 2007, shortly after turning 28 years old, 
when I said to myself"""))

gpt.add_example(Example("""10 tools for every data scientist, Here are ten tools that every data scientist should know and use.""",
"""Today I wanted to share my list of ten tools that every data scientist should know and use. 
This list will definitely not be comprehensive, but it is a good place to start when you are getting started."""))

gpt.add_example(Example("""10 tools for every data scientist, Here are ten tools that every data scientist should know and use.""",
"""When you start collecting data for analysis, whether it be for fun or profit you’ll begin to 
realize there are a lot of tools that are out there. It can be difficult to find the right one, 
so I put together this list of ten essential tools that every data scientist should know and use. 
If you’re new to this field, I hope this helps you as you gather and analyze your data."""))

gpt.add_example(Example("""10 tools for every data scientist, Here are ten tools that every data scientist should know and use.""",
"""Whether you work in marketing, business intelligence or any field that relies on data analysis, using the right 
tools will improve your productivity and your effectiveness. In this post, we review ten of the most useful tools 
for data scientists so that you do not have to waste time searching for them."""))




# Define UI configuration
config = UIConfig(description="Write your blog intro",
                  button_text="Brainstorm away",
                  placeholder="Write a title and a short description")

id = "blog-intro-app"
