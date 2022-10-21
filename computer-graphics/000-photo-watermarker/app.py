from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt

def calc_positon_watermarks(w,h):
  w_ten_percent=w//10
  h_ten_percent=h//10
  return [
      (w_ten_percent*0,h_ten_percent*0,),
      (w_ten_percent*2,h_ten_percent*2,),
      (w_ten_percent*4,h_ten_percent*4,),
      (w_ten_percent*6,h_ten_percent*6,),
      (w_ten_percent*8,h_ten_percent*8,),
  ]

watermark_text=input('Enter watermark text:')
# image opening
image = Image.open(input('Enter image path:'))
# this open the photo viewer
image.show()
plt.imshow(image)

# text Watermark
watermark_image = image.copy()
draw = ImageDraw.Draw(watermark_image)

font_size=watermark_image.width//28
# ("font type",font size)
font = ImageFont.truetype("arial.ttf", font_size)
  
for position in calc_positon_watermarks(
    watermark_image.width,
    watermark_image.height
    ):
  # add Watermark
  # (0,0,0)-black color text
  draw.text(position, watermark_text, (0, 0, 0), font=font)

# plt.subplot(1, 2, 1)
# plt.title("title text")
plt.imshow(watermark_image)
  