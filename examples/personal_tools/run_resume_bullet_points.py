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

#Create a bulletpoints for resume

gpt.add_example(Example("""Product Manager, Designed and built an app that got to $10k in sales.""",
"""“Designed and built out a user-facing mobile application that processed over $1 million in transactions, 
increasing revenue by 35% within the first 6 months."""))

gpt.add_example(Example("""Product Manager, Managed a team of 15 developers that designed and built an app 
that got to $10k in sales, turning the customers vision for the product into a reality.""",
"""“Managed a team of 15 designers and developers, working cross-functionally with Business Operations, 
Marketing, and Sales to launch innovative mobile app that got to $10k in sales within the first month of launch."""))

gpt.add_example(Example("""Product Manager, Managed a team of 15 developers that designed and built an app 
that got to $10k in sales, turning the customers vision for the product into a reality.""",
"""“Turned a customer idea into a reality, leading development of an app that generated $10k in sales."""))

gpt.add_example(Example("""Product Manager, Managed a team of 15 developers that designed and built an app 
that got to $10k in sales, turning the customers vision for the product into a reality.""",
"""“Managed a team of 15 developers and designers that built an app that quickly sold $10,000 in the first three 
months. The product is now in top-tier app stores and has been featured on several major tech sites."""))

gpt.add_example(Example("""Product Manager, Managed a team of 15 developers that designed and built an app 
that got to $10k in sales, turning the customers vision for the product into a reality.""",
"""“MManaged a team of 15 developers, focusing on all aspects of the mobile experience including product design, 
development, QA, and customer support."""))


# Define UI configuration
config = UIConfig(description="Create bullet points for your resume",
                  button_text="Generate",
                  placeholder="Position applying for, Your experience")

id = "resume-bullet-points"