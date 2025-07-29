import pandas as pd

# Caminho do arquivo
arquivo_excel = "F:\RPA\PythonAutomacaoClientesFisioterapia.xlsx"  #

# Leitura usando Pandas
abas = pd.read_excel(arquivo_excel, sheet_name=None)
# Armazena abas em variáveis
clientes = abas["CLIENTES"]
agenda = abas["07-2025"]
# Converte a coluna DURACAO para timedelta, para podermos fazer as operações
agenda["DURACAO"] = pd.to_timedelta(agenda["DURACAO"].astype(str))

# Merge CLIENTES usando CPF
agenda_completa = agenda.merge(clientes, on="CPF", how="left")

# Função para formatar e juntar as datas numa string separada por '; '
def juntar_datas(datas):
    return '; '.join(datas.dt.strftime('%d/%m/%Y').sort_values())

# Agrupa por ALUNO e CPF, junta as datas achadas, soma duração total e pega pagamento
resumo = agenda_completa.groupby(["ALUNO", "CPF"]).agg({
    "DATA": juntar_datas,
    "DURACAO": "sum",
    "PAGAMENTO": "first"
}).reset_index()

# Renomeia colunas DATAS e DURACAO_TOTAL
resumo.rename(columns={"DATA": "DATAS", "DURACAO": "DURACAO_TOTAL"}, inplace=True)

# Converte duração total para horas decimais arredondadas
resumo["DURACAO_TOTAL"] = resumo["DURACAO_TOTAL"].dt.total_seconds() / 3600
resumo["DURACAO_TOTAL"] = resumo["DURACAO_TOTAL"].round(1)

# Calcula valor a pagar, estabelecendo o valor fixo de 50 reais a hora
def calcular_pagamento(row):
    preco_hora = 50
    duracao = row["DURACAO_TOTAL"]
    if row["PAGAMENTO"] == "PACOTE":
        return 0
    elif row["PAGAMENTO"] == "AVULSO":
        return duracao * preco_hora
    else:
        return duracao * preco_hora

resumo["A_PAGAR"] = resumo.apply(calcular_pagamento, axis=1)

# Reorganiza colunas
resumo = resumo[["ALUNO", "CPF", "DATAS", "DURACAO_TOTAL", "A_PAGAR"]]

# Salva no Excel, sobrescrevendo a aba consolidada
with pd.ExcelWriter("F:\RPA\PythonAutomacaoClientesFisioterapia.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
    resumo.to_excel(writer, sheet_name="CONSOLIDADO-07-2025", index=False)


print('Final de Execução!')