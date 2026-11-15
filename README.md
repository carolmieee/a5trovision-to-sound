# A5TROVision
An experimental Python project that transforms NASA global temperature anomaly data into an interactive, multisensory experience. It combines scientific data visualization, audio sonification, and geographical temperature visualizations to make information more engaging and accessible. 
A5TROVision converts scientific data into something more easy to understand, utilizing sound to complement visuals.
Status: Prototype, currently focused on Global Temperature Anomalies

1. FEATURES
- Displays historical global temperature anomalies in a line graph.
- Converts temperature anomaly values into changing sound frequencies.
- Displays a NASA temperature visualization alongside the graph.
- Progresses through the historical data while updating the sound, graph marker, and map video.
- Allows users to select individual data points and hear their corresponding sound.
- Includes pause, resume, reset, and marker-clearing controls.
- Displays the selected year, temperature anomaly, and reference baseline.

2. Scientific Data
Data source: https://data.giss.nasa.gov/gistemp/
CSV dataset: https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv
Map Visuals (NASA SVS): https://svs.gsfc.nasa.gov/5603/?utm
The project uses the J-D column, which represents the annual January–December global mean temperature anomaly.
Measurement: Global temperature anomaly (°C), which is the difference between a measured temperature and the average temperature during a reference period.
Reference baseline: 1951–1980
Time period: Available complete annual records in the downloaded dataset

4. Further Improvements
A5TROVision is currently intended to complement traditional scientific visualizations, not replace them. And since it is still a prototype, further improvements can be made:
- To Expand the project to support additional NASA Earth science datasets.
- To Improve audio transitions for a smoother listening experience.
- To Add more interactive controls and playback options.
- To Improve synchronization and user interaction.
- To Explore additional sound mappings to represent different scientific variables.
- To Improve accessibility through keyboard interaction and clearer non-visual descriptions.

# How to run? :0
- Make sure you have Python installed (use IDLE to run), along with matplotlib, numpy, pandas, mplcursors, pygame, opencv. (Open CMD, type this: pip install matplotlib numpy pandas mplcursors pygame opencv-python )
- Make sure to download ALL FILES and put them in ONE SAME folder (and do NOT change any of the file names! Unless you know how to modif the code)
- for the "nasa_temp_video.mp4", make sure to install it from here https://github.com/carolmieee/a5trovision-to-sound/releases/tag/v1.0.0
(make sure the video name is "nasa_temp_video.mp4", do NOT change it! Put it in the same folder as the rest of the files)

