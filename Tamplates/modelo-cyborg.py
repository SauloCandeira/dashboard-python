import dash
from dash.development.base_component import Component
from dash.html import Div
from dash.html.Col import Col
from dash.html.H3 import H3
from dash.html.Span import Span
from dash_bootstrap_components._components.Card import Card
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import psycopg2
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas_datareader.data as web



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])



############################# BANCO DE DADOS
# ----------------- SELECT I 
conn =psycopg2.connect("dbname='teste' user='postgres' host='localhost' password='451550'")
def connectSQLServer(conn):
    connpostgree = conn
    return connpostgree

# ----------------- BIOMETRIAS
sql_query = (''' Select count(*) is_sincronizado, 'Biometrias Online' as conexao from bio_access where is_sincronizado is true 
                    union all 
                    Select count(*) is_sincronizado, 'Biometrias Offline' as conexao from bio_access where is_sincronizado is false ''')
# ----------------- TAGS
sql_query2 = (''' Select count(*) is_sincronizado, 'Tags Online' as conexao from auto_access_tag where is_sincronizado is true 
union all 
Select count(*) is_sincronizado, 'Tags Offline' as conexao from auto_access_tag where is_sincronizado is false ''')
# ----------------- CARD
sql_query3 = (''' Select count(*) is_sincronizado, 'Card Online' as conexao from bio_access_card where is_sincronizado is true 
union all 
Select count(*) is_sincronizado, 'Card Offline' as conexao from bio_access_card where is_sincronizado is false ''')
#----------------- MORADOR
sql_query4 = (''' Select count(*) is_sincronizado, 'Card Online' as conexao from morador where is_sincronizado is true 
union all 
Select count(*) is_sincronizado, 'Card Offline' as conexao from morador where is_sincronizado is false ''')
# ----------------- SELECT II
df = pd.read_sql(sql_query,conn)
df2 = pd.read_sql(sql_query2,conn)
df3 = pd.read_sql(sql_query3,conn)
df4 = pd.read_sql(sql_query4,conn)

############################# TRATAMENTO DE DADOS
bio_online = df['is_sincronizado'][0] 
bio_offline = df['is_sincronizado'][1]


############################# TRATAMENTO DE DADOS
tag_online = df2['is_sincronizado'][0] 
tag_offline = df2['is_sincronizado'][1]

############################# TRATAMENTO DE DADOS
card_online = df3['is_sincronizado'][0] 
card_offline = df3['is_sincronizado'][1]
############################# TRATAMENTO DE DADOS
morador_online = df4['is_sincronizado'][0] 
morador_offline = df4['is_sincronizado'][1]



############################# LAYOUT
app.layout = dbc.Container(children=[
    
    ############################# HEADER
    html.Div([
        #------------------- TITULO
        html.H2(children='CONDOMINIO DEDICADO'),
        # ------------------- DESCRIÇÃO I
        html.Div(children='''Mondelagem de dados'''),
    ]),
   
    ################### CARDS
    dbc.Row([
        dbc.Col([
            #----- ONLINE
            dbc.Card ([
                html.Span('BIOMETRIAS ONLINE: '),
                html.H3(style={"color": "#adfc92"}, children= bio_online),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão" )
            ]) 
        ]),

        dbc.Col([
            #----- OFFLINE
            dbc.Card ([
                html.Span('BIOMETRIAS OFFLINE:'),
                html.H3(style={"color": "#ff0000"}, children= bio_offline),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão2" )
            ]) 
        ]),
    ]),   

    dbc.Row([
        dbc.Col([
            #----- ONLINE
            dbc.Card ([
                html.Span('TAG ONLINE: '),
                html.H3(style={"color": "#adfc92"}, children= tag_online),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão3" )
            ]) 
        ]),

        dbc.Col([
            #----- OFFLINE
            dbc.Card ([
                html.Span('TAG OFFLINE:'),
                html.H3(style={"color": "#ff0000"}, children= tag_offline),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão4" )
            ]) 
        ]),
    ]),   

    dbc.Row([
        dbc.Col([
            #----- ONLINE
            dbc.Card ([
                html.Span('CARD ONLINE: '),
                html.H3(style={"color": "#adfc92"}, children= card_online),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão5" )
            ]) 
        ]),

        dbc.Col([
            #----- OFFLINE
            dbc.Card ([
                html.Span('CARD OFFLINE:'),
                html.H3(style={"color": "#ff0000"}, children= card_offline),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão6" )
            ]) 
        ]),
    ]),   

    dbc.Row([
        dbc.Col([
            #----- ONLINE
            dbc.Card ([
                html.Span('MORADOR ONLINE: '),
                html.H3(style={"color": "#adfc92"}, children= morador_online),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão7" )
            ]) 
        ]),

        dbc.Col([
            #----- OFFLINE
            dbc.Card ([
                html.Span('MORADOR OFFLINE:'),
                html.H3(style={"color": "#ff0000"}, children= morador_offline),
                dbc.Button( "Ver mais" , n_clicks = 0 , id = "Botão8" )
            ]) 
        ]),
    ]),   


    

])







    



if __name__ == '__main__':
    app.run_server(debug=True)