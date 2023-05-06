from dash import dash_table, html
from .plotly_helpers import create_surface, create_layout
from .surface import SURFACE_PROPERTIES
from .data_store import AXIS_TITLES
import plotly.graph_objects as go


def get_cam_data(cam_data: dict, input_graph: str):
    """
    The get_cam_data function takes in the camera data and input graph name, and returns a table
    of the camera properties. The function first checks if the cam_data is None or does not
    contain `scene.camera`. If so, it returns a string explaining that you need to interact
    with the graph to see its properties. Otherwise, it creates an empty list called
    data and a dictionary called data_dict containing keys for each axis (x, y, z) as well as eye
    and center values. It then loops through each key in `[eye, center]` which are sub-keys of scene.

    Args:
        cam_data (dict): `relayoutData` property of a plotly figure
        input_graph (str): Name of input graph, just used for the id of the table

    Returns:
        An `html.Div` containing a `dash_table.DataTable` with the `eye` and `center` values
    """
    if cam_data is None or "scene.camera" not in cam_data:
        return "Interact with the graph to see camera properties"

    camera_data = cam_data["scene.camera"]
    data = []

    data_dict = {'Axis': ['x', 'y', 'z'], 'Eye': [None, None, None], 'Center': [None, None, None]}

    for key in ["eye", "center"]:
        if key in camera_data:
            sub_dict = camera_data[key]
            for i, sub_key in enumerate(['x', 'y', 'z']):
                value = sub_dict.get(sub_key, None)
                data_dict[key.capitalize()][i] = value

    # Convert data dict to list of dicts
    data = [dict(zip(data_dict.keys(), values)) for values in zip(*data_dict.values())]

    return html.Div([
        dash_table.DataTable(
            id=f"{input_graph}-cam-properties",
            columns=[
                {"name": "Axis", "id": "Axis"},
                {"name": "Eye (Viewing Angle)", "id": "Eye"},
                {"name": "Center", "id": "Center"},
            ],
            data=data,
            style_cell={"textAlign": "left"},
            style_header={
                "backgroundColor": "rgb(230, 230, 230)",
                "fontWeight": "bold"
            },
            style_table={"width": "25%"},
        )
    ])


class Plot:
    def __init__(self, surface_1_key: str, surface_2_key: str, plot_title: str) -> None:
        self.layout = create_layout(
            title=plot_title,
            x_label=AXIS_TITLES[0],
            y_label=AXIS_TITLES[1],
            z_label=AXIS_TITLES[2]
        )
        # Given surface with the higher max z value will get opacity set to 0.75 and show_colorbar set to True
        max_z_1 = SURFACE_PROPERTIES[surface_1_key]["surface"]["z"].max()
        max_z_2 = SURFACE_PROPERTIES[surface_2_key]["surface"]["z"].max()

        def create_surface_with_properties(surface_key, opacity=None, show_colorbar=False):
            surface_properties = SURFACE_PROPERTIES[surface_key]
            surface = surface_properties["surface"]
            x, y, z = surface["x"], surface["y"], surface["z"]
            colorscale = surface_properties["colorscale"]
            n_colors = surface_properties["n_colors"]

            return create_surface(x, y, z, colorscale, n_colors, opacity=opacity, show_colorbar=show_colorbar)

        if max_z_1 > max_z_2:
            self.surface_1 = create_surface_with_properties(surface_1_key, opacity=0.75, show_colorbar=True)
            self.surface_2 = create_surface_with_properties(surface_2_key)
        else:
            self.surface_1 = create_surface_with_properties(surface_1_key)
            self.surface_2 = create_surface_with_properties(surface_2_key, opacity=0.75, show_colorbar=True)

        # TODO: add parameters for annotation position for interactive positioning

    def get_figure(self) -> go.Figure:
        return go.Figure(data=[self.surface_1, self.surface_2], layout=self.layout)
