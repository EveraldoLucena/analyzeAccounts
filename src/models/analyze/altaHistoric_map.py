import json
import pandas as pd


def media_historica_energetico(data_input):
    print("\nMédia Histórica Mês do Ano Anterior Energetico:")

    # Extracting the first account for comparison
    yearago_account = json.loads(data_input[12]["12"]["account"])

    account_data = {
        "demanda_p_map": yearago_account.get("demanda", {}).get("np", 0),
        "demanda_fp_map": yearago_account.get("demanda", {}).get("fp", 0),
        "consumo_p_map": yearago_account.get("consumo", {}).get("np", 0),
        "consumo_fp_map": yearago_account.get("consumo", {}).get("fp", 0),
        "reativo_p_map": (
            yearago_account.get("reativo", {}).get("np", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "reativo_fp_map": (
            yearago_account.get("reativo", {}).get("fp", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "reativo_exc_p_map": (
            yearago_account.get("reativo_exc", {}).get("np", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "reativo_exc_fp_map": (
            yearago_account.get("reativo_exc", {}).get("fp", 0)
            if "reativo" in yearago_account
            else 0
        ),
        "geracao_map": yearago_account.get("ger", 0),
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
        "demanda_p_map": first_account.get("demanda", {}).get("np", 0),
        "demanda_fp_map": first_account.get("demanda", {}).get("fp", 0),
        "consumo_p_map": first_account.get("consumo", {}).get("np", 0),
        "consumo_fp_map": first_account.get("consumo", {}).get("fp", 0),
        "reativo_p_map": (
            first_account.get("reativo", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_fp_map": (
            first_account.get("reativo", {}).get("fp", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_exc_p_map": (
            first_account.get("reativo_exc", {}).get("np", 0)
            if "reativo" in first_account
            else 0
        ),
        "reativo_exc_fp_map": (
            first_account.get("reativo_exc", {}).get("fp", 0)
            if "reativo" in first_account
            else 0
        ),
        "geracao_map": first_account.get("ger", 0),
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

    return variation_json, mean_values_json


def CT_energetico(data_input):
    print("\nHistorico Convencional Mês do Ano Anterior Energetico:")
    data = json.loads(data_input)

    if (
        data["demanda_np_map"] > 30
        or data["demanda_fp_map"] > 30
        or data["consumo_fp_map"] > 30
        or data["consumo_p_map"] > 30
        or data["reativo_exc_p_map"] > 30
        or data["reativo_exc_fp_map"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_map"] <= 30)
        or (15 <= data["demanda_p_map"] <= 30)
        or (15 <= data["consumo_fp_map"] <= 30)
        or (15 <= data["consumo_p_map"] <= 30)
        or (15 <= data["reativo_exc_p_map"] <= 30)
        or (15 <= data["reativo_exc_fp_map"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_eletrica_map": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def ML_energetico(data_input):
    print("Historico ML Mês do Ano Anterior Energetico:")
    data = json.loads(data_input)

    if (
        data["demanda_np_map"] > 30
        or data["demanda_fp_map"] > 30
        or data["consumo_fp_map"] > 30
        or data["consumo_p_map"] > 30
        or data["reativo_exc_p_map"] > 30
        or data["reativo_exc_fp_map"] > 30
    ):
        flag_historic = "red"

    elif (
        (15 <= data["consumo_fp_map"] <= 30)
        or (15 <= data["demanda_p_map"] <= 30)
        or (15 <= data["consumo_fp_map"] <= 30)
        or (15 <= data["consumo_p_map"] <= 30)
        or (15 <= data["reativo_exc_p_map"] <= 30)
        or (15 <= data["reativo_exc_fp_map"] <= 30)
    ):
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_eletrica_map": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def media_historica_custo(data_input):
    print("\nMédia Histórica Mês do Ano Anterior Custo:")

    # Extracting the first account for comparison
    yearago_account = json.loads(data_input[12]["12"]["account"])

    # Extracting the relevant data for the first account
    account_data = {"valor_fat_map": yearago_account.get("valor_fat", 0)}

    # Creating a DataFrame for the first account data
    df_account = pd.DataFrame([account_data])

    # Calculating the means
    mean_values = df_account.mean()

    # Display the mean values
    print(mean_values)

    # Extracting the first account for comparison
    first_account = json.loads(data_input[0]["0"]["account"])

    # Extracting the relevant data for the first account
    first_account_data = {"valor_fat_map": first_account.get("total_fat", 0)}

    # Creating a DataFrame for the first account data
    df_first_account = pd.DataFrame([first_account_data])

    # Calculating the variations
    variation = (df_first_account.iloc[0] - mean_values) / mean_values * 100
    print("\nVariação Percentual Mês do Ano Anterior Custo:")
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

    if data["valor_fat_map"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_map"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_custo_map": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def ML_custo(data_input):
    print("Historico ML Mês Anterior Custo:")
    data = json.loads(data_input)

    if data["valor_fat_map"] > 30:
        flag_historic = "red"

    elif 15 <= data["valor_fat_map"] <= 30:
        flag_historic = "yellow"

    else:
        flag_historic = "green"

    additional_fields = {"flag_hist_custo_map": flag_historic}
    data.update(additional_fields)
    output_historic = json.dumps(data, indent=4)
    print(output_historic)
    return output_historic


def alta_Historic_map(
    json_energetico, json_custo, modalidade_tarifaria, tipo_contrato
):
    print("Analise Mês do Ano Anterior de Alta:")
    try:
        historic_energetico = json.loads(json_energetico)
        historic_custo = json.loads(json_custo)
        variation_json, mean_values_json = media_historica_energetico(
            historic_energetico
        )
        variation_custo_json, mean_values_custo_json = media_historica_custo(
            historic_custo
        )

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
        print("Sem Conta do Mês do Ano Anterior")
        output_analyse = {
            "demanda_p_map": 0.0,
            "demanda_fp_map": 0.0,
            "consumo_p_map": 0.0,
            "consumo_fp_map": 0.0,
            "reativo_p_map": 0.0,
            "reativo_fp_map": 0.0,
            "reativo_exc_p_map": 0.0,
            "reativo_exc_fp_map": 0.0,
            "geracao_map": 0.0,
            "flag_hist_eletrica_map": "green",
        }
        output_custo = {"valor_fat_map": 0.0, "flag_hist_custo_map": "green"}
        mean_values_json = {
            "demanda_p_map": 0.0,
            "demanda_fp_map": 0.0,
            "consumo_p_map": 0.0,
            "consumo_fp_map": 0.0,
            "reativo_p_map": 0.0,
            "reativo_fp_map": 0.0,
            "reativo_exc_p_map": 0.0,
            "reativo_exc_fp_map": 0.0,
            "geracao_map": 0.0,
        }
        mean_values_custo_json = {"valor_fat_map": 0.0}

        output_analyse = json.dumps(output_analyse)
        output_custo = json.dumps(output_custo)
        mean_values_json = json.dumps(mean_values_json)
        mean_values_custo_json = json.dumps(mean_values_custo_json)

        return output_analyse, output_custo, mean_values_json, mean_values_custo_json
