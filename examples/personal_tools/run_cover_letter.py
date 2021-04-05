#Model works, after insprecting output in dev tools, the formatting issue is a UI issue, not a backend issue. 
import os
import sys
API_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')
sys.path.append(API_PATH)

from api import GPT, Example, UIConfig


# Construct GPT object and show some examples
gpt = GPT(engine="curie-instruct-beta",
          temperature=0.85,
          max_tokens=800)

gpt.add_example(Example('Data Scientist, Experience mining data, optimizing classifiers.',
'Ebony Moore\n(123) 456-7891\nemoore@email.com\nMay 1, 2018\nDear  Hiring Manager,\nI would like to introduce myself as an applicant for the Data Scientist position at River Tech, a prestigious and reputable name in innovative technology. I am confident in my ability to perform as a Data Scientist at River Tech due to my extensive education and work experience.\nDuring my work experience at Crane & Jenkins, I had an extensive range of responsibilities including selecting features, optimizing classifiers, mining data, expanding the company\'s data by incorporating third-party sources, improving data collection techniques, processing data, and doing ad-hoc analyses. As a Data Scientist, I was required to have excellent communication skills, understanding of algorithms, excellence in the MatLab tool kit, proficiency in GGplot, knowledge of SQL, and excellence in applied statistics. During my eight-year tenure at Crane & Jenkins, I applied these skills daily and performed exceptionally at the company.\nMy abilities as a Data Scientist are rooted in a sturdy education in mathematics. I began with a bachelor\'s degree in computer science from Longford Tech. I followed this with a master\'s degree in statistics and a Ph.D. in applied mathematics. I attribute my success as a Data Scientist in large part to this extensive and in-depth education. I believe my personality has also played a major role in my ability to succeed in this career. I am an extremely analytical, data-oriented, and calculated. Even in my personal life I like to look at the data before making a decision. I like to analyze outcomes.\nI would like to thank you for taking the time to review my application. I look forward to hearing more about River Tech and the details of the Data Scientist position. I feel that my education and experience will ensure my success in this role.\nSincerely,\nEbony Moore'))



# Define UI configuration
config = UIConfig(description="Create a cover letter.",
                  button_text="Create",
                  placeholder="Tell me the role you're applying for and what experience makes you a good candidate.")
id = "cover-letter-creator"
