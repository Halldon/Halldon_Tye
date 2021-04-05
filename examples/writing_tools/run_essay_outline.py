##updated api path, engine, top p, updated top p, temp, and tokens. 
##Runs as expected 

import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.5,
          top_p=.5,
          max_tokens=100)


##Create an essay outline


gpt.add_example(Example("""The earth quake of the 1998,The February 1998 Afghanistan earthquake occurred at 19:03 local time near the Afghanistan-Tajikistan border.""",
"""Section: The earthquake was in a very remote area
Section: Over 80 percent of the population affected by the earthquake lived in tents and other non-traditional housing 
Takeaway: Don't neglect traditional disaster relief.
Section: Do not rely on a single agency for disaster relief.
Section: Do not assume agencies will solve your problems.
Takeaway: Be prepared to take care of yourself."""))

gpt.add_example(Example("""The earth quake of the 1998,The February 1998 Afghanistan earthquake occurred at 19:03 local time near the Afghanistan-Tajikistan border.""",
"""Section: Because of the remoteness of the disaster area
∗∗∗ Section: Major international aid effort begins
Section: Pakistani army sent to help refugees
Section: Critics attack Pakistan Government handling of earthquake
Takeaway: Poor responses to natural disasters can impact the reputation of a country."""))

gpt.add_example(Example("""The benefits of universal healthcare, How the united states could benefit from embracing socialized medicine. """,
"""Section: Healthcare is a right
Section: Socialized medicine would reduce costs and increase benefits for everyone
Section: Universal healthcare would make the US more competitive economically
Takeaway: Universal healthcare will make businesses stronger by being able to attract talent from 
abroad and allow them to focus on growing their business, rather than getting crushed under the weight of healthcare. 
Universal healthcare will also allow individuals from poorer backgrounds to become successful, giving everyone a fair shot in life."""))

gpt.add_example(Example("""The benefits of universal healthcare, How the united states could benefit from embracing socialized medicine. """,
"""Section: countries with universal healthcare spend less and get more for it
Section: The united states can't afford not to have universal healthcare 
Section: Universal healthcare is inevitable in the united states
Takeaway: Expect universal healthcare in your lifetime. All Americans should have health insurance.
Section: Criticisms of socialized medicine are overstated
Takeaway: The evidence speaks for itself. This article will explain why socialized medicine works so well.
Section: If you're against"""))

gpt.add_example(Example("""The benefits of universal healthcare, How the united states could benefit from embracing socialized medicine. """,
"""Section: The United States is the only economically advanced nation that doesn't provide health care for all its citizens.
Section: Improved health care would boost productivity and consumer spending
Takeaway: Universal healthcare is the right thing to do.
Section: A single-payer system would promote competition among providers
Section: America's private system wasted money for profit, while a socialized system would be more efficient.
Section: Single-payer + some insurance for wealthier citizens would decrease overall costs"""))


# Define UI configuration
config = UIConfig(description="Create an outline for your essay",
                  button_text="Create",
                  placeholder="Enter a title (optional) & what your essay is about.")

id = "essay-outline"