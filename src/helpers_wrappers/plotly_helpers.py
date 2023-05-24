from typing import List, Tuple
import plotly.graph_objects as go
import numpy as np

COLOR_SCALES: dict[str, List[str]] = {
    'Set3': [
        "#8DD3C7",
        "#FFFFB3",
        "#BEBADA",
        "#FB8072",
        "#80B1D3",
        "#FDB462",
        "#B3DE69",
        "#FCCDE5",
        "#D9D9D9",
        "#BC80BD",
        "#CCEBC5",
        "#FFED6F",
    ],
    'R_rainbow_10': [
        "#FF0000",
        "#FF9900",
        "#CCFF00",
        "#33FF00",
        "#00FF66",
        "#00FFFF",
        "#0066FF",
        "#3300FF",
        "#CC00FF",
        "#FF0099",
    ],
    'D3': [
        "#1f77b4",
        "#ff7f0e",
        "#2ca02c",
        "#d62728",
        "#9467bd",
        "#8c564b",
        "#e377c2",
        "#7f7f7f",
        "#bcbd22",
        "#17becf",
    ],
    'Plotly': [
        "#636efa",
        "#EF553B",
        "#00cc96",
        "#ab63fa",
        "#FFA15A",
        "#19d3f3",
        "#FF6692",
        "#B6E880",
        "#FF97FF",
        "#FECB52",
    ],
    'G10': [
        "#3366CC",
        "#DC3912",
        "#FF9900",
        "#109618",
        "#990099",
        "#3B3EAC",
        "#0099C6",
        "#DD4477",
        "#66AA00",
        "#B82E2E",
    ],
    'Set1': [
        "#e41a1c",
        "#377eb8",
        "#4daf4a",
        "#984ea3",
        "#ff7f00",
        "#ffff33",
        "#a65628",
        "#f781bf",
        "#999999",
    ],
    'Light24': [
        '#FD3216', '#00FE35', '#6A76FC', '#FED4C4', '#FE00CE', '#0DF9FF', '#F6F926',
        '#FF9616', '#479B55', '#EEA6FB', '#DC587D', '#D626FF', '#6E899C', '#00B5F7',
        '#B68E00', '#C9FBE5', '#FF0092', '#22FFA7', '#E3EE9E', '#86CE00', '#BC7196',
        '#7E7DCD', '#FC6955', '#E48F72'
    ],
    'Vivid': [
        'rgb(229, 134, 6)', 'rgb(93, 105, 177)', 'rgb(82, 188, 163)', 'rgb(153, 201, 69)',
        'rgb(204, 97, 176)', 'rgb(36, 121, 108)', 'rgb(218, 165, 27)', 'rgb(47, 138, 196)',
        'rgb(118, 78, 159)', 'rgb(237, 100, 90)', 'rgb(165, 170, 153)'
    ],
    'Pastel': [
        'rgb(102, 197, 204)', 'rgb(246, 207, 113)', 'rgb(248, 156, 116)',
        'rgb(220, 176, 242)', 'rgb(135, 197, 95)', 'rgb(158, 185, 243)',
        'rgb(254, 136, 177)', 'rgb(201, 219, 116)', 'rgb(139, 224, 164)',
        'rgb(180, 151, 231)', 'rgb(179, 179, 179)'
    ]

}


def make_colorscale_cont(n_colors: int, pal: str = "Viridis") -> List[Tuple[float, str]]:
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


def make_colorscale_distinct(n_colors: int, pal: str = "Set3") -> List[Tuple[float, str]]:
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


