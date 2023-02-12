import cv2
from moviepy.editor import *
from random import *
from PIL import Image


full_clip = VideoFileClip(r"D:\Marko\VIDEO\2021-02-03 19-08-58.mp4")

print(full_clip.duration)

fps = 60
seconds = 4
differencial = 100
counter = 0
counter2 = 0
img_list = []
img_list2 = []
change_list = []
change_list_steamlined = []
list = []
repo = ()
final_clip = ()
for i in range(0,5000):
    img_list.append([])

for i in range(0,5000):
    img_list2.append([])

def check_frames():
    global counter, repo, img_list, fps, seconds
    cap = cv2.VideoCapture(r"D:\Marko\VIDEO\2021-02-03 19-08-58.mp4")
    for i in range(1, int(full_clip.duration) * fps, seconds * fps):
        cap.set(1, i)
        res, frame = cap.read()  # frame has your pixel values

        # Get frame height and width to access pixels
        height, width, channels = frame.shape
        #for x in range(1007, 1038):
            #for y in range(1838, 1853):
        # Accessing BGR pixel values
        for x in range(0, 26):
            for y in range(900, 1000):
                img_list[counter] += (frame[x, y, 2], frame[x, y, 1], frame[x, y, 0])
        # print(img_list)
        repo = tuple(img_list)
        # print(repo)
        counter += 1
        print("checking frames: " + str(counter - 1) + " out of " + str(int(full_clip.duration / seconds)))




print(counter)
print(img_list[0])
print(img_list[1])

def calc_diff():
    global change_list, differencial
    for i in range(0, counter - 1):
        for y in range(0, len(img_list[0])):
            if abs(int(img_list[i][y]) - int(img_list[i + 1][y])) > differencial:
                change_list.append(i * seconds)
                print(abs(img_list[i][y] - img_list[i + 1][y]))
        print("calculating differences: " + str(i) + " out of " + str(counter - 1))

    print(change_list)


def streamline():
    r_value = 0

    for i in range(len(change_list)):
        x = change_list[i]
        if x != r_value:
            drt = randrange(7, 10)
            change_list_steamlined.append([x, drt])
            r_value = x

    for i in range(len(change_list_steamlined)-1):
        if change_list_steamlined[i][0] < 7:
            change_list_steamlined.pop(i)

    print(change_list_steamlined)

    for i in range(len(change_list_steamlined)-1):
        #print(i)
        if i >= len(change_list_steamlined)-2:
            break

        if abs(int(change_list_steamlined[i][0]) - int(change_list_steamlined[i+1][0]))< seconds * 3:
            x = int(change_list_steamlined[i+2][0])
            change_list_steamlined.pop(i + 1)
            if abs(int(change_list_steamlined[i][0]) - x) < seconds * 3:
                change_list_steamlined.pop(i + 1)
            change_list_steamlined[i][1] = change_list_steamlined[i][1]*2
            print(len(change_list_steamlined))




[[9, 8], [69, 9], [153, 7], [171, 10], [183, 8], [216, 8], [219, 8], [243, 7], [261, 8], [264, 9], [300, 9], [348, 6], [375, 7], [378, 9], [390, 6], [399, 8], [408, 8], [453, 6], [477, 6], [480, 9], [489, 8], [579, 10], [600, 8], [603, 7], [612, 8], [642, 6], [663, 10], [672, 10], [735, 10], [783, 9], [825, 6], [855, 8], [876, 10], [879, 7], [882, 10], [891, 7], [918, 7], [921, 10], [996, 8], [999, 6], [1026, 10], [1050, 6], [1128, 10], [1179, 10], [1215, 8], [1350, 10], [1356, 9], [1359, 10]]




def generate_clip():
    global list, final_clip

    for i in range(len(change_list_steamlined)):
        begining = randrange(2, 4)
        clip = full_clip.subclip(int(change_list_steamlined[i][0]) - begining,
                                 int(change_list_steamlined[i][0]) - begining + int(change_list_steamlined[i][1]))
        list.append(clip)
        print("clip from second: " + str(change_list_steamlined[i])+" begining time offset: "+str(begining))

    final_clip = concatenate_videoclips(list)

    print(list)


def generate_clips():
    global list, final_clip

    for i in range(len(change_list_steamlined)):
        begining = randrange(2, 4)
        clip_name = "clip_"+str(i)+".mp4"
        clip = full_clip.subclip(int(change_list_steamlined[i][0]) - begining,
                                 int(change_list_steamlined[i][0]) - begining + int(change_list_steamlined[i][1]))
        print("clip " + str(i) + " out of " + str(len(change_list_steamlined)))
        print("clip from second: " + str(change_list_steamlined[i][0]) + " begining time offset: " + str(
            begining) + " clip duration (sec): " + str(int(change_list_steamlined[i][1])))
        clip.write_videofile(clip_name)


    print(list)



def render_video():
    audio_file = AudioFileClip(r"D:\Marko\PycharmProjects\Video_alpha\song.mp3")
    final_clip2 = final_clip.set_audio(audio_file)

    final_clip.write_videofile("video005.mp4")

check_frames()
calc_diff()
streamline()
#generate_clips()
generate_clip()
render_video()

#im= Image.new('RGB', (19, 2))
#im.putdata(repo)
#im.save('test.png')
#git token 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