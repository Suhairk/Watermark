#logo_text creation 
import moviepy.editor as mp
from moviepy.editor import *
def end_dp_logo(Width, Height,crop_image,gif_dir,dp_image_size,logo_end_size):

  dp = (mp.ImageClip(crop_image)
          .resize(height=dp_image_size) # if you need to resize...
          .margin(top=int(Height*.3), opacity=0).set_position(("center","top")))
          #.set_pos(("center")))
  logo_end = (mp.VideoFileClip(gif_dir,has_mask=True)
          .loop()
          #.set_duration(video.duration)
          .resize(height=(logo_end_size)) # if you need to resize...
          .margin(top=int(Height*.65), opacity=0).set_position(("center","top")))# (optional) logo-border padding
            #.set_position(("left","center")))
  return dp,logo_end
