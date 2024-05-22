from src.models.analyze.baixa import analyze_baixa
from src.models.analyze.alta import analyze_alta
from src.models.analyze.altaHistoric_12m import alta_Historic_12m
from src.models.analyze.baixaHistoric_12m import baixa_Historic_12m
from src.models.analyze.baixaHistoric_12m import leitura_baixa_energetico
from src.models.analyze.altaHistoric_12m import leitura_alta_energetico
from src.models.analyze.baixaHistoric_12m import leitura_baixa_custo
from src.models.analyze.altaHistoric_12m import leitura_alta_custo
from src.controllers.analyzeflag import flag
import json


def getAnalyze(result_read):
    read = json.loads(result_read)

    match read['data']['read']['subgrupo'][0]:
        case 'B':
            output_analyze = analyze_baixa(result_read)
            result_account = flag(output_analyze)
            return output_analyze, result_account
        case 'A':
            output_analyze = analyze_alta(result_read)
            result_account = flag(output_analyze)
            return output_analyze, result_account

def getHistoric(json_energetico, json_custo, subgrupo, modalidade_tarifaria, tipo_contrato):
    match subgrupo[0]:
        case 'B':
            output_analyse_12m, output_custo_12m = baixa_Historic_12m(json_energetico, json_custo, modalidade_tarifaria, tipo_contrato)
            return output_analyse_12m, output_custo_12m
        case 'A':
            output_analyse_12m, output_custo_12m = alta_Historic_12m(json_energetico, json_custo, modalidade_tarifaria, tipo_contrato)
            return output_analyse_12m, output_custo_12m
        
def getleituraHistoric(result_read):
    match result_read['data']['read']['subgrupo'][0]:
        case 'B':
            output_analyze = leitura_baixa_energetico(result_read)
            output_custo = leitura_alta_custo(result_read)
            return output_analyze, output_custo
        case 'A':
            output_analyze = leitura_alta_energetico(result_read)
            output_custo = leitura_alta_custo(result_read)
            return output_analyze, output_custo