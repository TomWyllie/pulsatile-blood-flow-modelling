import numpy as np
import scipy.special


def ux(r, t, w, alpha=3.5):
    area = 1
    rho = 1

    const_term = area / (1j * w * rho)
    bessel_term = (1 - j0(np.power(1j, 1.5) * alpha * r) / j0(
        np.power(1j, 1.5) * alpha))
    exp_term = np.exp(1j * w * t)

    return np.real(const_term * bessel_term * exp_term)


def j0(x):
    return scipy.special.jv(0., x)
