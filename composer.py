import cv2
from moviepy.editor import *
from random import *
import moviepy.video.fx.all as vfx

def compose_final():
    list = []
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_0.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_1.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_2.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_3.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_4.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_5.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_6.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_7.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_8.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_9.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_10.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_11.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_12.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_13.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_14.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_15.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_16.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_17.mp4"))
    #list.append(VideoFileClip(r"D:\Marko\PycharmProjects\Video_alpha\clip_18.mp4"))
    #final_clip = concatenate_videoclips(list)
    clip1 = VideoFileClip(r"D:\Marko\VIDEO\2021-01-21 04-30-22.mp4")
    clip2 = VideoFileClip(r"D:\Marko\VIDEO\2021-01-21 04-47-44.mp4")
    clip3 = VideoFileClip(r"D:\Marko\VIDEO\2021-01-21 04-57-40.mp4")
    clip4 = clip3.subclip(0,520)
    clip5 = clip3.subclip(0,78)
    final_clip = concatenate_videoclips([clip1,clip2,clip4])
    audio_file = AudioFileClip(r"D:\Marko\PycharmProjects\Video_alpha\song.mp3")
    audio_file2 = AudioFileClip(r"D:\Marko\PycharmProjects\Video_alpha\song3.mp3")
    audio_final = concatenate_audioclips([audio_file2])

    final_clip3 = final_clip.fx(vfx.speedx, 1.2 )
    final_clip4 = final_clip3.set_fps(60)
    final_clip5 = final_clip4.set_audio(audio_final)

    final_clip.write_videofile("clip_final008.mp4")


compose_final()