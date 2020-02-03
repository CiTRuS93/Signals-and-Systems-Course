import numpy as np
import matplotlib.pyplot as plt
from Util import v_to_db


def nice_wave(N: int, Desired) -> np.array:
    # create the signal in time and dft domains
    sig_rnd = np.random.uniform(-1, 1, N)
    Sig_rnd = np.fft.fft(sig_rnd)

    # build the desired shape in the dft domain

    # build a "filter" - a vector that will make the random signal in the
    # desired shape
    Desired = 10 ** (Desired / 20)
    Filt = abs(Desired) / abs(Sig_rnd)
    Sig = Sig_rnd * Filt
    sig = np.fft.ifft(Sig)
    sig_r_var = np.var(np.real(sig))
    sig_i_var = np.var(np.imag(sig))
    sig = np.real(sig)
    Sig = np.fft.fft(sig)
    return sig


def square(omega, a, b, k=2 * np.pi):
    sqr = np.array([1 if a < k_repeat(x, k) < b else 0 for x in omega])
    return (sqr)


def triangle(omega, center, r, k=2 * np.pi):
    tri = np.array([max(0, (1 - (abs(k_repeat(x, k) - center) / r))) for x in omega])
    return tri


def circle(omega, o, r, k=2 * np.pi):
    cir = np.array([np.sqrt(max(r ** 2 - abs(k_repeat(x, k) - o) ** 2, 0)) for x in omega])
    return cir
def dirac(omega, start, eps=0, k=2 * np.pi):
    dirc = np.array([1 if start<=k_repeat(x,k)<start+eps else 0 for x in omega]) 
    return dirc


waves_dict = {
    'square': square,

    'triangle': triangle,

    'circle': circle,

}


def get_keys():
    """returns all the available name for the waves"""
    return waves_dict.keys()


def two_pi_repeat(x) -> float:
    """

    Args:
        x: frequency

    Returns:
        recenter @x around 2*pi
    """
    return abs(x) - 2 * np.pi * np.round(abs(x) / (2 * np.pi))


def k_repeat(x, k):
    return abs(x) - k * np.round(abs(x) / k)


def get_wave_with_omega(name: str) -> [np.array, np.array]:
    """

    Args:
        name: The wave's name. for example:"square_HP".
                you can get all the names using get_keys() function

    Returns:
        the frequencies for the wave and the actual wave

    """
    omega = np.linspace(-np.pi, np.pi, 1000)
    wave = waves_dict.get(name)
    return omega, np.array([wave(two_pi_repeat(x)) for x in omega])


def get_wave(name: str, omega: np.array, a=np.pi / 2, b=np.pi / 2, k=2 * np.pi) -> np.array:
    """

   Parameters
   ----------
   name : str
       The wave's name. for example:"square_HP".
       you can get all the names using get_keys() function
   omega :  np.array
       the frequencies for the wave
   k: repeat freq
   a: start
   b: end

   Returns
   -------
   np.array
       the actual wave


   """

    wave = waves_dict.get(name)
    Y = wave(omega, a, b, k)
    Y = nice_wave(len(Y), Y * 60)

    return Y


import matplotlib.pyplot as plt

t = square(np.linspace(-np.pi, np.pi, 1000), np.pi / 2, 3 * np.pi / 4)
# plt.plot(np.linspace(-np.pi, np.pi, 1000)/np.pi, t)
# plt.show()
