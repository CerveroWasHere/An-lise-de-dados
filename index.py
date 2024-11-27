# Estrutura do Exercício
# Passo 1: Carregar e Explorar os Dados
# Carregar a base de dados cahamda "cancelamentos.csv" usando a biblioteca pandas.
# Observar infirmações gerais da base, identificando valores nulos, colunas e tipos de dados.

import pandas as pd

# Carregar os dados
df = pd.read_csv('cancelamentos.csv')

# Exibir informações gerais
print(df.info())
print(df.describe())

# Passo 2: Análise Exploratória para Identificação de Padrões de Cancelamento
# A análise exploratória deve focar nos possíveis de cancelamento.
# Utilizaremos a biblioteca plotly.express para a visualização de dados e para compreender padrões específicos de clientes que cancelaram o serviço.
# Abaixo estão algumas sugestões de análises que podem ser realizadas:
# Distribuição do Tempo como Cliente e Cancelamento: Verficar se clientes que ficam mens temo na empresa são mais propensos a cancelar.

import plotly.express as px 

fig = px.histogram(df, x='idade', color='cancelou', barmode='group', title="Distribuição do Tempo como Cliente")
fig.show()

# Idade vs Cancelamento: Avaliar a idade dos clientes e a taxa de cancelamento para identificar padrões.

fig = px.histogram(df, x='idade', color='cancelou', brmode='overlay', title="Distribuição de Idade e Cancelamento")
fig.show()

# Total Gasto vs Cancelamento:
# Entender a relação entre o valor gasto pelo Cliente e o cancelamento, verificando se há um perfil específicio de consumo entre os que cancelaram.

fig = px.box(df, x='total_gasto', title="DIstribuição de Total gasto por Cancelamento")
fig.show()

# Dias de Atraso e Cancelamento: Analisar se clientes que atrasam pagamentos são mais propensos a cancelar.

fig = px.histogram(df, x='dias_atraso', color='cancelou', barmode='overlay', title="Dias de Atraso e Cancelamento")
fig.show()

# Interações com Call Center e Cancelamento: Observa se o número de ligações para o Call Center tem relação com o cancelamento.

fig = px.box(df, x='cancelou', y='ligacoes_callcenter', title="Número de Lgações ao Call Center e Cancelamento")
fig.show()

# Passo 3: Identificação de Perfis e Padrões de Clientes
# Baseado nas analises anteriores, identifique perfis de clientes com alta probabilidade de cancelar, tais como:

# Clientes com alta frequêcia de atrasos.
# Clientes com menos temo de permanêcia.
# Clientes que fazem uso menos frequente do serviço.
# Passo 4: Projeção de Impacto com Ações de Retenção
# Simule o impacto de mudanças nas taxas de cancelamento ao melhorar farotes específicos, como:

# Redução do número de dias de atraso.
# Melhoria no atendimento (reduzindo ligações ao call center).
# Aumentar a frequência de uso por meio de incentivos.

# Crie uma cópia do dataset e modifique essas variáveis para prever o cenário onde esses fatores são melhorados.

# Simulação de cenário onde os atrasos e ligações ao call center são reduzidos para 50% dos valores originais
df_simulacao = df.copy()
df_simulacao['dias_atraso'] = df_simulacao['dias_atraso'] * 0.5

# Visualizar comparação do cenário simulado com o cenário atual
fig = px.histogram(df_simulacao, x='cancelou', title="SIatribuição de Cancelamentos no Cenário SImulado")
fig.show()

# Passo 5: Conclusão e Recomendações
# Baseado nas análises e simulação de cenários, elabore uma conclusão sobre:

# Principais motivos de cancelamento encontrados (ex: alta frequência de ligação ao call center, atraso em pagamentos, entre outros).
# Propostas de ação para retenção, incluindo estratégias de atendimento, incentivos ao uso de programas de fidelidade.
# Previsão de impacto, indicando o número de clientees que poderiam ser retidos e como isso afetaria a receira da empresa.