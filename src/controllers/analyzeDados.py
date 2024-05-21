from src.models.analyze.baixa import analyze_baixa
from src.models.analyze.alta import analyze_alta
from src.models.analyze.baixaHistoric import baixa_Historic
from src.models.analyze.baixaHistoric import leitura_baixa
from src.models.analyze.altaHistoric import leitura_alta
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
            return output_analyze,  

def getHistoric(json_output, subgrupo, modalidade_tarifaria, tipo_contrato):
    match subgrupo[0]:
        case 'B':
            analyze_historic = baixa_Historic(json_output, modalidade_tarifaria, tipo_contrato)
            return analyze_historic
        case 'A':
            analyze_historic = leitura_alta(json_output, modalidade_tarifaria, tipo_contrato)
            return analyze_historic
        
def getleituraHistoric(result_read):
    match result_read['data']['read']['subgrupo'][0]:
        case 'B':
            output_analyze = leitura_baixa(result_read)
            return output_analyze
        case 'A':
            output_analyze = leitura_alta(result_read)
            return output_analyze