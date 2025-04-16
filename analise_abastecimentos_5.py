import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns


#Análises comparativas por posto

# Análises adicionais por cliente ou por posto em todos os valores
#Análise de fidelização de clientes por posto
#Padrão de abastecimentos por posto ao longo dos meses
#Correlação entre volume de abastecimentos e ticket médio por posto
#Postos com maior crescimento ou queda ao longo do tempo
#Geração de gráficos visuais para apoio no relatório
df_todos = pd.read_csv('abastecimentosAgrisal.csv')
df_maior_100 = pd.read_csv('abastecimentos_df_100.csv')

# Número de clientes únicos por posto
clientes_unicos_posto_100 = df_maior_100.groupby('CNPJ')['customer_id'].nunique().reset_index(name='clientes_unicos')
clientes_unicos_posto = df_todos.groupby('CNPJ')['customer_id'].nunique().reset_index(name='clientes_unicos')

# Total de abastecimentos por posto
total_abastecimentos_posto_100 = df_maior_100.groupby('CNPJ').size().reset_index(name='total_abastecimentos')
total_abastecimentos_posto = df_todos.groupby('CNPJ').size().reset_index(name='total_abastecimentos')


# Mesclando os dois para cálculo da média de abastecimentos por cliente
fidelizacao = pd.merge(total_abastecimentos_posto, clientes_unicos_posto, on='CNPJ')
fidelizacao['abastecimentos_por_cliente'] = fidelizacao['total_abastecimentos'] / fidelizacao['clientes_unicos']
fidelizacao.sort_values('abastecimentos_por_cliente', ascending=False, inplace=True)
print(fidelizacao.head(10))

# Mesclando os dois para cálculo da média de abastecimentos acima de 100 reais por cliente 
fidelizacao_100 = pd.merge(total_abastecimentos_posto_100, clientes_unicos_posto, on='CNPJ')
fidelizacao_100['abastecimentos_por_cliente_100'] = fidelizacao_100['total_abastecimentos'] / fidelizacao_100['clientes_unicos']
fidelizacao_100.sort_values('abastecimentos_por_cliente_100', ascending=False, inplace=True)
print(fidelizacao_100.head(10))

# df_todos: inclui todos os abastecimentos
# df_maior_100: inclui somente abastecimentos com valor > R$100


# Unir os dois dataframes pela coluna 'CNPJ'
df_comparativo = pd.merge(
    fidelizacao[['CNPJ', 'abastecimentos_por_cliente']],
    fidelizacao_100[['CNPJ', 'abastecimentos_por_cliente_100']],
    on='CNPJ'
)

# Ordenar pelos maiores valores de 'Todos'
df_comparativo = df_comparativo.sort_values(by='abastecimentos_por_cliente', ascending=False)

# Criar gráfico de barras agrupadas
plt.figure(figsize=(14,6))
bar_width = 0.4
index = range(len(df_comparativo))

plt.bar(index, df_comparativo['abastecimentos_por_cliente'], width=bar_width, label='Todos os Abastecimentos')
plt.bar([i + bar_width for i in index], df_comparativo['abastecimentos_por_cliente_100'], width=bar_width, label='Acima de R$100')

plt.xlabel('CNPJ dos Postos')
plt.ylabel('Média de Abastecimentos por Cliente')
plt.title('Comparativo de Fidelização por Posto (Todos x > R$100)')
plt.xticks([i + bar_width/2 for i in index], df_comparativo['CNPJ'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.savefig("Gráfico_comparativo_clientes.png")
