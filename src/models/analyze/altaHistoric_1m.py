import json
import pandas as pd


def media_historica_energetico(data_input):
    print("\nMédia Histórica Mês Anterior Energetico:")

    # Extracting the first account for comparison
    second_account = json.loads(data_input[1]["1"]["account"])

    account_data = {
        "demanda_p_1m": second_account.get("demanda", {}).get("np", 0),
        "demanda_fp_1m": second_account.get("demanda", {}).get("fp", 0),
        "consumo_p_1m": second_account.get("consumo", {}).get("np", 0),
        "consumo_fp_1m": second_account.get("consumo", {}).get("fp", 0),
        "reativo_p_1m": (
            second_account.get("reativo", {}).get("np", 0)
            if "reativo" in second_account
            else 0
        ),
        "reativo_fp_1m": (
            second_account.get("reativo", {}).get("fp", 0)
            if "reativo" in second_account
            else 0
        ),
        "reativo_exc_p_1m": (
            second_account.get("reativo_exc", {}).get("np", 0)
            if "reativo" in second_account
            else 0
        ),
        "reativo_exc_fp_1m": (
            second_account.get("reativo_exc", {}).get("fp", 0)
            if "reativo" in second_account
            else 0
        ),
        "geracao_1m": second_account.get("ger", 0),
    }

    # Creating a DataFrame for the first account data
    df_account = pd.DataFrame([account_data])

    # Calculating the means
    mean_values = df_account.mean()

    # Display the mean values
    print(mean_values)

    # Extracting the first account for comparison
    first_account = json.loads(data_input[0]["0"]["account"])

    # Extracting the relevant data for the first account
    first_account_data = {
        "demanda_p_1m": first_account.get("demand", {}).get("np", 0),
        "demanda_fp_1m": first_account.get("demand", {}).get("fp", 0),
        "consumo_p_1m": first_account.get("cons", {}).get("np", 0),
        "consumo_fp_1m": first_account.get("cons", {}).get("fp", 0),
        "reativo_p_1m": (
            first_account.get("reativo", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_fp_1m": (
            first_account.get("reativo", {}).get("fp", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_exc_p_1m": (
            first_account.get("reativo_exc", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_exc_fp_1m": (
            first_account.get("reativo_exc", {}).get("fp", 0)
            if "reativo" in first_account
            else 0
        ),
        "geracao_1m": first_account.get("ger", 0),
    }

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Mês Anterior Energetico:")
    print(variation)

    variation = variation.fillna(0)
    variation_dict = variation.to_dict()
    variation_json = json.dumps(variation_dict)

    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_json = json.dumps(mean_values_dict)

    return variation_json, mean_values_json


def CT_energetico(data_input):
    print("\nHistorico Convencional Mês Anterior Energetico:")
    data = json.loads(data_input)

    if (
        data["demanda_p_1m"] > 30
        or data["demanda_fp_1m"] > 30
        or data["consumo_fp_1m"] > 30
        or data["consumo_p_1m"] > 30
        or data["reativo_exc_p_1m"] > 30
        or data["reativo_exc_fp_1m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_1m"] <= 30)
        or (15 <= data["demanda_p_1m"] <= 30)
        or (15 <= data["consumo_fp_1m"] <= 30)
        or (15 <= data["consumo_p_1m"] <= 30)
        or (15 <= data["reativo_exc_p_1m"] <= 30)
        or (15 <= data["reativo_exc_fp_1m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_eletrica_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def ML_energetico(data_input):
    print("Historico ML Mês Anterior Energetico:")
    data = json.loads(data_input)

    if (
        data["demanda_p_1m"] > 30
        or data["demanda_fp_1m"] > 30
        or data["consumo_fp_1m"] > 30
        or data["consumo_p_1m"] > 30
        or data["reativo_exc_p_1m"] > 30
        or data["reativo_exc_fp_1m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_1m"] <= 30)
        or (15 <= data["demanda_p_1m"] <= 30)
        or (15 <= data["consumo_fp_1m"] <= 30)
        or (15 <= data["consumo_p_1m"] <= 30)
        or (15 <= data["reativo_exc_p_1m"] <= 30)
        or (15 <= data["reativo_exc_fp_1m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_eletrica_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def media_historica_custo(data_input):
    print("\nMédia Histórica Mês Anterior Custo:")

    # Extracting the first account for comparison
    second_account = json.loads(data_input[1]["1"]["account"])

    # Extracting the relevant data for the first account
    account_data = {"valor_fat_1m": second_account.get("valor_fat", 0)}

    # Creating a DataFrame for the first account data
    df_account = pd.DataFrame([account_data])

    # Calculating the means
    mean_values = df_account.mean()

    # Display the mean values
    print(mean_values)
    
    # Extracting the first account for comparison
    first_account = json.loads(data_input[0]["0"]["account"])

    # Extracting the relevant data for the first account
    first_account_data = {"valor_fat_1m": first_account.get("total_fat", 0)}

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Mês Anterior Custo:")
    print(variation)

    variation = variation.fillna(0)
    variation_dict = variation.to_dict()
    variation_json = json.dumps(variation_dict)

    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_custo_json = json.dumps(mean_values_dict)

    return variation_json, mean_values_custo_json


def CT_custo(data_input):
    print("\nHistorico Convencional Mês Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_1m"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_1m"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_custo_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def ML_custo(data_input):
    print("Historico ML Mês Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_1m"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_1m"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_custo_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def alta_Historic_1m(json_energetico, json_custo, modalidade_tarifaria, tipo_contrato):
    print("Analise Mês Anterior de Alta:")
    try:
        historic_energetico = json.loads(json_energetico)
        historic_custo = json.loads(json_custo)
        variation_json, mean_values_json = media_historica_energetico(historic_energetico)
        variation_custo_json, mean_values_custo_json = media_historica_custo(historic_custo)

        match tipo_contrato:
            case "CT":
                print("CT")
                output_analyse = CT_energetico(variation_json)
                output_custo = CT_custo(variation_custo_json)
                return (
                    output_analyse,
                    output_custo,
                    mean_values_json,
                    mean_values_custo_json,
                )
            case "ML":
                print("ML")
                output_analyse = ML_energetico(variation_json)
                output_custo = ML_custo(variation_custo_json)
                return (
                    output_analyse,
                    output_custo,
                    mean_values_json,
                    mean_values_custo_json,
                )
    except:
        print("Sem Conta do Mês Anterior")
        output_analyse = {
            "demanda_p_1m": 0.0,
            "demanda_fp_1m": 0.0,
            "consumo_p_1m": 0.0,
            "consumo_fp_1m": 0.0,
            "reativo_p_1m": 0.0,
            "reativo_fp_1m": 0.0,
            "reativo_exc_p_1m": 0.0,
            "reativo_exc_fp_1m": 0.0,
            "geracao_1m": 0.0,
            "flag_hist_eletrica_1m": "green",
        }
        output_custo = {"valor_fat_1m": 0.0, "flag_hist_custo_1m": "green"}
        mean_values_json = {
            "demanda_p_1m": 0.0,
            "demanda_fp_1m": 0.0,
            "consumo_p_1m": 0.0,
            "consumo_fp_1m": 0.0,
            "reativo_p_1m": 0.0,
            "reativo_fp_1m": 0.0,
            "reativo_exc_p_1m": 0.0,
            "reativo_exc_fp_1m": 0.0,
            "geracao_1m": 0.0,
        }
        mean_values_custo_json = {"valor_fat_1m": 0.0}

        output_analyse = json.dumps(output_analyse)
        output_custo = json.dumps(output_custo)
        mean_values_json = json.dumps(mean_values_json)
        mean_values_custo_json = json.dumps(mean_values_custo_json)

        return output_analyse, output_custo, mean_values_json, mean_values_custo_json   
