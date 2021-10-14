#logo_text creation 
import moviepy.editor as mp
import gizeh as gz
import gizeh
from moviepy.editor import *
def final_clip(Width,Height,half_duration,end_duration):
  	CompositeVideoClip(
        [original_clip,
         graphics_clip_left.set_start(0).set_duration(x),
         graphics_clip_right.set_start(x).set_duration(x),
         logo_left.set_start(0).set_duration(half_duration),
         logo_right.set_start(half_duration).set_duration(half_duration),
         graphics_clip_end.set_start(duration).set_duration(end_duration),
         dp.set_start(duration).set_duration(end_duration),
         logo_end.set_start(duration).set_duration(end_duration)],
        size=(Width, Height))
  	return final_clip
