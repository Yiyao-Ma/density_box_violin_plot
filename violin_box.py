import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

FILE_PATH = "./example_data/violin_box_data.csv"

tips = pd.read_csv(FILE_PATH)

sns.set_theme(style="white")

# Color for violin and box plot, light orange and blue
palette_violin = {'normal': 'lightsalmon', 'special': 'cornflowerblue'}
palette_box = {'normal': 'tomato', 'special': 'royalblue'}

# Draw a nested violin_plot and split the violins for easier comparison
ax = sns.violinplot(data=tips, x="data", y="weight", hue="type",
                    split=True, inner="quartiles", linewidth=1, width=0.6,
                    dodge=False, palette=palette_violin)

# Draw a nested boxplot to show bills by day and time
ax = sns.boxplot(x="data", y="weight", hue="type",
                 showfliers=False, data=tips, width=0.15,
                 boxprops={'zorder': 2}, ax=ax, palette=palette_box)


sns.despine(bottom=False)

ax.legend_.remove()  # remove legend

plt.show()
# plt.savefig("./saved_figure/violin_box.png", dpi=300)
