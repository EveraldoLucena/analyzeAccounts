from src.models.analyze.baixa import analyze_baixa
from src.models.analyze.alta import analyze_alta
import json


def getAnalyze(result_read):
    read = json.loads(result_read)

    match read['data']['read']['subgrupo'][0]:
        case 'B':
            output_analyze = analyze_baixa(result_read)
            return output_analyze
        case 'A':
            output_analyze = analyze_alta(result_read)
            return output_analyze
