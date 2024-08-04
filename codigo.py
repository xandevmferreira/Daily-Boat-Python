from dash import Dash, html, dcc

app = Dash('daily boat')

app.layout = html.Div([
    html.Div(children=[
        html.Label('Paciente'),
        dcc.Dropdown(['Fulando da Silva', 'Siclano Ferreira', 'Raimundo Nonato'], 'Fulano da Silva'),

        html.Br(),
        html.Label('Hipótese Diagnóstica'),
        dcc.Dropdown(['Neurótico Obsessivo', 'Neurótico Histérico', 'Psicose','Perversão'],
                     [],
                     multi=True),

html.Br(),
        html.Label('Hipótese Diagnóstica Psiquiátrica'),
        dcc.Dropdown(['Depressão','Ansiedade generalizada', 'Transtorno de Humor Afetivo Bipolar', 'Paranóia','Boderline', 'Fobia', 'Autismo', 'TDAH', 'TOD'],
                     [],
                     multi=True),

        html.Br(),
        html.Label('Nota Fiscal'),
        dcc.Dropdown(['Sim', 'Não'],
                     [],
                     multi=True),

        html.Br(),
        html.Label('Método de pagamento'),
        dcc.Dropdown(['Débito', 'Crédito', 'Mensal', 'Por consulta'],
                     [],
                     multi=True),

        html.Br(),
        html.Label('Prioridade'),
        dcc.RadioItems(['Baixa', 'Média', 'Alta'], ''),
    ], style={'padding': 10, 'flex': 1}),

        html.Br(),
        html.Label('Dia da consulta'),
        dcc.Checklist(['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    style={'padding': 10, 'flex': 1}),

        html.Div(children=[
        html.Label('Flexbilidade de horário'),
        dcc.Checklist(['Sim', 'Não'],
                      ['']
        ),

        html.Br(),
        html.Label('Observações'),
        dcc.Input(value='anotações', type='text'),

        html.Br(),
        html.Label('Horário atendimento'),
        dcc.Slider(
            min=8,
            max=22,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 24)},
            value=0,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flexDirection': 'row'})

if __name__ == '__main__':
    app.run(debug=True)