import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns


#Exploração complementar dos dados

# Análises adicionais por cliente ou por posto em todos os valores
df_postos = pd.read_csv('abastecimentosAgrisal.csv')

#conversão de campo para date
df_postos['dEmi'] = pd.to_datetime(df_postos['dEmi'])


df_postos['ano'] = df_postos['dEmi'].dt.year
df_postos['mes'] = df_postos['dEmi'].dt.month

#print(df_postos.head())

# Agrupado Por da Mês por cliente
abastecimentos_cliente = df_postos.groupby(['mes', 'customer_id']).size().reset_index(name='total')
print(f"Total de abastecimentos POR CLIENTES: {abastecimentos_cliente.shape[0]}")
print(abastecimentos_cliente.sort_values('total'))

# Agrupado Por da Mês por posto
abastecimentos_CNPJ = df_postos.groupby(['mes', 'CNPJ']).size().reset_index(name='total')
print(f"Total de abastecimentos POR POSTO: {abastecimentos_CNPJ.shape[0]}")
print(abastecimentos_CNPJ.sort_values('total'))

# Agrupado Por da posto e cliente
abastecimentos_cliente_posto = df_postos.groupby(['CNPJ', 'customer_id']).size().reset_index(name='total')
print(f"Total de clientes POR POSTO: {abastecimentos_cliente_posto.shape[0]}")
print(abastecimentos_cliente_posto.sort_values('total'))

# Ticket médio por posto
ticket_medio = df_postos.groupby('CNPJ')['total'].mean().reset_index(name='ticket_medio')

# Ordenar do maior para o menor
ticket_medio = ticket_medio.sort_values(by='ticket_medio', ascending=False)

# Exibir os 10 maiores
print("Top 10 postos com maior ticket médio:")
print(ticket_medio.head(10))

#Gráfico de Calor
# Agrupando por mês e CNPJ
heatmap_data = df_postos.groupby(['mes', 'CNPJ']).size().unstack(fill_value=0)

# Criar o heatmap
plt.figure(figsize=(18, 8))
sns.heatmap(heatmap_data, cmap="YlGnBu", linewidths=0.5)
plt.title("Heatmap de abastecimentos por mês e CNPJ (acima de R$100)", fontsize=16)
plt.xlabel("CNPJ do Posto")
plt.ylabel("Mês")
plt.tight_layout()
plt.savefig("heat_de_abastecimentos_por_posto.png")
#Frequência média de abastecimento por cliente;

#Ticket médio mensal por posto;

#Participação dos top clientes no total de vendas;

#Comparativo entre clientes pessoa física e jurídica (se houver esse dado ou inferência pelo volume de gastos).