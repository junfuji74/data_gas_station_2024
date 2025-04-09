import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns


#agrupando resultados do novo data set

# Por meses
df_result = pd.read_csv('abastecimentos_df_100.csv')
#print(df_result.head())
# Por dia da semana
#rint(df_result.groupby('dia').size().sort_values(ascending=False))

df_result.groupby('mes').size()
acumulado = df_result.groupby('mes').size()
acumulado = acumulado.reset_index(name='total_abastecimentos')

print(acumulado)


print(f"Total de abastecimentos acima de R$100: {df_result.shape[0]}")

postos_mais_movimentados = df_result['CNPJ'].value_counts().head(10)
print(postos_mais_movimentados)


clientes_frequentes = df_result['customer_id'].value_counts().head(10)
print(clientes_frequentes)

print(df_result['total'].describe())

bins = [100, 300, 600, 1000, 3000, 10000]
labels = ['100-300', '301-600', '601-1000', '1001-3000', '3001+']
df_result['faixa_valor'] = pd.cut(df_result['total'], bins=bins, labels=labels)
print(df_result['faixa_valor'].value_counts())