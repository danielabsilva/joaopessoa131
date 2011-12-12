geimport json
import urllib

url = "http://0.0.0.0:5000/test/joaopessoa131/empenhos.json?fornecedor=FENICIA%20VIAGENS%20E%20TURISMO%20LTDA&ano=2010&mes=1"
arquivo = urllib.urlopen(url)
jason = json.load(arquivo)

total = 0
for empenho in jason:
    print empenho['historico']
#    total = total + int(empenho['valor'].strip("R$ ")[:-3].replace(".",""))#
#print total
    
