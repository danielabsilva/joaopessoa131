#-*- coding: utf-8 -*-

from webstore.client import Database
import urllib
from lxml.html import parse

entidades = {
    "2" : "Autarquia Especial Municipal de Limpeza Urbana - EMLUR",
    "13" : "Fundo Municipal de Saúde - FMS",
    "35" : "Fundo Municipal de Urbanização - FUNDURB",
    "33" : "Fundo Municipal de Apoio aos Pequenos Negócios",
    "10" : "Fundação Cultural de João Pessoa - FUNJOPE",
    "23" : "Instituto Cândida Vargas",
    "6" : "Instituto de Previdência Municipal - IPM",
    "8" : "Superintendência de Transportes e Trânsito - STTRANS"
    }

def monta_url():
    for ano in range(2010,2011):
        for mes in range(1,13):
            for entidade in entidades.iterkeys():
                url_base = "http://www2.joaopessoa.pb.gov.br:8080/lei131/DespesaEntidadeIndireta?ano=" + str(ano) + "&mes=" + str(mes) + "&entidade=" + entidade
                extract(url_base, entidades[entidade], entidade, ano, mes)
   
def extract(url_base, entidade, id_entidade, ano, mes):
    print "Getting " + entidade + " do mês " + str(mes) + " de " + str(ano)

    database = Database('0.0.0.0', 'test', 'joaopessoa131', port="5000")
    html = parse(url_base).getroot()
    tabela = html.cssselect(".bordatabela2")[0]
    linhas = tabela.cssselect("tr")
    linhas.pop(0)
    for linha in linhas:
        data = {}
        data["n_empenho"] = linha.cssselect("td")[0].text
        data["link_empenho"] = "http://www2.joaopessoa.pb.gov.br:8080/lei131/" + linha.cssselect("td")[0].get("onclick").split("'")[1]
        data["data_movimentacao"] = linha.cssselect("td")[1].text
        data["elemento"] = linha.cssselect("td")[2].text
        data["tipo"] = linha.cssselect("td")[3].text
        data["fornecedor"] = linha.cssselect("td")[4].text
        data["fonte_recurso"] = linha.cssselect("td")[5].text
        data["valor"] = linha.cssselect("td")[6].text
        data["orgao"] = entidade
        data["id_orgao"] = id_entidade
        data["ano"] = str(ano)
        data["mes"] = str(mes)
        database['empenhos'].writerow(data, unique_columns=['n_empenho'])

monta_url()
