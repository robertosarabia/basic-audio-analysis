# Example 1: short-term feature extraction
from pyAudioAnalysis import ShortTermFeatures as aF
from pyAudioAnalysis import audioBasicIO as aIO
import numpy as np
import plotly.graph_objs as go
import plotly
import IPython

# read audio data from file
# (returns sampling freq and signal as a numpy array)
fs, s = aIO.read_audio_file("data/object.wav")