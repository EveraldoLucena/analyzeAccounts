from src.controllers.readDados import getDados
from src.controllers.analyzeDados import getAnalyze
from src.controllers.getHistoricAnalyze import getHistoricAnalyze
from src.controllers.update import updateDocument


def action_type(cliente_req, cod_inst, document_id):
    action = cliente_req["action"]
    match action:
        case "read":
            result_read = getDados(cliente_req)
            return result_read
        case "analyze":
            result_read = getDados(cliente_req)
            result_analyze, result_account = getAnalyze(result_read)
            (
                output_analyse_12m,
                output_custo_12m,
                output_analyse_1m,
                output_custo_1m,
                mean_values_12m,
                mean_values_custo_12m,
                mean_values_1m,
                mean_values_custo_1m,
                output_analyse_moly,
                output_custo_moly,
                mean_values_moly,
                mean_values_custo_moly,
            ) = getHistoricAnalyze(result_analyze, cod_inst, document_id)
            updateDocument(
                document_id,
                result_account,
                output_analyse_12m,
                output_custo_12m,
                output_analyse_1m,
                output_custo_1m,
                mean_values_12m,
                mean_values_custo_12m,
                mean_values_1m,
                mean_values_custo_1m,
                output_analyse_moly,
                output_custo_moly,
                mean_values_moly,
                mean_values_custo_moly,
            )

            return
