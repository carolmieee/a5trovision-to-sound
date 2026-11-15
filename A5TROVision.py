import matplotlib.pyplot as plt
import mplcursors
from matplotlib.animation import FuncAnimation
from io import StringIO
import pandas as pd
import numpy as np
import pygame
from matplotlib.widgets import Button
import cv2

pygame.mixer.init(frequency=44100, size=-16, channels=2)
plt.rcParams["toolbar"] = "None"

#FILE
with open("GLB.Ts+dSST.csv", "r", encoding="utf-8") as file:
    temp_csv = file.read()

data = pd.read_csv(
    StringIO(temp_csv.strip()),
    skiprows=1,
    na_values="***"
)

data = data.dropna(subset=["J-D"])
years = data["Year"].to_numpy()
temp = data["J-D"].to_numpy()

#PLOTTING
fig, (ax, mapax) = plt.subplots(
    1, 2,
    figsize=(16, 7)
    )
fig.suptitle(
    "A5TROVision",
    fontsize=22,
    fontweight="bold",
    color="#FFD166"
    )
fig.canvas.manager.set_window_title("A5TROVision")
fig.subplots_adjust(
    bottom=0.18,
    top=0.84
    )

fig.subplots_adjust(
    left=0.08,
    right=0.96,
    top=0.82,
    bottom=0.18,
    wspace=0.20
    )

fig.text(
    0.5, 0.005,
    "A5TROVision | Data Sources: NASA GISTEMP v4, NASA SVS | 1880–2025 | Note: Red line is draggable!",
    ha="center",
    fontsize=9,
    color="#AAB7C4"
    )

video = cv2.VideoCapture("nasa_temp_video.mp4")
video.set(cv2.CAP_PROP_POS_FRAMES, 1)
success, frame = video.read()
mapimage = mapax.imshow(frame)

if success:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    fig.canvas.draw_idle()
    mapimage.set_data(frame)
    mapax.axis("off")
else:
    print("Video frame unreadable")
    
mapax.set_title("Global Map")
mapax.title.set_color("white")

fps = video.get(cv2.CAP_PROP_FPS)
totalframes = video.get(cv2.CAP_PROP_FRAME_COUNT)

temp_plot, = ax.plot(
    years, temp,
    color="#FFD166",
    linewidth=2.5,
    marker="o",
    markersize=3,
    picker=5
)
ax.set_facecolor("#101820")
fig.patch.set_facecolor("#101820")
ax.set_title("Temperature History")
ax.set_xlabel("Year")
ax.set_ylabel("Temperature Anomaly (°C)")
ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")

fig.subplots_adjust(bottom=0.18)

button_ax = fig.add_axes([0.78, 0.045, 0.16, 0.07])

audio_button = Button(
    button_ax,
    "Pause Playback",
    color="#243447",
    hovercolor="#FFD166"
)

audio_button.label.set_color("white")
audio_button.label.set_fontweight("bold")

statustext = ax.text(
    0.03, 0.95,
    "",
    transform=ax.transAxes,
    color="white", fontsize=12, verticalalignment="top",
    bbox=dict(
        facecolor="#243447", edgecolor="#FFD166", alpha=0.9
        )
    )

#FUNCTIONS
def play_temperature_sound(value):
    sample_rate = 44100
    duration = 0.25
    frequency = np.interp(
        value,
        (temp.min(), temp.max()),
        (180, 650)
    )
    t = np.linspace(
        0, duration,
        int(sample_rate*duration),
        endpoint=False
    )
    wave = (
    0.6* np.sin(2*np.pi*frequency*t)
    + 0.12*np.sin(2*np.pi*frequency*2*t)
    )
    envelope = np.ones(len(t))
    fade = int(sample_rate * 0.02)
    envelope[:fade] = np.linspace(0, 1, fade)
    envelope[-fade:] = np.linspace(1, 0, fade)
    wave = wave * envelope
    wave = wave / np.max(np.abs(wave))
    
    left = (wave*32767).astype(np.int16)
    right = (wave*32767).astype(np.int16)
    audio = np.column_stack((left, right))
    
    sound = pygame.sndarray.make_sound(audio)
    sound.play()

selectpoint, = ax.plot(
    [], [],
    marker="o",
    markersize=12,
    linestyle=None
    )

def on_pick(event):
    selected_index = event.ind[0]
    selectedyear = years[selected_index]
    selectedtemp = temp[selected_index]
    play_temperature_sound(selectedtemp)
    selectpoint.set_data([selectedyear], [selectedtemp])
    fig.canvas.draw_idle()

def clearmarkers(event):
    selectpoint.set_data([],[])
    fig.canvas.draw_idle()

