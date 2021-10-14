#logo creation 
import moviepy.editor as mp
import gizeh as gz
import gizeh
from moviepy.editor import *
def logo(Width, Height,gif_dir,logo_size):
	logo_left = (mp.VideoFileClip(gif_dir,has_mask=True)
          .loop()
          .resize(height=logo_size) # if you need to resize...
          .margin(left=int(Width*.012), top=int(Height*.012), opacity=0) # (optional) logo-border padding
          .set_pos(("left","top")))

	logo_right=(mp.VideoFileClip(gif_dir,has_mask=True)
          .loop()
          .resize(height=logo_size) # if you need to resize...
          .margin(right=int(Width*.015), bottom=int(Height*.04), opacity=0) # (optional) logo-border padding
          .set_pos(("right","bottom")))
	
	return logo_left, logo_right 
