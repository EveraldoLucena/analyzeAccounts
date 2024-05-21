from src.controllers.readDados import getDados
from src.controllers.analyzeDados import getAnalyze
from src.controllers.getHistoricAnalyze import getHistoricAnalyze
from src.controllers.update import updateDocument

def action_type(cliente_req, cod_inst, document_id):
    action = cliente_req['action']
    match action:
        case 'read':
            result_read = getDados(cliente_req)
            return result_read
        case 'analyze':
            result_read = getDados(cliente_req)
            result_analyze, result_account = getAnalyze(result_read)
            result_historic = getHistoricAnalyze(result_analyze, cod_inst, document_id)
            updateDocument(document_id, result_account, result_historic)
            
            return 
