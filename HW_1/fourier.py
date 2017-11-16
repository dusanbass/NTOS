import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math
N = 5
Nf = 3
t = np.arange(N, dtype=float)
Ts = sci.rand(Nf) * 2000 + 10
fs = 1. / Ts
amp = sci.rand(Nf) * 200 + 100
phi = sci.rand(Nf) * 2 * math.pi
h = sci.rand(N)
print('t =', t, '\nTs =', Ts, '\namp =', amp, '\nphi =', phi, '\nh=', h)

