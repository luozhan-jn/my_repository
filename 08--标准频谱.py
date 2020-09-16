import librosa.display
import numpy as np
import matplotlib.pyplot as plt

y,sr = librosa.load(r'D:\数据集\EmoDB\03a01Fa.wav')
plt.figure()
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)),ref=np.max)
# stft短时傅里叶变换，复数的实部：np.abs(D(f,t))频率的振幅
# 幅度转为分贝，ref为参考值
plt.subplot(2,1,1)
librosa.display.specshow(D,y_axis='linear')
plt.colorbar(format='%+2.0f dB')
plt.title('linear-frequency power spectrogram')

plt.subplot(2,1,2)
librosa.display.specshow(D,y_axis='log')   # 频谱以对数刻度展示
plt.colorbar(format='%+2.0f dB')
plt.title('log-frequency power spectrogram')
plt.show()