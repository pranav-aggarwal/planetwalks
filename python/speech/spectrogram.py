import sounddevice
from scipy.io.wavfile import write
fps=44100
duration=2
print("record....")
recording=sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
sounddevice.wait()
print("done!")
write("output.wav",fps,recording)
