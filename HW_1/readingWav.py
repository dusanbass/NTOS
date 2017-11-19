import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
plt.ion()
rate, data = wavfile.read('./sounds/mix1.wav')

print ('rate =',rate)
print ('data =',data)

m1l = mix1_side_l = data[:,0]
m1r = mix1_side_r = data[:,1]

data_len = len(data)
t = np.arange(data_len)

print ('len =', data_len)
print ('t =',t)

plt.figure(1)
plt.plot(t, mix1_side_l)
plt.show()


M1l = np.fft.fft(m1l)
freq = np.fft.fftfreq(data_len)
plt.figure(2)
plt.plot(freq, M1l)
plt.show()

ind = np.arange(1, int(data_len/2) + 1)
psd = abs(M1l[ind])**2 * abs(M1l[-ind])**2
print (psd)
plt.figure(3)
plt.plot(freq[ind], psd)
plt.show()
