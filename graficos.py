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