from src.controllers.dataFirestore import FirestoreDatabase
import json
db = FirestoreDatabase()

def updateDocument(doc_id, result_account, output_analyse_12m, output_custo_12m, output_analyse_1m, output_custo_1m, mean_values_12m, mean_values_custo_12m, mean_values_1m, mean_values_custo_1m):
    print("\nSalvando Análise...")
    result_account = json.loads(result_account)
    response =  db.update_analyzes_account(doc_id, result_account)
    print("\n", response)

    try:
        print("\nAnálise Elétrica 12M: OK!")
        output_analyse_12m = json.loads(output_analyse_12m)
        response = db.update_eletric_analyzes(doc_id, output_analyse_12m)
        print("\n", response)
        print("\nAnálise Custo 12M: OK!")
        output_custo_12m = json.loads(output_custo_12m)
        response = db.update_cust_analyzes(doc_id, output_custo_12m)
        print("\n", response)
        
        print("\nAnálise Elétrica 1M: OK!")
        output_analyse_1m = json.loads(output_analyse_1m)
        response = db.update_eletric_analyzes(doc_id, output_analyse_1m)
        print("\n", response)
        print("\nAnálise Custo 1M: OK!")
        output_custo_1m = json.loads(output_custo_1m)
        response = db.update_cust_analyzes(doc_id, output_custo_1m)
        print("\n", response)
        
        print("\nMédia Elétrica dos 12M: OK!")
        mean_values_12m = json.loads(mean_values_12m)
        response = db.update_means_12m(doc_id, mean_values_12m)
        print("\n", response)
        print("\nMédia Custo dos 12M: OK!")
        mean_values_custo_12m = json.loads(mean_values_custo_12m)
        response = db.update_means_12m(doc_id, mean_values_custo_12m)
        print("\n", response)
        
        print("\nElétrica Mês Anterior: OK!")
        mean_values_1m = json.loads(mean_values_1m)
        response = db.update_last_month(doc_id, mean_values_1m)
        print("\n", response)
        print("\nCusto Mês Anterior: OK!")
        mean_values_custo_1m = json.loads(mean_values_custo_1m)
        response = db.update_last_month(doc_id, mean_values_custo_1m)
        print("\n", response)
     
    except Exception as error:
        print("An exception occurred:", error)
    
    return
