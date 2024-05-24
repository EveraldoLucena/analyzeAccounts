import json
import pandas as pd


def media_historica_energetico(data_input):
    print("\nMédia Histórica Mês Anterior Energetico:")

    # Extracting the first account for comparison
    second_account = json.loads(data_input[1]["1"]["account"])

    # Extracting the relevant data for the first account
    account_data = {
        "consumo_p_1m": second_account.get("consumo", {}).get("np", 0),
        "consumo_int_1m": second_account.get("consumo", {}).get("inter", 0),
        "consumo_fp_1m": second_account.get("consumo", {}).get("fp", 0),
        "reativo_p_1m": (
            second_account.get("reativo", {}).get("np", 0)
            if "reativo" in second_account
            else 0
        ),
        "reativo_int_1m": (
            second_account.get("reativo", {}).get("inter", 0)
            if "reativo" in second_account
            else 0
        ),
        "reativo_fp_1m": (
            second_account.get("reativo", {}).get("fp", 0)
            if "reativo" in second_account
            else 0
        ),
        "geracao_1m": second_account.get("geracao", 0),
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
        "consumo_p_1m": first_account.get("cons", {}).get("np", 0),
        "consumo_int_1m": first_account.get("cons", {}).get("inter", 0),
        "consumo_fp_1m": first_account.get("cons", {}).get("fp", 0),
        "reativo_p_1m": (
            first_account.get("reativo", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_int_1m": (
            first_account.get("reativo", {}).get("inter", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_fp_1m": (
            first_account.get("reativo", {}).get("fp", 0)
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


def Convencional_energetico(data_input):
    print("\nHistorico Convencional Mês Anterior Energetico")
    data = json.loads(data_input)

    if data["consumo_fp_1m"] > 30 or data["reativo_fp_1m"] > 30:
        flag_historic = "red"

    elif (15 <= data["consumo_fp_1m"] <= 30) or (15 <= data["reativo_fp_1m"] <= 30):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def Branca_energetico(data_input):
    print("Historico Branca Mês Anterior Energetico")
    data = json.loads(data_input)

    if (
        data["consumo_fp_1m"] > 30
        or data["reativo_fp_1m"] > 30
        or data["consumo_int_1m"] > 30
        or data["reativo_int_1m"] > 30
        or data["consumo_p_1m"] > 30
        or data["reativo_p_1m"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_1m"] <= 30)
        or (15 <= data["reativo_fp_1m"] <= 30)
        or (15 <= data["consumo_int_1m"] <= 30)
        or (15 <= data["reativo_int_1m"] <= 30)
        or (15 <= data["consumo_p_1m"] <= 30)
        or (15 <= data["reativo_p_1m"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def GD_energetico(data_input):
    print("Historico GD Mês Anterior Energético:")
    data = json.loads(data_input)

    if (
        data["consumo_fp_1m"] > 30
        or data["reativo_fp_1m"] > 30
        or data["consumo_int_1m"] > 30
        or data["reativo_int_1m"] > 30
        or data["consumo_p_1m"] > 30
        or data["reativo_p_1m"] > 30
        or data["geracao_1m"] < -50
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_1m"] <= 30)
        or (15 <= data["reativo_fp_1m"] <= 30)
        or (15 <= data["consumo_int_1m"] <= 30)
        or (15 <= data["reativo_int_1m"] <= 30)
        or (15 <= data["consumo_p_1m"] <= 30)
        or (15 <= data["reativo_p_1m"] <= 30)
        or (-75 <= data["geracao_1m"] <= -50)
    ):
        flag_historic = "yellow"

    elif (
        (data["consumo_fp_1m"] <= -25)
        or (15 <= data["consumo_int_1m"] <= -25)
        or (15 <= data["consumo_p_1m"] <= -25)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_1m": flag_historic}
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
    variation_custo_json = json.dumps(variation_dict)

    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_custo_json = json.dumps(mean_values_dict)

    return variation_custo_json, mean_values_custo_json


def Convencional_custo(data_input):
    print("\nHistorico Convencional Mês Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_1m"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_1m"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def Branca_custo(data_input):
    print("Historico Branca Mês Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_1m"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_1m"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def GD_custo(data_input):
    print("Historico GD Mês Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_1m"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_1m"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_1m": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def baixa_Historic_1m(json_energetico, json_custo, modalidade_tarifaria, tipo_contrato):
    print("Analise Mês Anterior de Baixa:")
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
                    return (
                        output_analyse,
                        output_custo,
                        mean_values_json,
                        mean_values_custo_json,
                    )
                case "GD":
                    output_analyse = GD_energetico(variation_json)
                    output_custo = GD_custo(variation_custo_json)
                    return (
                        output_analyse,
                        output_custo,
                        mean_values_json,
                        mean_values_custo_json,
                    )

        case "BRANCA":
            output_analyse = Branca_energetico(variation_json)
            output_custo = Branca_custo(variation_custo_json)
            return (
                output_analyse,
                output_custo,
                mean_values_json,
                mean_values_custo_json,
            )
