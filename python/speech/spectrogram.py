import sounddevice
from scipy.io.wavfile import write
import os
import librosa
import librosa.display
import IPython.display as ipd
import numpy as np
import matplotlib.pyplot as plt

import os
import time

FPS=4076
DURATION=2

# Get number of input channels using python3 -m sounddevice 
INPUT_CHANNELS = 1

OUTPUT_DIR = "recordings/"

soundSample = input("Give name of sample recording, say if recoridng hello, then name would be hello\n")

if soundSample == "":
    soundSample = "random"
    
path = OUTPUT_DIR+soundSample+'/'
os.makedirs(path, exist_ok=True)

timestamp = time.time()
print("record....")
recording=sounddevice.rec(int(DURATION*FPS),samplerate=FPS,channels=INPUT_CHANNELS)
sounddevice.wait()
print("done!")
currentRecordingName = f'{soundSample}-{timestamp}'
currentRecordingNameWithExtension = f'{currentRecordingName}.wav'
recordingPath = f'{path}{currentRecordingNameWithExtension}'
write(recordingPath, FPS,recording)


#---------------------------------------------------------------------------
#Loading recorded file for spectrogram 

ipd.Audio(recordingPath)
# load audio files with librosa
scale, sr = librosa.load(recordingPath)



FRAME_SIZE = 2048     #Define Frame Size
HOP_SIZE = 512        #Define Hop Size

S_scale = librosa.stft(scale, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
S_scale.shape
type(S_scale[0][0])
Y_scale = np.abs(S_scale) ** 2

spectrogramPath = f'{path}{currentRecordingName}.csv'
np.savetxt(spectrogramPath,Y_scale, delimiter=",")
type(Y_scale[0][0])
def plot_spectrogram(Y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y,
                             sr=sr,
                             hop_length=hop_length,
                             x_axis="time",
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")
Y_log_scale = librosa.power_to_db(Y_scale)
plot_spectrogram(Y_log_scale, sr, HOP_SIZE)
plot_spectrogram(Y_log_scale, sr, HOP_SIZE, y_axis="log")