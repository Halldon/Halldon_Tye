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

##Creates Pain-Agitate-Solution

gpt.add_example(Example("""Candles, All natural soy wax candles made with essential oils.""",
"""Pain: With the hustle and bustle of todays’ lifestyles, candles can be a great way to relax, 
unwind and shut out all the distractions. So why are you being distracted by the man MADE fragrances 
when all you want is that amazing natural soy smell?
Agitate: We use uplifting combinations of pure natural essential oils in our candles. You don’t need to 
worry about coughing from fumes or getting a headache because our candles are all natural. Our handmade 
soy candles burn cleaner and much longer than paraffin candles!
Solution: We were looking for soy wax candles made of 100% natural soy wax with quality pure essential 
oils when we couldn’t find any anywhere! That’"""))


gpt.add_example(Example("""Candles, All natural soy wax candles made with essential oils.""",
"""Pain: Most candles are laden with chemicals, toxins, and fillers to cut costs.
Agitate: We only use natural soy wax, essential oils and jar sizes which allow the scents to fully develop in your home environment.
Solution: Our range of ‘clean’ scented candles are 100% natural, clean burning & perfect for you."""))

gpt.add_example(Example("""Candles, All natural soy wax candles made with essential oils.""",
"""Pain: Traditional candles are not very... natural. Additives, wicks and nasty chemicals release an off smell.
Agitate: You deserve a pure candle experience. Pure bliss!
Solution: Candles made by hand with 100% soy wax and essential oils so they smell great and stay clean burning. Pure bliss in a candle!"""))

gpt.add_example(Example("""Candles, All natural soy wax candles made with essential oils.""",
"""Pain: Not all candles are equal. Store-bought candles often contain harmful chemicals.
Agitate: So why do we still buy them? We don’t have to.
Solution: Cliche as it may be, the solution is simple – Candles, made from Soy Wax and essential oils. All our products are handmade 
in the UK by a professional candle maker with 20 years experience in the industry, using only 100% natural soy wax and essential oils. 
Each product is designed for maximum aroma and will burn for up to 50 hours - perfect for a relaxing evening in!"""))

gpt.add_example(Example("""Candles, All natural soy wax candles made with essential oils.""",
"""Pain: Not all candles are equal. Store-bought candles often contain harmful chemicals.
Agitate: So why do we still buy them? We don’t have to.
Solution: Cliche as it may be, the solution is simple – Candles, made from Soy Wax and essential oils. All our products are handmade 
in the UK by a professional candle maker with 20 years experience in the industry, using only 100% natural soy wax and essential oils. 
Each product is designed for maximum aroma and will burn for up to 50 hours - perfect for a relaxing evening in!"""))

gpt.add_example(Example("""heated mug, Never let your coffee go cold again with this heated mug.""",
"""Pain: Cursing your coffee for going cold? You know the feeling.
Agitate: We know just how bad that taste is, which is why we’ve designed Heated Mug. It keeps your 
drink temperature at the ideal all-day drinking temperature for up to 5 hours.
Solution: All you need is our revolutionary heated mug. Take a look at our website to find out 
it all works and the benefits it can bring you."""))

gpt.add_example(Example("""heated mug, Never let your coffee go cold again with this heated mug.""",
"""Pain: Ice cold coffee. Who invented that?
Agitate: Keep your coffee warm for up to 12 hours with our heated mug. Just press the button on 
the side and watch your hot beverage come to life.
Solution: Our heated design means no more burnt tongue, just a great cup of warm coffee, tea or cocoa. 
Perfect for at home or work."""))

gpt.add_example(Example("""heated mug, Never let your coffee go cold again with this heated mug.""",
"""Pain: The smell of fresh coffee is one thing, but the taste is another.
Agitate: Your morning is precious and you only get one shot at getting it right.
Solution: Enjoy every sip of your coffee with the heated mug. This unique mug preserves the temperature 
to keep your coffee at just the right temperature for longer."""))

gpt.add_example(Example("""heated mug, Never let your coffee go cold again with this heated mug.""",
"""Pain: Cold coffee…yuk.
Agitate: You love your morning coffee, but hate it when it goes lukewarm before you’ve even had a chance to savour it.
Solution: Heated mug is the only mug on the planet where your coffee will never go cold or taste watered down, 
no matter how long you leave it! No batteries required and costs less than a cheap takeaway latte!"""))

gpt.add_example(Example("""heated mug, Never let your coffee go cold again with this heated mug.""",
"""Pain: Cold coffee…yuk.
Agitate: You love your morning coffee, but hate it when it goes lukewarm before you’ve even had a chance to savour it.
Solution: Heated mug is the only mug on the planet where your coffee will never go cold or taste watered down, 
no matter how long you leave it! No batteries required and costs less than a cheap takeaway latte!"""))

gpt.add_example(Example("""plant shelf, Organize all of your plants.""",
"""Pain: You’re the type of person that likes to keep everything neat and orderly. But one day you realize that 
all your plants are taking over your home – they’re everywhere!
Agitate: There’s something else too. You worry about the safety of your plants. You know they need light, but will 
they get enough? What if you accidentally leave a window open? How about water – will they get enough? Plants are 
difficult to take care of for most people – you need all the help you can get.
Solution: With plant shelf, you can finally organize all of your plants into easy to use and see containers with custom 
shelves that grow around them. Plus, you can also easily control the lights"""))

gpt.add_example(Example("""plant shelf, Organize all of your plants.""",
"""Pain: Keeping all of your plants organized can be overwhelming, particularly in a small studio.
Agitate: Plants are so good for you, but keeping them tidy and without over crowding is near impossible.
Solution: plant-shelf is the perfect solution for plant lovers everywhere. No longer will your beautiful plants look messy; 
simply place them on our reusable plant shelf and enjoy their health benefits and beauty. Happy customers say 
it’s “just what they’ve been waiting for!”"""))


# Define UI configuration
config = UIConfig(description="Create a Pain-Agitate-Solution.",
                  button_text="Create",
                  placeholder="Product/Brand name (optional), Describe your product.")

id = "create-pas-app"