# def get_inputs(
#         sheet: str,
#         z_format: str = "numpy"
# ) -> Tuple[np.ndarray | List[List[float]], List[Tuple[float, str]], int]:
#     """
#     Reads data from the specified Excel sheet and returns it in form of a numpy ndarray,
#     along with a colorscale and the amount of colors used.
#
#     Args:
#         sheet (str): Name of the Excel sheet to read from.
#         z_format (str, optional): Format of the input data. Defaults to "numpy".
#
#     Returns:
#         A tuple (z, colorscale, n_colors) where z is the input data as a numpy ndarray,
#         colorscale is a list of tuples of the form (scaled_value, color), and n_colors is the amount
#         of colors used.
#     """
#     df: pd.DataFrame = pd.read_excel(DATA_PATH, sheet_name=sheet, header=None)
#     if z_format == "numpy":
#         z = df.to_numpy()
#     elif z_format == "list":
#         z = df.values.tolist()
#     else:
#         raise ValueError(f"z_format must be either 'numpy' or 'list', not {z_format}")
#
#     z_max: int = int(np.ceil(np.max(z)))
#     n_colors: int = z_max // 2
#     colorscale: List[Tuple[float, str]] = make_colorscale_distinct(n_colors)
#     return z, colorscale, n_colors


def create_surface(
        x: np.ndarray,
        y: np.ndarray,
        z: np.ndarray,
        colors_scaled: List[List],
        n_colors: int,
        opacity: float = 1.0,
        show_colorbar: bool = False,
        ambient_light: float = 0.9,
) -> go.Surface:
    """
    Takes values and produces a surface that can be added to a plotly plot.

    Args:
        x (ndarray): X-axis values.
        y (ndarray): Y-axis values.
        z (ndarray): Input data in form of a numpy ndarray (as returned by `get_inputs`).
        colors_scaled (List[Tuple[float, str]]): List of tuples of the form (scaled_value, color).
        n_colors (int): Amount of groups to generate colors for.
        opacity (float, optional): Opacity of the surface. Defaults to 1.
        show_colorbar (bool, optional): Whether to show colorbar. Defaults to False.
        ambient_light (float, optional): Ambient light of the surface. Defaults to 0.9.

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
            x=0.9,
            len=0.5,
            tickfont=dict(size=20),
        ),
        contours=dict(
            x=dict(show=True, start=0, end=10, size=2, color="black", width=5),
            y=dict(show=True, start=0, end=1.5, size=0.5, color="black", width=5),
        ),
        hoverinfo="skip",
        lighting=dict(
            ambient=ambient_light,
            diffuse=0.5,
        ),
    )

def get_annotation_point(x, y, z):
    if len(x) < 2 or len(y) < 2:
        raise ValueError("x and y must have at least two elements")

    x_value = x[-1]
    y_value = y[-1]
    z_value = z.iloc[-1, -1]

    return x_value, y_value, z_value


def create_layout(
        x_label: str,
        y_label: str,
        z_label: str,
        surface_1_name: str,
        surface_2_name: str,
        surface_1: np.ndarray | go.Surface = None,
        surface_2: np.ndarray | go.Surface= None,
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
        surface_1_name (str): Name of surface 1
        surface_2_name (str): Name of surface 2
        surface_1 (ndarray, optional): Surface 1. Defaults to None.
        surface_2 (ndarray, optional): Surface 2. Defaults to None.
        x_scale (float, optional): Set the x-axis scale. Defaults to 1.
        y_scale (float, optional): Set the y-axis scale. Defaults to 0.5
        z_scale (float, optional): Set the z-axis scale. Defaults to 0.5

    Returns:
        go.Layout: Layout to be added to a plotly plot
    """

    surface_1_x, surface_1_y, surface_1_z = get_annotation_point(surface_1["x"], surface_1["y"], surface_1["z"])
    surface_2_x, surface_2_y, surface_2_z = get_annotation_point(surface_2["x"], surface_2["y"], surface_2["z"])
    y_tick_labels_cs = ["0", "0.5", "1"]
    y_tick_vals_cs = [0, 0.5, 1]
    y_tick_labels_wpi = ["15", "12", "9", "6"]
    y_tick_vals_wpi = [15, 12, 9, 6]
    z_tick_labels_see = ["", "2", "4", "6", "8", "10", "12", "14"]
    z_tick_vals_see = [0, 2, 4, 6, 8, 10, 12, 14]
    z_tick_labels_wpi = ["", "2", "4", "6", "8", "10", "12", "14", "16", "18", "20"]
    z_tick_vals_wpi = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    z_tick_labels_shown = z_tick_labels_wpi if "WPI" in surface_1_name else z_tick_labels_see
    z_tick_vals_shown = z_tick_vals_wpi if "WPI" in surface_1_name else z_tick_vals_see

    return go.Layout(
        autosize=False,
        height=900,
        margin=dict(r=0, b=0, l=0, t=0, pad=0, autoexpand=True),
        title='',
        scene=dict(
            aspectmode="manual",
            aspectratio=dict(x=x_scale, y=y_scale, z=z_scale),
            xaxis=dict(
                backgroundcolor="#999",
                linecolor="black",
                linewidth=5,
                mirror=True,
                range=[0, 10],
                showbackground=True,
                showgrid=True,
                showline=True,
                showticklabels=True,
                tickcolor="white",
                tickfont=dict(size=21, color="black", family="Arial"),
                ticklen=20,
                tickmode="array",
                ticks="outside",
                ticktext=["0", "2", "4", "6", "8", "10"],
                tickvals=[0, 2, 4, 6, 8, 10],
                tickwidth=5,
                title='',
                # zeroline=True,
                # zerolinecolor="black",
                # zerolinewidth=5,
            ),
            yaxis=dict(
                backgroundcolor="#999",
                linecolor="black",
                linewidth=5,
                mirror=True,
                range=[15, 6] if "WPI" in surface_1_name else [0.00, 1.5],
                showbackground=True,
                showgrid=True,
                showline=True,
                showticklabels=True,
                tickcolor="white",
                tickfont=dict(size=21, color="black", family="Arial"),
                ticklen=20,
                tickmode="array",
                ticks="outside",
                ticktext=y_tick_labels_wpi if "WPI" in surface_1_name else y_tick_labels_cs,
                tickvals=y_tick_vals_wpi if "WPI" in surface_1_name else y_tick_vals_cs,
                tickwidth=5,
                title='',
                # zeroline=True,
                # zerolinecolor="black",
                # zerolinewidth=5,
            ),
            zaxis=dict(
                backgroundcolor="#999",
                linecolor="black",
                linewidth=5,
                mirror=True,
                range=[0, 14] if "SEE" in surface_1_name else [0, 6],
                showbackground=True,
                showgrid=True,
                showline=True,
                showticklabels=True,
                tickcolor="white",
                tickfont=dict(size=21, color="black", family="Arial"),
                ticklen=20,
                tickmode="array",
                ticks="outside",
                ticktext=z_tick_labels_shown,
                tickvals=z_tick_vals_shown,
                tickwidth=5,
                title='',
                # zeroline=True,
                # zerolinecolor="black",
                # zerolinewidth=5,
            ),
            annotations=[
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
                ),
                dict(
                    x=0.05,
                    y=0.02,
                    z=7 if "SEE" in surface_1_name else 3,
                    textangle=-94,
                    text=z_label,
                    showarrow=False,
                    font=dict(size=25),
                    xanchor="right",
                    xshift=-60,
                    yanchor="middle",
                ),
                dict(
                    x=surface_1_x,
                    y=surface_1_y,
                    z=surface_1_z,
                    bgcolor="white",
                    bordercolor="black",
                    text=surface_1_name,
                    font=dict(size=21),
                    arrowhead=6,
                    ax=70,
                    ay=-20,
                    xanchor="left",
                ),
                dict(
                    x=surface_2_x,
                    y=surface_2_y,
                    z=surface_2_z,
                    bgcolor="white",
                    bordercolor="black",
                    text=surface_2_name,
                    font=dict(size=21),
                    arrowhead=6,
                    ax=70,
                    ay=20,
                    xanchor="left",
                )
            ],
            camera=dict(
                center=dict(x=0.1, y=0.1, z=0),
                eye=dict(x=0.96, y=-1.12, z=0.26),
            ),
        ),
    )


