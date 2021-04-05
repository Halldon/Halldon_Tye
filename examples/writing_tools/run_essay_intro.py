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

#Create an intro to an essay

gpt.add_example(Example("""Why America should move to socialized medicine""",
"""“There's no shortage of people in America who lack access to medicine. 
That fact is a direct result of the way we pay for it. Since I've lived and worked in both 
systems, I can vouch for the benefits of socialized medine. If you get care under a socialized 
system you rarely worry about its cost and availability. It's always there for you when you need 
it, and it doesn't leave you is crippling debt - and it is not primarily paid by third parties like"""))

gpt.add_example(Example("""Why America should move to socialized medicine""",
"""“Healthcare is more than a public good. It is also an economic imperative for a nation such as America, 
whose businesses compete in the global marketplace. Health care costs are rising beyond anyone's ability 
to pay nearly every year. The US as a whole spends about twice as much per person on health care as any other 
industrialized country, but our life expectancy is shorter and our infant mortality rates are higher."""))

gpt.add_example(Example("""Why America should move to socialized medicine""",
"""“The US has the most expensive health care in the world. Our total spending on medicine is more than twice 
what any other nation spends. Yet we have poor health outcomes by many measures. Our infant mortality rates 
are some of the worst in the developed world. So are our life expectancies. A large part of this problem is 
how fundamentally broken our medical market structure is. Some examples of broken markets include: All Payers 
Pay the Same Price / No Consumer Choice / No-Negotiations / Mon"""))

gpt.add_example(Example("""Why America should move to socialized medicine""",
"""“Healthcare is an industry that's not working. People are sick and they can't get well. The sick are unhappy 
and the doctors, nurses and managers are miserable too. All of us are paying more for healthcare than we should 
be, and all of us would pay a lot less if it were working well enough to keep everyone healthy at a reasonable price."""))

gpt.add_example(Example("""The difference between data science and data analysis""",
"""“Data analysis is a subset of data science. Data science is the sum total of three different things: Data Analysis, 
Software Engineering, and Product Development."""))

gpt.add_example(Example("""The difference between data science and data analysis""",
"""“Data science is a buzzword in programming. What does it actually mean? As far as I can tell, data analysis 
is the process of deriving insights from data. Data are information that already has some meaning to somebody. 
Data science is the process of finding that meaning."""))

gpt.add_example(Example("""The difference between data science and data analysis""",
"""“What is data science? What does it mean to be a data scientist? And how should one approach the data science 
life? In this article, we'll take a look at the different kinds of tasks that make up 'data science' and see what 
skills you need to become a real-world data scientist."""))

gpt.add_example(Example("""The difference between data science and data analysis""",
"""“Data science is a new and popular term that people use to refer to the work of applying statistical analysis, 
machine learning algorithms, data visualization etc. on ever increasing amounts of data collected through the internet. 
In order to be valuable this data needs to collected, cleaned, transformed into information then assembled and modeled . 
Data science can also involve extracting knowledge from unstructured sources like text and images."""))


# Define UI configuration
config = UIConfig(description="Create an introduction to your essay.",
                  button_text="Create",
                  placeholder="What is the essay about?")

id = "essay-intro"