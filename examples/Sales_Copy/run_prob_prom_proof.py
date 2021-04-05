##updated api path, engine, top p, updated temperature to produce better output.
##Runs as expected 
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.85,
          top_p=1,
          max_tokens=100)



##Generate problem-promise-proof-proposal 

gpt.add_example(Example("""laptop case, protext laptop from scratches with high quality leather case.""",
"""Problem: Since the introduction of laptops, there has been a huge trend of owning a new laptop but leaving it unprotected.
Promise: Quality protection for your laptop with leather case
Proof: [Customer Proof 'with this high-quality leather case, you can have peace of mind that you are not going to damage your device'].
Proposal: Buy Laptop Cover Now! | High quality leather case covering your entire device or order protection only for screen."""))

gpt.add_example(Example("""heated blanket, soft, warm, electric, heated blanket""",
"""Problem: You can’t wait to get into bed, but once under the covers you’re still cold.
Promise: With our heated blanket you’ll be toasty warm all-night long.
Proof: [Customer Proof - "It conserves my heating oil, and has given me a more comfortable winter."]
Proposal: Order your electric heated blanket today!"""))


gpt.add_example(Example("""AirPods, AirPods deliver an unparalleled listening experience with all your devices. 
Every model connects effortlessly and packs rich, high-quality sound into an innovative wireless design.""",
"""Problem: Riding in the car or on public transport when everyone is plugged into their own music can be frustrating.
Promise: AirPods are designed with innovative wireless technology and seamless integration with all your devices.
Proof: [Customer Proof 'With AirPods, Apple has broken new ground. These headphones are slick and classy, fun and functional'].
Proposal: Don't just hear it - experience it!"""))

gpt.add_example(Example("""AirPods, AirPods deliver an unparalleled listening experience with all your devices. 
Every model connects effortlessly and packs rich, high-quality sound into an innovative wireless design.""",
"""Problem: What can you do when it's time to use ear buds again?
Promise: AirPods combine ease of use with a great sound experience.
Proof: [Customer Proof 'It's just so much easier to have one less thing to take care of. I stay organized, and I can always have my music on me.']
Proposal: [Special Offer] get a $50 Apple gift card when you buy AirPods. http://www.apple.com/airpods/"""))

gpt.add_example(Example("""AirPods Max, Introducing AirPods Max — a perfect balance of exhilarating high-fidelity audio 
and the effortless magic of AirPods. The ultimate personal listening experience is here.""",
"""Problem: Your old headphones don't seal out loud noises well enough.
Promise: AirPods Max create an immersive listening experience that lets you immerse yourself in your music.
Proof: [Customer Proof 'I can't even describe how cool these things are, they just are.']
Proposal: It's time for you to grab the future of headphones today!"""))

gpt.add_example(Example("""AirPods Max, Introducing AirPods Max — a perfect balance of exhilarating high-fidelity audio 
and the effortless magic of AirPods. The ultimate personal listening experience is here.""",
"""Problem: When you’re deep into your music, nothing should stop you from losing yourself in the moment.
Promise: AirPods Max use one charge to last three times longer than AirPods. Want even more? Our multi-device power case is also included 
so you can charge both your AirPods Max and your iPhone for an hour of playtime with just one charge.
Proof: [Customer Proof 'Some people can’t hear well with small earbuds. With AirPods Max, their mom could hear their music again.']
Proposal: Give your ears the pleasure they deserve and find out what headphones are really supposed to sound like with AirPods Max today!"""))



# Define UI configuration
config = UIConfig(description="Create Problem-Promise-Proof-Proposal for your product",
                  button_text="Create",
                  placeholder="Enter product description and name")

id = "prob-prom-proof"