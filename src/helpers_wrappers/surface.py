from itertools import combinations
import os
import pandas as pd
import numpy as np
import math
import pickle


def color_store():
    return {
        "Set3": ["#8DD3C7", "#FFFFB3", "#BEBADA", "#FB8072", "#80B1D3", "#FDB462", "#B3DE69", "#FCCDE5", "#D9D9D9",
                 "#BC80BD", "#CCEBC5", "#FFED6F"],

        "R_rainbow_10": ["#FF0000", "#FF9900", "#CCFF00", "#33FF00", "#00FF66", "#00FFFF", "#0066FF", "#3300FF",
                         "#CC00FF", "#FF0099"],
        "D3": ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22",
               "#17becf"],
        "Plotly": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF",
                   "#FECB52"],
        "G10": ["#3366CC", "#DC3912", "#FF9900", "#109618", "#990099", "#3B3EAC", "#0099C6", "#DD4477", "#66AA00",
                "#B82E2E"],
        "Set1": ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999"],
        "Light24": ["#FD3216", "#00FE35", "#6A76FC", "#FED4C4", "#FE00CE", "#0DF9FF", "#F6F926", "#FF9616", "#479B55",
                    "#EEA6FB", "#DC587D", "#D626FF", "#6E899C", "#00B5F7", "#B68E00", "#C9FBE5", "#FF0092", "#22FFA7",
                    "#E3EE9E", "#86CE00", "#BC7196", "#7E7DCD", "#FC6955", "#E48F72"],
        "Vivid": ["#E58606", "#5D69B1", "#52BCA3", "#99C945", "#CC61B0", "#24796C", "#DAA51B", "#2F8AC4", "#764E9F",
                  "#ED645A", "#A5AA99"],
        "Pastel": ["#66C5CC", "#F6CF71", "#F89C74", "#DCB0F2", "#87C55F", "#9EB9F3", "#FE88B1", "#C9DB74", "#8BE0A4",
                   "#B497E7", "#B3B3B3"]
    }


COLOR_SCALES = color_store()


def generate_plot_titles(file_paths):
    # Split the file paths into folder names and file names
    split_paths = []
    for path in file_paths:
        folder, file = os.path.split(path)
        file_name = os.path.splitext(file)[0]
        split_paths.append({
            "folder": folder, "file": file_name
        })

    # Initialize empty list to store results
    combined_paths = []

    # Get unique folder names
    unique_folders = list(set(x["folder"] for x in split_paths))

    # For each unique folder, generate combinations of files in that folder
    for folder in unique_folders:
        # Get all file names for this folder
        file_names = [x["file"] for x in split_paths if x["folder"] == folder]

        # Generate combinations of file names
        if len(file_names) > 1:
            file_combinations = list(combinations(file_names, 2))
            combined_paths.extend(["+".join(comb) for comb in file_combinations])

    return combined_paths


def make_colorscale_distinct(num_colors_dist, pal="Set3") -> any:
    scaled_values = np.linspace(0, 1, num_colors_dist + 1)

    if pal in COLOR_SCALES:
        colors = COLOR_SCALES[pal]
    else:
        raise ValueError(f"Palette {pal} not found in COLOR_SCALES")

    colors = colors[:num_colors_dist]
    colorscale = []

    for i in range(num_colors_dist):
        entry1 = (scaled_values[i], colors[i])
        entry2 = (scaled_values[i + 1], colors[i])
        colorscale.extend((entry1, entry2))

    return colorscale


def make_colorscale_distinct_single(num_colors_dist, pal="Set3") -> any:
    scaled_values = np.linspace(0, 1, num=num_colors_dist + 1)

    if pal not in COLOR_SCALES:
        raise ValueError(f"Palette {pal} not found in COLOR_SCALES")

    colors = COLOR_SCALES[pal][:min(num_colors_dist, len(COLOR_SCALES[pal]))]
    colorscale = []

    for i in range(num_colors_dist):
        entry = [scaled_values[i], colors[i]]
        colorscale.append((entry, entry))

    return colorscale


