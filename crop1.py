from PIL import Image, ImageOps, ImageDraw
def cropped_img(input_dir,output_dir):
  size = (512, 512)
  mask = Image.new('L', size, 0)
  draw = ImageDraw.Draw(mask) 
  draw.ellipse((0, 0) + size, fill=255)
  img = Image.open(input_dir)

  output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
  output.putalpha(mask)
  output.save(output_dir)
  return output_dir