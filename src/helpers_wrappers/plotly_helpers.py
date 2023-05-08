from typing import List, Tuple
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from .data_store import COLOR_SCALES

DATA_PATH: str = "../data/SEE_index.xlsx"


# axis = {
#     "x": {"title": "Wave Height [m]", "range": np.linspace(0, 10, 21)},
#     "y": {"title": "Current Speed [m/s]", "range": np.linspace(0, 1.5, 16)},
#     "z": {"title": "SEE index", "range": np.linspace(0, 14, 15)},
# }
#
# COLOR_SCALES: dict[str, List[str]] = {
#     'RCB_Set3_12': [
#         "#8DD3C7",
#         "#FFFFB3",
#         "#BEBADA",
#         "#FB8072",
#         "#80B1D3",
#         "#FDB462",
#         "#B3DE69",
#         "#FCCDE5",
#         "#D9D9D9",
#         "#BC80BD",
#         "#CCEBC5",
#         "#FFED6F",
#     ],
#     'R_rainbow_10': [
#         "#FF0000",
#         "#FF9900",
#         "#CCFF00",
#         "#33FF00",
#         "#00FF66",
#         "#00FFFF",
#         "#0066FF",
#         "#3300FF",
#         "#CC00FF",
#         "#FF0099",
#     ]
# }


def make_colorscale_cont(n_colors: int, pal: str = "RCB_Set3_12") -> List[Tuple[float, str]]:
    """
    Generate a continuous colorscale for a given number of groups.

    Args:
        n_colors (int): Amount of groups to generate colors for.
        pal (str, optional): Name of color palette to take colors from. Defaults to "RCB_Set3_12".

    Raises:
        ValueError: Specified palette `pal` not found in COLOR_SCALES.

    Returns:
        List[Tuple[float, str]]: List of tuples of the form (scaled_value, color).
    """
    scaled_values = np.linspace(0, 1, n_colors + 1)

    if pal in COLOR_SCALES:
        colors = COLOR_SCALES[pal]
    else:
        raise ValueError(f"Palette {pal} not found in COLOR_SCALES")

    colors = colors[:n_colors]
    colorscale = []

    for i in range(n_colors):
        entry1 = (scaled_values[i], colors[i])
        colorscale.extend(entry1)

    return colorscale


def make_colorscale_distinct(n_colors: int, pal: str = "Plotly") -> List[Tuple[float, str]]:
    """
    Generate a distinct colorscale for a given number of groups.

    Args:
        n_colors (int): Amount of groups to generate colors for.
        pal (str, optional): Name of color palette to take colors from. Defaults to "RCB_Set3_12".

    Raises:
        ValueError: Specified palette `pal` not found in COLOR_SCALES.

    Returns:
        List[Tuple[float, str]]: List of tuples of the form (scaled_value, color).
    """
    scaled_values = np.linspace(0, 1, n_colors + 1)

    if pal in COLOR_SCALES:
        colors = COLOR_SCALES[pal]
    else:
        raise ValueError(f"Palette {pal} not found in COLOR_SCALES")

    colors = colors[:n_colors]
    colorscale = []

    for i in range(n_colors):
        entry1 = (scaled_values[i], colors[i])
        entry2 = (scaled_values[i + 1], colors[i])
        colorscale.extend((entry1, entry2))

    return colorscale


def get_inputs(
        sheet: str,
        z_format: str = "numpy"
) -> Tuple[np.ndarray | List[List[float]], List[Tuple[float, str]], int]:
    """
    Reads data from the specified Excel sheet and returns it in form of a numpy ndarray,
    along with a colorscale and the amount of colors used.

    Args:
        sheet (str): Name of the Excel sheet to read from.
        z_format (str, optional): Format of the input data. Defaults to "numpy".

    Returns:
        A tuple (z, colorscale, n_colors) where z is the input data as a numpy ndarray,
        colorscale is a list of tuples of the form (scaled_value, color), and n_colors is the amount
        of colors used.
    """
    df: pd.DataFrame = pd.read_excel(DATA_PATH, sheet_name=sheet, header=None)
    if z_format == "numpy":
        z = df.to_numpy()
    elif z_format == "list":
        z = df.values.tolist()
    else:
        raise ValueError(f"z_format must be either 'numpy' or 'list', not {z_format}")

    z_max: int = int(np.ceil(np.max(z)))
    n_colors: int = z_max // 2
    colorscale: List[Tuple[float, str]] = make_colorscale_distinct(n_colors)
    return z, colorscale, n_colors


