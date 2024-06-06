from src.controllers.dataFirestore import FirestoreDatabase
import json

db = FirestoreDatabase()


def updateDocument(
    doc_id,
    result_account,
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
):
    print("\nSalvando Análise...")
    result_account = json.loads(result_account)
    db.update_analyzes_account(doc_id, result_account)

    try:
        print("\nAnálise Elétrica 12M:")
        output_analyse_12m = json.loads(output_analyse_12m)
        db.update_eletric_analyzes(doc_id, output_analyse_12m)

        print("\nAnálise Custo 12M:")
        output_custo_12m = json.loads(output_custo_12m)
        db.update_cust_analyzes(doc_id, output_custo_12m)

        print("\nMédia Elétrica dos 12M:")
        mean_values_12m = json.loads(mean_values_12m)
        db.update_means_12m(doc_id, mean_values_12m)

        print("\nMédia Custo dos 12M:")
        mean_values_custo_12m = json.loads(mean_values_custo_12m)
        db.update_means_12m(doc_id, mean_values_custo_12m)
    except:
        pass


    try:
        print("\nAnálise Elétrica Mês Anterior:")
        output_analyse_1m = json.loads(output_analyse_1m)
        db.update_eletric_analyzes(doc_id, output_analyse_1m)

        print("\nAnálise Custo Mês Anterior:")
        output_custo_1m = json.loads(output_custo_1m)
        db.update_cust_analyzes(doc_id, output_custo_1m)

        print("\nElétrica Mês Anterior:")
        mean_values_1m = json.loads(mean_values_1m)
        db.update_last_month(doc_id, mean_values_1m)

        print("\nCusto Mês Anterior:")
        mean_values_custo_1m = json.loads(mean_values_custo_1m)
        db.update_last_month(doc_id, mean_values_custo_1m)
    except:
        pass


    try:
        print("\nAnálise Elétrica Mês do Ano Anterior:")
        output_analyse_map = json.loads(output_analyse_map)
        db.update_eletric_analyzes(doc_id, output_analyse_map)

        print("\nAnálise Custo Mês do Ano Anterior:")
        output_custo_map = json.loads(output_custo_map)
        db.update_cust_analyzes(doc_id, output_custo_map)

        print("\nElétrica Mês do Ano Anterior:")
        mean_values_map = json.loads(mean_values_map)
        db.update_map(doc_id, mean_values_map)

        print("\nCusto Mês do Ano Anterior:")
        mean_values_custo_map = json.loads(mean_values_custo_map)
        db.update_map(doc_id, mean_values_custo_map)
    except:
        pass

    return
