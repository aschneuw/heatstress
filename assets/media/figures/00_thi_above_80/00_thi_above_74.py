#! /usr/bin/env python3

import pandas as pd
import geopandas as gp
gp.options.io_engine = "pyogrio"
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.colors as mcolors

t = 74
df = pd.read_parquet("/home/aschneuwl/workspace/agecon-thesis/notebooks/00_preprocessing/daily_weather_data_zip_centers.parquet")
localities_swiss = gp.read_parquet("/home/aschneuwl/workspace/agecon-thesis/notebooks/AMTOVZ_ZIP_wgs84.parquet")

# Create year column
df.loc[:, "year"] = df.time.dt.year

# Function to process data for a given year range
def process_data(start_year, end_year):
    data = df[(df["year"] >= start_year-1) & (df["year"] < end_year+1)].groupby(["ZIP4", "year"])["thi_max"].apply(lambda x: (x > t).sum()).reset_index().groupby("ZIP4").thi_max.median().reset_index()
    data.loc[:,"thi_max"] = data["thi_max"].apply(lambda x: x + 1)
    return localities_swiss.merge(data, on="ZIP4")

# Generate data for each 5-year period
data_periods = [process_data(start_year, start_year + 5) for start_year in range(1984, 2024, 5)]

# Create subplots
fig, axs = plt.subplots(4, 2, figsize=(14, 20))
axs = axs.flatten()

# Set common color scale
vmin = min([data['thi_max'].min() for data in data_periods])
vmax = max([data['thi_max'].max() for data in data_periods])
norm = mcolors.LogNorm(vmin=vmin + 1, vmax=vmax)

# Plot each data period
for i, ax in enumerate(axs):
    if i < len(data_periods):
        data_periods[i].plot(ax=ax, column="thi_max", legend=False, cmap='jet', vmin=vmin, vmax=vmax, norm=norm)
        ax.set_title(f'{1984 + i*5}-{1988 + i*5}', fontsize=15)
    else:
        ax.axis('off')
    
    # Remove axes and ticks
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# Add a common colorbar
sm = plt.cm.ScalarMappable(cmap='jet', norm=norm)
fig.tight_layout(rect=[0, 0.05, 1, 0.95])
sm._A = []
cbar_ax = fig.add_axes([0.15, 0.02, 0.7, 0.02])
cbar = fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')
cbar.set_ticks([2, 11, 31, 51, 71])
cbar.set_ticklabels([0, 10, 30, 50, 70])
cbar.set_label(f'Median Number of Days with Max THI > {t} per Year', fontsize=15)

# Save or display the figure
save_fpath_pdf = Path(__file__).parent.resolve() / Path(f"thi_above_{t}.pdf")
save_fpath_png = Path(__file__).parent.resolve() / Path(f"thi_above_{t}.png")
fig.savefig(save_fpath_pdf, format='pdf', bbox_inches='tight')
fig.savefig(save_fpath_png, format='png', bbox_inches='tight')

plt.show()