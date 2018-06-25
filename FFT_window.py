# -*- coding: utf-8 -*-
from scipy import arange, hamming, sin, pi
from scipy.fftpack import fft, ifft
from matplotlib import pylab as pl

fs = 8000 # Sampling rate
L = 1024 # Signal length

# 440[Hz]のサイン波を作る。
sine_440 = sin(2. * pi * arange(L) * 440. / fs)
# 600[Hz]のサイン波を作る。
sine_600 = 2 * sin(2. * pi * arange(L) * 600. / fs)
# 800[Hz]のサイン波を作る。
sine_800 = 3 * sin(2. * pi * arange(L) * 800. / fs)

# 全部足す
sig = sine_440 + sine_600 + sine_800

# 窓関数
win = hamming(L)

# フーリエ変換
spectrum_nw = fft(sig) # 窓関数なし
spectrum = fft(sig * win) # 窓関数あり
half_spectrum_nw = abs(spectrum_nw[: L / 2 + 1])
half_spectrum = abs(spectrum[: L / 2 + 1])

# フーリエ逆変換
resyn_sig = ifft(spectrum)
resyn_sig /= win

# 図を表示
fig = pl.figure()
fig.add_subplot(411)
pl.plot(sig)
pl.xlim([0, L])
pl.title("1. Input signal", fontsize = 20)
fig.add_subplot(412)
pl.plot(half_spectrum_nw)
pl.xlim([0, len(half_spectrum_nw)])
pl.title("2. Spectrum (no window)", fontsize = 20)
fig.add_subplot(413)
pl.plot(half_spectrum)
pl.xlim([0, len(half_spectrum)])
pl.title("3. Spectrum (with window)", fontsize = 20)
fig.add_subplot(414)
pl.plot(resyn_sig)
pl.xlim([0, L])
pl.title("4. Resynthesized signal", fontsize = 20)

pl.show()