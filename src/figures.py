from .utils import config_loader
import matplotlib.pyplot as plt

PATH_CONFIG = "../config/config.yaml"
N_BINS = config_loader(PATH_CONFIG)["N_BINS"]

def _style(ax, title, xlabel, ylabel):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_axisbelow(True)
    ax.grid(visible=True, linewidth=0.5)

def hist_grid(df):
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    specs = [("Spross",  "sprout mass", "weight"),
             ("Wurzel",  "root mass",   "weight"),
             ("Ratio",   "mass-ratio",  "ratio")]
    for ax, (col, title, xlabel) in zip(axs, specs):
        ax.hist(df[col], bins=N_BINS, density=True, edgecolor="black")
        _style(ax, title, xlabel, "freq.")
    fig.tight_layout()
    return fig

def correlation(df):
    fig, ax = plt.subplots()
    ax.scatter(x=df["Spross"], y=df["Wurzel"])
    _style(ax, "root-sprout-mass-correlation", "sprout mass", "root mass")
    return fig

def curve_fit(df, column, title, curves, labels):
    fig, ax = plt.subplots()
    ax.hist(df[column], density=True, bins=N_BINS, edgecolor="black", label="data")
    for curve, label in zip(curves, labels):
        ax.plot(*curve,  label=label)
    _style(ax, title, "weight", "freq.")
    ax.legend()
    return fig

def discrete_fit(df, column, title, labels, data):
    label_hist, label_bar = labels
    fig, ax = plt.subplots()
    ax.hist(df[column], density=True, bins=N_BINS, edgecolor="black", label=label_hist)
    ax.bar(*data, color="r", label=label_bar)
    _style(ax, title, "weights", "freq")
    ax.legend()
    return fig