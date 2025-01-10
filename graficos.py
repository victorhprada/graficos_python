import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um DataFrame com 20 registros
idades = np.random.randint(20, 60, 20) # Idades aleatórias entre 20 e 60
salarios = idades * np.random.randint(80, 120, 20) # Salários relacionas á idade
pontuacoes = salarios * np.random.uniform(0.5, 1.5, 20) # Pontuações relacionadas ao salário
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

# DataFrame
new_data = {
    'Idade': idades,
    'Salário': salarios,
    'Pontuação': pontuacoes.round(2) # Arredondando as pontuaçoes para 2 casas decimais
}

df = pd.DataFrame(new_data)
df['Profissão'] = np.random.choice(profissoes, size=len(df))
print(df.head(10))

# Gráfico de Barras
plt.figure(figsize=(12, 6))
salario_por_profissao = df.groupby('Profissão')['Salário'].mean() # Agrupando os dados do DataFrame por profissão e calculando a média do salário para cada profissão
plt.bar(salario_por_profissao.index, salario_por_profissao, color='skyblue') # Indicamos aqui os índices do DataFrame no eixo x e os salários no eixo y
plt.title('Distribuição de Salários', fontsize=16)
plt.xlabel('Índice', fontsize=12)
plt.ylabel('Salário', fontsize=12)
plt.xticks(rotation=45) # Rotacionar o rótulo do eixo x em 45 graus para melhorar a leitura
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

media_score_por_idade = df.groupby('Idade')['Pontuação'].mean() # Calculando a média do score para cada idade com agrupamento
media_score_por_idade = media_score_por_idade.sort_index() # ordenando as idades em ordemcrescente utilizando o sort_index

# Gráfico de Linha
plt.figure(figsize=(12,6))
plt.plot(media_score_por_idade.index, media_score_por_idade, marker='o', color='red') # marker ='o' significa que os pontos no gráfico serão marcados com círculos ('o')

plt.title('Média do Score por Idade', fontsize=16)
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Média do Score', fontsize=12)
plt.grid(True, linestyle='-', alpha=0.7)
plt.show()

# Gráfico de Linahs e Colunas
media_score_por_idade = df.groupby('Idade')['Salário'].mean()
media_score_por_idade = media_score_por_idade.sort_index()

# Criando gráfico de linha
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotando a média do score por idade
ax1.plot(media_score_por_idade.index, media_score_por_idade, marker='o', color='red', label='Média do Score')
ax1.set_xlabel('Idade', fontsize=12)
ax1.set_ylabel('Média do Score', color='red', fontsize=12)

# Adicionando uma segunda coluna para a média de salário por idade, nessa etapa é a configuração do gráfico de barras
ax2 = ax1.twinx() # Criando o segundo eixo y
ax2.bar(media_score_por_idade.index, media_score_por_idade, color='blue', alpha=0.5, label='Média do Salário')
ax2.set_ylabel('Média do Salário', color='blue', fontsize=12)

# Legendas:
lines1, labels1 = ax1.get_legend_handles_labels() # obtendo as linhas e rótulos da legenda do primeiro eixo y (ax1)
lines2, labels2 = ax2.get_legend_handles_labels() # obtendo as linhas e rétulos da legenda do segundo eixo y (ax2)

ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', bbox_to_anchor=(1.2, 1.2))
# labels1 + labels2 concatena os rótulos das legendas dos dois eixos y
# loc='upper righ' especifica que a legenda será posicionada no canto superior direito do gráfico
# bbox_to_anchor=(1,2,1.2) especifica que a legenda será posicionada a uma distândia de 1.2 unidades de largura 

plt.title('Média do Score e Média do Salário por Idade', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Gráfico de Dispersão de salário em relação a idade
plt.figure(figsize=(12,6))
plt.scatter(df['Idade'], df['Salário'], color='purple', alpha=0.7)
plt.title('Relação entre salário e idade')
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Salário', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Boxplot para coluna de salário
plt.figure(figsize=(12, 6))
plt.boxplot(df['Salário'])

plt.title('Boxplot do Salário', fontsize=16)
plt.xlabel('Salário', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Boxplot para coluna de pontuação
plt.figure(figsize=(12, 6))
plt.boxplot(df['Pontuação'])

plt.title('Boxplot da Pontuação', fontsize=16)
plt.ylabel('Pontuação', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Boxplot para idade e salário
plt.figure(figsize=(12, 6))
plt.boxplot([df['Pontuação'], df['Salário']], label=['Pontuação', 'Salário'])

plt.title('Boxplot de pontuação e salário', fontsize=16)
plt.ylabel('Valor', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Criar um cenário com salários muitos espaçados e outliers
salarios = np.random.randint(2000, 10000, 18) # 18 salários aleatórios
outliers = [15000, 18000]
salarios_com_outliers = np.concat((salarios, outliers))

df_salarios = pd.DataFrame({'Salário': salarios_com_outliers})
print(df_salarios.head(5))

plt.figure(figsize=(12, 6))
plt.boxplot(df_salarios['Salário'])

plt.title('Boxplot dos Salários', fontsize=16)
plt.ylabel('Salário', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()