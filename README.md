# A5TROVision
An experimental Python project that transforms NASA global temperature anomaly data into an interactive, multisensory experience. It combines scientific data visualization, audio sonification, and geographical temperature visualizations to make information more engaging and accessible.
Status: Prototype, currently focused on Global Temperature Anomalies

1. Problem:
Scientific information is often communicated through charts, graphs, and visualizations. While these formats are useful, relying on visual information alone can create barriers for people who benefit from alternative ways of experiencing data.
A5TROVision offers another way to interpret changes in our planet, utilizing sound other to complement visuals.

2. Solution
A5TROVision makes Earth Information more accessible and interactive through utilization of sight, sound, and numerical information. Sound helps in complementing visual information, making it more easier to understand, and to know which direction the data is going/showing.

3. FEATURES
- Displays historical global temperature anomalies in a line graph.
- Converts temperature anomaly values into changing sound frequencies.
- Displays a NASA temperature visualization alongside the graph.
- Progresses through the historical data while updating the sound, graph marker, and map video.
- Allows users to select individual data points and hear their corresponding sound.
- Includes pause, resume, reset, and marker-clearing controls.
- Displays the selected year, temperature anomaly, and reference baseline.

4. Scientific Data
Data source: https://data.giss.nasa.gov/gistemp/
CSV dataset: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv
The project uses the J-D column, which represents the annual January–December global mean temperature anomaly.
Measurement: Global temperature anomaly (°C), which is the difference between a measured temperature and the average temperature during a reference period.
Reference baseline: 1951–1980
Time period: Available complete annual records in the downloaded dataset

This program maps the datasets to 180 Hz and 650 Hz, minimum and maximum.
Lower temperature anomaly values produce lower pitches.
Higher temperature anomaly values produce higher pitches.
The sound is generated using NumPy and played through Pygame.
- For the video, the graph and video are related representations, not necessarily identical ones, as the graph shows the mean temp anomaly, while the map is a visualization.

# How to run? :0
- Make sure you have Python installed (use IDLE to run), along with matplotlib, numpy, pandas, mplcursors, pygame, opencv. (Open CMD, type this: pip install matplotlib numpy pandas mplcursors pygame opencv-python )
- Make sure to download ALL FILES and put them in ONE SAME folder (and do NOT change any of the file names! Unless you know how to modif the code)
- for the "nasa_temp_video.mp4", make sure to install it from here https://github.com/carolmieee/a5trovision-to-sound/releases/tag/v1.0.0
(make sure the video name is "nasa_temp_video.mp4", do NOT change it! Put it in the same folder as the rest of the files)

5. Purpose
To make Earth science more accessible and engaging by combining visual information with sound, and to explore sound as a different way to explore and understand the changes happening to our planet.

6. Tech Used
Python = Main programming language
Pandas = Reading and processing NASA datasets
NumPy = Numerical calculations and audio waveform generation
Matplotlib =  Data visualization and interactive graphs
mplcursors =  Interactive graph information
Pygame =  Audio generation and playback
OpenCV = Reading and displaying the NASA geographical visualization

7. Further Improvements
A5TROVision is currently intended to complement traditional scientific visualizations, not replace them. And since it is still a prototype, further improvements can be made:
- To Expand the project to support additional NASA Earth science datasets.
- To Improve audio transitions for a smoother listening experience.
- To Add more interactive controls and playback options.
- To Improve synchronization and user interaction.
- To Explore additional sound mappings to represent different scientific variables.
- To Improve accessibility through keyboard interaction and clearer non-visual descriptions.
