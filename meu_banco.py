import sqlite3
from dash import Dash, html, dcc, Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Label('Paciente'),
        dcc.Dropdown(
            id='paciente',
            options=[
                {'label': 'Fulando da Silva', 'value': 'Fulando da Silva'},
                {'label': 'Siclano Ferreira', 'value': 'Siclano Ferreira'},
                {'label': 'Raimundo Nonato', 'value': 'Raimundo Nonato'}
            ],
            value='Fulando da Silva'
        ),
        html.Br(),
        html.Label('Hipótese Diagnóstica'),
        dcc.Dropdown(
            id='hipotese_diagnostica',
            options=[
                {'label': 'Neurótico Obsessivo', 'value': 'Neurótico Obsessivo'},
                {'label': 'Neurótico Histérico', 'value': 'Neurótico Histérico'},
                {'label': 'Psicose', 'value': 'Psicose'},
                {'label': 'Perversão', 'value': 'Perversão'}
            ],
            value=[],
            multi=True
        ),
        html.Br(),
        html.Label('Hipótese Diagnóstica Psiquiátrica'),
        dcc.Dropdown(
            id='hipotese_diagnostica_psiquiatrica',
            options=[
                {'label': 'Depressão', 'value': 'Depressão'},
                {'label': 'Ansiedade generalizada', 'value': 'Ansiedade generalizada'},
                {'label': 'Transtorno de Humor Afetivo Bipolar', 'value': 'Transtorno de Humor Afetivo Bipolar'},
                {'label': 'Paranóia', 'value': 'Paranóia'},
                {'label': 'Borderline', 'value': 'Borderline'},
                {'label': 'Fobia', 'value': 'Fobia'},
                {'label': 'Autismo', 'value': 'Autismo'},
                {'label': 'TDAH', 'value': 'TDAH'},
                {'label': 'TOD', 'value': 'TOD'}
            ],
            value=[],
            multi=True
        ),
        html.Br(),
        html.Label('Nota Fiscal'),
        dcc.Dropdown(
            id='nota_fiscal',
            options=[
                {'label': 'Sim', 'value': 'Sim'},
                {'label': 'Não', 'value': 'Não'}
            ],
            value=[],
            multi=True
        ),
        html.Br(),
        html.Label('Método de pagamento'),
        dcc.Dropdown(
            id='metodo_pagamento',
            options=[
                {'label': 'Débito', 'value': 'Débito'},
                {'label': 'Crédito', 'value': 'Crédito'},
                {'label': 'Mensal', 'value': 'Mensal'},
                {'label': 'Por consulta', 'value': 'Por consulta'}
            ],
            value=[],
            multi=True
        ),
        html.Br(),
        html.Label('Prioridade'),
        dcc.RadioItems(
            id='prioridade',
            options=[
                {'label': 'Baixa', 'value': 'Baixa'},
                {'label': 'Média', 'value': 'Média'},
                {'label': 'Alta', 'value': 'Alta'}
            ],
            value=None
        ),
    ], style={'padding': 10, 'flex': 1}),

    html.Div([
        html.Br(),
        html.Label('Dia da consulta'),
        dcc.Checklist(
            id='dia_consulta',
            options=[
                {'label': 'Segunda', 'value': 'Segunda'},
                {'label': 'Terça', 'value': 'Terça'},
                {'label': 'Quarta', 'value': 'Quarta'},
                {'label': 'Quinta', 'value': 'Quinta'},
                {'label': 'Sexta', 'value': 'Sexta'}
            ],
            value=[]
        ),
        html.Br(),
        html.Label('Flexibilidade de horário'),
        dcc.Checklist(
            id='flexibilidade',
            options=[
                {'label': 'Sim', 'value': 'Sim'},
                {'label': 'Não', 'value': 'Não'}
            ],
            value=[]
        ),
        html.Br(),
        html.Label('Observações'),
        dcc.Input(
            id='observacoes',
            value='anotações',
            type='text'
        ),
        html.Br(),
        html.Label('Horário atendimento'),
        dcc.Slider(
            id='horario_atendimento',
            min=8,
            max=22,
            step=1,
            marks={i: str(i) for i in range(8, 23)},
            value=8,
        ),
    ], style={'padding': 10, 'flex': 1}),

    html.Br(),
    html.Button('Salvar', id='salvar-button', n_clicks=0),
    html.Div(id='mensagem', style={'padding': 10})
], style={'display': 'flex', 'flexDirection': 'column'})

@app.callback(
    Output('mensagem', 'children'),
    Input('salvar-button', 'n_clicks'),
    State('paciente', 'value'),
    State('hipotese_diagnostica', 'value'),
    State('hipotese_diagnostica_psiquiatrica', 'value'),
    State('nota_fiscal', 'value'),
    State('metodo_pagamento', 'value'),
    State('prioridade', 'value'),
    State('dia_consulta', 'value'),
    State('flexibilidade', 'value'),
    State('observacoes', 'value'),
    State('horario_atendimento', 'value')
)
def salvar_formulario(n_clicks, paciente, hipotese_diagnostica,
                      hipotese_diagnostica_psiquiatrica, nota_fiscal,
                      metodo_pagamento, prioridade, dia_consulta,
                      flexibilidade, observacoes, horario_atendimento):
    if n_clicks > 0:
        # Conecta ou cria o banco de dados
        conn = sqlite3.connect('meu_banco.db')
        cursor = conn.cursor()
        # Cria a tabela se não existir
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS formulario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente TEXT,
                hipotese_diagnostica TEXT,
                hipotese_diagnostica_psiquiatrica TEXT,
                nota_fiscal TEXT,
                metodo_pagamento TEXT,
                prioridade TEXT,
                dia_consulta TEXT,
                flexibilidade TEXT,
                observacoes TEXT,
                horario_atendimento INTEGER
            )
        ''')
        # Insere os dados do formulário
        cursor.execute('''
            INSERT INTO formulario (
                paciente, hipotese_diagnostica, hipotese_diagnostica_psiquiatrica,
                nota_fiscal, metodo_pagamento, prioridade, dia_consulta,
                flexibilidade, observacoes, horario_atendimento
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            paciente,
            ', '.join(hipotese_diagnostica) if isinstance(hipotese_diagnostica, list) else hipotese_diagnostica,
            ', '.join(hipotese_diagnostica_psiquiatrica) if isinstance(hipotese_diagnostica_psiquiatrica, list) else hipotese_diagnostica_psiquiatrica,
            ', '.join(nota_fiscal) if isinstance(nota_fiscal, list) else nota_fiscal,
            ', '.join(metodo_pagamento) if isinstance(metodo_pagamento, list) else metodo_pagamento,
            prioridade,
            ', '.join(dia_consulta) if isinstance(dia_consulta, list) else dia_consulta,
            ', '.join(flexibilidade) if isinstance(flexibilidade, list) else flexibilidade,
            observacoes,
            horario_atendimento
        ))
        conn.commit()
        conn.close()
        return "Dados salvos com sucesso!"
    return ""

if __name__ == '__main__':
    app.run(debug=True)
