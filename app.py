#! python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import A
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash_bootstrap_components._components.Card import Card
from dash_bootstrap_components._components.CardBody import CardBody
from dash_bootstrap_components._components.Col import Col
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pyodbc
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
#app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


############################# BANCO DE DADOS
# ----------------- SELECT I 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-BHUVH4U;DATABASE=db-Projetos;Trusted_Connection=yes;')
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-BHUVH4U;DATABASE=db-Pojetos;Trusted_Connection=yes;')
def connectSQLServer(conn):
    connSQLServer = conn
    return connSQLServer
sql_query = (''' SELECT * FROM bpo order by DATA ''')
sql_query2 = (''' SELECT * FROM carteira_Ativos$ order by valor,dt''')
sql_query3 = ('''SELECT * FROM impressoras''' )
#sql_query4 = (''' SELECT * FROM despesas_orgaos order by mesAno''')
sql_query4 = (''' SELECT nmOrgao, mesAno, valorDespesaEmpenhada FROM despesas_orgaos order by mesAno''')
sql_query5 = (''' SELECT * FROM despesas_orgaos order by len(valorDespesaEmpenhada), 'valorDespesaEmpenhada' ''')
#sql_query5 = (''' select * from despesas_orgaos order by mesAno ''')


############################# TRATAMENTO DE DADOS

df = pd.read_sql(sql_query,conn)
df2 = pd.read_sql(sql_query2,conn)
df3 = pd.read_sql(sql_query3,conn)
df4 = pd.read_sql(sql_query4,conn)
df5 = pd.read_sql(sql_query5,conn)


############################# GRAFICOS
#----- PATRIMONIO
fig = px.bar(df, x=(df["DATA"]), y=(df["PATRIMONIO"]), barmode="group")
fig2 = px.bar(df3, x=(df3["nome"]), y=(df3["tonner"]), barmode="group")
fig3 = px.line(df4, x=(df4["mesAno"]), y=df5["valorDespesaEmpenhada"], color="nmOrgao")
fig4 = px.scatter(df5, x=(df5["mesAno"]), y=(df5["valorDespesaEmpenhada"]), color="nmOrgao")




# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("SOCIAUD", className="display-4"),
        html.Hr(),
        html.P(
            "O povo unido jamais será vencido!", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Video Aulas", href="/page-1", active="exact"),
                dbc.NavLink("Forum", href="/page-2", active="exact"),
                dbc.NavLink("Relatorios", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



layout_page_1 = html.Div([
    dbc.Col([

     # ------------------- RELATORIO I
        dbc.CardHeader([
            html.H4("Controle Patrimonial", className="card-title"),
            dbc.Card([
            # ------------------- MENU DROPDOWN
                dcc.Dropdown(
                    id='dropdown-bpo',
                    options=[
                        {'label': 'Patrimonio', 'value': 'PATRIMONIO'},
                        {'label': 'Variacao', 'value': 'VARIACAO'},
                        {'label': 'Resultado', 'value': 'RESULTADO'}
                    ],
                    value='PATRIMONIO'
                ),
                # ------------------- GRAFICO I
                dcc.Graph(
                    id='graph-bpo',
                    figure= fig,
                ),
            ]),
            html.Div([
                dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
            ],
                className="d-grid gap-2 d-md-flex justify-content-md-end",
            ),      
        ]),

        # ------------------- RELATORIO II
        dbc.CardHeader([
            html.H4("Rastreamento de Impressoras", className="card-title"),
            # ------------------- MENU DROPDOWN
            dbc.Card([
                dcc.Dropdown(
                    id='dropdown-impressoras',
                    options=[
                        {'label': 'Tonner', 'value': 'TONNNER'},
                        {'label': 'Cilindro', 'value': 'CILINDRO'},
                        {'label': 'Consumo', 'value': 'CONSUMO'}
                    ],
                    value='TONNER'
                ),
                # ------------------- GRAFICO I
                dcc.Graph(
                    id='graph-impressoras',
                    figure= fig2,
                ),

            ]),    
            html.Div([
                dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
            ],
                className="d-grid gap-2 d-md-flex justify-content-md-end",
            ),

        ]),

        # ------------------- RELATORIO III
        dbc.CardHeader([
            html.H4("Despesas Orgãos", className="card-title"),
            # ------------------- MENU DROPDOWN

            dbc.Card([
                dcc.Dropdown(
                    id='dropdown-orgaos',
                    options=[
                        {'label': 'Despesas', 'value': 'DESPESAS'},
                        {'label': 'Cilindro', 'value': 'CILINDRO'},
                        {'label': 'Consumo', 'value': 'CONSUMO'}
                    ],
                    value='DESPESAS'
                ),
                # ------------------- GRAFICO I
                dcc.Graph(
                    id='graph-orgaos',
                    figure= fig3,
                ),
            ]),

            html.Div([
                dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
            ],
                className="d-grid gap-2 d-md-flex justify-content-md-end",
            ),
        ]),
    ]),
]),

layout_page_home = html.Div([

    dbc.Col([
        dbc.CardBody([
            html.H4("Video-Aulas", className="card-title"),
            dbc.Row([

                dbc.Col([

                    #----- ONLINE
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("WebScraping com Python", className="card-title"),
                                    html.P(
                                        "Some quick example text to build on the card title and "
                                        "make up the bulk of the card's content.",
                                        className="card-text",
                                    ),

                                    dbc.Progress(
                                        value=80, id="animated-progress", animated=False, striped=True, className="mb-3"
                                    ),
                                    
                                    html.Div(
                                        [
                                            dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                                            dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
                                        ],
                                        className="d-grid gap-2 d-md-flex justify-content-md-end",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ]),

                dbc.Col([
                    #----- ONLINE
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Python Basico", className="card-title"),
                                    html.P(
                                        "Some quick example text to build on the card title and "
                                        "make up the bulk of the card's content.",
                                        className="card-text",
                                    ),

                                    dbc.Progress(
                                        value=80, id="animated-progress", animated=False, striped=True, className="mb-3"
                                    ),
                                    
                                    html.Div(
                                        [
                                            dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                                            dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
                                        ],
                                        className="d-grid gap-2 d-md-flex justify-content-md-end",
                                    ),
                                ]
                            ),
                        ],
                    ),
                ]),

                dbc.Col([
                    #----- ONLINE
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("SQLServer Basico", className="card-title"),
                                    html.P(
                                        "Some quick example text to build on the card title and "
                                        "make up the bulk of the card's content.",
                                        className="card-text",
                                    ),

                                    dbc.Progress(
                                        value=80, id="animated-progress", animated=False, striped=True, className="mb-3"
                                    ),
                                    
                                    html.Div(
                                        [
                                            dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                                            dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
                                        ],
                                        className="d-grid gap-2 d-md-flex justify-content-md-end",
                                    ),
                                ]
                            ),
                        ],
                    ),
                ]),
            ])
        ]),
    ]),      

    dbc.Col([
        dbc.CardBody([
            html.H4("Relatorios", className="card-title"),
            dbc.Row([

                dbc.Col([
                    #----- ONLINE
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Despesas Orgãos", className="card-title"),
                                    html.P(
                                        "Some quick example text to build on the card title and "
                                        "make up the bulk of the card's content.",
                                        className="card-text",
                                    ),

                                    dbc.Progress(value=25, color="success", className="mb-3"),
                                    dbc.Progress(value=50, color="warning", className="mb-3"),
                                    dbc.Progress(value=75, color="danger", className="mb-3"),

                                    html.Div(
                                        [
                                            dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                                            dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
                                        ],
                                        className="d-grid gap-2 d-md-flex justify-content-md-end",
                                    ),
                                ]
                            ),
                        ],
                    ),
                ]),

                dbc.Col([
                    #----- ONLINE
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Salario Servidores", className="card-title"),
                                    html.P(
                                        "Some quick example text to build on the card title and "
                                        "make up the bulk of the card's content.",
                                        className="card-text",
                                    ),

                                    dbc.Progress(value=25, color="success", className="mb-3"),
                                    dbc.Progress(value=50, color="warning", className="mb-3"),
                                    dbc.Progress(value=75, color="danger", className="mb-3"),

                                    html.Div(
                                        [
                                            dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                                            dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
                                        ],
                                        className="d-grid gap-2 d-md-flex justify-content-md-end",
                                    ),
                                ]
                            ),
                        ],
                    ),
                ]),

                dbc.Col([
                    #----- ONLINE
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Receitas Publicas", className="card-title"),
                                    html.P(
                                        "Some quick example text to build on the card title and "
                                        "make up the bulk of the card's content.",
                                        className="card-text",
                                    ),

                                    dbc.Progress(value=25, color="success", className="mb-3"),
                                    dbc.Progress(value=50, color="warning", className="mb-3"),
                                    dbc.Progress(value=75, color="danger", className="mb-3"),

                                    html.Div(
                                        [
                                            dbc.Button("Github", size="lg", className="me-1", color="secondary"),
                                            dbc.Button("Visualizar", size="lg", className="me-1", color="danger"),
                                        ],
                                        className="d-grid gap-2 d-md-flex justify-content-md-end",
                                    ),
                                ]
                            ),
                        ],
                    ),
                ]),
            ])
        ]),
    ]), 
]),




content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return layout_page_home
    elif pathname == "/page-1":
        return html.P("Bem vindo a Video Aulas!")
    elif pathname == "/page-2":
        return html.P("Bem vindo ao Forum!")
    elif pathname == "/page-3":
        return layout_page_1
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )




@app.callback(
    Output(component_id='graph-bpo', component_property='figure'),
    Input(component_id='dropdown-bpo', component_property='value')
)
def changeText(value):
    if value == 'PATRIMONIO':
        return px.bar(df, x=(df["DATA"]), y=(df["PATRIMONIO"]), barmode="group")
    elif value == 'VARIACAO':
        return px.bar(df, x=(df["DATA"]), y=(df["VARIAÇÃO"]), barmode="group") 
    else:
        return px.line(df2, x=(df2["dt"]), y=(df2["valor"]), color='nome') 
    return



@app.callback(
    Output(component_id='graph-impressoras', component_property='figure'),
    Input(component_id='dropdown-impressoras', component_property='value')
)
def changeText(value):
    if value == 'TONNER':
        return px.bar(df3, x=(df3["nome"]), y=(df3["tonner"]), barmode="group")
    #elif value == 'CILINDRO':
    #    return px.bar(df3, x=(df3["nome"]), y=(df3["tonner"]), barmode="group") 
    #else:
        #return px.line(df3, x=(df3["dt"]), y=(df3["valor"]), color='nome') 
    return



@app.callback(
    Output(component_id='dropdown-orgaos', component_property='figure'),
    Input(component_id='dropdown-orgaos', component_property='value')
)
def changeText(value):
    if value == 'DESPESAS':
        #return px.line(df4, x=(df5["mesAno"]), y=(df4["valorDespesaEmpenhada"]), color="nmOrgao")
        return px.line(df4, x=(df4["mesAno"]), y=df5["valorDespesaEmpenhada"], color="nmOrgao")
    return






if __name__ == "__main__":
    app.run_server(debug=True)