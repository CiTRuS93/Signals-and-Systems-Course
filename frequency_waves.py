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
    Desired = 10**(Desired/20)
    Filt = abs(Desired) / abs(Sig_rnd)
    Sig = Sig_rnd * Filt
    sig = np.fft.ifft(Sig)
    sig_r_var = np.var(np.real(sig))
    sig_i_var = np.var(np.imag(sig))
    sig = np.real(sig)
    Sig = np.fft.fft(sig)
    return sig


# dictionary of different wave function, with their name as key.
waves_dict = {
    'square_HP': lambda x: max(0, np.sign(np.sin(x - np.pi / 2))),
    'square_LP': lambda x: max(0, np.sign(np.sin(x + np.pi / 2))),
    'triangle_LP': lambda x: max(0, (1 - (2 * abs(x) / np.pi))),
    'triangle_HP': lambda x: max(0, (2 * abs(x) / np.pi) - 1),
    'circle_LP': lambda x: np.sqrt(max((np.pi / 2) ** 2 - abs(x) ** 2, 0)),
    'circle_HP': lambda x: np.sqrt(
        max([(np.pi / 2) ** 2 - abs(x + np.pi) ** 2, (np.pi / 2) ** 2 - abs(x - np.pi) ** 2, 0]))
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


def square(omega, a, b, k=2 * np.pi):
    sqr = np.array([1 if a < k_repeat(x, k) < b else 0 for x in omega])
    return (sqr)


def reverse_square(omega, a, b, k=2 * np.pi):
    sqr = np.array([0 if a < k_repeat(x, k) < b else 1 for x in omega])
    return sqr


def triangle(omega, center, r):
    tri = np.array([max(0, (1 - (abs(two_pi_repeat(x) - center) / r))) for x in omega])
    return tri


def reverse_triangle(omega, r):
    tri = np.array([max(0, (1 - (abs(x - min(omega)) / r)), 1 - (abs(x + min(omega)) / r)) for x in omega])
    return tri


def circle(omega, o, r):
    cir = np.array([np.sqrt(max((r) ** 2 - abs(two_pi_repeat(x) - o) ** 2, 0)) for x in omega])
    return cir


def get_wave(name: str, omega: np.array) -> np.array:
    """

   Parameters
   ----------
   name : str
       The wave's name. for example:"square_HP".
       you can get all the names using get_keys() function
   omega :  np.array
       the frequencies for the wave

   Returns
   -------
   np.array
       the actual wave
   """

    wave = waves_dict.get(name)
    Y = np.array([wave(two_pi_repeat(x)) for x in omega])
    Y=nice_wave(len(Y),Y*60)
    return ((Y))


import matplotlib.pyplot as plt

#t = square(np.linspace(-np.pi, np.pi, 1000), np.pi / 2, 3 * np.pi / 4)
#plt.plot(np.linspace(-np.pi, np.pi, 1000)/np.pi, t)
#plt.show()
