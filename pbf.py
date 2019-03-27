import numpy as np


def thin(x, tau, x0=0):
    """The classical, square-law structure media thin screen approximation for a pulse broadening function.
    See e.g. Cordes & Rickett (1998) and Lambert & Rickett (1999).

    :param x: time over which to evaluate the PBF [array-like]
    :param tau: pulse broadening time scale [float]
    :param x0: where the PBF turns on [float, in range of x]
    :return: evaluated thin screen PBF [array-like]
    """
    t = x - x0
    h = (1 / tau) * np.exp(-t / tau)  # normalised to unit area

    # Turn on a unit step function at the given x0 offset.
    h[x <= x0] = 0

    return h


def thick(x, tau, x0=0):
    """The thick screen pulse broadening function as presented in Williamson (1972, 1973).

    :param x: time over which to evaluate the PBF [array-like]
    :param tau: pulse broadening time scale [float]
    :param x0: where the PBF turns on [float, in range of x]
    :return: evaluated thick screen PBF [array-like]
    """
    t = x - x0
    h = np.sqrt((np.pi * tau) / (4 * t ** 3)) * np.exp(-tau * np.pi ** 2 / (16 * t))  # normalised to unit area

    # In some cases (for negative t), h will not be well-defined (nan).
    # However, this is not important in this case, thus we can simply
    # replace those values with 0.
    h[np.isnan(h)] = 0

    return h


def uniform(x, tau, x0=0):
    """The uniform media pulse broadening function as presented in Williamson (1972, 1973).

    :param x: time over which to evaluate the PBF [array-like]
    :param tau: pulse broadening time scale [float]
    :param x0: where the PBF turns on [float, in range of x]
    :return: evaluated PBF for a uniform scattering medium [array-like]
    """
    t = x - x0
    h = np.sqrt((np.pi**5 * tau**3) / (8 * t**5)) * np.exp(-tau * np.pi**2 / (4 * t))  # normalised to unit area

    # In some cases (for negative t), h will not be well-defined (nan).
    # However, this is not important in this case, thus we can simply
    # replace those values with 0.
    h[np.isnan(h)] = 0

    return h
