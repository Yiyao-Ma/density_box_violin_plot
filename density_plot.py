import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def create_cmp():
    from matplotlib import cm
    from matplotlib.colors import ListedColormap
    blue = cm.get_cmap('Blues_r', 256)
    new_colors = blue(np.linspace(0.5, 0.85, 256))
    new_cmp = ListedColormap(new_colors)
    # plot_examples([blue, new_cmp])
    return new_cmp


def plot_examples(cms):
    """
    helper function to plot two colormaps
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)

    fig, axs = plt.subplots(1, 2, figsize=(6, 3), constrained_layout=True)
    for [ax, cmap] in zip(axs, cms):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        fig.colorbar(psm, ax=ax)
    plt.show()


def density_show():
    cmap = create_cmp()  # create your own cmap
    data = pd.read_csv('./example_data/density_data.csv')
    x, y = 'x', 'y'
    fig, ax = plt.subplots(figsize=(10, 12))
    sns.kdeplot(data=data, x=x, y=y, fill=True, levels=12, thresh=0.1, cmap=cmap, ax=ax)
    sns.regplot(data=data, x=x, y=y, scatter=False, color='steelblue', line_kws={'linewidth': '8'})
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    x_left, x_right = -1.2, 1.2  # range of x data
    y_low, y_high = 0.12, 0.28  # range of y data
    ratio = 1.35  # plot's height/width
    fontsize = 47
    ax.set_xlim([x_left, x_right])
    ax.set_ylim([y_low, y_high])
    ax.set_aspect(abs((x_right - x_left) / (y_low - y_high)) * ratio)
    ax.set_xlabel('X-Data Description', fontsize=fontsize, fontname="Arial")
    ax.set_ylabel('Y-Data Description', fontsize=fontsize, fontname="Arial")
    ax.set_xticks(np.arange(-1, 1.1, 0.5))
    ax.set_yticks(np.arange(0.14, 0.261, 0.04), fontsize=fontsize, fontname="Arial")
    fig.subplots_adjust(
        top=0.981,
        bottom=0.12,
        left=0.22,
        right=0.9,
        hspace=0.2,
        wspace=0.2
    )
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize)
        tick.label.set_fontname("Arial")
    for tick in ax.yaxis.get_major_ticks():
        tick.label.set_fontsize(fontsize)
        tick.label.set_fontname("Arial")
    for _, s in ax.spines.items():
        s.set_color('black')
        s.set_linewidth(3)
    plt.show()
    # plt.savefig('./saved_figure/density.png', dpi=300)


if __name__ == '__main__':
    # create_cmp()
    density_show()
