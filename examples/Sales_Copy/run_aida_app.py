##upated api path, engine, top_p 
#works just fine 
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=0.5,
          max_tokens=100)


gpt.add_example(Example("""Charmin ultra soft""",
"""Attention: Three rolls for the price of two? You can save when you buy Charmin Ultra Soft!
Interest: The ultra soft sheets are ultra durable too! In fact, rips and tears don’t stand a chance.
Desire: That’s great news because Charmin Ultra Soft is the best toilet paper for dependable comfort!
Action: Buy Charmin Ultra Soft bulk rolls now!"""))

gpt.add_example(Example("""Black Diamond mountaineering gear hiking equipment""" ,
"""Attention: Redefining excellence and safety
Interest: Introducing the first MCE-certified line of mountaineering equipment in the world.
Desire: Mountain travel shouldn’t be limited to only experienced alpinists. Black Diamond supplies its gear so that everyone can enjoy the incredible allure that comes with mountain travel.
Action: Go out, do amazing things, and document it for others to see. Follow @blackdiamondusa on Instagram, or email hi@blackdiamondequipment.com to learn more."""))

gpt.add_example(Example("""Black Diamond climbing gear safety equipment""",
"""Attention: Black Diamond is the global leader in climbing, mountaineering, and skiing equipment; we manufacture gear and clothing for alpine climbing, ice climbing, mountaineering, rock climbing, backpacking, skiing, hiking, biking.
Interest: Why would anyone climb a mountain? Curiosity is the prime mover. Familiarity with the mountain environment is critical for safety.
Desire: We create innovative solutions to the challenges of mountain travel and self-expression by designing gear and clothing that move you to new levels of performance and experience.
Action: Experience mountain freedom with Black Diamond at  blackdiamondequipment.com """))

gpt.add_example(Example("""Halldon marketing advertising we make websites that make you money""",
"""Attention: We specialize in branded digital marketing, so your website can profit from first-click traffic
Interest: Online customers will arrive at your site and stay there, which increases the number of visitors by up to 400%
Desire: Our websites are proven to increase conversions and sales by an average of 174% per month.
Action: Schedule a free consultation today @ halldon.com/free-consultation"""))

gpt.add_example(Example("""Halldon marketing advertising we make websites that make you money""",
"""Attention: Halldon is proud to represent more than 100 clients on over 50 different platforms, with headquarters and offices in over 15 countries
Interest: We’ve been helping E-commerce businesses make money online since 2014
Desire: We’d love to help you too – visit our website and watch our short video.
Action: Click here """))

gpt.add_example(Example("""Verizon Wireless fastest 5G network""",
"""Attention: Verizon announced the rollout of its new 5g network, providing speeds 10 times faster than 4g and 100 times faster than traditional broadband.
Interest: As a result, consumers will enjoy a higher quality mobile experience of streaming videos with less buffering or lag time.
Desire: It will also give new capabilities and transform commerce, entertainment, healthcare, security, transportation, and education.
Action: Click here to learn more. """))

gpt.add_example(Example("""Verizon Wireless fastest 5G network""",
"""Attention: Verizon Wireless is the first wireless network in the country to have a 5g service (Verizon)
Interest: Up to 50 times faster download speeds than LTE! And nearly unlimited video streaming
Desire: Faster internet and HD video streaming without tying up your phone’s data means more time doing the things you want.
Action: Sign up here for more information."""))

gpt.add_example(Example("""Microsoft Azure""",
"""Attention: Azure can handle an extreme amount of data and enable you to build fast, responsive websites using AI and machine learning—whether your application users are on a mobile device, a web site, or industrial IoT equipment.
Interest: It’s powered by the fastest, most available virtual machines globally and offers insights with predictive analytics—to enable you to set realistic goals, schedule, forecast sales, and optimize operations.
Desire: Azure monitors scalability limits in real time and adapts resources to meet changing cloud demands. Automated planning and monitoring helps you to predict customer behavior.
Action: Sign up here for a free trial. """))

gpt.add_example(Example("""Microsoft Azure""",
"""Attention: Microsoft Azure is the world’s premier cloud platform for building, deploying, and managing enterprise applications.
Interest: It provides intelligent insights across the app lifecycle to optimize performance and make the most of your Azure investment.
Desire: It streamlines app development—enabling teams to build at scale, AI/ML integration, automation, and DevOps capabilities.
Action: Visit microsoft.com/azure today to get started with a free trial! """))

gpt.add_example(Example("""Handcrafted wooden plant pots unique customizable""",
"""Attention: The plant pots are handcrafted and made with the highest quality wood
Interest: They're customizable, with a variety of choices for you to make your pot truly unique.
Desire: Its simplicity and beauty will bring life to any living space!
Action: Click here for more info on each product. """))

gpt.add_example(Example("""Handcrafted wooden plant pots unique customizable""",
"""Attention: Handcrafted plant pots crafted from wood and other natural materials. The products are high quality, and come in different shapes and styles; they're also customizable and unique!
Interest: My tabletop rock planters are a perfect way to create indoor greenery wherever you like.
Desire: I want to introduce you to a very special range of unique products that you won't find anywhere else.
Action: Click here to check them out! """))



# Define UI configuration
config = UIConfig(description="AIDA Generator",
                  button_text="Generate",
                  placeholder="Some information about your business and services")

id = "aida-application"
