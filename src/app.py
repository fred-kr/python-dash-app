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
server = app.server

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
                        html.Div(id="cam-output"),
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
                    ], width=6
                ),
                dbc.Col(
                    [
                        html.Label("X Axis Title:"),
                        html.Div(
                            [
                                html.Label("Annotation x:"),
                                dcc.Input(id="annotation-x-x", type="number", value=3,
                                    step=0.01, min=0, max=10),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation y:"),
                                dcc.Input(id="annotation-x-y", type="number", value=0.45,
                                    step=0.01, min=0, max=1.5),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation z:"),
                                dcc.Input(id="annotation-x-z", type="number", value=0, step=0.1,
                                    max=14),
                            ]
                        ),

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
                                            ], value="top"
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
                                dcc.Input(id="annotation-x-yshift", type="number", value=-85,
                                    step=1),
                            ]
                        ),
                        html.Hr(),
                        html.Label("Text Angle:"),
                        dcc.Input(id="annotation-x-textangle", type="number", value=22, step=1),
                        html.Hr(),

                    ], width=1
                ),
                dbc.Col(
                    [
                        html.Label("Y Axis Title:"),
                        html.Div(
                            [
                                html.Label("Annotation x:"),
                                dcc.Input(id="annotation-y-x", type="number", value=9.8,
                                    step=0.01, min=0, max=10),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation y:"),
                                dcc.Input(id="annotation-y-y", type="number", value=0.25,
                                    step=0.01, min=0, max=1.5),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation z:"),
                                dcc.Input(id="annotation-y-z", type="number", value=0,
                                    step=0.01, min=0, max=14),
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
                                            ], value="left"
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
                                dcc.Input(id="annotation-y-xshift", type="number", value=78,
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
                        dcc.Input(id="annotation-y-textangle", type="number", value=-43, step=1),
                        html.Hr(),

                    ], width=1
                ),
                dbc.Col(
                    [
                        html.Label("Z Axis Title:"),
                        html.Div(
                            [
                                html.Label("Annotation x:"),
                                dcc.Input(id="annotation-z-x", type="number", value=0.05,
                                    step=0.01, min=0, max=10),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation y:"),
                                dcc.Input(id="annotation-z-y", type="number", value=0.02,
                                    step=0.01, min=0, max=1.5),
                            ]
                        ),
                        html.Div(
                            [
                                html.Label("Annotation z:"),
                                dcc.Input(id="annotation-z-z", type="number", value=7,
                                    step=0.01, min=0, max=14),
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
                                            ], value="right"
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
                                dcc.Input(id="annotation-z-xshift", type="number", value=-60,
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
                        dcc.Input(id="annotation-z-textangle", type="number", value=-94, step=1),
                        html.Hr(),

                    ], width=1
                )
            ],
        ),
    ], fluid=True
)


@app.callback(
    Output("cam-output", "children"),
    Input("plot-window", "relayoutData"),
)
def update_camera_output(relayout_data):
    return get_cam_data(relayout_data, "main")


@app.callback(
    Output("plot-window", "figure"),
    [
        Input("graph-selector", "value"),
        Input("annotation-x-x", "value"),
        Input("annotation-x-y", "value"),
        Input("annotation-x-z", "value"),
        Input("annotation-x-font-size", "value"),
        Input("annotation-x-xanchor", "value"),
        Input("annotation-x-yanchor", "value"),
        Input("annotation-x-xshift", "value"),
        Input("annotation-x-yshift", "value"),
        Input("annotation-x-textangle", "value"),
        Input("annotation-y-x", "value"),
        Input("annotation-y-y", "value"),
        Input("annotation-y-z", "value"),
        Input("annotation-y-font-size", "value"),
        Input("annotation-y-xanchor", "value"),
        Input("annotation-y-yanchor", "value"),
        Input("annotation-y-xshift", "value"),
        Input("annotation-y-yshift", "value"),
        Input("annotation-y-textangle", "value"),
        Input("annotation-z-x", "value"),
        Input("annotation-z-y", "value"),
        Input("annotation-z-z", "value"),
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
        annotation_x_z,
        annotation_x_font_size,
        annotation_x_xanchor,
        annotation_x_yanchor,
        annotation_x_xshift,
        annotation_x_yshift,
        annotation_x_textangle,
        annotation_y_x,
        annotation_y_y,
        annotation_y_z,
        annotation_y_font_size,
        annotation_y_xanchor,
        annotation_y_yanchor,
        annotation_y_xshift,
        annotation_y_yshift,
        annotation_y_textangle,
        annotation_z_x,
        annotation_z_y,
        annotation_z_z,
        annotation_z_font_size,
        annotation_z_xanchor,
        annotation_z_yanchor,
        annotation_z_xshift,
        annotation_z_yshift,
        annotation_z_textangle,
):
    annotations = [
        dict(
            x=annotation_x_x,
            y=annotation_x_y,
            z=annotation_x_z,
            font=dict(size=annotation_x_font_size),
            xshift=annotation_x_xshift,
            yshift=annotation_x_yshift,
            textangle=annotation_x_textangle,
            xanchor=annotation_x_xanchor,
            yanchor=annotation_x_yanchor,
        ),
        dict(
            x=annotation_y_x,
            y=annotation_y_y,
            z=annotation_y_z,
            font=dict(size=annotation_y_font_size),
            xshift=annotation_y_xshift,
            yshift=annotation_y_yshift,
            textangle=annotation_y_textangle,
            xanchor=annotation_y_xanchor,
            yanchor=annotation_y_yanchor,
        ),
        dict(
            x=annotation_z_x,
            y=annotation_z_y,
            z=annotation_z_z,
            font=dict(size=annotation_z_font_size),
            xshift=annotation_z_xshift,
            yshift=annotation_z_yshift,
            textangle=annotation_z_textangle,
            xanchor=annotation_z_xanchor,
            yanchor=annotation_z_yanchor,
        ),
        dict(),
        dict()
    ]

    fig = figs[graph_selector]
    fig.update_layout(
        scene=dict(annotations=annotations),
        uirevision=graph_selector,
        overwrite=False,

    )

    return fig


@app.callback(
    Output('plot-window', 'figure', allow_duplicate=True),
    Input("graph-selector", "value"),
)
def select_graph(graph):
    fig = figs[graph]
    fig.update_layout(
        uirevision=graph,
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