clearax = fig.add_axes([0.60, 0.045, 0.15, 0.07])
clearbutton = Button(
    clearax,
    "Clear Marker",
    color="#243447",
    hovercolor="#FFD166"
)

clearbutton.label.set_color("white")
clearbutton.label.set_fontweight("bold")
clearbutton.on_clicked(clearmarkers)

audio_state = {"playing": True}

def toggle_audio(event):
    if currentframe >= len(years):
        return
    
    if audio_state["playing"]:
        pygame.mixer.pause()
        audio_state["playing"] = False
        audio_button.label.set_text("Resume Playback")

    else:
        pygame.mixer.unpause()
        audio_state["playing"] = True
        audio_button.label.set_text("Pause Playback")

audio_button.on_clicked(toggle_audio)

line = ax.axvline(x=1880, color="red")

#MOVES LINE
dragging = {"active": False}
def on_press(event):
    if event.inaxes == ax:
        contains, details = line.contains(event)
        if contains:
            dragging["active"] = True
            
def on_motion(event):
    global currentframe

    if dragging["active"] and event.inaxes == ax:

        selected_index = np.argmin(np.abs(years - event.xdata))

        currentframe = selected_index

        selectedyear = years[selected_index]
        selectedtemp = temp[selected_index]

        line.set_xdata([selectedyear, selectedyear])

        statustext.set_text(
            f"Year: {selectedyear}\n"
            f"Temperature Anomaly: {selectedtemp:+.2f} °C"
        )

        fig.canvas.draw_idle()
        
def on_release(event):
    dragging["active"] = False

#ANIMATION
def init_animation():
    line.set_xdata([years[0], years[0]])
    return line,

currentframe = 0
def update(frame):
    global currentframe
    
    if currentframe >= len(years):
            audio_state["playing"] = False
            pygame.mixer.pause()
            audio_button.label.set_text("Playback Complete")
            return line, mapimage, statustext
            
    if audio_state["playing"]:
        year = years[currentframe]
        temperature = temp[currentframe]
        play_temperature_sound(temp[currentframe])

        statustext.set_text(
            f"Year: {year}\n"
            f"Annual Global Temp Mean Anomaly: {temperature:+.2f} °C\n"
            f"Reference Baseline: 1951-1980"
            )
        line.set_xdata([year, year])
        
        video_frame_index = (year - 1880) * 12
        
        video.set(cv2.CAP_PROP_POS_FRAMES, video_frame_index)
        success, videoframe = video.read()

        if success:
            videoframe = cv2.cvtColor(
                videoframe, cv2.COLOR_BGR2RGB)
            mapimage.set_data(videoframe)
        else:
            print("Videoframe unreadable")    
        currentframe+=1
    return line, mapimage, statustext

def reset(event):
    global currentframe
    currentframe = 0
    pygame.mixer.stop()
    audio_state["playing"] = True
    audio_button.label.set_text("Pause Playback")
    line.set_xdata([years[0], years[0]])
    statustext.set_text(
        f"Year: {years[0]}\n"
        f"Temperature Anomaly: {temp[0]:+.2f} °C"
        )
    video.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, videoframe = video.read()
    if success:
        videoframe = cv2.cvtColor(
            videoframe, cv2.COLOR_BGR2RGB)
        mapimage.set_data(videoframe)
    fig.canvas.draw_idle()

resetax = fig.add_axes([0.40, 0.045, 0.15, 0.07])
resetbutton = Button(
    resetax,
    "Reset Playback",
    color="#243447",
    hovercolor="#FFD166"
)

resetbutton.label.set_color("white")
resetbutton.label.set_fontweight("bold")
resetbutton.on_clicked(reset)

animation = FuncAnimation(
    fig,
    update,
    frames=None,
    init_func=init_animation,
    interval=410,
    blit=False,
    cache_frame_data=False
)

fig.canvas.mpl_connect("pick_event", on_pick)
fig.canvas.mpl_connect("button_press_event", on_press)
fig.canvas.mpl_connect("motion_notify_event", on_motion)
fig.canvas.mpl_connect("button_release_event", on_release)

cursor = mplcursors.cursor(temp_plot, hover=2)
@cursor.connect("add")
def on_add(sel):
    index = int(sel.index)

    selected_year = years[index]
    selected_temp = temp[index]

    sel.annotation.set_text(
        f"Year: {selected_year}\nTemperature: {selected_temp:.2f}°C"
    )
    sel.annotation.set_color("white")
    sel.annotation.get_bbox_patch().set(
        facecolor="#243447",
        edgecolor="#FFD166",
        alpha=0.95
        )

plt.show()