def create_surface(
        x: np.ndarray,
        y: np.ndarray,
        z: np.ndarray,
        colors_scaled: List[Tuple[float, str]],
        n_colors: int,
        opacity: float = 1.0,
        show_colorbar: bool = False,
        ambient_light: float = 0.9,
) -> go.Surface:
    """
    Takes return values from `get_inputs` and produces a surface that can be added to a plotly plot.

    Args:
        x (ndarray): X-axis values.
        y (ndarray): Y-axis values.
        z (ndarray): Input data in form of a numpy ndarray (as returned by `get_inputs`).
        colors_scaled (List[Tuple[float, str]]): List of tuples of the form (scaled_value, color).
        n_colors (int): Amount of groups to generate colors for.
        opacity (float, optional): Opacity of the surface. Defaults to 1.
        show_colorbar (bool, optional): Whether to show colorbar. Defaults to False.

    Returns:
        go.Surface: Surface to be added to a plotly plot

    """
    return go.Surface(
        x=x,
        y=y,
        z=z,
        opacity=opacity,
        colorscale=colors_scaled,
        cmin=0,
        cmax=(n_colors * 2),
        showscale=show_colorbar,
        colorbar=dict(
            tickmode="array",
            tickvals=np.arange(0, (n_colors * 2) + 1, 2),
            ticktext=np.arange(0, (n_colors * 2) + 1, 2),
            orientation="v",
            y=0.5,
            x=0.95,
            len=0.5,
            tickfont=dict(size=20),
        ),
        contours=dict(
            x=dict(show=True, start=0, end=10, size=2, color="black", width=5),
            y=dict(show=True, start=0, end=1.5, size=0.5, color="black", width=5),
            # z=dict(show=True, start=0, end=(n_colors * 2), size=2),
        ),
        hoverinfo="skip",
        lighting=dict(
            ambient=ambient_light,
            diffuse=0.5,
        ),
    )


