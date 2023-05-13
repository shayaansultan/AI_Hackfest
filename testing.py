import easyocr
import PIL
from PIL import ImageDraw
import numpy as np
import re

# Load image and extract text using EasyOCR
reader = easyocr.Reader(['en'], gpu=False)
im = PIL.Image.open("/content/veggie-grocery-receipt_orig.png")
im_np = np.array(im)
bounds = reader.readtext(im_np)

# Draw bounding boxes around text
def draw_boxes(image, bounds, color='red', width=2):
  draw = ImageDraw.Draw(image)

  for bound in bounds:
    p0, p1, p2, p3 = bound[0]
    draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
  
  return image

im_with_boxes = draw_boxes(im, bounds)

# Extract product names and prices
reciept_text = ""
for i in range(len(bounds)):
  reciept_text += str(bounds[i][1]) + " "

product_pattern = r'[A-Z ]+'
price_pattern = r'\d+\.\d{2}'
product_prices = re.findall(product_pattern + r'\n' + price_pattern, reciept_text)

# Print extracted products and prices
for item in product_prices:
  product, price = item.split('\n')
  print(f'Product: {product}, Price: {price}')


receipt_text = ""
for i in range(len(bounds)):
    receipt_text+= bounds[i][1]
    receipt_text += "\n"
print(receipt_text)

import openai

# Set up the OpenAI API
openai.api_key = "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"

# Call the API
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", 
         "content": f"Given the following text from a receipt, kindly identify what items are bought and for how much. Display it in the format [Product Name] : [Price]. Do not include anything else.\n{receipt_text}"}
        ]
)

# Print the response
print(response['choices'][0]['message']['content'])