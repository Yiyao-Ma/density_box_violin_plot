from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

FILE_PATH = "./example_data/vionlin_scatter_box_data.csv"

iris = pd.read_csv(FILE_PATH)

# Background setting
sns.set_style('white')

# Color setting
palette_violin = {'Apple': 'lightsalmon', 'Orange': 'cornflowerblue'}
palette_scatter = {'Apple': 'tomato', 'Orange': 'royalblue'}
palette_box = {'Apple': 'mistyrose', 'Orange': 'lavender'}

# violin part
ax = sns.violinplot(x="data", y="diff", data=iris, hue="data", dodge=False,
                    palette=palette_violin, width=0.5, scale="width", inner=None)
xlim = ax.get_xlim()
ylim = ax.get_ylim()

for violin in ax.collections:
    bbox = violin.get_paths()[0].get_extents()
    x0, y0, width, height = bbox.bounds
    violin.set_clip_path(plt.Rectangle((x0, y0), width / 2, height, transform=ax.transData))

# boxplot part
sns.boxplot(x="data", y="diff", data=iris, saturation=1, showfliers=False,
            width=0.12, boxprops={'zorder': 3, 'facecolor': 'none'}, ax=ax)
old_len_collections = len(ax.collections)

# scatter part
sns.stripplot(x="data", y="diff", data=iris, hue="data", palette=palette_scatter, dodge=False, ax=ax,
              alpha=0.7)

for dots in ax.collections[old_len_collections:]:
    dots.set_offsets(dots.get_offsets() + np.array([0.08, 0]))

sns.despine()

# final plot
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.legend_.remove()
plt.show()
# plt.savefig("./saved_figure/violin_scatter_box.png", dpi=300)