def merge_properties():
    for key in AXIS_DATA:
        AXIS_DATA[key].update({
            "colorscale": SURFACE_COLORS[key],
            "n_colors": n_colors[key],
        })
    return AXIS_DATA


file_paths = []
directory = "E:/projects/python-dash-app/plot_data/"
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)

axis_titles = {
    "x": {
        "WH": "Wave Height [m]"
    }, "y": {
        "CS": "Current Speed [m/s]", "WP": "Wave Period [s]"
    }, "z": {
        "SEE": "SEE Index", "EV": "EVRD Index"
    }
}

AXIS_DATA = {
    "A01": {
        "names": [os.path.basename(path).replace(".txt", "") for path in file_paths if "A01" in path],
        "paths": [path for path in file_paths if "A01" in path], "files": {}, "axes": {
            "x": {
                "title": "Wave Height [m]", "values": list(np.linspace(0, 10, num=21)), "range": [0, 10],
                "tickvals": list(np.linspace(0, 10, num=6)), "ticktext": ["0", "2", "4", "6", "8", "10"],
            }, "y": {
                "title": "Current Speed [m/s]", "values": list(np.linspace(0, 1.5, num=16)), "range": [0, 1.5],
                "tickvals": list(np.linspace(0, 1.5, num=4)), "ticktext": ["0", "0.5", "1", "1.5"],
            }, "z": {
                "title": "EVRD Index", "values": list(np.linspace(0, 6, num=7)), "range": [0, 6],
                "tickvals": list(np.linspace(0, 6, num=7)), "ticktext": ["0", "1", "2", "3", "4", "5", "6"],
            }
        },

    }, "A02": {
        "names": [os.path.basename(path).replace(".txt", "") for path in file_paths if "A02" in path],
        "paths": [path for path in file_paths if "A02" in path], "files": {}, "axes": {
            "x": {
                "title": "Wave Height [m]", "values": list(np.linspace(0, 10, num=21)), "range": [0, 10],
                "tickvals": list(np.linspace(0, 10, num=6)), "ticktext": ["0", "2", "4", "6", "8", "10"],
            }, "y": {
                "title": "Current Speed [m/s]", "values": list(np.linspace(0, 1.5, num=16)), "range": [0, 1.5],
                "tickvals": list(np.linspace(0, 1.5, num=4)), "ticktext": ["0", "0.5", "1", "1.5"],
            }, "z": {
                "title": "SEE Index", "values": list(np.linspace(0, 14, num=15)), "range": [0, 14],
                "tickvals": list(np.linspace(0, 14, num=8)), "ticktext": ["0", "2", "4", "6", "8", "10", "12", "14"],
            }
        },

    }, "B01": {
        "names": [os.path.basename(path).replace(".txt", "") for path in file_paths if "B01" in path],
        "paths": [path for path in file_paths if "B01" in path], "files": {}, "axes": {
            "x": {
                "title": "Wave Height [m]", "values": list(np.linspace(0.5, 10, num=20)), "range": [0.5, 10],
                "tickvals": list(np.linspace(0.5, 10, num=5)), "ticktext": ["0.5", "2.5", "5", "7.5", "10"],
            }, "y": {
                "title": "Wave Period [s]", "values": list(np.linspace(15, 6, num=10)), "range": [15, 6],
                "tickvals": list(np.linspace(15, 6, num=5)), "ticktext": ["15", "12", "9", "6"],
            }, "z": {
                "title": "EVRD Index", "values": list(np.linspace(0, 6, num=7)), "range": [0, 6],
                "tickvals": list(np.linspace(0, 6, num=7)), "ticktext": ["0", "1", "2", "3", "4", "5", "6"],
            },
        },

    }, "B02": {
        "names": [os.path.basename(path).replace(".txt", "") for path in file_paths if "B02" in path],
        "paths": [path for path in file_paths if "B02" in path], "files": {}, "axes": {
            "x": {
                "title": "Wave Height [m]", "values": list(np.linspace(0.5, 10, num=20)), "range": [0.5, 10],
                "tickvals": list(np.linspace(0.5, 10, num=5)), "ticktext": ["0.5", "2.5", "5", "7.5", "10"],
            }, "y": {
                "title": "Wave Period [s]", "values": list(np.linspace(15, 6, num=10)), "range": [15, 6],
                "tickvals": list(np.linspace(15, 6, num=5)), "ticktext": ["15", "12", "9", "6"],
            }, "z": {
                "title": "SEE Index", "values": list(np.linspace(0, 18, num=19)), "range": [0, 18],
                "tickvals": list(np.linspace(0, 18, num=10)),
                "ticktext": ["0", "2", "4", "6", "8", "10", "12", "14", "16", "18"],
            },
        },

    }
}

