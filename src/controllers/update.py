from src.controllers.dataFirestore import FirestoreDatabase
import json
db = FirestoreDatabase()

def updateDocument(doc_id, result_account, output_analyse_12m, output_custo_12m):
    print("\nSalvando Análise...")
    result_account = json.loads(result_account)
    response =  db.update_analyzes_account(doc_id, result_account)
    print("\n", response)

    try:
        output_analyse_12m = json.loads(output_analyse_12m)
        response = db.update_eletric_analyzes(doc_id, output_analyse_12m)
        print("\n", response)
        output_custo_12m = json.loads(output_custo_12m)
        response = db.update_cust_analyzes(doc_id, output_custo_12m)
        print("\n", response)
     
    except Exception as error:
        print("An exception occurred:", error)
    
    return
