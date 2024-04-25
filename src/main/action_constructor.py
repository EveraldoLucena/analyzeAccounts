from src.controllers.readDados import getDados
from src.controllers.analyzeDados import getAnalyze
from src.controllers.analyzeflag import flag

def action_type(cliente_req):
    action = cliente_req['action']
    match action:
        case 'read':
            result_read = getDados(cliente_req)
            return result_read
        case 'analyze':
            result_read = getDados(cliente_req)
            result_analyze = getAnalyze(result_read)
            result = flag(result_analyze)
            return result
