#logo_text creation 
import moviepy.editor as mp
import gizeh as gz
import gizeh
from moviepy.editor import *
def logo_text(Width,Height,username,video_dir,logo_text_size,half_duration,logo_size):
	
	def make_frame_left(t):
  		surface = gz.Surface(width=Width, height=Height)
  		text = gz.text(username, fontfamily="Helvetica",fill=(0.9607843137254902, 0.9607843137254902, 0.9607843137254902),
                 fontweight='bold',h_align="left",
                fontsize=logo_text_size ,xy=(int(Width*.03),int(Height*0.012+10.5+logo_size))
                )
  		text.draw(surface)
  		return surface.get_npimage(transparent=True)

	def make_frame_right(t):
  		surface = gz.Surface(width=Width, height=Height)
  		text = gz.text(username, fontfamily="Helvetica",fill=(0.9607843137254902, 0.9607843137254902, 0.9607843137254902),
                 fontweight='bold',h_align='right',
                fontsize=logo_text_size , xy=(int(Width*.98),int(Height*.97))
                )
  		text.draw(surface)
  		return surface.get_npimage(transparent=True)

	original_clip = VideoFileClip(video_dir)

	graphics_clip_mask_left = VideoClip(lambda t: make_frame_left(t)[:, :, 3] / 255.0, 
                                   duration=half_duration, ismask=True)
	graphics_clip_left = VideoClip(lambda t: make_frame_left(t)[:, :, :3],
                              duration=half_duration).set_mask(graphics_clip_mask_left)

	graphics_clip_mask_right = VideoClip(lambda t: make_frame_right(t)[:, :, 3] / 255.0, 
                                   duration=half_duration, ismask=True)
	graphics_clip_right= VideoClip(lambda t: make_frame_right(t)[:, :, :3],
                              duration=half_duration).set_mask(graphics_clip_mask_right)





	return original_clip,graphics_clip_left, graphics_clip_right


