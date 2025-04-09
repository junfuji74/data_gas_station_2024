import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns


#agrupando resultados do novo data set

# Por meses
df_result = pd.read_csv('abastecimentos_df_100.csv')
#print(df_result.head())
# Por dia da semana
#rint(df_result.groupby('dia').size().sort_values(ascending=False))


#Agrupamentos de dados com uma coluna
df_result.groupby('mes').size()
acumulado = df_result.groupby('mes').size()
acumulado = acumulado.reset_index(name='total_abastecimentos')
print(f"Total em cada mês: {df_result.shape[0]}")

print(acumulado)

#Agrupamentos de dados com 2 colunas 
total_posto = df_result.groupby(['mes', 'CNPJ']).size().reset_index(name='total')
print(f"Total de abastecimentos por posto em cada mês: {df_result.shape[0]}")
print(total_posto)

plt.figure(figsize=(14, 7))
sns.barplot(data=total_posto, x='mes', y='total', hue='CNPJ', palette='tab10')

#plt.title('Total de abastecimentos por mês e por posto')
#plt.xlabel('Mês')
#plt.ylabel('Total de abastecimentos')
#plt.legend(title='Posto (CNPJ)', bbox_to_anchor=(1.05, 1), loc='upper left')
#plt.tight_layout()
#plt.savefig("abastecimentos_por_mes_posto.png")

#print(f"Total de abastecimentos acima de R$100: {df_result.shape[0]}")

##postos_mais_movimentados = df_result['CNPJ'].value_counts().head(10)
#print(postos_mais_movimentados)


#clientes_frequentes = df_result['customer_id'].value_counts().head(10)
#print(clientes_frequentes)

#print(df_result['total'].describe())

#bins = [100, 300, 600, 1000, 3000, 10000]
#labels = ['100-300', '301-600', '601-1000', '1001-3000', '3001+']
#df_result['faixa_valor'] = pd.cut(df_result['total'], bins=bins, labels=labels)
#print(df_result['faixa_valor'].value_counts())

#Percentuais e proporções
total_por_posto = df_result.groupby('CNPJ').size()
porcentagem = (total_por_posto / total_por_posto.sum()) * 100

print("Percentual de vendas")
print(porcentagem)

#Análises condicionais mais avançadas

tick_med= df_result.groupby('CNPJ')['total'].mean().sort_values(ascending=False)  # Ticket médio por mês

client = df_result.groupby('customer_id')['total'].sum().sort_values(ascending=False).head(10)  # Top 10 clientes por valor gasto

print("Ticket Medio:\n MES - VALOR", tick_med )
print("TOP 10 clientes ")
print(client)

# quartis de clientes por volume de compras:
quartil= df_result['quartil_clientes'] = pd.qcut(df_result.groupby('customer_id')['total'].transform('sum'), q=4)

print("Quartil de clientes>", quartil)