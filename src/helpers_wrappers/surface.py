import numpy as np
import pandas as pd
from .plotly_helpers import make_colorscale_distinct
from .data_store import FILES


X = np.linspace(0, 10, 21)
Y = np.linspace(0, 1.5, 16)
Z_VALUES = [
    pd.read_table(FILES[0], header=None).to_numpy(),
    pd.read_table(FILES[1], header=None).to_numpy(),
    pd.read_table(FILES[2], header=None).to_numpy(),
    pd.read_table(FILES[3], header=None).to_numpy()
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
