import pandas as pd # type: ignore
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Análises com probalidades e chances de dentro do primeiro sorteio
#Verificação da quantidade de abastecimentos por cliente, retirando uma média 
#verificando o comportamento durante o mês todo dos que abasteceram mais de 2 vezes no mês.


df_clientes = pd.read_csv('abastecimentosPrimeiroSorteio.csv')

df = df_clientes.drop(['Sorteio'],  axis = 1)
df['DataCompra']= pd.to_datetime(df['DataCompra'])

df['dia'] = df['DataCompra'].dt.day
print(df.head())
#Agrupamento das vendas participantes dos sorteios
#print(df.groupby('dia').size())

#1. Distribuição dos cupons por valor gasto
#    Objetivo: Verificar a proporção de cupons emitidos em relação ao valor gasto.
#    Gráfico: scatterplot ou lineplot com regressão.
df_ate_50 = df.loc[df['TotalGasto']<=50]
#print(df_ate_50)
df_mais_50 = df.loc[df['TotalGasto']>50]
#print(df_mais_50)

gasto_por_cliente_ate_50 = df_ate_50.groupby('Cliente')['TotalGasto'].sum().reset_index()
#print(gasto_por_cliente_ate_50)

gasto_por_cliente_mais_50 = df_mais_50.groupby('Cliente')['TotalGasto'].sum().reset_index()
#print(gasto_por_cliente_mais_50)

#Gráfico comparativo entre populações 
clientes_ate_50 = df_ate_50['Cliente'].nunique()
clientes_mais_50 = df_mais_50['Cliente'].nunique()

plt.bar(['Até R$50', 'Acima de R$50'], [clientes_ate_50, clientes_mais_50], color=['yellow', 'green'])
plt.title('Número de Clientes por Faixa de Gasto')
plt.ylabel('Quantidade de Clientes')
plt.savefig("grafico_comparativo_Clientes_soteio1.png")  # salvar como imagem



#2. Clientes que mais geram cupons
#    Objetivo: Identificar clientes que geram muitos cupons (possivelmente grandes consumidores).
#    Gráfico: barplot dos top 10.

#Gráfico Clientes que mais gastaram
top_mais_50 = df_mais_50.groupby('Cliente', as_index=False)['TotalGasto'].sum().sort_values(by='TotalGasto', ascending=False).head(10)

#plt.figure(figsize=(10,6))
#sns.barplot(data=top_mais_50, x='TotalGasto', y='Cliente', palette='Greens_r', )
#plt.title('Top 10 Clientes - Gastos acima de R$50')
#plt.xlabel('Total Gasto (R$)')
#plt.ylabel('Cliente')
#plt.tight_layout()
#plt.savefig("Clientes_TOP.png")  # salvar como imagem

3#. Comportamento por posto
#    Objetivo: Quais postos emitem mais cupons? Qual o ticket médio por posto?
#    Gráfico: heatmap cruzando CNPJ x média de cupons ou valor gasto.
# Ticket médio por posto

df_posto = pd.read_csv('TotalVendaPorPosto.csv')
#print(df_posto.head(10))
#df_posto['total_gasto'] = df['total_gasto'].astype('float')
#print(df.head())
ticket_medio = df_posto.groupby('CNPJ')['total_gasto'].mean().reset_index(name='ticket_medio')

# Agrupando cupons por CNPJ
apuracao_postos = df.groupby('Posto')['QtdCupons'].sum().reset_index(name='Qtd de cupons por posto')

# Salvando novo CSV limpo
ticket_medio.to_csv("df_ticke.csv", index=False)
apuracao_postos.to_csv("df_cupons.csv", index=False)

df_ticket = pd.read_csv("df_ticke.csv")
df_cupons = pd.read_csv("df_cupons.csv")

# Renomeia a coluna para fazer o merge
df_cupons.rename(columns={'Posto': 'CNPJ'}, inplace=True)

print(df_ticket.head(20))
print(df_cupons.head(20))

# Faz o merge com base no CNPJ
df_merge = pd.merge(df_ticket, df_cupons, on='CNPJ')

# Converte CNPJ para string (opcional, se quiser deixar mais legível no eixo X)
df_merge['CNPJ'] = df_merge['CNPJ'].astype(str)

print(df_merge.head(20))

# Dados
cnpjs = df_merge['CNPJ']
ticket = df_merge['ticket_medio']
cupons = df_merge['Qtd de cupons por posto']

# Posição no eixo X
x = np.arange(len(cnpjs))
largura = 0.4

# Criando o gráfico
fig, ax1 = plt.subplots(figsize=(15, 6))

# Barras do ticket médio
barras1 = ax1.bar(x - largura/2, ticket, width=largura, label='Ticket Médio (R$)', color='skyblue')

# Criando um segundo eixo Y
ax2 = ax1.twinx()

# Barras da quantidade de cupons
barras2 = ax2.bar(x + largura/2, cupons, width=largura, label='Qtd Cupons', color='orange')

# Ajustando labels e ticks
ax1.set_xlabel('CNPJ do Posto')
ax1.set_ylabel('Ticket Médio (R$)', color='skyblue')
ax2.set_ylabel('Qtd de Cupons', color='orange')
plt.xticks(x, cnpjs, rotation=90)
plt.title('Ticket Médio vs Qtd de Cupons por Posto')
plt.tight_layout()

# Legenda
fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

plt.savefig("grafico_resultado_Postos.png")  # salvar como imagem


#Gráfico de disperção

# Criando o gráfico
plt.figure(figsize=(12, 7))
sns.regplot(data=df_merge, 
            x='ticket_medio', 
            y='Qtd de cupons por posto',
            scatter=True,
            ci=None,  # remove intervalo de confiança
            line_kws={'color': 'red'}  # cor da linha
            )

# Adiciona rótulos aos pontos
for i in range(len(df_merge)):
    plt.text(df_merge['ticket_medio'][i], df_merge['Qtd de cupons por posto'][i], df_merge['CNPJ'][i], fontsize=8)

# Título e rótulos
plt.title('Relação entre Ticket Médio e Quantidade de Cupons por Posto')
plt.xlabel('Ticket Médio (R$)')
plt.ylabel('Qtd de Cupons por Posto')

plt.grid(True)
plt.tight_layout()
plt.savefig("graficoDispercao_resultado_Postos.png")  # salvar como imagem