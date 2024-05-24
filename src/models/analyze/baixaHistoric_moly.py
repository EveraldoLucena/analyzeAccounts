import json
import pandas as pd


def media_historica_energetico(data_input):
    print("\nMédia Histórica Mês do Ano Anterior Energetico:")

    # Extracting the first account for comparison
    yearago_account = json.loads(data_input[12]["12"]["account"])

    # Extracting the relevant data for the first account
    account_data = {
        "consumo_np_moly": yearago_account.get("consumo", {}).get("np", 0),
        "consumo_inter_moly": yearago_account.get("consumo", {}).get("inter", 0),
        "consumo_fp_moly": yearago_account.get("consumo", {}).get("fp", 0),
        "reativo_np_moly": (
            yearago_account.get("reativo", {}).get("np", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "reativo_inter_moly": (
            yearago_account.get("reativo", {}).get("inter", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "reativo_fp_moly": (
            yearago_account.get("reativo", {}).get("fp", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "geracao_moly": yearago_account.get("geracao", 0),
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
        "consumo_np_moly": first_account.get("cons", {}).get("np", 0),
        "consumo_inter_moly": first_account.get("cons", {}).get("inter", 0),
        "consumo_fp_moly": first_account.get("cons", {}).get("fp", 0),
        "reativo_np_moly": (
            first_account.get("reativo", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_inter_moly": (
            first_account.get("reativo", {}).get("inter", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_fp_moly": (
            first_account.get("reativo", {}).get("fp", 0)
            if "reativo" in first_account
            else 0
        ),
        "geracao_moly": first_account.get("ger", 0),
    }

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Mês do Ano Anterior Energetico:")
    print(variation)

    variation = variation.fillna(0)
    variation_dict = variation.to_dict()
    variation_json = json.dumps(variation_dict)

    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_json = json.dumps(mean_values_dict)
    print(mean_values_json)

    return variation_json, mean_values_json


def Convencional_energetico(data_input):
    print("\nHistorico Convencional Mês do Ano Anterior Energetico")
    data = json.loads(data_input)

    if data["consumo_fp_moly"] > 30 or data["reativo_fp_moly"] > 30:
        flag_historic = "red"

    elif (15 <= data["consumo_fp_moly"] <= 30) or (15 <= data["reativo_fp_moly"] <= 30):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_moly": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def Branca_energetico(data_input):
    print("Historico Branca Mês do Ano Anterior Energetico")
    data = json.loads(data_input)

    if (
        data["consumo_fp_moly"] > 30
        or data["reativo_fp_moly"] > 30
        or data["consumo_inter_moly"] > 30
        or data["reativo_inter_moly"] > 30
        or data["consumo_np_moly"] > 30
        or data["reativo_np_moly"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_moly"] <= 30)
        or (15 <= data["reativo_fp_moly"] <= 30)
        or (15 <= data["consumo_inter_moly"] <= 30)
        or (15 <= data["reativo_inter_moly"] <= 30)
        or (15 <= data["consumo_np_moly"] <= 30)
        or (15 <= data["reativo_fp_moly"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_moly": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def GD_energetico(data_input):
    print("Historico GD Mês do Ano Anterior Energético:")
    data = json.loads(data_input)

    if (
        data["consumo_fp_moly"] > 30
        or data["reativo_fp_moly"] > 30
        or data["consumo_inter_moly"] > 30
        or data["reativo_inter_moly"] > 30
        or data["consumo_np_moly"] > 30
        or data["reativo_np_moly"] > 30
        or data["geracao_moly"] < -50
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_moly"] <= 30)
        or (15 <= data["reativo_fp_moly"] <= 30)
        or (15 <= data["consumo_inter_moly"] <= 30)
        or (15 <= data["reativo_inter_moly"] <= 30)
        or (15 <= data["consumo_np_moly"] <= 30)
        or (15 <= data["reativo_np_moly"] <= 30)
        or (-75 <= data["geracao_moly"] <= -50)
    ):
        flag_historic = "yellow"

    elif (
        (data["consumo_fp_moly"] <= -25)
        or (15 <= data["consumo_inter_moly"] <= -25)
        or (15 <= data["consumo_np_moly"] <= -25)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Historic_moly": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def media_historica_custo(data_input):
    print("\nMédia Histórica Mês do Ano Anterior Custo:")

    # Extracting the first account for comparison
    yearago_account = json.loads(data_input[12]["12"]["account"])

    # Extracting the relevant data for the first account
    account_data = {"valor_fat_moly": yearago_account.get("valor_fat", 0)}

    # Creating a DataFrame for the first account data
    df_account = pd.DataFrame([account_data])

    # Calculating the means
    mean_values = df_account.mean()
    # Display the mean values
    print(mean_values)

    # Extracting the first account for comparison
    first_account = json.loads(data_input[0]["0"]["account"])

    # Extracting the relevant data for the first account
    first_account_data = {"valor_fat_moly": first_account.get("total_fat", 0)}

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Mês do Ano Anterior Custo:")
    print(variation)

    variation = variation.fillna(0)
    variation_dict = variation.to_dict()
    variation_custo_json = json.dumps(variation_dict)

    mean_values = mean_values.fillna(0)
    mean_values_dict = mean_values.to_dict()
    mean_values_custo_json = json.dumps(mean_values_dict)
    print(mean_values_custo_json)

    return variation_custo_json, mean_values_custo_json


def Convencional_custo(data_input):
    print("\nHistorico Convencional Mês do Ano Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_moly"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_moly"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_moly": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def Branca_custo(data_input):
    print("Historico Branca Mês do Ano Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_moly"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_moly"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_moly": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def GD_custo(data_input):
    print("Historico GD Mês do Ano Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_moly"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_moly"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_Hist_Custo_moly": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def baixa_Historic_MOLY(
    json_energetico, json_custo, modalidade_tarifaria, tipo_contrato
):
    print("Analise Mês do Ano Anterior de Baixa:")
    try:
        historic_energetico = json.loads(json_energetico)
        historic_custo = json.loads(json_custo)
        variation_json, mean_values_json = media_historica_energetico(
            historic_energetico
        )
        variation_custo_json, mean_values_custo_json = media_historica_custo(
            historic_custo
        )

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
    except:
        print("Sem Conta do Mês do Ano Anterior")
        output_analyse = {
            "consumo_np_moly": 0.0,
            "consumo_inter_moly": 0.0,
            "consumo_fp_moly": 0.0,
            "reativo_np_moly": 0.0,
            "reativo_inter_moly": 0.0,
            "reativo_fp_moly": 0.0,
            "geracao_moly": 0.0,
            "flag_Historic_moly": "green",
        }
        output_custo = {"valor_fat_moly": 0.0, "flag_Hist_Custo_moly": "green"}
        mean_values_json = {
            "consumo_np_moly": 0.0,
            "consumo_inter_moly": 0.0,
            "consumo_fp_moly": 0.0,
            "reativo_np_moly": 0.0,
            "reativo_inter_moly": 0.0,
            "reativo_fp_moly": 0.0,
            "geracao_moly": 0.0,
        }
        mean_values_custo_json = {"valor_fat_moly": 0.0}

        output_analyse = json.dumps(output_analyse)
        output_custo = json.dumps(output_custo)
        mean_values_json = json.dumps(mean_values_json)
        mean_values_custo_json = json.dumps(mean_values_custo_json)

        return output_analyse, output_custo, mean_values_json, mean_values_custo_json
