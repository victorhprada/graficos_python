import pandas as pd
import plotly.express as px

data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}

df = pd.DataFrame(data)

# Converter colunas para tipos numéricos
df['Salário'] = pd.to_numeric(df['Salário'])
df['Limite_Credito'] = pd.to_numeric(df['Limite_Credito'])

df.head(5)



# Agrupar os dados do DataFrame por profissão e salário, e calculando a média do limite de crédito para cada profissão e salário
score_salario_profissao = df.groupby(['Profissão', 'Salário'])['Limite_Credito'].mean().reset_index()

# Com o TreeMap é possível ver as profissões e os salários que mais possume limite de crédito
fig = px .treemap(score_salario_profissao,
                  path=['Profissão', 'Salário'],
                  values='Limite_Credito',
                  title='Limite de Cédito por Profissão e Salários',
                  color='Salário')

fig.show()

# Gráfico de dispersão para isualizar a correlação entre o salário e o limite de crédito
fig = px.scatter(df,
                 x='Salário',
                 y='Limite_Credito',
                 color='Profissão',
                 size='Idade',
                 title='Salários vc Limite de Crédito por Profissão')

fig.show()

# Box Plot para comparar a distribuição do limite de crédito entre estados civis
fig = px.box(df,
             x='Estado_Civil',
             y='Limite_Credito',
             color='Profissão',
             title='Distribuição do Limite de crédito por Estado Civil e profissão')

fig.show()

fig = px.parallel_categories(df,
                             dimensions=['Estado_Civil', 'Profissão', 'Imovel_Proprio'],
                             color='Limite_Credito',
                             title='Relação entre estado civil, profissão e imóvel próprio')

fig.show()