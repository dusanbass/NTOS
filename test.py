import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import wave
import sys
from scipy.fftpack import fft
from pylab import*

fileW1 = 'Mixdown 1.wav'
fileW2 = 'Mixdown 2.wav'

sampFreq1, wav1 = wavfile.read(fileW1, mmap=True)
wav1 =  wav1 / (2.**15)
number_of_samples1 = wav1.shape[0]
T1 = number_of_samples1 / sampFreq1
wav1s1 = wav1[:,0]

sampFreq2, wav2 = wavfile.read(fileW2, mmap=True)
wav2 = wav2 / (2.**15)
number_of_samples2 = wav2.shape[0]
T2 = number_of_samples2 / sampFreq2
wav2s1 = wav2[:,0]

timeArray1 = arange(0, number_of_samples1, 1)
timeArray1 = timeArray1 / T1
timeArray1 = timeArray1 * 1000 #milliseconds

plot(timeArray1, wav1s1, color='k')
ylabel('Amplitude')
xlabel('Time (ms)')
plot.show()

spf = wave.open('Mixdown 1.wav', 'r')

plt.figure(1)
plt.subplot(211)
plt.title('high pitch')
plt.plot(wav1, 'b')

plt.subplot(212)
plt.title('low pitch')
plt.plot(wav2, 'r')
plt.show()


