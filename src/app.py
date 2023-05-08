from dash import dash, dcc, html, Output, Input, State, callback_context
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from helpers_wrappers.surface_plot_creation import Plot, get_cam_data
from helpers_wrappers.data_store import PLOT_TITLES
from helpers_wrappers.dash_helpers import create_tab_content

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css]
app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    prevent_initial_callbacks="initial_duplicate"
)

fig_1 = Plot("25m@10s", "50m@10s", PLOT_TITLES["25m50m@10s"])
fig_2 = Plot("50m@15s", "25m@15s", PLOT_TITLES["25m50m@15s"])
fig_3 = Plot("25m@10s", "25m@15s", PLOT_TITLES["25m@10s15s"])
fig_4 = Plot("50m@10s", "50m@15s", PLOT_TITLES["50m@10s15s"])
figs = {
    "graph-1": fig_1.get_figure(),
    "graph-2": fig_2.get_figure(),
    "graph-3": fig_3.get_figure(),
    "graph-4": fig_4.get_figure(),
}

app.layout = dbc.Container(
    [
        html.H1("SEE Index Visualisations", className="text-primary text-center mb-3"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Label('Eye Coordinates:'),
                                        html.Div(
                                            [
                                                html.Label('x:'),
                                                dcc.Slider(
                                                    id='eye-x-slider',
                                                    min=-3,
                                                    max=3,
                                                    value=0.8,
                                                    step=0.01,
                                                    updatemode='drag',
                                                    marks={
                                                        "-3": "-3",
                                                        "-2": "-2",
                                                        "-1": "-1",
                                                        "0": "0",
                                                        "1": "1",
                                                        "2": "2",
                                                        "3": "3"
                                                    }
                                                ),
                                                dcc.Input(
                                                    id='eye-x-input',
                                                    type='number',
                                                    min=-3,
                                                    max=3,
                                                    value=0.8,
                                                    step=0.01
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Label('y:'),
                                                dcc.Slider(
                                                    id='eye-y-slider',
                                                    min=-3,
                                                    max=3,
                                                    value=-1.25,
                                                    step=0.01,
                                                    updatemode='drag',
                                                    marks={
                                                        "-3": "-3",
                                                        "-2": "-2",
                                                        "-1": "-1",
                                                        "0": "0",
                                                        "1": "1",
                                                        "2": "2",
                                                        "3": "3"
                                                    }
                                                ),
                                                dcc.Input(
                                                    id='eye-y-input',
                                                    type='number',
                                                    min=-3,
                                                    max=3,
                                                    value=-1.25,
                                                    step=0.01
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Label('z:'),
                                                dcc.Slider(
                                                    id='eye-z-slider',
                                                    min=-3,
                                                    max=3,
                                                    value=0.2,
                                                    step=0.01,
                                                    updatemode='drag',
                                                    marks={
                                                        "-3": "-3",
                                                        "-2": "-2",
                                                        "-1": "-1",
                                                        "0": "0",
                                                        "1": "1",
                                                        "2": "2",
                                                        "3": "3"
                                                    }
                                                ),
                                                dcc.Input(
                                                    id='eye-z-input',
                                                    type='number',
                                                    min=-3,
                                                    max=3,
                                                    value=0.2,
                                                    step=0.01
                                                ),
                                            ]
                                        ),
                                    ]
                                ),
                                html.Hr(),
                                html.Div(
                                    [
                                        html.Label('Center Coordinates:'),
                                        html.Div(
                                            [
                                                html.Label('x:'),
                                                dcc.Slider(
                                                    id='center-x-slider',
                                                    min=-3,
                                                    max=3,
                                                    value=0,
                                                    step=0.01,
                                                    updatemode='drag',
                                                    marks={
                                                        "-3": "-3",
                                                        "-2": "-2",
                                                        "-1": "-1",
                                                        "0": "0",
                                                        "1": "1",
                                                        "2": "2",
                                                        "3": "3"
                                                    },
                                                ),
                                                dcc.Input(
                                                    id='center-x-input',
                                                    type='number',
                                                    min=-3,
                                                    max=3,
                                                    value=0,
                                                    step=0.01
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Label('y:'),
                                                dcc.Slider(
                                                    id='center-y-slider',
                                                    min=-3,
                                                    max=3,
                                                    value=0,
                                                    step=0.01,
                                                    updatemode='drag',
                                                    marks={
                                                        "-3": "-3",
                                                        "-2": "-2",
                                                        "-1": "-1",
                                                        "0": "0",
                                                        "1": "1",
                                                        "2": "2",
                                                        "3": "3"
                                                    },
                                                ),
                                                dcc.Input(
                                                    id='center-y-input',
                                                    type='number',
                                                    min=-3,
                                                    max=3,
                                                    value=0,
                                                    step=0.01
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            [
                                                html.Label('z:'),
                                                dcc.Slider(
                                                    id='center-z-slider',
                                                    min=-3,
                                                    max=3,
                                                    value=0,
                                                    step=0.01,
                                                    updatemode='drag',
                                                    marks={
                                                        "-3": "-3",
                                                        "-2": "-2",
                                                        "-1": "-1",
                                                        "0": "0",
                                                        "1": "1",
                                                        "2": "2",
                                                        "3": "3"
                                                    },
                                                ),
                                                dcc.Input(
                                                    id='center-z-input',
                                                    type='number',
                                                    min=-3,
                                                    max=3,
                                                    value=0,
                                                    step=0.01
                                                ),
                                            ]
                                        ),
                                    ]
                                )
                            ],
                        ),
                    ], width=2
                ),

                dbc.Col(
                    [
                        dcc.Graph(
                            id="plot-window",
                            config={
                                "editable": True,
                                "edits": {
                                    "colorbarTitleText": False,
                                    "annotationText": False,
                                    "annotationPosition": True,
                                    "annotationTail": True,
                                    "titleText": True,
                                },
                                "showEditInChartStudio": True,
                                "plotlyServerURL": "https://chart-studio.plotly.com",
                                "responsive": True,
                                "toImageButtonOptions": {
                                    "format": "svg",  # one of png, svg, jpeg, webp

                                }
                            },
                        ),
                        html.Div(
                            [
                                html.Label("Select a plot to view:"),
                                dcc.Dropdown(
                                    id="graph-selector",
                                    options=[
                                        {
                                            "label": "Depth: 25m, 50m; Wave Period: 10s",
                                            "value": "graph-1"},
                                        {
                                            "label": "Depth: 25m, 50m; Wave Period: 15s",
                                            "value": "graph-2"},
                                        {
                                            "label": "Depth: 25m; Wave Period: 10s, 15s",
                                            "value": "graph-3"},
                                        {
                                            "label": "Depth: 50m; Wave Period: 10s, 15s",
                                            "value": "graph-4"},
                                    ],
                                    value="graph-1",
                                    clearable=False,
                                    style={"width": "50%"}
                                ),
                            ]
                        ),
                    ], width=7
                ),
                dbc.Col(
                    [
                        html.Label("X Axis Title:"),
                        html.Div(
                            [
                                html.Label("Annotation x:"),
                                dcc.Input(id="annotation-x-x", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation y:"),
                                dcc.Input(id="annotation-x-y", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),
                        # html.Div(
                        #     [
                        #         html.Label("Annotation z:"),
                        #         dcc.Input(id="annotation-x-z", type="number", value=0, step=0.1, ),
                        #     ]
                        # ),

                        html.Hr(),
                        html.Label("Font Size:"),
                        dcc.Input(id="annotation-x-font-size", type="number", value=25, step=1),
                        html.Hr(),
                        html.Span(
                            [
                                html.Div(
                                    [
                                        html.Label("X Anchor:"),
                                        dcc.RadioItems(
                                            id="annotation-x-xanchor", options=[
                                                {"label": "Left", "value": "left"},
                                                {"label": "Center", "value": "center"},
                                                {"label": "Right", "value": "right"},
                                            ], value="center"
                                        ),
                                    ]
                                ),
                                html.Div(
                                    [
                                        html.Label("Y Anchor:"),
                                        dcc.RadioItems(
                                            id="annotation-x-yanchor", options=[
                                                {"label": "Top", "value": "top"},
                                                {"label": "Middle", "value": "middle"},
                                                {"label": "Bottom", "value": "bottom"},
                                            ], value="middle"
                                        ),
                                    ]
                                ),
                            ], style={"display": "flex", "flex-direction": "row", "gap": "20px"}
                        ),
                        html.Hr(),
                        html.Div(
                            [
                                html.Label("X Shift: "),
                                dcc.Input(id="annotation-x-xshift", type="number", value=20,
                                    step=1),

                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Y Shift: "),
                                dcc.Input(id="annotation-x-yshift", type="number", value=-50,
                                    step=1),
                            ]
                        ),
                        html.Hr(),
                        html.Label("Text Angle:"),
                        dcc.Input(id="annotation-x-textangle", type="number", value=14, step=1),
                        html.Hr(),

                    ], width=1
                ),
                dbc.Col(
                    [
                        html.Label("Y Axis Title:"),
                        html.Div(
                            [
                                html.Label("Annotation x:"),
                                dcc.Input(id="annotation-y-x", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation y:"),
                                dcc.Input(id="annotation-y-y", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation z:"),
                                dcc.Input(id="annotation-y-z", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),

                        html.Hr(),
                        html.Label("Font Size:"),
                        dcc.Input(id="annotation-y-font-size", type="number", value=25, step=1),
                        html.Hr(),
                        html.Span(
                            [
                                html.Div(
                                    [
                                        html.Label("X Anchor:"),
                                        dcc.RadioItems(
                                            id="annotation-y-xanchor", options=[
                                                {"label": "Left", "value": "left"},
                                                {"label": "Center", "value": "center"},
                                                {"label": "Right", "value": "right"},
                                            ], value="center"
                                        ),
                                    ]
                                ),
                                html.Div(
                                    [
                                        html.Label("Y Anchor:"),
                                        dcc.RadioItems(
                                            id="annotation-y-yanchor", options=[
                                                {"label": "Top", "value": "top"},
                                                {"label": "Middle", "value": "middle"},
                                                {"label": "Bottom", "value": "bottom"},
                                            ], value="middle"
                                        ),
                                    ]
                                ),
                            ], style={"display": "flex", "flex-direction": "row", "gap": "20px"}
                        ),
                        html.Hr(),
                        html.Div(
                            [
                                html.Label("X Shift: "),
                                dcc.Input(id="annotation-y-xshift", type="number", value=75,
                                    step=1),

                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Y Shift: "),
                                dcc.Input(id="annotation-y-yshift", type="number", value=0, step=1),
                            ]
                        ),
                        html.Hr(),
                        html.Label("Text Angle:"),
                        dcc.Input(id="annotation-y-textangle", type="number", value=-60, step=1),
                        html.Hr(),

                    ], width=1
                ),
                dbc.Col(
                    [
                        html.Label("Z Axis Title:"),
                        html.Div(
                            [
                                html.Label("Annotation x:"),
                                dcc.Input(id="annotation-z-x", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation y:"),
                                dcc.Input(id="annotation-z-y", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation z:"),
                                dcc.Input(id="annotation-z-z", type="number", value=0.5,
                                    step=0.01, min=0, max=1),
                            ]
                        ),

                        html.Hr(),
                        html.Label("Font Size:"),
                        dcc.Input(id="annotation-z-font-size", type="number", value=25, step=1),
                        html.Hr(),
                        html.Span(
                            [
                                html.Div(
                                    [
                                        html.Label("X Anchor:"),
                                        dcc.RadioItems(
                                            id="annotation-z-xanchor", options=[
                                                {"label": "Left", "value": "left"},
                                                {"label": "Center", "value": "center"},
                                                {"label": "Right", "value": "right"},
                                            ], value="center"
                                        ),
                                    ]
                                ),
                                html.Div(
                                    [
                                        html.Label("Y Anchor:"),
                                        dcc.RadioItems(
                                            id="annotation-z-yanchor", options=[
                                                {"label": "Top", "value": "top"},
                                                {"label": "Middle", "value": "middle"},
                                                {"label": "Bottom", "value": "bottom"},
                                            ], value="middle"
                                        ),
                                    ]
                                ),
                            ], style={"display": "flex", "flex-direction": "row", "gap": "20px"}
                        ),
                        html.Hr(),
                        html.Div(
                            [
                                html.Label("X Shift: "),
                                dcc.Input(id="annotation-z-xshift", type="number", value=-50,
                                    step=1),

                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Y Shift: "),
                                dcc.Input(id="annotation-z-yshift", type="number", value=0, step=1),
                            ]
                        ),
                        html.Hr(),
                        html.Label("Text Angle:"),
                        dcc.Input(id="annotation-z-textangle", type="number", value=-90, step=1),
                        html.Hr(),

                    ], width=1
                )
            ],
        ),
    ], fluid=True
)


# Sync the eye x input and slider
@app.callback(
    Output("eye-x-input", "value", allow_duplicate=True),
    Output("eye-x-slider", "value", allow_duplicate=True),
    Input("eye-x-input", "value"),
    Input("eye-x-slider", "value"),
)
def sync_eye_x(input_value, slider_value):
    ctx = callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if input_id == "eye-x-input":
            return input_value, input_value
        elif input_id == "eye-x-slider":
            return slider_value, slider_value
    return input_value, slider_value


# Sync the eye y input and slider
@app.callback(
    Output("eye-y-input", "value", allow_duplicate=True),
    Output("eye-y-slider", "value", allow_duplicate=True),
    Input("eye-y-input", "value"),
    Input("eye-y-slider", "value"),
)
def sync_eye_y(input_value, slider_value):
    ctx = callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if input_id == "eye-y-input":
            return input_value, input_value
        elif input_id == "eye-y-slider":
            return slider_value, slider_value
    return input_value, slider_value


# Sync the eye z input and slider
@app.callback(
    Output("eye-z-input", "value", allow_duplicate=True),
    Output("eye-z-slider", "value", allow_duplicate=True),
    Input("eye-z-input", "value"),
    Input("eye-z-slider", "value"),
)
def sync_eye_z(input_value, slider_value):
    ctx = callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if input_id == "eye-z-input":
            return input_value, input_value
        elif input_id == "eye-z-slider":
            return slider_value, slider_value
    return input_value, slider_value


# Sync the center x input and slider
@app.callback(
    Output("center-x-input", "value", allow_duplicate=True),
    Output("center-x-slider", "value", allow_duplicate=True),
    Input("center-x-input", "value"),
    Input("center-x-slider", "value"),
)
def sync_center_x(input_value, slider_value):
    ctx = callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if input_id == "center-x-input":
            return input_value, input_value
        elif input_id == "center-x-slider":
            return slider_value, slider_value
    return input_value, slider_value


# Sync the center y input and slider
@app.callback(
    Output("center-y-input", "value", allow_duplicate=True),
    Output("center-y-slider", "value", allow_duplicate=True),
    Input("center-y-input", "value"),
    Input("center-y-slider", "value"),
)
def sync_center_y(input_value, slider_value):
    ctx = callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if input_id == "center-y-input":
            return input_value, input_value
        elif input_id == "center-y-slider":
            return slider_value, slider_value
    return input_value, slider_value


# Sync the center z input and slider
@app.callback(
    Output("center-z-input", "value", allow_duplicate=True),
    Output("center-z-slider", "value", allow_duplicate=True),
    Input("center-z-input", "value"),
    Input("center-z-slider", "value"),
)
def sync_center_z(input_value, slider_value):
    ctx = callback_context
    if ctx.triggered:
        input_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if input_id == "center-z-input":
            return input_value, input_value
        elif input_id == "center-z-slider":
            return slider_value, slider_value
    return input_value, slider_value


# Update sliders and inputs whenever camera is moved by dragging the plot
@app.callback(
    [
        Output("eye-x-input", "value", allow_duplicate=True),
        Output("eye-x-slider", "value", allow_duplicate=True),
        Output("eye-y-input", "value", allow_duplicate=True),
        Output("eye-y-slider", "value", allow_duplicate=True),
        Output("eye-z-input", "value", allow_duplicate=True),
        Output("eye-z-slider", "value", allow_duplicate=True),
        Output("center-x-input", "value", allow_duplicate=True),
        Output("center-x-slider", "value", allow_duplicate=True),
        Output("center-y-input", "value", allow_duplicate=True),
        Output("center-y-slider", "value", allow_duplicate=True),
        Output("center-z-input", "value", allow_duplicate=True),
        Output("center-z-slider", "value", allow_duplicate=True),
    ],
    Input("plot-window", "relayoutData"),
)
def update_camera_coordinates(relayout_data):
    if relayout_data is None or "scene.camera" not in relayout_data:
        raise PreventUpdate

    camera_data = relayout_data["scene.camera"]
    eye_x = camera_data["eye"]["x"]
    eye_y = camera_data["eye"]["y"]
    eye_z = camera_data["eye"]["z"]
    center_x = camera_data["center"]["x"]
    center_y = camera_data["center"]["y"]
    center_z = camera_data["center"]["z"]

    return (
        eye_x, eye_x,
        eye_y, eye_y,
        eye_z, eye_z,
        center_x, center_x,
        center_y, center_y,
        center_z, center_z,
    )


@app.callback(
    Output("plot-window", "figure"),
    [
        Input("graph-selector", "value"),
        Input("annotation-x-x", "value"),
        Input("annotation-x-y", "value"),
        # Input("annotation-x-z", "value"),
        Input("annotation-x-font-size", "value"),
        Input("annotation-x-xanchor", "value"),
        Input("annotation-x-yanchor", "value"),
        Input("annotation-x-xshift", "value"),
        Input("annotation-x-yshift", "value"),
        Input("annotation-x-textangle", "value"),
        Input("annotation-y-x", "value"),
        Input("annotation-y-y", "value"),
        # Input("annotation-y-z", "value"),
        Input("annotation-y-font-size", "value"),
        Input("annotation-y-xanchor", "value"),
        Input("annotation-y-yanchor", "value"),
        Input("annotation-y-xshift", "value"),
        Input("annotation-y-yshift", "value"),
        Input("annotation-y-textangle", "value"),
        Input("annotation-z-x", "value"),
        Input("annotation-z-y", "value"),
        # Input("annotation-z-z", "value"),
        Input("annotation-z-font-size", "value"),
        Input("annotation-z-xanchor", "value"),
        Input("annotation-z-yanchor", "value"),
        Input("annotation-z-xshift", "value"),
        Input("annotation-z-yshift", "value"),
        Input("annotation-z-textangle", "value"),
    ],
)
def update_annotation_pos(
        graph_selector,
        annotation_x_x,
        annotation_x_y,
        # annotation_x_z,
        annotation_x_font_size,
        annotation_x_xanchor,
        annotation_x_yanchor,
        annotation_x_xshift,
        annotation_x_yshift,
        annotation_x_textangle,
        annotation_y_x,
        annotation_y_y,
        # annotation_y_z,
        annotation_y_font_size,
        annotation_y_xanchor,
        annotation_y_yanchor,
        annotation_y_xshift,
        annotation_y_yshift,
        annotation_y_textangle,
        annotation_z_x,
        annotation_z_y,
        # annotation_z_z,
        annotation_z_font_size,
        annotation_z_xanchor,
        annotation_z_yanchor,
        annotation_z_xshift,
        annotation_z_yshift,
        annotation_z_textangle,
):
    annotations = [
        dict(
            text="X Axis",
            x=annotation_x_x,
            y=annotation_x_y,
            # z=annotation_x_z,
            font=dict(size=annotation_x_font_size),
            xshift=annotation_x_xshift,
            yshift=annotation_x_yshift,
            textangle=annotation_x_textangle,
            xanchor=annotation_x_xanchor,
            yanchor=annotation_x_yanchor,
        ),
        dict(
            text="Y Axis",
            x=annotation_y_x,
            y=annotation_y_y,
            # z=annotation_y_z,
            font=dict(size=annotation_y_font_size),
            xshift=annotation_y_xshift,
            yshift=annotation_y_yshift,
            textangle=annotation_y_textangle,
            xanchor=annotation_y_xanchor,
            yanchor=annotation_y_yanchor,
        ),
        dict(
            text="Z Axis",
            x=annotation_z_x,
            y=annotation_z_y,
            # z=annotation_z_z,
            font=dict(size=annotation_z_font_size),
            xshift=annotation_z_xshift,
            yshift=annotation_z_yshift,
            textangle=annotation_z_textangle,
            xanchor=annotation_z_xanchor,
            yanchor=annotation_z_yanchor,
        ),
    ]

    fig = figs[graph_selector]
    fig.update_layout(annotations=annotations)

    return fig


# Update the plot based on the sliders and input boxes
@app.callback(
    Output('plot-window', 'figure', allow_duplicate=True),
    [
        Input("graph-selector", "value"),
        Input('eye-x-input', 'value'),
        Input('eye-x-slider', 'value'),
        Input('eye-y-input', 'value'),
        Input('eye-y-slider', 'value'),
        Input('eye-z-input', 'value'),
        Input('eye-z-slider', 'value'),
        Input('center-x-input', 'value'),
        Input('center-x-slider', 'value'),
        Input('center-y-input', 'value'),
        Input('center-y-slider', 'value'),
        Input('center-z-input', 'value'),
        Input('center-z-slider', 'value'),
    ]
)
def update_figure(
        graph_selector,
        eye_x_input,
        eye_x_slider,
        eye_y_input,
        eye_y_slider,
        eye_z_input,
        eye_z_slider,
        center_x_input,
        center_x_slider,
        center_y_input,
        center_y_slider,
        center_z_input,
        center_z_slider
):
    eye_x = eye_x_input if eye_x_input is not None else eye_x_slider
    eye_y = eye_y_input if eye_y_input is not None else eye_y_slider
    eye_z = eye_z_input if eye_z_input is not None else eye_z_slider
    center_x = center_x_input if center_x_input is not None else center_x_slider
    center_y = center_y_input if center_y_input is not None else center_y_slider
    center_z = center_z_input if center_z_input is not None else center_z_slider

    fig = figs[graph_selector]
    fig.update_layout(
        autosize=True,

        scene=dict(
            camera=dict(
                eye=dict(x=eye_x, y=eye_y, z=eye_z),
                center=dict(x=center_x, y=center_y, z=center_z)
            )
        )
    )
    return fig


@app.callback(
    Output('plot-window', 'figure', allow_duplicate=True),
    Input("graph-selector", "value"),
)
def select_graph(graph):
    return figs[graph]


if __name__ == '__main__':
    app.run(debug=True)
