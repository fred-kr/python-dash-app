from dash import dash, dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

from helpers_wrappers.surface_plot_creation import Plot, get_cam_data
from helpers_wrappers.data_store import PLOT_TITLES
from helpers_wrappers.dash_helpers import create_tab_content

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
        dcc.Store(id="store", data=figs),
        html.H1("SEE Index Visualisations", className="text-primary text-center mb-3"), html.Hr(),
        dbc.Button("Reset Graphs", color="primary", className="mb-3", id="reset-button"), dbc.Tabs(
        [
            dbc.Tab(
                label="Plot 1", tab_id="tab-graph-1", ),
            dbc.Tab(
                label="Plot 2", tab_id="tab-graph-2", ),
            dbc.Tab(
                label="Plot 3", tab_id="tab-graph-3", ),
            dbc.Tab(
                label="Plot 4", tab_id="tab-graph-4", ),
            dbc.Tab(
                label="Side-by-Side (2)",
                tab_id="tab-side-by-side_2",
                children=[
                    html.Label("Select layout for 2 graphs:", className="mt-3"),
                    dcc.RadioItems(
                        id="layout-radio",
                        options=[
                            {"label": "Horizontal", "value": "horizontal"},
                            {"label": "Vertical", "value": "vertical"},
                        ],
                        value="horizontal",
                    ),
                ]
            ),
            dbc.Tab(
                label="2x2 Grid", tab_id="tab-grid_2x2"
            )
        ],
            id="tabs",
            active_tab="tab-graph-1"
        ),
        html.Div(id="tab-content", className="p-4"),
    ], fluid=True
)


@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data"), Input("layout-radio", "value")],
)
def render_tab_content(active_tab, data, layout):
    return create_tab_content(active_tab, data)


@app.callback(
    [Output("graph-1", "figure")],
    [Input("dropdown-1", "value")]
)
def update_graphs(selected_value):
    if selected_value is None:
        raise PreventUpdate
    return figs[selected_value]


if __name__ == '__main__':
    app.run(debug=True)
