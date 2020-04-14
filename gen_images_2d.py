import os

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

import pulsatile_flow


def main():
    w = 1.
    num_frames = 100
    ts = np.linspace(-np.pi / w, np.pi / w, num_frames, endpoint=False)
    r_fraction = np.linspace(-1., 1., 100, endpoint=True)

    out_dir = 'img'
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    alphas = [1, 2, 5, 10]

    fig = plt.figure(frameon=False, figsize=(8,6))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')

    for i, t in tqdm(enumerate(ts), total=num_frames,
                     desc='Rendering frames: ', ascii=True):
        ax.cla()
        for alpha in alphas:
            u = pulsatile_flow.ux(r_fraction, t, w, alpha=alpha)
            ax.plot(u, label=r'$\alpha={:.1f}$'.format(alpha))
        plt.ylim(-1.5, 1.5)
        ax.legend(loc='upper right')
        plt.savefig(os.path.join(out_dir, f'{i}.png'), dpi=300)


if __name__ == '__main__':
    main()
