from dash import dash_table, \
    html
from .plotly_helpers import create_surface, \
    create_layout, \
    create_diff_layout
from .data_store import AXIS_TITLES, \
    SURFACE_PROPERTIES, \
    DIFF_SURFACES
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_cam_data(
        cam_data: dict,
        input_graph: str
):
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

    data_dict = {
        'Axis': ['x', 'y', 'z'],
        'Eye': [None, None, None],
        'Center': [None, None, None]}

    for key in ["eye", "center"]:
        if key in camera_data:
            sub_dict = camera_data[key]
            for i, sub_key in enumerate(
                    ['x', 'y', 'z']
            ):
                value = sub_dict.get(
                    sub_key,
                    None
                )
                data_dict[key.capitalize()][i] = value

    # Convert data dict to list of dicts
    data = [dict(
        zip(
            data_dict.keys(),
            values
        )
    ) for values in zip(
        *data_dict.values()
    )]

    return html.Div(
        [
            dash_table.DataTable(
                id=f"{input_graph}-cam-properties",
                columns=[
                    {
                        "name": "Axis",
                        "id": "Axis"},
                    {
                        "name": "Eye (Viewing Angle)",
                        "id": "Eye"},
                    {
                        "name": "Center",
                        "id": "Center"},
                ],
                data=data,
                style_cell={
                    "textAlign": "left"},
                style_header={
                    "backgroundColor": "rgb(230, 230, 230)",
                    "fontWeight": "bold"
                },
                style_table={
                    "width": "25%"},
            )
        ]
    )


class Plot:
    def __init__(
            self,
            surface_1_name: str,
            surface_1_key: str,
            surface_2_name: str,
            surface_2_key:
            str,
            plot_title: str
    ) -> None:
        self.layout = create_layout(
            title=plot_title,
            x_label=AXIS_TITLES[0],
            y_label=AXIS_TITLES[1],
            z_label=AXIS_TITLES[2],
            surface_1_name=surface_1_name,
            surface_2_name=surface_2_name,
            surface_1=SURFACE_PROPERTIES[surface_1_key]["surface"],
            surface_2=SURFACE_PROPERTIES[surface_2_key]["surface"],
        )
        # Given surface with the higher max z value will get opacity set to 0.75 and
        # show_colorbar set to True
        max_z_1 = SURFACE_PROPERTIES[surface_1_key]["surface"]["z"].max()
        max_z_2 = SURFACE_PROPERTIES[surface_2_key]["surface"]["z"].max()

        def create_surface_with_properties(
                surface_key,
                opacity=None,
                show_colorbar=False,
                ambient_light=0.8
        ):
            surface_properties = SURFACE_PROPERTIES[surface_key]
            surface = surface_properties["surface"]
            x, y, z = surface["x"], surface["y"], surface["z"]
            colorscale = surface_properties["colorscale"]
            n_colors = surface_properties["n_colors"]

            return create_surface(
                x,
                y,
                z,
                colorscale,
                n_colors,
                opacity=opacity,
                show_colorbar=show_colorbar,
                ambient_light=ambient_light
            )

        if max_z_1 > max_z_2:
            self.surface_1 = create_surface_with_properties(
                surface_1_key,
                opacity=0.8,
                show_colorbar=True,
                ambient_light=0.5
            )
            self.surface_2 = create_surface_with_properties(
                surface_2_key
            )
        else:
            self.surface_1 = create_surface_with_properties(
                surface_1_key
            )
            self.surface_2 = create_surface_with_properties(
                surface_2_key,
                opacity=0.8,
                show_colorbar=True,
                ambient_light=0.5
            )

    def get_figure(
            self
    ) -> go.Figure:
        return go.Figure(
            data=[self.surface_1, self.surface_2],
            layout=self.layout
        )


def create_diff_surface(
        x,
        y,
        z,
        showscale=False
):
    return go.Surface(
        x=x,
        y=y,
        z=z,
        colorscale="RdBu_r",
        showscale=showscale,
        colorbar=dict(
            orientation="v",
            y=0.5,
            x=0.1,
            len=0.5,
            xanchor="center",
        ),
        contours=dict(
            x=dict(
                show=True,
                start=0,
                end=10,
                size=2,
                color="black",
                width=5
            ),
            y=dict(
                show=True,
                start=0,
                end=1.5,
                size=0.5,
                color="black",
                width=5
            ),
        ),
    )


class DiffPlot:
    def __init__(
            self,
            surface_1: str,
            surface_1_name: str,
            surface_2: str,
            surface_2_name: str,
            surface_3: str,
            surface_3_name: str,
            surface_4: str,
            surface_4_name: str,
    ) -> None:
        self.layout = create_diff_layout(

            title="%-Difference between the four surfaces, using 50m at 15s wave period as "
                  "reference",
            x_label=AXIS_TITLES[0],
            y_label=AXIS_TITLES[1],
            z_label="Difference [%]",
            surface_1_name=surface_1_name,
            surface_1=DIFF_SURFACES[surface_1],
            surface_2_name=surface_2_name,
            surface_2=DIFF_SURFACES[surface_2],
            surface_3_name=surface_3_name,
            surface_3=DIFF_SURFACES[surface_3],
            surface_4_name=surface_4_name,
            surface_4=DIFF_SURFACES[surface_4],
        )
        self.surfaces = [
            create_diff_surface(
                DIFF_SURFACES[surface_1]["x"],
                DIFF_SURFACES[surface_1]["y"],
                DIFF_SURFACES[surface_1]["z"],

            ),
            create_diff_surface(
                DIFF_SURFACES[surface_2]["x"],
                DIFF_SURFACES[surface_2]["y"],
                DIFF_SURFACES[surface_2]["z"],
                showscale=True,
            ),
            create_diff_surface(
                DIFF_SURFACES[surface_3]["x"],
                DIFF_SURFACES[surface_3]["y"],
                DIFF_SURFACES[surface_3]["z"],
            ),
            create_diff_surface(
                DIFF_SURFACES[surface_4]["x"],
                DIFF_SURFACES[surface_4]["y"],
                DIFF_SURFACES[surface_4]["z"],
            ),

        ]

    def get_figure(
            self
    ) -> go.Figure:
        return go.Figure(
            data=self.surfaces,
            layout=self.layout
        )

    def get_subplot(
            self
    ) -> go.Figure:
        fig = make_subplots(
            rows=2,
            cols=2,
            specs=[[{
                "type": "scene"}, {
                "type": "scene"}],
                [{
                    "type": "scene"}, {
                    "type": "scene"}]],
        )
        fig.add_trace(
            self.surfaces[0],
            row=1,
            col=1
        )
        fig.add_trace(
            self.surfaces[1],
            row=1,
            col=2
        )
        fig.add_trace(
            self.surfaces[2],
            row=2,
            col=1
        )
        fig.add_trace(
            self.surfaces[3],
            row=2,
            col=2
        )
        return fig
