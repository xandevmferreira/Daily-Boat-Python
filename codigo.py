from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.Label('Paciente'),
        dcc.Dropdown(
            options=['Fulando da Silva', 'Siclano Ferreira', 'Raimundo Nonato'],
            value='Fulando da Silva'
        ),

        html.Br(),
        html.Label('Hipótese Diagnóstica'),
        dcc.Dropdown(
            options=['Neurótico Obsessivo', 'Neurótico Histérico', 'Psicose','Perversão'],
            value=[],
            multi=True
        ),

        html.Br(),
        html.Label('Hipótese Diagnóstica Psiquiátrica'),
        dcc.Dropdown(
            options=['Depressão','Ansiedade generalizada', 'Transtorno de Humor Afetivo Bipolar', 'Paranóia','Borderline', 'Fobia', 'Autismo', 'TDAH', 'TOD'],
            value=[],
            multi=True
        ),

        html.Br(),
        html.Label('Nota Fiscal'),
        dcc.Dropdown(
            options=['Sim', 'Não'],
            value=[],
            multi=True
        ),

        html.Br(),
        html.Label('Método de pagamento'),
        dcc.Dropdown(
            options=['Débito', 'Crédito', 'Mensal', 'Por consulta'],
            value=[],
            multi=True
        ),

        html.Br(),
        html.Label('Prioridade'),
        dcc.RadioItems(
            options=['Baixa', 'Média', 'Alta'],
            value=None
        ),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Br(),
        html.Label('Dia da consulta'),
        dcc.Checklist(
            options=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
            value=[]
        ),

        html.Br(),
        html.Label('Flexibilidade de horário'),
        dcc.Checklist(
            options=['Sim', 'Não'],
            value=[]
        ),

        html.Br(),
        html.Label('Observações'),
        dcc.Input(value='anotações', type='text'),

        html.Br(),
        html.Label('Horário atendimento'),
        dcc.Slider(
            min=8,
            max=22,
            step=1,
            marks={i: str(i) for i in range(8, 23)},
            value=8,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flexDirection': 'row'})

if __name__ == '__main__':
    app.run(debug=True)