def create_layout(
        title: str,
        x_label: str,
        y_label: str,
        z_label: str,
        surface_1_name: str,
        surface_2_name: str,
        surface_1: np.ndarray = None,
        surface_2: np.ndarray = None,
        x_scale: float = 1.0,
        y_scale: float = 0.5,
        z_scale: float = 0.5,
) -> go.Layout:
    """
    Layout settings for a plotly plot

    Args:
        title (str): Plot title
        x_label (str): x-axis label
        y_label (str): y-axis label
        z_label (str): z-axis label
        surface_1 (ndarray, optional): Surface 1. Defaults to None.
        surface_2 (ndarray, optional): Surface 2. Defaults to None.
        x_scale (float, optional): Set the x-axis scale. Defaults to 1.
        y_scale (float, optional): Set the y-axis scale. Defaults to 0.5
        z_scale (float, optional): Set the z-axis scale. Defaults to 0.5

    Returns:
        go.Layout: Layout to be added to a plotly plot
    """
    if surface_1 is not None:
        surface_1_x = surface_1["x"][20]
        surface_1_y = surface_1["y"][13]
        surface_1_z = surface_1["z"][13][20]
    else:
        surface_1_x = 10
        surface_1_y = 1.4
        surface_1_z = 12

    if surface_2 is not None:
        surface_2_x = surface_2["x"][20]
        surface_2_y = surface_2["y"][13]
        surface_2_z = surface_2["z"][13][20]
    else:
        surface_2_x = 10
        surface_2_y = 1.4
        surface_2_z = 10

    return go.Layout(
        template="ggplot2",
        autosize=False,
        height=1000,
        # width=1400,
        margin=dict(r=10, b=10, l=10, t=10),
        # paper_bgcolor="LightSteelBlue",
        title=dict(
            text=title,
            x=0.5,
            y=0.825,
            xanchor="center",
            yanchor="middle",
            font=dict(size=30)
        ),
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=x_scale, y=y_scale, z=z_scale),
            xaxis=dict(
                title='',
                tickfont=dict(size=16),
                tickangle=0,
                tickwidth=5,
                ticks="outside",
                showgrid=True,
                showbackground=True,
                # backgroundcolor="gray",
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                range=[0, 10],
                tickmode="array",
                tickvals=[0, 2, 4, 6, 8, 10],
                ticktext=["0", "2", "4", "6", "8", "10"],
            ),
            yaxis=dict(
                title='',
                tickfont=dict(size=16),
                ticks="outside",
                tickwidth=5,
                showgrid=True,
                showbackground=True,
                # backgroundcolor="gray",
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                tickmode="array",
                tickvals=[0, 0.5, 1.0, 1.5],
                ticktext=["0.0", "0.5", "1.0", "1.5"],
                range=[0.00, 1.5],
            ),
            zaxis=dict(
                title='',
                tickfont=dict(size=16),
                ticks="outside",
                showgrid=True,
                tickwidth=5,
                showbackground=True,
                # backgroundcolor="gray",
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                tickmode="array",
                tickvals=[0, 2, 4, 6, 8, 10, 12, 14],
                ticktext=["", "2", "4", "6", "8", "10", "12", "14"],
                range=[0, 14],
            ),
            annotations=[  # 3d Annotations
                dict(
                    x=3,
                    y=0.45,
                    z=0,
                    textangle=21,
                    yshift=-71,
                    xshift=20,
                    text=x_label,
                    showarrow=False,
                    font=dict(size=25),
                    xanchor="center",
                    yanchor="top",
                    # captureevents=True,
                ),
                dict(
                    x=9.8,
                    y=0.25,
                    z=0,
                    textangle=-43,
                    text=y_label,
                    showarrow=False,
                    font=dict(size=25),
                    xanchor="left",
                    xshift=78,
                    yanchor="middle",
                    # captureevents=True,
                ),
                dict(
                    x=0.05,
                    y=0.02,
                    z=7,
                    textangle=-94,
                    text=z_label,
                    showarrow=False,
                    font=dict(size=25),
                    xanchor="right",
                    xshift=-60,
                    yanchor="middle",
                    # captureevents=True,
                ),
                dict(
                    x=surface_1_x,
                    y=surface_1_y,
                    z=surface_1_z,
                    text=surface_1_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=-20,
                    xanchor="left",
                ),
                dict(
                    x=surface_2_x,
                    y=surface_2_y,
                    z=surface_2_z,
                    text=surface_2_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=-20,
                    xanchor="left",
                )
            ],
            camera=dict(
                center=dict(x=0, y=0, z=0),
                eye=dict(x=0.96, y=-1.12, z=0.26),
            ),
        ),

    )


def percentage_difference(base_array, compare_array):
    # Calculate the absolute difference between the arrays
    difference = np.abs(base_array - compare_array)

    # Determine the maximum and minimum values in the base array
    max_value = np.max(base_array)
    min_value = np.min(base_array)

    # Normalize the differences by the maximum possible difference in the base array
    max_possible_difference = max_value - min_value
    normalized_difference = difference / max_possible_difference

    # Convert the normalized difference to percentage
    percentage_difference = normalized_difference * 100

    return percentage_difference



