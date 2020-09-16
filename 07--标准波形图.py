import librosa.display
import matplotlib.pyplot as plt
y,sr = librosa.load(r'D:\数据集\EmoDB\03a01Fa.wav',sr=None)
librosa.display.waveplot(y,sr=sr,x_axis='time')
print(type(y))
print(sr)
plt.show()