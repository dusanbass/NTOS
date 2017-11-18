Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import scipy.signal
>>> scipy.signal?
SyntaxError: invalid syntax
>>> 
>>> scipy.signal
<module 'scipy.signal' from 'C:\\Python36\\lib\\site-packages\\scipy\\signal\\__init__.py'>
>>> import scipy.fftpack
>>> scipy.fft
<function fft at 0x03478A98>
>>> scipy.fftpack?
SyntaxError: invalid syntax
>>> help(numpy.fft)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    help(numpy.fft)
NameError: name 'numpy' is not defined
>>> import numpy
>>> import numpy.*
SyntaxError: invalid syntax
>>> import numpy.ffty
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import numpy.ffty
ModuleNotFoundError: No module named 'numpy.ffty'
>>> import numpy.fft
>>> rand(3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    rand(3)
NameError: name 'rand' is not defined
>>> np.ranodm.rand(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    np.ranodm.rand(3)
NameError: name 'np' is not defined
>>> numpy.random.rand(3)
array([ 0.74651565,  0.90148154,  0.95494194])
>>> numpy.random.rand(3) * 1000
array([  59.75044806,  358.27119539,  645.33500924])
>>> h = zeros(3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    h = zeros(3)
NameError: name 'zeros' is not defined
>>> h = numpy.zeros(3)
>>> h
array([ 0.,  0.,  0.])
>>> import numpy as np
>>> N = 10001
>>> Nf = 3
>>> arrange(3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    arrange(3)
NameError: name 'arrange' is not defined
>>> np.arrange(3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    np.arrange(3)
AttributeError: module 'numpy' has no attribute 'arrange'
>>> np.arange(3)
array([0, 1, 2])
>>> np.arange(100)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
>>> t = np.arange(N)
>>> t
array([    0,     1,     2, ...,  9998,  9999, 10000])
>>> rand(Nf)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    rand(Nf)
NameError: name 'rand' is not defined
>>> np.rand(Nf)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    np.rand(Nf)
AttributeError: module 'numpy' has no attribute 'rand'
>>> import numpy.random.rand as rand
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    import numpy.random.rand as rand
ModuleNotFoundError: No module named 'numpy.random.rand'
>>> import numpy.random as r
>>> r.rand(3)
array([ 0.35374887,  0.07729147,  0.85184857])
>>> r.rand(Nf) * 100
array([ 60.43178792,  99.90095574,   0.55930252])
>>> Ts = r.rand(Nf) * 200 + 100
>>> Ts
array([ 286.14320862,  286.35103246,  153.18136126])
>>> fs = 1./Ts
>>> fs
array([ 0.00349475,  0.00349222,  0.00652821])
>>> Ts = r.rand(Nf) * 2000 + 10
>>> Ts
array([  307.32204693,  1557.38434284,  1754.90052303])
>>> fs
array([ 0.00349475,  0.00349222,  0.00652821])
>>> fs = 1./Ts
>>> fs
array([ 0.00325392,  0.0006421 ,  0.00056983])
>>> amp = r.rand(Nf) * 200 + 100
>>> amp
array([ 271.46926979,  126.13507632,  145.26655023])
>>> fs
array([ 0.00325392,  0.0006421 ,  0.00056983])
>>> phi = rand(Nf) * 2 * np.pi
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    phi = rand(Nf) * 2 * np.pi
NameError: name 'rand' is not defined
>>> pi
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> np.pi
3.141592653589793
>>> phi = r.rand(Nf) * 2 * np.pi
>>> phi
array([ 6.22964611,  3.77064623,  4.59530078])
>>> zeros(N)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    zeros(N)
NameError: name 'zeros' is not defined
>>> zeroes(N)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    zeroes(N)
NameError: name 'zeroes' is not defined
>>> np.zeroes(N)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    np.zeroes(N)
AttributeError: module 'numpy' has no attribute 'zeroes'
>>> zeros(N)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    zeros(N)
NameError: name 'zeros' is not defined
>>> np.zeros(N)
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> np.zeros(10)
array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
>>> np.zeros(5)
array([ 0.,  0.,  0.,  0.,  0.])
>>> h = np.zeros(N)
>>> h
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> for j in range(len(fs)):
	print j
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(j)?
>>> for j in range(len(fs)):
	print (j)
	return
SyntaxError: 'return' outside function
>>> for j in range(len(fs)):
	print (5)

	
5
5
5
>>> sin(5)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    sin(5)
NameError: name 'sin' is not defined
>>> np.sin(5)
-0.95892427466313845
>>> np.sin(np.pi / 2)
1.0
>>> for j in range(len(fs)):
	h += amp[j] * np.sin(2 * np.pi * fs[j] + phi[j])

	
>>> h
array([-227.94037219, -227.94037219, -227.94037219, ..., -227.94037219,
       -227.94037219, -227.94037219])
>>> randn(3)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    randn(3)
NameError: name 'randn' is not defined
>>> r.randon(3)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    r.randon(3)
AttributeError: module 'numpy.random' has no attribute 'randon'
>>> r.randn(3)
array([ 0.26626718, -0.87772671, -0.32891583])
>>> r.randn(1)
array([ 0.4750835])
>>> r.randn(11)
array([-1.46283562,  1.86032407, -0.45969512, -1.81730052, -0.56028605,
        0.44875625,  0.6064626 ,  1.62367217, -0.29804999,  0.7136571 ,
       -0.53292839])
>>> hn = h + r.randn(N) * 3 * h + r.randn(N) * 700
>>> hn
array([ 878.02534315,  -90.45252205, -830.10559693, ...,  146.3824435 ,
       -824.35625496, -942.58571243])
>>> plot(t, hn, 'k,', label='signal)
     
SyntaxError: EOL while scanning string literal
>>> plot(t, hn, 'k,', label='signal')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    plot(t, hn, 'k,', label='signal')
NameError: name 'plot' is not defined
>>> import np.plot as plot
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    import np.plot as plot
ModuleNotFoundError: No module named 'np'
>>> import matplotlib.pyplot as plt
>>> plt
<module 'matplotlib.pyplot' from 'C:\\Python36\\lib\\site-packages\\matplotlib\\pyplot.py'>
>>> plt.plot(t, hn, 'k,', label='Signal')
[<matplotlib.lines.Line2D object at 0x058CC2B0>]
>>> plt.show()
>>> Hn = fft.fft(hn)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    Hn = fft.fft(hn)
NameError: name 'fft' is not defined
>>> np.fft.fft(hn)
array([-2393630.59924267     +0.j        ,
          10529.73062681  -9826.92109039j,
          13423.77867902-100478.83145082j, ...,
         -22894.88327141 +16337.11537147j,
          13423.77867902+100478.83145082j,
          10529.73062681  +9826.92109039j])
>>> np.fft.fftfreq
<function fftfreq at 0x03478858>
>>> np.fft.fftgreq.help()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    np.fft.fftgreq.help()
AttributeError: module 'numpy.fft' has no attribute 'fftgreq'
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help(np.fft.fftfreq)
Help on function fftfreq in module numpy.fft.helper:

fftfreq(n, d=1.0)
    Return the Discrete Fourier Transform sample frequencies.
    
    The returned float array `f` contains the frequency bin centers in cycles
    per unit of the sample spacing (with zero at the start).  For instance, if
    the sample spacing is in seconds, then the frequency unit is cycles/second.
    
    Given a window length `n` and a sample spacing `d`::
    
      f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (d*n)   if n is even
      f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n)   if n is odd
    
    Parameters
    ----------
    n : int
        Window length.
    d : scalar, optional
        Sample spacing (inverse of the sampling rate). Defaults to 1.
    
    Returns
    -------
    f : ndarray
        Array of length `n` containing the sample frequencies.
    
    Examples
    --------
    >>> signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5], dtype=float)
    >>> fourier = np.fft.fft(signal)
    >>> n = signal.size
    >>> timestep = 0.1
    >>> freq = np.fft.fftfreq(n, d=timestep)
    >>> freq
    array([ 0.  ,  1.25,  2.5 ,  3.75, -5.  , -3.75, -2.5 , -1.25])

>>> Hn = np.fft.fft(hn)
>>> Hn
array([-2393630.59924267     +0.j        ,
          10529.73062681  -9826.92109039j,
          13423.77867902-100478.83145082j, ...,
         -22894.88327141 +16337.11537147j,
          13423.77867902+100478.83145082j,
          10529.73062681  +9826.92109039j])
>>> np.fft.fftfreq(N)
array([  0.00000000e+00,   9.99900010e-05,   1.99980002e-04, ...,
        -2.99970003e-04,  -1.99980002e-04,  -9.99900010e-05])
>>> freq = no.fft.fftfreq(N)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    freq = no.fft.fftfreq(N)
NameError: name 'no' is not defined
>>> freq = np.fft.fftfreq(N)
>>> freq
array([  0.00000000e+00,   9.99900010e-05,   1.99980002e-04, ...,
        -2.99970003e-04,  -1.99980002e-04,  -9.99900010e-05])
>>> np.arange(1, N/2 + 1)
array([  1.00000000e+00,   2.00000000e+00,   3.00000000e+00, ...,
         4.99900000e+03,   5.00000000e+03,   5.00100000e+03])
>>> ind = arange(1, N/2 + 1)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    ind = arange(1, N/2 + 1)
NameError: name 'arange' is not defined
>>> ind = np.arange(1, N/2 + 1)
>>> ind
array([  1.00000000e+00,   2.00000000e+00,   3.00000000e+00, ...,
         4.99900000e+03,   5.00000000e+03,   5.00100000e+03])
>>> freq[ind]
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    freq[ind]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> np.arange(1, N/2 + 1)
array([  1.00000000e+00,   2.00000000e+00,   3.00000000e+00, ...,
         4.99900000e+03,   5.00000000e+03,   5.00100000e+03])
>>> int(np.arange(1, N/2 + 1))
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    int(np.arange(1, N/2 + 1))
TypeError: only length-1 arrays can be converted to Python scalars
>>> N/2
5000.5
>>> int(N/2)
5000
>>> np.arange(1, int(N/2) + 1)
array([   1,    2,    3, ..., 4998, 4999, 5000])
>>> ind = np.arange(1, int(N/2) + 1)
>>> freq[ind]
array([  9.99900010e-05,   1.99980002e-04,   2.99970003e-04, ...,
         4.99750025e-01,   4.99850015e-01,   4.99950005e-01])
>>> freq[-ind]
array([ -9.99900010e-05,  -1.99980002e-04,  -2.99970003e-04, ...,
        -4.99750025e-01,  -4.99850015e-01,  -4.99950005e-01])
>>> np.abs(-1)
1
>>> psd = np.abs(Hn[ind]) ** 2
>>> psd
array([  2.07443605e+08,   1.02761934e+10,   7.91077019e+08, ...,
         8.82449918e+09,   5.44412116e+08,   2.73676786e+10])
>>> psd = np.abs(Hn[ind])**2 + np.abs(Hn[-ind])**2
>>> figure(2)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    figure(2)
NameError: name 'figure' is not defined
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x05743390>
>>> plt.show()
>>> ion()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    ion()
NameError: name 'ion' is not defined
>>> plt.ion()
>>> plt.show()
>>> plt.figure(2).show()
>>> plt.plot(freq[ind], psd, 'k-')
[<matplotlib.lines.Line2D object at 0x05AB1090>]
>>> amp = r.rand(Nf) * 200 + 100
>>> amp
array([ 167.76728729,  271.0491547 ,  184.79012423])
>>> amp = r.rand(Nf) * 2000 + 100
>>> for j in range(len(fs)):
	h += amp[j] * np.sin(2 * np.pi * fs[j] + phi[j])

>>> h
array([-1658.27310948, -1658.27310948, -1658.27310948, ..., -1658.27310948,
       -1658.27310948, -1658.27310948])
>>> where(psd>1.35e11)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    where(psd>1.35e11)
NameError: name 'where' is not defined
>>> np.where(psd>1.35e11)
(array([ 453, 1741, 2380, 4030, 4777], dtype=int32),)
>>> np.where(psd>1.36e11)
(array([ 453, 1741, 2380, 4777], dtype=int32),)
>>> ind ,= where(psd>1.36e11)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    ind ,= where(psd>1.36e11)
NameError: name 'where' is not defined
>>> ind, = np.where(psd>1.36e11)
>>> ind
array([ 453, 1741, 2380, 4777], dtype=int32)
>>> freq[ind]
array([ 0.04529547,  0.17408259,  0.2379762 ,  0.47765223])
>>> axvline(0.04529547)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    axvline(0.04529547)
NameError: name 'axvline' is not defined
>>> plt.axvline(0.04529547)
<matplotlib.lines.Line2D object at 0x05985170>
>>> inf_freq = np.arange(1, N/2 + 1)
>>> inf_freq
array([  1.00000000e+00,   2.00000000e+00,   3.00000000e+00, ...,
         4.99900000e+03,   5.00000000e+03,   5.00100000e+03])
>>> ind_freq[ind]
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    ind_freq[ind]
NameError: name 'ind_freq' is not defined
>>> freq[ind_freq[ind]]
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    freq[ind_freq[ind]]
NameError: name 'ind_freq' is not defined
>>> ind_freq = inf_freq
>>> freq[ind_freq[ind]]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    freq[ind_freq[ind]]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> ind_freq = np.arange(1, int(N/2) + 1)
>>> ind_freq
array([   1,    2,    3, ..., 4998, 4999, 5000])
>>> freq[ind_freq[ind]]
array([ 0.04539546,  0.17418258,  0.23807619,  0.47775222])
>>> Hn_cut = np.zeros_like(Hn)
>>> Hn_cut
array([ 0.+0.j,  0.+0.j,  0.+0.j, ...,  0.+0.j,  0.+0.j,  0.+0.j])
>>> Hn_cut[ind_freq[ind]] = Hn[ind_freq[ind]]
>>> Hn_cut
array([ 0.+0.j,  0.+0.j,  0.+0.j, ...,  0.+0.j,  0.+0.j,  0.+0.j])
>>> Hn_cut[-ind_freq[ind]] = Hn[-ind_freq[ind]]
>>> hn_cut = fft.ifft(Hn_cut)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    hn_cut = fft.ifft(Hn_cut)
NameError: name 'fft' is not defined
>>> hn_cut = np.fft.ifft(Hn_cut)
>>> hn_cut
array([  42.51297368 +2.76458743e-14j,  -49.16346306 +4.11050500e-14j,
         -2.51526524 +2.91009204e-15j, ..., -143.40577291 -1.01009158e-13j,
        -78.39661095 -8.98884674e-14j,   30.18392501 +7.17132371e-14j])
>>> clf()
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    clf()
NameError: name 'clf' is not defined
>>> plt.clf()
>>> plt.plot(t, hn, 'k,', label='Signal')
[<matplotlib.lines.Line2D object at 0x016A7390>]
>>> plt.plot(t, np.fft.ifft(Hn), 'r', label='Signal')

Warning (from warnings module):
  File "C:\Python36\lib\site-packages\numpy\core\numeric.py", line 531
    return array(a, dtype, copy=False, order=order)
ComplexWarning: Casting complex values to real discards the imaginary part
[<matplotlib.lines.Line2D object at 0x05726E30>]
>>> figure(1)
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    figure(1)
NameError: name 'figure' is not defined
>>> plt.figure(1)
<matplotlib.figure.Figure object at 0x0167B350>
>>> plt.plot(t, hn_cut, 'r--', lw=2, label='Freq. cut')
[<matplotlib.lines.Line2D object at 0x04BCDC10>]
>>> plt.plot(t, h, 'k-', lw=2, label='true signal')
[<matplotlib.lines.Line2D object at 0x01691510>]
>>> legend(loc = 'best')
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    legend(loc = 'best')
NameError: name 'legend' is not defined
>>> plt.legend(loc = 'best')
<matplotlib.legend.Legend object at 0x04BC3ED0>
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x058CCAB0>
>>> N
10001
>>> Nf
3
>>> t
array([    0,     1,     2, ...,  9998,  9999, 10000])
>>> Ts
array([  307.32204693,  1557.38434284,  1754.90052303])
>>> Ts = r.rand(Nf) * 2000 + 10
>>> Ts
array([ 1153.64284541,  1623.3517949 ,  1281.30160735])
>>> fs = 1./Ts
>>> fs
array([ 0.00086682,  0.00061601,  0.00078046])
>>> amp = r.rand(Nf) * 200 + 100
>>> amp
array([ 121.65743294,  247.04072945,  139.19353843])
>>> phi = r.rand(Nf) * 2 * pi
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    phi = r.rand(Nf) * 2 * pi
NameError: name 'pi' is not defined
>>> prhi = r.rand(Nf) * 2 * np.pi
>>> phi
array([ 6.22964611,  3.77064623,  4.59530078])
>>> h = zeros(N)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    h = zeros(N)
NameError: name 'zeros' is not defined
>>> h = np.zeros(N)
>>> h
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> for j in range(len(fs)):
	h += amp[j] * np.sin(2 * pi * t * fs[j] + phi[j])

	
Traceback (most recent call last):
  File "<pyshell#190>", line 2, in <module>
    h += amp[j] * np.sin(2 * pi * t * fs[j] + phi[j])
NameError: name 'pi' is not defined
>>> for j in range(len(fs)):
	h += amp[j] * np.sin(2 * np.pi * t * fs[j] + phi[j])

	
>>> h
array([-290.104575  , -290.29296868, -290.4756737 , ..., -378.33797755,
       -379.30930703, -380.27317682])
>>> r.randn(N)*3*h
array([  999.20431433,   930.44251637,  1619.27248804, ...,   -97.92247803,
       -1182.80006305,  1845.12267139])
>>> r.randn(N)*700
array([ 1290.22659614,   239.51818465,     2.01749958, ...,  -180.15479676,
        1046.35813403,  -647.90285129])
>>> r.randn(N)*3
array([-0.5569537 , -1.15025689,  0.32992447, ..., -1.16895648,
       -0.48519614,  1.54876572])
>>> r.randn(N) * 700
array([ -604.07583809,   608.28564363,   602.60755019, ..., -1110.78958248,
        -191.82300667,  -400.8554921 ])
>>> h + r.randn(N)*3*h
array([-1897.63986836,   696.92458436,  -719.25385643, ...,  -952.39498377,
        1983.16682324,  -555.03725326])
>>> h + r.randn(N)*3*h + r.randn(N)*700
array([   55.25053409,   611.29514264,    31.55782181, ..., -1264.18308966,
         671.44022274,   610.30000036])
>>> hn = h + r.randn(N)*3*h + r.randn(N)*700
>>> hn
array([  713.09401737,   634.42035457,  -568.32840082, ...,  1469.46074147,
       -1106.76224904,  -204.48625609])
>>> np.fft.fft(hn)
array([-74515.08375365    +0.j        ,  34289.68327864+47556.06277052j,
       -24415.02674188 -8517.24801088j, ...,
       -37209.21947129-72145.72852692j, -24415.02674188 +8517.24801088j,
        34289.68327864-47556.06277052j])
>>> plt.plot(t, hn, 'k,', lw=1, legend='noise signal')
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    plt.plot(t, hn, 'k,', lw=1, legend='noise signal')
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3240, in plot
    ret = ax.plot(*args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1710, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1437, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 394, in _plot_args
    seg = func(x[:, j % ncx], y[:, j % ncy], kw, kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 301, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Python36\lib\site-packages\matplotlib\lines.py", line 426, in __init__
    self.update(kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 847, in update
    for k, v in props.items()]
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 847, in <listcomp>
    for k, v in props.items()]
  File "C:\Python36\lib\site-packages\matplotlib\artist.py", line 840, in _update_property
    raise AttributeError('Unknown property %s' % k)
AttributeError: Unknown property legend
>>> plt.plot(t, hn, 'k,')
[<matplotlib.lines.Line2D object at 0x05AB95D0>]
>>> plt.plot(t, h, 'b-')
[<matplotlib.lines.Line2D object at 0x016E1A50>]
>>> plt.figure(3)
<matplotlib.figure.Figure object at 0x016CC5D0>
>>> Hn = np.fft.fft(hn)
>>> Hn
array([-74515.08375365    +0.j        ,  34289.68327864+47556.06277052j,
       -24415.02674188 -8517.24801088j, ...,
       -37209.21947129-72145.72852692j, -24415.02674188 +8517.24801088j,
        34289.68327864-47556.06277052j])
>>> np.fft.fftfreq(N)
array([  0.00000000e+00,   9.99900010e-05,   1.99980002e-04, ...,
        -2.99970003e-04,  -1.99980002e-04,  -9.99900010e-05])
>>> freq = np.fft.fftfreq(N)
>>> freq
array([  0.00000000e+00,   9.99900010e-05,   1.99980002e-04, ...,
        -2.99970003e-04,  -1.99980002e-04,  -9.99900010e-05])
>>> ind = np.arange(1, int(N/2) + 1)
>>> ind
array([   1,    2,    3, ..., 4998, 4999, 5000])
>>> freq[ind]
array([  9.99900010e-05,   1.99980002e-04,   2.99970003e-04, ...,
         4.99750025e-01,   4.99850015e-01,   4.99950005e-01])
>>> freq[-ind]
array([ -9.99900010e-05,  -1.99980002e-04,  -2.99970003e-04, ...,
        -4.99750025e-01,  -4.99850015e-01,  -4.99950005e-01])
>>> abs(-1)
1
>>> psd = abs(Hn[ind])**2 + abs(Hn[-ind])**2
>>> psd
array([  6.87472297e+09,   1.33727409e+09,   1.31790643e+10, ...,
         1.48738196e+10,   1.98762544e+09,   1.75945618e+10])
>>> plt.figure(1)
<matplotlib.figure.Figure object at 0x016A74B0>
>>> plt.plot(freq[ind], psd, 'k-')
[<matplotlib.lines.Line2D object at 0x058CC230>]
>>> np.where(psd > 0.25e12)
(array([5, 6, 7, 8], dtype=int32),)
>>> ind, = where(psd > 0.25e12)
Traceback (most recent call last):
  File "<pyshell#223>", line 1, in <module>
    ind, = where(psd > 0.25e12)
NameError: name 'where' is not defined
>>> ind ,= np.where(psd > 0.25e12)
>>> ind
array([5, 6, 7, 8], dtype=int32)
>>> freq[ind]
array([ 0.00049995,  0.00059994,  0.00069993,  0.00079992])
>>> avxline(0.00049995)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    avxline(0.00049995)
NameError: name 'avxline' is not defined
>>> plt.axvline(0.00049995)
<matplotlib.lines.Line2D object at 0x016A7AB0>
>>> ind_freq = np.arange(1, int(N/2) +1)
>>> ind_freq
array([   1,    2,    3, ..., 4998, 4999, 5000])
>>> freq[ind_freq[ind]]
array([ 0.00059994,  0.00069993,  0.00079992,  0.00089991])
>>> ind_freq[ind]
array([6, 7, 8, 9])
>>> freq[ind_freq[ind]]
array([ 0.00059994,  0.00069993,  0.00079992,  0.00089991])
>>> plt.axvline(0.00059994)
<matplotlib.lines.Line2D object at 0x016737F0>
>>> Hn_cut = np.zeroes_like(Hn)
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    Hn_cut = np.zeroes_like(Hn)
AttributeError: module 'numpy' has no attribute 'zeroes_like'
>>> Hn_cut = np.zeros_like(Hn)
>>> Hn_cut
array([ 0.+0.j,  0.+0.j,  0.+0.j, ...,  0.+0.j,  0.+0.j,  0.+0.j])
>>> Hn_cut[ind_freq[ind]] = Hn[ind_freq[ind]]
>>> Hn_cut[-ind_freq[ind]] = Hn[-ind_freq[ind]]
>>> Hn_cut
array([ 0.+0.j,  0.+0.j,  0.+0.j, ...,  0.+0.j,  0.+0.j,  0.+0.j])
>>> np.fft.ifft(Hn_cut)
array([-269.15419596 +2.18256903e-13j, -269.65623256 +2.18256903e-13j,
       -270.15233727 +2.26987179e-13j, ..., -267.61258228 -1.25046276e-13j,
       -268.13236192 -2.50309963e-13j, -268.64623614 -2.37191237e-13j])
>>> hn_cut = np.fft.ifft(Hn_cut)
>>> hn_cut
array([-269.15419596 +2.18256903e-13j, -269.65623256 +2.18256903e-13j,
       -270.15233727 +2.26987179e-13j, ..., -267.61258228 -1.25046276e-13j,
       -268.13236192 -2.50309963e-13j, -268.64623614 -2.37191237e-13j])
>>> clf()
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    clf()
NameError: name 'clf' is not defined
>>> plt.clf()
>>> plt.figure(1)
<matplotlib.figure.Figure object at 0x016A74B0>
>>> plt.plot(t, hn, 'k, ', label='Signal')
[<matplotlib.lines.Line2D object at 0x0669E750>]
>>> plt.plot(t, np.fft.ifft(Hn), 'r,' label='inverse')
SyntaxError: invalid syntax
>>> plt.plot(t, np.fft.ifft(Hn), 'r,', label='inverse Hn')
[<matplotlib.lines.Line2D object at 0x0595EE90>]
>>> plt.clf
<function clf at 0x05731108>
>>> plt.clf()
>>> plt.plot(t, hn, 'k,', label='Signal')
[<matplotlib.lines.Line2D object at 0x04DCC130>]
>>> plot(t, hn_cut, 'r--', lw=1, label='Freq cut')
Traceback (most recent call last):
  File "<pyshell#253>", line 1, in <module>
    plot(t, hn_cut, 'r--', lw=1, label='Freq cut')
NameError: name 'plot' is not defined
>>> plt.plot(t, hn_cut, 'r--', lw=1, label='Freq. cut')
[<matplotlib.lines.Line2D object at 0x04DE0D90>]
>>> plt.plot(t, hn, 'k-', lw=1, label='True signal')
[<matplotlib.lines.Line2D object at 0x04DCC230>]
>>> plt.pop()
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    plt.pop()
AttributeError: module 'matplotlib.pyplot' has no attribute 'pop'
>>> plt.plot.pop()
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    plt.plot.pop()
AttributeError: 'function' object has no attribute 'pop'
>>> plt.cla()
>>> pla.clf()
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    pla.clf()
NameError: name 'pla' is not defined
>>> plt.clf()
>>> plt.plot(t, hn, 'k,', label='Noise signal')
[<matplotlib.lines.Line2D object at 0x04B38D70>]
>>> hn_cut
array([-269.15419596 +2.18256903e-13j, -269.65623256 +2.18256903e-13j,
       -270.15233727 +2.26987179e-13j, ..., -267.61258228 -1.25046276e-13j,
       -268.13236192 -2.50309963e-13j, -268.64623614 -2.37191237e-13j])
>>> plt.plot(t, hn_cut, 'r--', lw=2, label='Freq. cut')
[<matplotlib.lines.Line2D object at 0x06673ED0>]
>>> plt.plot(t, h, 'b-', lw=1, label='True signal')
[<matplotlib.lines.Line2D object at 0x04B28EF0>]
>>> freq[ind_freq[ind]]
array([ 0.00059994,  0.00069993,  0.00079992,  0.00089991])
>>> fs
array([ 0.00086682,  0.00061601,  0.00078046])
>>> plt.figure(1)
<matplotlib.figure.Figure object at 0x04BE8C70>
>>> plt.plot(t, hn, 'k,', label='Noise signal')
[<matplotlib.lines.Line2D object at 0x04B1C290>]
>>> plt.plot(t, hn_cut, 'r--', lw=2, label='Freq. cut')
[<matplotlib.lines.Line2D object at 0x04B4B3D0>]
>>> plt.plot(t, h, 'b-', lw=1, label='True signal')
[<matplotlib.lines.Line2D object at 0x04B1CF30>]
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x04B38CF0>
>>> sigma
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    sigma
NameError: name 'sigma' is not defined
>>> np.sigma
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    np.sigma
AttributeError: module 'numpy' has no attribute 'sigma'
>>> np.sigma()
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    np.sigma()
AttributeError: module 'numpy' has no attribute 'sigma'
>>> sigma = 100
>>> sigma
100
>>> sigma = 100.
>>> sigma
100.0
>>> tt = np.arange(-int(N/2), int(N/2))
>>> tt
array([-5000, -4999, -4998, ...,  4997,  4998,  4999])
>>> g = exp(-tt**2/2/sigma**2)/sqrt(np.pi)/sigma
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    g = exp(-tt**2/2/sigma**2)/sqrt(np.pi)/sigma
NameError: name 'exp' is not defined
>>> g = np.exp(2)
>>> g
7.3890560989306504
>>> g = np.exp(-tt**2/2/sigma**2)/np.sqrt(np.pi)/sigma
>>> g
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> plt.plot(tt, g)
[<matplotlib.lines.Line2D object at 0x04E1D490>]
>>> plt.figure(1).legend
<bound method Figure.legend of <matplotlib.figure.Figure object at 0x04BE8C70>>
>>> plt.ax.legend(loc='best')
Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    plt.ax.legend(loc='best')
AttributeError: module 'matplotlib.pyplot' has no attribute 'ax'
>>> plt.plot.legend(loc='best')
Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    plt.plot.legend(loc='best')
AttributeError: 'function' object has no attribute 'legend'
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x04B30310>
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x04B38CF0>
>>> G = np.fft.fft(g)
>>> G
array([ 1.41421356 +0.00000000e+00j, -1.41142477 +5.19081695e-16j,
        1.40309135 -1.03230616e-15j, ..., -1.38931150 +6.78802494e-15j,
        1.40309135 -7.46102690e-15j, -1.41142477 +8.13042397e-15j])
>>> HG = Hn * G
Traceback (most recent call last):
  File "<pyshell#294>", line 1, in <module>
    HG = Hn * G
ValueError: operands could not be broadcast together with shapes (10001,) (10000,) 
>>> tt = np.arange(-int(N/2), int(N/2) + 1)
>>> tt
array([-5000, -4999, -4998, ...,  4998,  4999,  5000])
>>> g = exp(-tt**2/2/sigma**2)/sqrt(np.pi)/sigma
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    g = exp(-tt**2/2/sigma**2)/sqrt(np.pi)/sigma
NameError: name 'exp' is not defined
>>> g = np.exp(-tt**2/2/sigma**2)/sqrt(np.pi)/sigma
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    g = np.exp(-tt**2/2/sigma**2)/sqrt(np.pi)/sigma
NameError: name 'sqrt' is not defined
>>> g = np.exp(-tt**2/2/sigma**2)/np.sqrt(np.pi)/sigma
>>> g
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> G = np.fft.fft(g)
>>> HG = G * Hn
>>> Hg
Traceback (most recent call last):
  File "<pyshell#303>", line 1, in <module>
    Hg
NameError: name 'Hg' is not defined
>>> HG
array([-105380.24204578     +0.j        ,
        -48376.24021521 -67137.03109053j,
        -34249.05209872 -11972.01536967j, ...,
         51789.81544713+100184.48518909j,
        -34249.05209872 +11972.01536967j,  -48376.24021521 +67137.03109053j])
>>> smooting with gaussina
SyntaxError: invalid syntax
>>> 'smoothing with gaussian'
'smoothing with gaussian'
>>> 'this is fourier space, so transform back'
'this is fourier space, so transform back'
>>> hn_smooth1 = np.fft.ifft(HG)
>>> clf()
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    clf()
NameError: name 'clf' is not defined
>>> plt.clf()
>>> plt.plot(t, h, 'k-', label='True signal')
[<matplotlib.lines.Line2D object at 0x04DE0E90>]
>>> plot.plot(t, hn_smooth1, 'r--', label='Smooth one')
Traceback (most recent call last):
  File "<pyshell#312>", line 1, in <module>
    plot.plot(t, hn_smooth1, 'r--', label='Smooth one')
NameError: name 'plot' is not defined
>>> plt.plot(t, hn_smooth1, 'r--', label='Smooth one')
[<matplotlib.lines.Line2D object at 0x04DE0110>]
>>> 'not much agreeing'
'not much agreeing'
>>> 'we dont need to do this by hand...'
'we dont need to do this by hand...'
>>> 'we have convolve in numpy'
'we have convolve in numpy'
>>> convolve(hn, g)
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    convolve(hn, g)
NameError: name 'convolve' is not defined
>>> np.convolve(hn, g)
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> hn_smooth2 = np.convolve(hn, g)
>>> plt.figure(3)
<matplotlib.figure.Figure object at 0x04E3B0B0>
>>> plt.plot(t, hn_smooth2, 'b-', label='np Convolve')
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    plt.plot(t, hn_smooth2, 'b-', label='np Convolve')
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3240, in plot
    ret = ax.plot(*args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1710, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1437, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 384, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 243, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (10001,) and (20001,)
>>> hn_smooth2
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> plt.plot(t, hn_smooth2, 'b', label='np convolve')
Traceback (most recent call last):
  File "<pyshell#323>", line 1, in <module>
    plt.plot(t, hn_smooth2, 'b', label='np convolve')
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3240, in plot
    ret = ax.plot(*args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1710, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1437, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 384, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 243, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (10001,) and (20001,)
>>> plt.plot(hn_smooth2)
[<matplotlib.lines.Line2D object at 0x058CC270>]
>>> 'zero padding happened'
'zero padding happened'
>>> hn_smooth2[N/2:3*N/2]
Traceback (most recent call last):
  File "<pyshell#326>", line 1, in <module>
    hn_smooth2[N/2:3*N/2]
TypeError: slice indices must be integers or None or have an __index__ method
>>> hn_smooth[int(N/2):int(3*N/2)]
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    hn_smooth[int(N/2):int(3*N/2)]
NameError: name 'hn_smooth' is not defined
>>> hn_smooth2[int(N/2):int(3*N/2)]
array([-240.81535592, -242.92950883, -245.04396614, ..., -217.29219646,
       -215.88405024, -214.46717597])
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x04B38CF0>
>>> plot(t, hn_smooth2, 'g-.', label='Smooth 2')
Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    plot(t, hn_smooth2, 'g-.', label='Smooth 2')
NameError: name 'plot' is not defined
>>> plt.plot(t, hn_smooth2, 'g-.', label='Smooth 2')
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    plt.plot(t, hn_smooth2, 'g-.', label='Smooth 2')
  File "C:\Python36\lib\site-packages\matplotlib\pyplot.py", line 3240, in plot
    ret = ax.plot(*args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\__init__.py", line 1710, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_axes.py", line 1437, in plot
    for line in self._get_lines(*args, **kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 404, in _grab_next_args
    for seg in self._plot_args(this, kwargs):
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 384, in _plot_args
    x, y = self._xy_from_xy(x, y)
  File "C:\Python36\lib\site-packages\matplotlib\axes\_base.py", line 243, in _xy_from_xy
    "have shapes {} and {}".format(x.shape, y.shape))
ValueError: x and y must have same first dimension, but have shapes (10001,) and (20001,)
>>> plot(t, hn_smooth2[int(N/2):int(3*N/2)], 'g-.', label='Smooth 2')
Traceback (most recent call last):
  File "<pyshell#332>", line 1, in <module>
    plot(t, hn_smooth2[int(N/2):int(3*N/2)], 'g-.', label='Smooth 2')
NameError: name 'plot' is not defined
>>> plt.plot(t, hn_smooth2[int(N/2):int(3*N/2)], 'g-.', label='Smooth 2')
[<matplotlib.lines.Line2D object at 0x04B387F0>]
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x0667FE90>
>>> hz = np.zeros(2*N)
>>> hz
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> 'adding padding by hand'
'adding padding by hand'
>>> hz[N:] = hn
>>> plt.figure(3)
<matplotlib.figure.Figure object at 0x04E3B0B0>
>>> plt.plot(hz)
[<matplotlib.lines.Line2D object at 0x017231F0>]
>>> Hz =  np.fft.fft(hz)
>>> tt = np.arange(-N, N)
>>> g = np.exp(-tt**2/2/sigma**2)/np.sqrt(2*pi)/sigma
Traceback (most recent call last):
  File "<pyshell#343>", line 1, in <module>
    g = np.exp(-tt**2/2/sigma**2)/np.sqrt(2*pi)/sigma
NameError: name 'pi' is not defined
>>> g = np.exp(-tt**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma
>>> g
array([ 0.,  0.,  0., ...,  0.,  0.,  0.])
>>> G = np.fft.fft(g)
>>> HzG = Hz*G
>>> hz_new = np.fft.ifft(HzG)
>>> plt.figure(3)
<matplotlib.figure.Figure object at 0x04E3B0B0>
>>> plt.clf()
>>> plt.plot(hz_new)
[<matplotlib.lines.Line2D object at 0x05AA7EB0>]
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x04B38CF0>
>>> plt.plot(t, hz_new[:N], 'b:', label='Zero padded')
[<matplotlib.lines.Line2D object at 0x059658F0>]
>>> plt.legend(loc='best')
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x04E092F0>
>>> plt.figure(1)
<matplotlib.figure.Figure object at 0x04BE8C70>
>>> plt.figure(2)
<matplotlib.figure.Figure object at 0x04B38CF0>
>>> Hn_filter = Hn.copy()
>>> fs
array([ 0.00086682,  0.00061601,  0.00078046])
>>> np.where(freq>0.0009)
(array([  10,   11,   12, ..., 4998, 4999, 5000], dtype=int32),)
>>> 'but this wont cut the negative freqs'
'but this wont cut the negative freqs'
>>> 'we need also, and the negative values, so use abs'
'we need also, and the negative values, so use abs'
>>> Hn_filter[abs(freq)>0.002]
array([ 90125.94618615+33333.49394618j, -98695.74221735-61737.61132604j,
        -8633.61084667-85200.51009797j, ...,
        -8633.61084667+85200.51009797j, -98695.74221735+61737.61132604j,
        90125.94618615-33333.49394618j])
>>> Hn_filter[abs(freq)>0.002] = 0
>>> hn_filter = np.fft.ifft(Hn_filter)
>>> figure(1)
Traceback (most recent call last):
  File "<pyshell#366>", line 1, in <module>
    figure(1)
NameError: name 'figure' is not defined
>>> plt.figure(1)
<matplotlib.figure.Figure object at 0x04BE8C70>
>>> plot(t, hn_filter, 'g-.', lw=2, label='High filter')
Traceback (most recent call last):
  File "<pyshell#368>", line 1, in <module>
    plot(t, hn_filter, 'g-.', lw=2, label='High filter')
NameError: name 'plot' is not defined
>>> plt.plot(t, hn_filter, 'g-.', lw=2, label='High filter')
[<matplotlib.lines.Line2D object at 0x016CC610>]
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x06660450>
>>> plt.gca().lines[0].set_visible(false)
Traceback (most recent call last):
  File "<pyshell#371>", line 1, in <module>
    plt.gca().lines[0].set_visible(false)
NameError: name 'false' is not defined
>>> plt.gca().lines[0].set_visible(False)
>>> plt.ylim(-700, 700)
(-700, 700)
>>> 
