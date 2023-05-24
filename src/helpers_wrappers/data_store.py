import numpy as np
import pandas as pd
from .plotly_helpers import make_colorscale_distinct
from typing import Dict

# Hard coded for now. TODO: Refactor to be dynamic
FILES = [
    "../data/25m@10s.txt",
    "../data/50m@10s.txt",
    "../data/25m@15s.txt",
    "../data/50m@15s.txt"
]

PLOT_TITLES: Dict[str, str] = {
    "25m50m@10s": "SEE index at 25m and 50m <br> Influence of current and wave (10s wave period)",
    "25m50m@15s": "SEE index at 25m and 50m <br> Influence of current and wave (15s wave period)",
    "25m@10s15s": "SEE index at 25m <br> Influence of current and wave (10s and 15s wave period)",
    "50m@10s15s": "SEE index at 50m <br> Influence of current and wave (10s and 15s wave period)",
}

DIFF_PLOT_TITLES: Dict[str, str] = {
    "50m@15s_self": "Reference value (50m@15s)",
    "50m@15s_vs_25m@10s": "25m@10s vs Reference (50m@15s)",
    "50m@15s_vs_25m@15s": "25m@15s vs Reference (50m@15s)",
    "50m@15s_vs_50m@10s": "50m@10s vs Reference (50m@15s)",
}

AXIS_TITLES = [
    "Wave Height [m]",
    "Current Speed [m/s]",
    "SEE index"
]

X = np.linspace(0, 10, 21)
Y = np.linspace(0, 1.5, 16)
Z_VALUES = [
    pd.read_table(FILES[0], header=None).to_numpy(),  # 25m@10s
    pd.read_table(FILES[1], header=None).to_numpy(),  # 50m@10s
    pd.read_table(FILES[2], header=None).to_numpy(),  # 25m@15s
    pd.read_table(FILES[3], header=None).to_numpy(),   # 50m@15s
]

Z_DIFFS = [
    (Z_VALUES[3]/np.max(Z_VALUES[3])) * 100,
    (Z_VALUES[0]/np.max(Z_VALUES[3])) * 100,
    (Z_VALUES[2]/np.max(Z_VALUES[3])) * 100,
    (Z_VALUES[1]/np.max(Z_VALUES[3])) * 100,
]

N_COLORS = {
    "25m@10s": int(np.ceil(np.max(Z_VALUES[0])) // 2),
    "50m@10s": int(np.ceil(np.max(Z_VALUES[1])) // 2),
    "25m@15s": int(np.ceil(np.max(Z_VALUES[2])) // 2),
    "50m@15s": int(np.ceil(np.max(Z_VALUES[3])) // 2),
}

SURFACE_COLORS = {
    "25m@10s": make_colorscale_distinct(N_COLORS["25m@10s"]),
    "50m@10s": make_colorscale_distinct(N_COLORS["50m@10s"]),
    "25m@15s": make_colorscale_distinct(N_COLORS["25m@15s"]),
    "50m@15s": make_colorscale_distinct(N_COLORS["50m@15s"]),
}

SURFACES = {
    "25m@10s": {"x": X, "y": Y, "z": Z_VALUES[0]},
    "50m@10s": {"x": X, "y": Y, "z": Z_VALUES[1]},
    "25m@15s": {"x": X, "y": Y, "z": Z_VALUES[2]},
    "50m@15s": {"x": X, "y": Y, "z": Z_VALUES[3]},
}

DIFF_SURFACES = {
    "50m@15s_self": {"x": X, "y": Y, "z": Z_DIFFS[0]},
    "50m@15s_vs_25m@10s": {"x": X, "y": Y, "z": Z_DIFFS[1]},
    "50m@15s_vs_25m@15s": {"x": X, "y": Y, "z": Z_DIFFS[2]},
    "50m@15s_vs_50m@10s": {"x": X, "y": Y, "z": Z_DIFFS[3]},
}


def merge_properties():
    # sourcery skip: dict-comprehension, inline-immediately-returned-variable
    """
    Merge all properties into a single dictionary
    """
    properties = {}
    for key, value in SURFACES.items():
        properties[key] = {
            "surface": value,
            "colorscale": SURFACE_COLORS[key],
            "n_colors": N_COLORS[key],
        }
    return properties


SURFACE_PROPERTIES = merge_properties()
