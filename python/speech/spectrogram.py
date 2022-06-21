import sounddevice
from scipy.io.wavfile import write
import os
import librosa
import librosa.display
import IPython.display as ipd
import numpy as np
import matplotlib.pyplot as plt
fps=44100
duration=2
print("record....")
recording=sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
sounddevice.wait()
print("done!")
write("output.wav",fps,recording)
scale_file = "C:\Users\adi61\planetwalks\python\speech\output.wav"
ipd.Audio(scale_file)
# load audio files with librosa
scale, sr = librosa.load(scale_file)
FRAME_SIZE = 2048
HOP_SIZE = 512
S_scale = librosa.stft(scale, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
S_scale.shape
type(S_scale[0][0])
Y_scale = np.abs(S_scale) ** 2
Y_scale.shape
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