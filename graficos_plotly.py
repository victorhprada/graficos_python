import pandas as pd
import numpy as np
import plotly.express as px

idades = np.random.randint(20, 60, 20)
salarios = idades * np.random.randint(80, 120, 20)
pontuacoes = salarios * np.random.uniform(0.5, 1.5, 20)
profissoes = [
    'Engenheiro',
    'Professor',
    'Médico',
    'Advogado',
    'Designer',
    'Analista',
    'Gerente',
    'Programador'
]

estado_civil = [
    'Casado',
    'Solteiro'
]

novo_data = {
    'Idade': idades,
    'Salário': salarios,
    'Pontuação': pontuacoes
}

df = pd.DataFrame(novo_data)
df['Profissão'] = np.random.choice(profissoes, size=len(df))
df['estado_civil'] = np.random.choice(estado_civil, size=len(df))

print(df.head(10))

# Gráfico de barras horizontais com a média dos salários por profissão

# Agrupando os dados do DataFrame por profissão e calculando a média do salário para cada profissão
salario_por_profissao = df.groupby('Profissão')['Salário'].mean().reset_index()

# Criando o gráfico de barras horizontais
fig = px.bar(salario_por_profissao, x='Salário', y='Profissão', orientation='h',
             title='Salários por Profissão',
             labels={'Salário': 'Salário Médio', 'Profissão': 'Profissão'})

fig.show()

# Alterando cor e tamanho
fig = px.bar(salario_por_profissao, x='Salário', y='Profissão', orientation='h',
             title='Salários por Profissão',
             labels={'Salário': 'Salário Médio', 'Profissão': 'Profissão'},
             color='Salário', # Especificando a cor baseada nos valores de salário
             width=800) # definindo a largura do gráfico em pixels

fig.show()

# Agrupamos os dados do DataFrame por profissão e estado civil, e calculando a média do salário para cada profissão e estado civil
salario_profissao_estado_civil = df.groupby(['Profissão', 'estado_civil'])['Salário'].mean().reset_index()

# Criando o gráfico de treemap com os salários por profissão, usando cores para representar os estados civis
fig = px.treemap(salario_profissao_estado_civil,
                 path=['Profissão', 'estado_civil'],
                 values='Salário',
                 title='Salários por Profissão e Estados Civis',
                 color='estado_civil')

fig.show()

# Boxplot de idade
fig = px.box(df, y='Idade', title='Boxplot de Idade')

fig.show()