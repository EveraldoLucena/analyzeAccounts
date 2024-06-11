from src.controllers.dataFirestore import FirestoreDatabase
from src.controllers.getInfoaccount import Cliente
from src.controllers.readDados import getDados
from src.controllers.analyzeDados import getHistoric
from src.controllers.analyzeDados import getleituraHistoric
from datetime import datetime
import json

db = FirestoreDatabase()


def getHistoricAnalyze(result, cod_inst, document_id):
    print(f"Código de instalção: {cod_inst}")
    accounts = db.get_documents_by_installation_code(cod_inst)
    accounts.remove(document_id)
    print(f"Contas encontradas: {accounts}")

    try:
        historic = []
        for account in accounts:
            request = {"document_id": "account", "action": "read"}
            document_data = db.get_document(account)
            subgrupo = document_data["data"]["dados"]["unidade_consumidora"]["subgrupo"]
            modalidade_tarifaria = document_data["data"]["dados"][
                "unidade_consumidora"
            ]["modalidade_tarifaria"]
            tipo_contrato = document_data["data"]["dados"]["unidade_consumidora"][
                "tipo_contrato"
            ]
            client = Cliente(
                subgrupo, modalidade_tarifaria, tipo_contrato, document_data, request
            )
            response = client.process_request()
            result_read = getDados(response)
            historic.append(result_read)

        # Parse the JSON strings into dictionaries
        parsed_historic = [
            json.loads(entry) if isinstance(entry, str) else entry for entry in historic
        ]

        # Function to convert date string to datetime object
        def parse_date(date_str):
            return datetime.fromisoformat(date_str.replace("Z", "+00:00"))

        # Sorting the historic list by 'mes_ref' in descending order
        sorted_historic = sorted(
            parsed_historic,
            key=lambda x: parse_date(x["data"]["read"]["mes_ref"]),
            reverse=True,
        )

        # Creating a new list with the organized data
        organized_historic = [entry for entry in sorted_historic]

        merged_energetico_12m = []
        merged_custo_12m = []
        for i, account_data in enumerate(organized_historic[:11], 1):
            output_energetico, output_custo = getleituraHistoric(account_data)
            obj_energetico = {str(i): {"account": output_energetico}}
            merged_energetico_12m.append(obj_energetico)
            obj_custo = {str(i): {"account": output_custo}}
            merged_custo_12m.append(obj_custo)

        new_entry = {"0": {"account": result}}
        merged_energetico_12m.insert(0, new_entry)
        merged_custo_12m.insert(0, new_entry)
        json_energetico = json.dumps(merged_energetico_12m, indent=2)
        json_custo = json.dumps(merged_custo_12m, indent=2)

        print(json_energetico)
        print(json_custo)

        (
            output_analyse_12m,
            output_custo_12m,
            output_analyse_1m,
            output_custo_1m,
            mean_values_12m,
            mean_values_custo_12m,
            mean_values_1m,
            mean_values_custo_1m,
            output_analyse_map,
            output_custo_map,
            mean_values_map,
            mean_values_custo_map,
        ) = getHistoric(
            json_energetico, json_custo, subgrupo, modalidade_tarifaria, tipo_contrato
        )
        return (
            output_analyse_12m,
            output_custo_12m,
            output_analyse_1m,
            output_custo_1m,
            mean_values_12m,
            mean_values_custo_12m,
            mean_values_1m,
            mean_values_custo_1m,
            output_analyse_map,
            output_custo_map,
            mean_values_map,
            mean_values_custo_map,
        )
    except Exception as error:
        print("An exception occurred: Sem histórico!", error)
        pass
