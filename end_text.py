import moviepy.editor as mp
import gizeh as gz
import gizeh
from moviepy.editor import *
from moviepy.editor import VideoFileClip
def texts_end(Width,Height,username,username_size,user_pro_name,video_dir,dp_image_size,user_pro_name_size,last_duration):
  def make_frame(t):
    surface = gizeh.Surface(width=Width, height=Height)
    text_user=gz.text(user_pro_name,fontfamily="Helvetica",fill=(0.9607843137254902, 0.9607843137254902, 0.9607843137254902),
                fontweight="bold",
                fontsize=user_pro_name_size, xy=(int(Width*.5),int(Height*.3+1.2*dp_image_size)),h_align='center'
                )
    text = gz.text(username, fontfamily="Helvetica",fill=(0.5019607843137255, 0.5019607843137255, 0.5019607843137255),
                 fontweight="bold",
                fontsize=username_size, xy=(int(Width*.5), int(Height*.3+1.45*user_pro_name_size+dp_image_size)),h_align='center'
                )
    text_user.draw(surface)
    text.draw(surface)
    return surface.get_npimage(transparent=True)
  original_clip = VideoFileClip(video_dir)
  graphics_clip_mask_end = VideoClip(lambda t: make_frame(t)[:, :, 3] / 255.0, 
                                   duration=last_duration, ismask=True)
  graphics_clip_end= VideoClip(lambda t: make_frame(t)[:, :, :3],
                              duration=last_duration).set_mask(graphics_clip_mask_end)   
  return original_clip,graphics_clip_end