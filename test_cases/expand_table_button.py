

import dash
from dash import html
from dash.dependencies import Input, Output, State, ALL, MATCH

app = dash.Dash(__name__, external_stylesheets=["/assets/styles.css"], suppress_callback_exceptions=True)

def generate_outer_tables():
    # Define the number of outer tables
    num_outer_tables = 10

    # Generate the layout for the outer tables dynamically
    outer_tables = []
    for i in range(num_outer_tables):
        outer_tables.append(
            html.Table(
                [
                    html.Tr(
                        [
                            html.Td( html.Button("+", id={"type": "toggle-button", "index": i+1},
                                            className="toggle-button")  ),
                            html.Td(f"Outer Table {i+1} Cell 2"),
                            html.Td(f"Outer Table {i+1} Cell 3"),
                        ]
                    ),
                    html.Tr(
                        [
                            html.Td(
                                html.Table(
                                    [
                                        html.Tr(
                                            [
                                                html.Td(f"Inner Table {i+1} Cell 1"),
                                                html.Td(f"Inner Table {i+1} Cell 2"),
                                                html.Td(f"Inner Table {i+1} Cell 3"),
                                            ]
                                        ),
                                        html.Tr(
                                            [
                                                html.Td(f"Inner Table {i+1} Cell 4"),
                                                html.Td(f"Inner Table {i+1} Cell 5"),
                                                html.Td(f"Inner Table {i+1} Cell 6"),
                                            ]
                                        ),
                                    ],
                                    id={"type": "inner-table", "index": i+1},
                                    className="inner-table",
                                    style={"display": "none"},
                                ),
                                colSpan=3,
                            )
                        ]
                    ),
                ],
                id={"type": "outer-table", "index": i+1},
            )
        )

    return html.Div(outer_tables)

app.layout = generate_outer_tables


@app.callback(
    Output({"type": "inner-table", "index": MATCH}, "style"),
    Output({"type": "toggle-button", "index": MATCH}, "children"),
    Input({"type": "toggle-button", "index": MATCH}, "n_clicks"),
    State({"type": "inner-table", "index": MATCH}, "style"),
    prevent_initial_callback=True
)
def toggle_inner_table(n_clicks, style):
    button_text = "+"
    if n_clicks: 
        if style["display"] == "table":
            style["display"] = "none"
        else:
            style["display"] = "table"
            button_text = "-"

    return style, button_text

if __name__ == "__main__":
    app.run_server(debug=True)
