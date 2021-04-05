##updated api path, updated engine, added top_p, updated temp
##runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)


from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.7,
          top_p=0.5,
          max_tokens=100)

##This will generate product descriptions based on product name and short description

gpt.add_example(Example("""Diamond rings, Highest quality diamonds on the market""",
"""If you are looking for the highest quality diamonds on the market, and value exceptional craftsmanship, 
then you are in the right place. Our rings come with a lifetime guarantee, 
and our team is always here to answer any of your questions."""))

gpt.add_example(Example("""Diamond rings, Highest quality diamonds on the market""",
"""We are thrilled to be able to offer you the highest quality diamonds on the market, 
all at unmatched prices that will leave you feeling delighted and confident in your purchase. 
These AAA-quality diamonds, available in rounds, trilliants, emerald cut, 
exclusive baguette cut with large table facets, and princess cut."""))

gpt.add_example(Example("""Diamond rings, Highest quality diamonds on the market""",
"""You will fall in love with our rings. Each and every ring in our assortment is crafted from 
conflict-free diamonds, and every one of them sparkles as brightly as the next. 
Quality is what we strive for, and our diamonds are by far the highest quality on the market today."""))

gpt.add_example(Example("""Yoga pants, Our buttery soft leggings will be the only ones you need. Odor free technology, weightless, and timeless.""",
"""Our buttery soft leggings will be the only ones you need. Odor free technology, weightless, 
and timeless. Our 2-Way Stretch fabric offers a full range of motion making them perfect
for everything from weightlifting to walking, or lounging around the house."""))

gpt.add_example(Example("""Yoga pants, Our buttery soft leggings will be the only ones you need. Odor free technology, weightless, and timeless.""",
"""Butter-Soft. Odor-Free. Weightless. Timeless: Our original, all-season 2-way yoga pant is the ultimate
 in comfort and style. Side pockets with hidden no-slip silicone closure ensure you can take everything 
 you need now and later, while flattering seams eliminate any distraction from your workout. Lightweight, 
 stretchy leggings move with you and keep you cool and comfortable, day or night. Plus, we added a durable 
 gusset for a chafe free fit. The highest quality nylon/spandex blend delivers a luxurious feel that keeps 
 your most important asset—your"""))

gpt.add_example(Example("""Camera strap, Keep your camera safe and secure with our new leather camera straps.""",
"""A camera strap is a photographers best friend. It should keep your camera safe and secure and easily 
accessible. No matter if you're in the city or on the move, our leather camera straps are the perfect addition to your camera."""))

gpt.add_example(Example("""Camera strap, Keep your camera safe and secure with our new leather camera straps.""",
"""Our new camera straps are crafted in the USA from high quality leather with a webbing shoulder pad for
added comfort. They also feature premium hardware, including brass quick release buckles and a metal
D-ring for attaching the strap to your camera bag."""))

gpt.add_example(Example("""Camera strap, Keep your camera safe and secure with our new leather camera straps.""",
"""With a range of sizes available, our new camera straps are the perfect item to upgrade your 
existing camera strap. Made from high quality leather, they are designed and handcrafted to 
ensure optimal comfort for all day use."""))

gpt.add_example(Example("""Cell phone case, keep your phone free from scratches and cracks with our new drop resistant phone case! """,
"""Our Drop Resistant phone case is designed with a screen guard to keep your glass from cracking 
in the event of a fall. With full access to all ports and buttons, it will keep your phone looking 
good while preventing accidental drops from damaging it."""))

gpt.add_example(Example("""Cell phone case, keep your phone free from scratches and cracks with our new drop resistant phone case! """,
"""Our new 7 layer, drop resistant phone case will protect your phone from bumps, drops, and scratches. 
Keep your favorite photos or images on the back of the case and personalize it for yourself or as a gift. 
Our slim design won't add extra bulk so you can easily fit your phone into your pocket, purse, or bag."""))

gpt.add_example(Example("""Photography prints, High quality print of the mountains.""",
"""The ideal print to remind you of your love for the mountains.  This image is both beautiful, and an 
excellent reminder of the majestic beauty of our planet. The image itself is a high quality reproduction
on a semi gloss surface that will not fade or start to peel with normal wear.  The print is available in several sizes."""))

gpt.add_example(Example("""Photography prints, High quality print of the mountains.""",
"""Our photography print features a stunning shot of the mountains. It makes a beautiful 
yet affordable alternative to our other decorative photo prints, making it ideal as a gift 
or for adding a bit of bold color to your home."""))

# Define UI configuration
config = UIConfig(description="Create a product description",
                  button_text="Create",
                  placeholder="Enter your product/brand name (optional), briefly describe your product")

id = "product-description"