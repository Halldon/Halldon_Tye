##updated api path, engine, top p 
##Runs as expected 
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=1,
          max_tokens=100)

##Construct before-after-bridge based on product + description of product

gpt.add_example(Example("""plant shelf, organize all of your plants""",
"""Before: I am always trying to find ways to organize all the plants in my house. Since we have moved into this new place, I have bought several tools and grows but they somehow do not help me manage all these plants.
After: One day my husband chip surprised me with this amazing plant shelf stand that he had designed and built for me. He said "I saw these shelves somewhere, probably on bike messenger bags , but was not sure about the dimensions since it wasn't a picture of the entire shelf structure. Then I figured it out how it could be done and built it for you."
Bridge: And I want to thank him for making my life so much easier!"""))

gpt.add_example(Example("""plant shelf, organize all of your plants""",
"""Before: Do you think about plants when you think about interior decoration?
After: Have you given much thought to that empty corner of your living room where your latest investment was killed by neglect?  
Bridge: So, are you in peak growing season and want to organize your indoor plants and flowers. Well, we'd like to help you with 
plant shelf that will help you organize all your plants with very less effort."""))

gpt.add_example(Example("""record stand, organize and display all of your favorite records and record player""",
"""Before: Have you ever faced this problem? You want to display all of your favorite records but don't wanted to buy an expensive shelving unit for it.
After: Thanks to record stand, you can now custom-design how you want your records and record player to be displayed.
Bridge: Imagine the process to creating a customized design taking just 3 minutes. We at record stand have built a tool that does just 
that! It helps you import all of your favorite music files from internet radio, create playlists, organize them by genre, subgenre etc. 
and gives you the option of designing a shelf with different number of slots as per your requirement. Prefer to display more than 100 records? 
no problem! - we provide an option"""))

gpt.add_example(Example("""heated blanket, stay warm with an electric heated blanket""",
"""Before: As the winters are approaching, you may find it tough to stay warm keeping yourself off your electric blanket.
After: As the winter season approaches, wouldn't you prefer a soft warm bed that keeps you cozy and prevents from getting out of bed 
even when you have so much work to do? Instead of finding the perfect color for keeping your room warm, wouldn't you rather stay in 
hibernation mode all day long with the perfect electric blanket?
Bridge: If you think an electric blanket is something that will come to your rescue this winter, then we invite you to learn more about 
HEATED BLANKET, that promises to be a dream come true for cozy sleepers little do we know sleeper's can dream too."""))

gpt.add_example(Example("""heated blanket, stay warm with an electric heated blanket""",
"""Before: For years we have been buying electric blankets to warm ourselves on winter mornings and evenings.
After: Imagine if you could automatically turn on an electric blanket at a desired time each day, without lifting a finger, and 
in the process save up to 50% as compared to buying a similar blanket every year. Bridge: This is what the heated blanket wifi 
smart controller brings into the world.
Bridge + benefit: This means that if you would like to have an easy way of using a heated blanket, all you need is to plug it into your wifi.."""))


# Define UI configuration
config = UIConfig(description="Create a before-after-bridge for your product",
                  button_text="Create",
                  placeholder="Enter your product and a brief description")

id = "ba-bridge-app"