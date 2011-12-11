#-*- coding: utf-8 -*-
import urllib
from lxml.html import parse
import json

arquivo = urllib.urlopen("empenhos.json")

def pega_link():
	empenhos = json.load(arquivo)
	for empenho in empenhos:
		if empenho["link_empenho"][:4] != "http":
			pega_dados("http://www2.joaopessoa.pb.gov.br:8080/lei131/" + empenho["link_empenho"])
		else:
			pega_dados(empenho["link_empenho"])

def pega_dados(url_base):
	html = parse(url_base).getroot()
	tabela = html.cssselect(".tabelaDetalhe")[0]
	linhas = tabela.cssselect("tr")
	tabela2 = html.cssselect(".tabelaDetalhe")[2]
	linhas2 = tabela2.cssselect("tr")
	data = {}
	data["n_empenho"] = linhas[0].cssselect("td")[1].text
	data["data_empenho"] = linhas[1].cssselect("td")[1].text
	data["tipo_empenho"] = linhas[2].cssselect("td")[1].text
	data["elemento_despesas"] = linhas[3].cssselect("td")[1].text
	data["fonte_recurso"] = linhas[4].cssselect("td")[1].text
	data["fornecedor"] = linhas[5].cssselect("td")[1].text
	data["n_processo_pagamento"] = linhas[6].cssselect("td")[1].text
	data["modalidade_n_licitacao"] = linhas[7].cssselect("td")[1].text
	data["tipo_despesa"] = linhas[8].cssselect("td")[1].text
	data["historico"] = linhas[9].cssselect("td")[1].text
	data["valores"] = []
	for linha2 in linhas2:
		valores = {}
		valores["tipo_movimento"] = linha2.cssselect("td")[0].text
		valores["data_movimento"] = linha2.cssselect("td")[1].text
		valores["parcela"] = linha2.cssselect("td")[2].text
		valores["valor"] = linha2.cssselect("td")[3].text
		data["valores"].append(valores)
	print data

pega_link()