def create_diff_layout(
        title: str,
        x_label: str,
        y_label: str,
        z_label: str,
        surface_1_name: str,
        surface_1: np.ndarray = None,
        x_scale: float = 1.0,
        y_scale: float = 0.5,
        z_scale: float = 0.5,
) -> go.Layout:
    """
    Layout settings for a plotly plot

    Args:
        title (str): Plot title
        x_label (str): x-axis label
        y_label (str): y-axis label
        z_label (str): z-axis label
        surface_1 (ndarray, optional): Surface 1. Defaults to None.
        surface_2 (ndarray, optional): Surface 2. Defaults to None.
        x_scale (float, optional): Set the x-axis scale. Defaults to 1.
        y_scale (float, optional): Set the y-axis scale. Defaults to 0.5
        z_scale (float, optional): Set the z-axis scale. Defaults to 0.5

    Returns:
        go.Layout: Layout to be added to a plotly plot
    """
    if surface_1 is not None:
        surface_1_x = surface_1["x"][20]
        surface_1_y = surface_1["y"][13]
        surface_1_z = surface_1["z"][13][20]
    else:
        surface_1_x = 10
        surface_1_y = 1.4
        surface_1_z = 12

    return go.Layout(
        template="ggplot2",
        autosize=False,
        height=1000,
        # width=1400,
        margin=dict(r=10, b=10, l=10, t=10),
        # paper_bgcolor="LightSteelBlue",
        title=dict(
            text=title,
            x=0.5,
            y=0.825,
            xanchor="center",
            yanchor="middle",
            font=dict(size=30)
        ),
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=x_scale, y=y_scale, z=z_scale),
            xaxis=dict(
                title=x_label,
                tickfont=dict(size=16),
                tickangle=0,
                tickwidth=5,
                ticks="outside",
                showgrid=True,
                showbackground=True,
                # backgroundcolor="gray",
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                range=[0, 10],
                tickmode="array",
                tickvals=[0, 2, 4, 6, 8, 10],
                ticktext=["0", "2", "4", "6", "8", "10"],
            ),
            yaxis=dict(
                title=y_label,
                tickfont=dict(size=16),
                ticks="outside",
                tickwidth=5,
                showgrid=True,
                showbackground=True,
                # backgroundcolor="gray",
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                tickmode="array",
                tickvals=[0, 0.5, 1.0, 1.5],
                ticktext=["0.0", "0.5", "1.0", "1.5"],
                range=[0.00, 1.5],
            ),
            zaxis=dict(
                title=z_label,
                tickfont=dict(size=16),
                ticks="outside",
                showgrid=True,
                tickwidth=5,
                showbackground=True,
                # backgroundcolor="gray",
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
            ),
            annotations=[  # 3d Annotations
                # dict(
                #     x=3,
                #     y=0.45,
                #     z=0,
                #     textangle=21,
                #     yshift=-71,
                #     xshift=20,
                #     text=x_label,
                #     showarrow=False,
                #     font=dict(size=25),
                #     xanchor="center",
                #     yanchor="top",
                #     # captureevents=True,
                # ),
                # dict(
                #     x=9.8,
                #     y=0.25,
                #     z=0,
                #     textangle=-43,
                #     text=y_label,
                #     showarrow=False,
                #     font=dict(size=25),
                #     xanchor="left",
                #     xshift=78,
                #     yanchor="middle",
                #     # captureevents=True,
                # ),
                # dict(
                #     x=0.05,
                #     y=0.02,
                #     z=7,
                #     textangle=-94,
                #     text=z_label,
                #     showarrow=False,
                #     font=dict(size=25),
                #     xanchor="right",
                #     xshift=-60,
                #     yanchor="middle",
                #     # captureevents=True,
                # ),
                dict(
                    x=surface_1_x,
                    y=surface_1_y,
                    z=surface_1_z,
                    text=surface_1_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=-20,
                    xanchor="left",
                ),
            ],
            camera=dict(
                center=dict(x=0, y=0, z=0),
                eye=dict(x=0.96, y=-1.12, z=0.26),
            ),
        ),

    )
