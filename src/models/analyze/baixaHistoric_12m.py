import json
import pandas as pd
import numpy as np

def leitura_baixa_energetico(input):
    data_input = input["data"]["read"]
    cons = data_input["leitura"]["cons"]
    reativo = data_input["leitura"]["reativo"]
    ger = data_input["leitura"]["ger"]

    output = {"consumo": cons, "reativo": reativo, "geracao": ger}

    output_json = json.dumps(output)
    return output_json

def media_historica_energetico(data_input):
    print("\nMédia Histórica Energetico:")

    # Parsing JSON data and extracting relevant fields starting from the second account
    accounts_data = [
        json.loads(item[str(i)]["account"]) for i, item in enumerate(data_input)
    ][1:]

    # Creating a DataFrame
    df = pd.DataFrame(
        [
            {
                "consumo_np_12m": (
                    item.get("cons", {}).get("np", 0)
                    if "cons" in item
                    else item.get("consumo", {}).get("np", 0)
                ),
                "consumo_inter_12m": (
                    item.get("cons", {}).get("inter", 0)
                    if "cons" in item
                    else item.get("consumo", {}).get("inter", 0)
                ),
                "consumo_fp_12m": (
                    item.get("cons", {}).get("fp", 0)
                    if "cons" in item
                    else item.get("consumo", {}).get("fp", 0)
                ),
                "reativo_np_12m": item.get("reativo", {}).get("np", 0),
                "reativo_inter_12m": item.get("reativo", {}).get("inter", 0),
                "reativo_fp_12m": item.get("reativo", {}).get("fp", 0),
                "geracao_12m": (
                    item.get("ger", 0) if "ger" in item else item.get("geracao", 0)
                ),
            }
            for item in accounts_data
        ]
    )

    # Calculating the means
    mean_values = df.mean()

    # Display the mean values
    print(mean_values)

    # Extracting the first account for comparison
    first_account = json.loads(data_input[0]["0"]["account"])

    # Extracting the relevant data for the first account
    first_account_data = {
        "consumo_np_12m": first_account.get("cons", {}).get("np", 0),
        "consumo_inter_12m": first_account.get("cons", {}).get("inter", 0),
        "consumo_fp_12m": first_account.get("cons", {}).get("fp", 0),
        "reativo_np_12m": (
            first_account.get("reativo", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_inter_12m": (
            first_account.get("reativo", {}).get("inter", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_fp_12m": (
            first_account.get("reativo", {}).get("fp", 0)
            if "reativo" in first_account
            else 0
        ),
        "geracao_12m": first_account.get("ger", 0),
    }

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Energetico:")
    print(variation)

    variation = variation.fillna(0)
    variation_dict = variation.to_dict()
    variation_json = json.dumps(variation_dict)
    
    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_json = json.dumps(mean_values_dict)

    return variation_json, mean_values_json

def Convencional_energetico(data_input):
    print("\nHistorico Convencional Energetico")
    data = json.loads(data_input)

    if data["consumo_fp_12m"] > 30 or data["reativo_fp_12m"] > 30:
        flag_historic = "red"

    elif (15 <= data["consumo_fp_12m"] <= 30) or (15 <= data["reativo_fp_12m"] <= 30):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_12m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic

def Branca_energetico(data_input):
    print("Historico Branca Energetico")
    data = json.loads(data_input)

    if (
        data["consumo_fp_12m"] > 30
        or data["reativo_fp_12m"] > 30
        or data["consumo_inter_12m"] > 30
        or data["reativo_inter_12m"] > 30
        or data["consumo_np_12m"] > 30
        or data["reativo_np_12m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_12m"] <= 30)
        or (15 <= data["reativo_fp_12m"] <= 30)
        or (15 <= data["consumo_inter_12m"] <= 30)
        or (15 <= data["reativo_inter_12m"] <= 30)
        or (15 <= data["consumo_np_12m"] <= 30)
        or (15 <= data["reativo_fp_12m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_12m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic

def GD_energetico(data_input):
    print("Historico GD")
    data = json.loads(data_input)

    if (
        data["consumo_fp_12m"] > 30
        or data["reativo_fp_12m"] > 30
        or data["consumo_inter_12m"] > 30
        or data["reativo_inter_12m"] > 30
        or data["consumo_np_12m"] > 30
        or data["reativo_np_12m"] > 30
        or data["geracao_12m"] < -50
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_12m"] <= 30)
        or (15 <= data["reativo_fp_12m"] <= 30)
        or (15 <= data["consumo_inter_12m"] <= 30)
        or (15 <= data["reativo_inter_12m"] <= 30)
        or (15 <= data["consumo_np_12m"] <= 30)
        or (15 <= data["reativo_np_12m"] <= 30)
        or (-75 <= data["geracao_12m"] <= -50)
    ):
        flag_historic = "yellow"
    
    elif (
        (data["consumo_fp_12m"] <= -25)
        or (15 <= data["consumo_inter_12m"] <= -25)
        or (15 <= data["consumo_np_12m"] <= -25)

    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_12m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic

def leitura_baixa_custo(input):
    data_input = input["data"]["read"]
    total = data_input["detalh_fat"]["valor_final_faturado"]

    output = {
        "valor_fat": total
    }

    output_fat_json = json.dumps(output)
    return output_fat_json

def media_historica_custo(data_input):
    print("\nMédia Histórica Custo:")

    # Parsing JSON data and extracting relevant fields starting from the second account
    accounts_data = [
        json.loads(item[str(i)]["account"]) for i, item in enumerate(data_input)
    ][1:]

    # Creating a DataFrame
    df = pd.DataFrame(
        [
            {
                "valor_fat_12m": (
                    item.get("valor_fat", 0)
                    if "valor_fat" in item
                    else item.get("valor_fat", 0)
                )
            }
            for item in accounts_data
        ]
    )

    # Calculating the means
    mean_values = df.mean()

    # Display the mean values
    print(mean_values)

    # Extracting the first account for comparison
    first_account = json.loads(data_input[0]["0"]["account"])

    # Extracting the relevant data for the first account
    first_account_data = {
        "valor_fat_12m": first_account.get("total_fat", 0)
    }

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Custo:")
    print(variation)

    variation = variation.fillna(0)
    variation_dict = variation.to_dict()
    variation_custo_json = json.dumps(variation_dict)
    
    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_custo_json = json.dumps(mean_values_dict)

    return variation_custo_json, mean_values_custo_json

def Convencional_custo(data_input):
    print("\nHistorico Convencional Custo:")
    data = json.loads(data_input)

    if (
        data["valor_fat_12m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["valor_fat_12m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_12m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic

def Branca_custo(data_input):
    print("Historico Branca Custo")
    data = json.loads(data_input)

    if (
        data["valor_fat_12m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["valor_fat_12m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_12m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic

def GD_custo(data_input):
    print("Historico GD Custo")
    data = json.loads(data_input)

    if (
        data["valor_fat_12m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["valor_fat_12m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_12m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def baixa_Historic_12m(json_energetico, json_custo, modalidade_tarifaria, tipo_contrato):
    print("Analise Historico de Baixa:")
    historic_energetico = json.loads(json_energetico)
    historic_custo = json.loads(json_custo)
    variation_json, mean_values_json = media_historica_energetico(historic_energetico)
    variation_custo_json, mean_values_custo_json = media_historica_custo(historic_custo)

    match modalidade_tarifaria:
        case "CONVENCIONAL":
            match tipo_contrato:
                case "CT":
                    output_analyse = Convencional_energetico(variation_json)
                    output_custo = Convencional_custo(variation_custo_json)
                    return output_analyse, output_custo, mean_values_json, mean_values_custo_json
                case "GD":
                    output_analyse = GD_energetico(variation_json)
                    output_custo = GD_custo(variation_custo_json)
                    return output_analyse, output_custo, mean_values_json, mean_values_custo_json

        case "BRANCA":
            output_analyse = Branca_energetico(variation_json)
            output_custo = Branca_custo(variation_custo_json)
            return output_analyse, output_custo, mean_values_json, mean_values_custo_json
