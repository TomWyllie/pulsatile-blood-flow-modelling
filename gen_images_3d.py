import argparse
import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
# noinspection PyUnresolvedReferences
from mpl_toolkits.mplot3d import Axes3D
from tqdm import tqdm

import pulsatile_flow


def main(alpha):
    w = 1.
    num_frames = 120
    ts = np.linspace(-np.pi / w, np.pi / w, num_frames, endpoint=False)
    height_of_3d_plot = 1.2

    resolution = 60
    x = np.linspace(-1.0, 1.0, resolution)
    y = np.linspace(-1.0, 1.0, resolution)
    x, y = np.meshgrid(x, y)
    r = np.sqrt(x ** 2 + y ** 2)
    r[r > 1.] = 1.

    out_dir = 'img3d-{:.2f}'.format(alpha)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    fig = plt.figure(frameon=False, figsize=(8, 6))
    ax = fig.gca(projection='3d')

    for i, t in tqdm(enumerate(ts), total=num_frames,
                     desc='Rendering frames: ', ascii=True):
        ax.cla()
        ax.grid(False)
        ax.set_title(r'$\alpha={:.2f}$'.format(alpha), color='white')
        fig.set_facecolor('black')
        ax.set_facecolor('black')
        ax.xaxis.pane.set_edgecolor('black')
        ax.yaxis.pane.set_edgecolor('black')
        ax.zaxis.pane.set_edgecolor('black')
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.w_xaxis.line.set_color('white')
        ax.w_yaxis.line.set_color('white')
        ax.w_zaxis.line.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='z', colors='white')

        # Matplotlib bugged as usual :((
        # https://stackoverflow.com/questions/53549960/setting-tick-colors-of-matplotlib-3d-plot
        # noinspection PyProtectedMember
        ax.xaxis._axinfo['tick']['color'] = 'white'
        # noinspection PyProtectedMember
        ax.yaxis._axinfo['tick']['color'] = 'white'
        # noinspection PyProtectedMember
        ax.zaxis._axinfo['tick']['color'] = 'white'

        u = pulsatile_flow.ux(r, t, w, alpha=alpha)

        # Plot the surface.
        # noinspection PyUnresolvedReferences
        ax.plot_surface(x, y, u, cmap=cm.plasma,    # plasma :)))
                        vmin=-height_of_3d_plot,
                        vmax=height_of_3d_plot, linewidth=0, antialiased=True)

        # Customize the z axis.
        ax.set_zlim(-height_of_3d_plot, height_of_3d_plot)

        plt.savefig(os.path.join(out_dir, f'{i}.png'), dpi=150,
                    bbox_inches='tight', pad_inches=0.)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--alpha', default=3.0, type=float)
    args = arg_parser.parse_args()
    main(args.alpha)
