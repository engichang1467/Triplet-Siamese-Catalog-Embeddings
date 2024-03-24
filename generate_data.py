import cohere
import csv
import os
from dotenv import load_dotenv, find_dotenv


# Load the API key from the .env file
_ = load_dotenv(find_dotenv()) # read local .env file
cohere_api_key = os.environ['COHERE_API']

command_prompt= '''This is a sample dataset in csv below, and I want you to help me generate more data with different variations (at least 100 examples) 
(FYI: the `QUERY_TEXT` can include:  alcohol, backed goods, bowl, bread, breakfast, burger, burrito, cake, chicken, coffee, cookie, curry, dessert, donut, dumpling, eggs, fried food, fries, hot dog, huevos con jamon, ice crea,, juice mixed vegetables, noodle, pancake, pasta, pie, pizza, plate, poke, rice, salad, sandwich, sauce, seafood, skewer, skewers, smoothie, soda, soup, steak, stir fry, sushi, taco, tea, water, wings, and  wrap)

```csv
QUERY_TEXT,POSITIVE,NEGATIVE
desserts, shakes,veggie burger with cheeese
sushi, thai chef fresh rolls, meat lasagna
acai bowl, acai bowl delivered, mint chocolate chip polar pizza
cupcake, carrot, buffalo chicken
```'''

co = cohere.Client(cohere_api_key)
response = co.generate(
  model='command',
  prompt=command_prompt,
  max_tokens=2606,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')

txt_response = response.generations[0].text

txt_split_1 = txt_response.split("```csv")
txt_split_2 = txt_split_1[1].split("```")
data_text = txt_split_2[0]

# Split the string into lines
lines = data_text.strip().split('\n')

# Write the data to a CSV file
with open('data/additional_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for line in lines:
        writer.writerow(line.split(', '))

print("CSV file 'additional_data.csv' has been created successfully!")