def percentage_difference(base_array: np.ndarray, compare_array: np.ndarray) -> np.ndarray:
    # Calculate the absolute difference between the arrays
    difference = np.abs(base_array - compare_array)

    # Determine the maximum and minimum values in the base array
    max_value = np.max(base_array)
    min_value = np.min(base_array)

    # Normalize the differences by the maximum possible difference in the base array
    max_possible_difference = max_value - min_value
    normalized_difference = difference / max_possible_difference

    return normalized_difference * 100


def create_diff_layout(
        title: str,
        x_label: str,
        y_label: str,
        z_label: str,
        surface_1_name: str,
        surface_1: np.ndarray = None,
        surface_2_name: str = None,
        surface_2: np.ndarray = None,
        surface_3_name: str = None,
        surface_3: np.ndarray = None,
        surface_4_name: str = None,
        surface_4: np.ndarray = None,
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
        surface_1_name (str): Name of surface 1
        surface_1 (ndarray, optional): Surface 1. Defaults to None.
        x_scale (float, optional): Set the x-axis scale. Defaults to 1.
        y_scale (float, optional): Set the y-axis scale. Defaults to 0.5
        z_scale (float, optional): Set the z-axis scale. Defaults to 0.5

    Returns:
        go.Layout: Layout to be added to a plotly plot
    """
    surface_1_x = surface_1["x"][20]
    surface_1_y = surface_1["y"][13]
    surface_1_z = surface_1["z"][13][20]

    surface_2_x = surface_2["x"][20]
    surface_2_y = surface_2["y"][13]
    surface_2_z = surface_2["z"][13][20]

    surface_3_x = surface_3["x"][20]
    surface_3_y = surface_3["y"][13]
    surface_3_z = surface_3["z"][13][20]

    surface_4_x = surface_4["x"][20]
    surface_4_y = surface_4["y"][13]
    surface_4_z = surface_4["z"][13][20]

    return go.Layout(
        template="ggplot2",
        autosize=False,
        height=1000,
        width=1400,
        margin=dict(r=50, b=10, l=10, t=10),
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
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                range=[0, 10],
                tickmode="array",
                tickvals=[0, 2, 4, 6, 8, 10],
                ticktext=["", "2", "4", "6", "8", "10"],
            ),
            yaxis=dict(
                title='',
                tickfont=dict(size=16),
                ticks="outside",
                tickwidth=5,
                showgrid=True,
                showbackground=True,
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
                tickfont=dict(size=13),
                ticks="outside",
                showgrid=True,
                tickwidth=5,
                showbackground=True,
                linecolor="black",
                linewidth=5,
                showline=True,
                zeroline=False,
                mirror=True,
                tickmode="array",
                tickvals=[0, 20, 40, 60, 80, 100, 120, 140, 160],
                ticktext=["-100", "-80", "-60", "-40", "-20", "0", "+20", "+40", "+60", "+80"],
                range=[0, 180]
            ),
            annotations=[
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
                ),
                dict(
                    x=0.05,
                    y=0.02,
                    z=80,
                    textangle=-94,
                    text=z_label,
                    showarrow=False,
                    font=dict(size=25),
                    xanchor="right",
                    xshift=-60,
                    yanchor="middle",
                ),
                dict(
                    x=surface_1_x,
                    y=surface_1_y,
                    z=surface_1_z,
                    bgcolor="white",
                    bordercolor="black",
                    text=surface_1_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=50,
                    xanchor="left",
                ),
                dict(
                    x=surface_2_x,
                    y=surface_2_y,
                    z=surface_2_z,
                    bgcolor="white",
                    bordercolor="black",
                    text=surface_2_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=-50,
                    xanchor="left",
                ),
                dict(
                    x=surface_3_x,
                    y=surface_3_y,
                    z=surface_3_z,
                    bgcolor="white",
                    bordercolor="black",
                    text=surface_3_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=-20,
                    xanchor="left",
                ),
                dict(
                    x=surface_4_x,
                    y=surface_4_y,
                    z=surface_4_z,
                    bgcolor="white",
                    bordercolor="black",
                    text=surface_4_name,
                    font=dict(size=20),
                    arrowhead=6,
                    ax=70,
                    ay=25,
                    xanchor="left",
                ),
            ],
            camera=dict(
                center=dict(x=0, y=0, z=0),
                eye=dict(x=0.96, y=-1.12, z=0.26),
            ),
        ),
    )
