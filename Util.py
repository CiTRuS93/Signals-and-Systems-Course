import numpy
import numpy as np


# this function performs a dft to the vector x, where the dft resolution is n. in case that n is higher than x, the
# # default fft function of numpy is padding x with zeros. in case that n is lower than x,
# the signal x is folded to length n, and the result is gone through the dft (the default operation of the numpy fft
# in this case is to cut only the n first samples of x, an idiotic choice for default)



def fold_and_dft(x, n):
    # if the required resolution is lower than the signal length - fold it:
    if n < len(x):
        x = fold_signal(x, n)
    # perform dft
    x_dft = np.fft.fft(x, n, 0)
    return x_dft

# this function is very useful in signal frequency processing, it gets a signal (the vector x) and folds it to a shorter
# vector (of length n). this folding is done by splitting x to partial vectors each of length n (if the length doesn't
# fit, we add zeros at the end of the last partial vector), and then summing these vectors.

def fold_signal(x, n):
    # dimensions
    nx = len(x)
    # number of segments
    ns = int(np.ceil(nx / n))
    # run over the signal's segments and fold
    x_fold = 0 * x[0: n]
    for idx in range(ns):
        # define the indices range
        idx_first = idx * n
        idx_last = (idx + 1) * n
        # if this is the last frame:
        if idx_last < nx:
            x_fold = x_fold + x[idx_first: idx_last]
        else:  # in all the other frames:
            idx_last_out = nx - idx_first
            x_fold[0: idx_last_out] = x_fold[0: idx_last_out] + x[idx_first: nx]
    return x_fold


def drop_every_kth(k,x):
    return np.delete(x, np.arange(0, x.size, k))


def zero_padding(k,x):
    return np.insert(x, range(0, len(x), k), 0)


def v_to_db(x):
    return 20*np.log10(abs(x))