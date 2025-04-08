import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns


abastecimentos_df = pd.read_csv('abastecimentosAgrisal.csv')

#print(abastecimentos_df.head())
abastecimentos_df['dEmi'] = pd.to_datetime(abastecimentos_df['dEmi'])

abastecimentos_df_100 = abastecimentos_df[abastecimentos_df['total'] > 100]



abastecimentos_df_100['ano'] = abastecimentos_df_100['dEmi'].dt.year
abastecimentos_df_100['mes'] = abastecimentos_df_100['dEmi'].dt.month
abastecimentos_df_100['dia'] = abastecimentos_df_100['dEmi'].dt.day_name()
#print(abastecimentos_df_100)

# Salvando novo CSV limpo
abastecimentos_df_100.to_csv("abastecimentos_df_100.csv", index=False)



#agrupando resultados do novo data set

# Por meses
df_result = pd.read_csv('abastecimentos_df_100.csv')

# Por dia da semana
#print(df_result.groupby('dia').size().sort_values(ascending=False))

df_result.groupby('mes').size()
acumulado = df_result.groupby('mes').size()
acumulado = acumulado.reset_index(name='total_abastecimentos')

print(acumulado)


#PARA GERAR um gráfico 
#sns.scatterplot(
#    data=acumulado,
#    x='total_abastecimentos',
#   y='mes'
#)
#plt.title("Abastecimentos acima de R$100 por Mês")
#plt.tight_layout()
#plt.savefig("grafico_abastecimentos_por_mes.png")  # salvar como imagem

plt.figure(figsize=(8,4))
sns.countplot(data=acumulado, x='mes', hue='mes', palette='Greens') 
plt.title('Abastecimentos acima de R$100 por Mês')
plt.ylabel('Quantidade')
plt.xlabel('Mês')
plt.tight_layout()
plt.savefig("grafico_abastecimentos_por_mesQT.png")  # salvar como imagem