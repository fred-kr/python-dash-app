import dash_bootstrap_components as dbc
from dash import dash, dcc, html, Input, Output, State


def create_dropdown(id):
    """
    Dropdown menu to append to plot window to select which surface to display
    Args:
        id (str): id of the dropdown menu

    Returns: A `dcc.Dropdown` with the id `id` and options for the four different combinations of
    surfaces

    """
    return dcc.Dropdown(
        id=id,
        options=[
            {"label": "Depth: 25m, 50m; Wave Period: 10s", "value": "graph-1"},
            {"label": "Depth: 25m, 50m; Wave Period: 15s", "value": "graph-2"},
            {"label": "Depth: 25m; Wave Period: 10s, 15s", "value": "graph-3"},
            {"label": "Depth: 50m; Wave Period: 10s, 15s", "value": "graph-4"},
        ],
        value=id.split('-')[-1],
    )


def create_graph(id, figure):
    return dcc.Graph(
        responsive="auto",
        config=dict(
            editable=True,
            editSelection=True,
            edits=dict(colorbarTitleText=False),
            showTips=True,
            showLink=True,
            plotlyServerURL="https://chart-studio.plotly.com",
        ),
        id=id,
        figure=figure,
    )


def create_tab_content(active_tab, data, layout):
    if active_tab and data is not None:
        if active_tab.startswith("tab-graph"):
            graph_id = active_tab.split('-')[-1]
            return html.Div([
                create_dropdown(f"graph-selector-{graph_id}"),
                create_graph(f"graph-{graph_id}", data[f"graph-{graph_id}"])
            ])
        elif active_tab.startswith("tab-side-by-side_2") and layout == "horizontal":
            return dbc.Row([
                dbc.Col([
                    create_dropdown(f"graph-selector-side-by-side-{layout}-1"),
                    create_graph(f"graph-side-by-side-{layout}-1", data["graph-1"])
                ], width=6),
                dbc.Col([
                    create_dropdown(f"graph-selector-side-by-side-{layout}-2"),
                    create_graph(f"graph-side-by-side-{layout}-2", data["graph-3"])
                ], width=6),
            ])
        elif active_tab.startswith("tab-side-by-side_2") and layout == "vertical":
            return dbc.Row(
                [
                    dbc.Col(
                        [
                            create_dropdown(
                                f"graph-selector-side-by-side-{layout}-1"
                            ),
                            create_graph("graph-1", data["graph-1"]),
                            create_dropdown(
                                f"graph-selector-side-by-side-{layout}-2"
                            ),
                            create_graph("graph-3", data["graph-3"]),
                        ],
                        width=12,
                    )
                ]
            )
        elif active_tab == "tab-grid_2x2":
            return html.Div([
                dbc.Row([
                    dbc.Col(create_graph("graph-1", data["graph-1"]), width=6),
                    dbc.Col(create_graph("graph-2", data["graph-2"]), width=6),
                ]),
                dbc.Row([
                    dbc.Col(create_graph("graph-3", data["graph-3"]), width=6),
                    dbc.Col(create_graph("graph-4", data["graph-4"]), width=6),
                ]),
            ])

    return "No tab selected"


# html.Label("Select layout for 2 graphs:", className="mt-3"),
# dcc.RadioItems(
#     id="layout-radio",
#     options=[
#         {"label": "Horizontal", "value": "horizontal"},
#         {"label": "Vertical", "value": "vertical"},
#     ],
#     value="horizontal",
# ),
