
# community example: with AG Grid
# Note, This is enterprised license feature, can run but will have water mark
#
#  https://community.plotly.com/t/dash-ag-grid-grouped-rows-rendering-selection-boxes-to-leaf-nodes/74920
#
import dash_ag_grid as dag
import dash
from dash import html, dcc
import pandas as pd


app = dash.Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    # Row group by country and by year is enabled.
    {"field": "country", "sortable": True, "filter": True, "rowGroup": True, "hide": True},
    {"field": "year", "sortable": True, "filter": True, "rowGroup": True, "hide": True},
    {"field": "athlete", "sortable": True, "filter": True, 
     "cellRendererParams": {
                        "checkbox": True,
                    },
     "cellRenderer": "agGroupCellRenderer"
     },
    {"field": "age", "sortable": True, "filter": True},
    {"field": "date", "sortable": True, "filter": True},
    {"field": "sport", "sortable": True, "filter": True},
    {"field": "total", "sortable": True, "filter": True},
]

app.layout = html.Div(
    [
        dcc.Markdown("Demonstration of row groupings in a Dash AG Grid."),
        dcc.Markdown("This grid groups first by country and then by year."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            dashGridOptions={
                "autoGroupColumnDef": {
                    "cellRenderer": "agGroupCellRenderer",
                    "cellRendererParams": {
                        "checkbox": True,
                    },
                    "headerCheckboxSelection": True,
                },
                "rowSelection": "multiple",
                "groupSelectsChildren": True,
                "suppressRowClickSelection": True,
                "suppressAggFuncInHeader": True,
                "groupDisplayType": "multipleColumns",
            },
            defaultColDef=dict(
                resizable=True,
            ),
            id="grouped-grid",
            enableEnterpriseModules=True,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)