tables = [pd.read_csv(file_path, sep="\t", header=None) for file_path in file_paths]
# tables2 = [pd.read_csv(file_path, sep="\t", header=None).T if "WPI" in file_path else
#            pd.read_csv(file_path, sep="\t", header=None) for file_path in file_paths]

table_names = [os.path.basename(file_path).replace(".txt", "") for file_path in file_paths]

for i, file in enumerate(tables):
    file_name = table_names[i]  # Get the corresponding file name
    for group in AXIS_DATA:
        # Check if the file name is in the names list of this group
        if file_name in AXIS_DATA[group]['names']:
            # If it is, append the file to this group's paths list
            AXIS_DATA[group]['files'][file_name] = file
            break  # No need to check other groups

max_values = {}
for subgroup in AXIS_DATA:
    subgroup_max_values = {name: df.max().max() for name, df in AXIS_DATA[subgroup]['files'].items()}
    max_values[subgroup] = subgroup_max_values

n_colors = {}
for subgroup in AXIS_DATA:
    if subgroup in ["A01", "B01"]:
        subgroup_n_colors = {name: math.ceil(max_val) for name, max_val in max_values[subgroup].items()}
    elif subgroup in ["A02", "B02"]:
        subgroup_n_colors = {name: math.ceil(max_val / 2) for name, max_val in max_values[subgroup].items()}
    else:
        subgroup_n_colors = "how did you get here?"

    n_colors[subgroup] = subgroup_n_colors


# n_colors_see_ev = {}
#
# for key, val in AXIS_DATA.items():
#     if key in ["A01", "A02"]:
#         n_colors_see_ev[key] = math.ceil(max_vals[val] / 2)
#     elif key in ["B01", "B02"]:
#         n_colors_see_ev[key] = math.ceil(max_vals[val])

# SURFACE_COLORS = {key: make_colorscale_distinct(value) for key, value in n_colors_see_ev.items()}
# SURFACE_COLORS = {key: make_colorscale_distinct(value) if "SEE" in key else make_colorscale_distinct_single(value) for
#                   key, value in n_colors_see_ev.items()}

SURFACE_COLORS = {
    outer_key: {
        inner_key: make_colorscale_distinct(inner_value) if outer_key in ['A01', 'A02'] else make_colorscale_distinct_single(inner_value)
        for inner_key, inner_value in outer_value.items()
    }
    for outer_key, outer_value in n_colors.items()
}

# SURFACES = {}
# for i in range(len(table_dict)):
#     name = list(table_dict.keys())[i]
#     group = "WPI" if "WPI" in name else "CS"
#     surface = {"x": axis_vals["x"][group], "y": axis_vals["y"][group], "z": table_dict[name]}
#     SURFACES[name] = surface

axis_merged = merge_properties()

titles = generate_plot_titles(file_paths)
figures = {}

for key in axis_merged:
    names = axis_merged[key]['names']
    all_combinations = []
    for r in range(1, len(names) + 1):
        all_combinations.extend(combinations(names, r))
    all_combinations = [list(comb) for comb in all_combinations]
    axis_merged[key]['combinations'] = all_combinations


# with open("E:/projects/python-dash-app/out/binaries/DATA_BATCH_1.pickle", "wb") as file:
#     pickle.dump(figures, file)
