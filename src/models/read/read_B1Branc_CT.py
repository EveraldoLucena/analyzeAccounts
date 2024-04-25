import json

def B1Branc_CT(document_data):
    distribuidora = document_data['data']['dados']['distribuidora']
    nome = document_data['data']['dados']['unidade_consumidora']['nome']
    contrato = document_data['data']['dados']['unidade_consumidora']['contrato']
    subgrupo = document_data['data']['dados']['unidade_consumidora']['subgrupo']
    modalidade_tarifaria = document_data['data']['dados']['unidade_consumidora']['modalidade_tarifaria']
    tipo_contrato = document_data['data']['dados']['unidade_consumidora']['tipo_contrato']
    dias = document_data['data']['dados']['fatura']['leitura']['periodo_dias']
    mes_ref = document_data['data']['dados']['fatura']['mes_referencia']
    bandeira = document_data['data']['dados']['fatura']['bandeiras_tarifarias'][0]['nome']
    pis = document_data['data']['dados']['fatura']['tributos'][0]['taxa']
    cofins = document_data['data']['dados']['fatura']['tributos'][1]['taxa']
    icms = document_data['data']['dados']['fatura']['tributos'][2]['taxa']
    debitos = document_data['data']['dados']['outros']['possui_debitos']
    total_fat = document_data['data']['dados']['fatura']['total_fatura']

    # Função Genérica - Leituras
    def func_leitura(document_data, position):
        leitura = document_data['data']['dados']['fatura']['leitura']['medidores'][0]['leituras'][position]
        return leitura.get("valor_leitura", 0)

    consumo_np = func_leitura(document_data, 0)
    consumo_fp = func_leitura(document_data, 1)
    consumo_inter = func_leitura(document_data, 2)

    # Função Genérica - Produtos
    def func_produto(document_data, target_description):
        produtos = document_data["data"]["dados"]["fatura"]["produtos"]
        for produto in produtos:
            if produto["descricao"] == target_description:
                return {
                    "valor_total": produto.get("valor_total", 0),
                    "quantidade": produto.get("quantidade", 0),
                    "tarifa_sem_impostos": produto.get("tarifa_sem_impostos", 0),
                    "tarifa_com_impostos": produto.get("tarifa_com_impostos", 0)
                }
        return {
            "valor_total": 0,
            "quantidade": 0,
            "tarifa_sem_impostos": 0,
            "tarifa_com_impostos": 0
        }

    prod_cons_TUSD_np = func_produto(document_data, "Consumo TUSD kWh Ponta")
    prod_cons_TUSD_fp = func_produto(document_data, "Consumo TUSD kWh Fora Ponta")
    prod_cons_TUSD_inter = func_produto(document_data, "Consumo TUSD kWh Intermediário")
    prod_cons_TE_np = func_produto(document_data, "Consumo TE kWh Ponta")
    prod_cons_TE_fp = func_produto(document_data, "Consumo TE kWh Fora Ponta")
    prod_cons_TE_inter = func_produto(document_data, "Consumo TE kWh Intermediário")
    prod_ilum_pub = func_produto(
        document_data, "Contribuição Iluminação Pública")
    prod_icms_CDE = func_produto(document_data, "ICMS - Subvenção CDE")
    prod_doacao = func_produto(document_data, "Doações")
    prod_multasCOSIP = func_produto(
        document_data, "Multas/Juros/Corr.Monetária de Cont. Ilum. Pública")
    prod_multasNF = func_produto(document_data, "Multas/Juros/Corr.Monetária")
    prod_parc = func_produto(document_data, "Parcelamentos")
    prod_imp_som_dim = func_produto(
        document_data, "Importe a Somar ou Diminuir (C/Imposto)")
    try:
        aviso_corte = document_data['data']['dados']['outros']['aviso_corte']
    except:
        aviso_corte = 'false'

    print('\n ------------------------------------------------------------------------')
    print("INFORMAÇÕES GERAIS:")
    print("Distribuidora:", distribuidora)
    print(f'Dias: {dias}, Mês de Referência: {mes_ref}')
    print(f'Cliente: {nome}, Contrato: {contrato}, Subgrupo: {
          subgrupo}, Modalidade: {modalidade_tarifaria}, Tipo: {tipo_contrato}')

    print('\n ------------------------------------------------------------------------')
    print("DETALHAMENTO DA LEITURA:")
    print(f'Consumo Ativo NP: {consumo_np}, Consumo Ativo INTER: {consumo_inter}, Consumo Ativo FP: {consumo_fp}')

    print('\n ------------------------------------------------------------------------')
    print("TARIFAS, BANDEIRA E IMPOSTOS:")
    print(f'Bandeira Tarifária: {bandeira}')
    print(f'PIS: {pis}, COFINS: {cofins}, ICMS: {icms}')
    print(f'Tarifa Consumo TUSD NP S/Impost: {prod_cons_TUSD_np['tarifa_sem_impostos']}, Tarifa Consumo TUSD NP C/Impost: {prod_cons_TUSD_np['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TUSD INTER S/Impost: {prod_cons_TUSD_inter['tarifa_sem_impostos']}, Tarifa Consumo TUSD INTER C/Impost: {prod_cons_TUSD_inter['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TUSD FP S/Impost: {prod_cons_TUSD_fp['tarifa_sem_impostos']}, Tarifa Consumo TUSD FP C/Impost: {prod_cons_TUSD_fp['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TE NP S/Impost: {prod_cons_TE_np['tarifa_sem_impostos']}, Tarifa Consumo TE NP C/Impost: {prod_cons_TE_np['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TE INTER S/Impost: {prod_cons_TE_inter['tarifa_sem_impostos']}, Tarifa Consumo TE INTER C/Impost: {prod_cons_TE_inter['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TE FP S/Impost: {prod_cons_TE_fp['tarifa_sem_impostos']}, Tarifa Consumo TE FP C/Impost: {prod_cons_TE_fp['tarifa_com_impostos']}')

    print('\n ------------------------------------------------------------------------')
    print("DETALHAMENTO DO FATURAMENTO:")
    print(f'Consumo TUSD NP: {prod_cons_TUSD_np['valor_total']}, Consumo TE NP: {
          prod_cons_TE_np['valor_total']}')
    print(f'Consumo TUSD INTER: {prod_cons_TUSD_inter['valor_total']}, Consumo TE INTER: {
          prod_cons_TE_inter['valor_total']}')
    print(f'Consumo TUSD FP: {prod_cons_TUSD_fp['valor_total']}, Consumo TE FP: {
          prod_cons_TE_fp['valor_total']}')
    print(f'Iluminação Pública: {prod_ilum_pub['valor_total']}')
    print(f'ICMS CDE: {
          prod_icms_CDE['valor_total']}, Imp.Som/Dim.: {prod_imp_som_dim['valor_total']}')
    print(f'Multas NF: {prod_multasNF['valor_total']}, Multas COSIP: {prod_multasCOSIP['valor_total']}, Parcelamentos: {
          prod_parc['valor_total']}, Doações: {prod_doacao['valor_total']}')
    print(f'Valor Final Faturado: {total_fat}')

    print('\n ------------------------------------------------------------------------')
    print("OUTROS:")
    print(f'Aviso de Corte: {aviso_corte}')
    print(f'Possui Débitos: {debitos}')

    data = {
        'data': {
            'read': {
                'distribuidora': distribuidora,
                'dias': dias,
                'mes_ref': mes_ref,
                'cliente': nome,
                'contrato': contrato,
                'subgrupo': subgrupo,
                'modalidade': modalidade_tarifaria,
                'tipo_contrato': tipo_contrato,
                'band': bandeira,
                'impost': {
                    'pis': pis,
                    'icms': icms,
                    'cofins': cofins
                },
                'leitura': {
                    'cons': {
                        'np': consumo_np,
                        'inter': consumo_inter,
                        'fp': consumo_fp
                    },
                    'ger': 0,
                },
                'tarifas': {
                    'consumo_tusd_np': {
                        's_impost': prod_cons_TUSD_np['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TUSD_np['tarifa_com_impostos']
                    },
                    'consumo_tusd_inter': {
                        's_impost': prod_cons_TUSD_inter['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TUSD_inter['tarifa_com_impostos']
                    },
                    'consumo_tusd_fp': {
                        's_impost': prod_cons_TUSD_fp['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TUSD_fp['tarifa_com_impostos']
                    },
                    'consumo_te_np': {
                        's_impost': prod_cons_TE_np['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TE_np['tarifa_com_impostos']
                    },
                    'consumo_te_inter': {
                        's_impost': prod_cons_TE_inter['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TE_inter['tarifa_com_impostos']
                    },
                    'consumo_te_fp': {
                        's_impost': prod_cons_TE_fp['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TE_fp['tarifa_com_impostos']
                    }
                },
                'detalh_fat': {
                    'consumo_tusd': {
                        'np': prod_cons_TUSD_np['valor_total'],
                        'inter': prod_cons_TUSD_inter['valor_total'],
                        'fp': prod_cons_TUSD_fp['valor_total']
                    },
                    'consumo_te': {
                        'np': prod_cons_TE_np['valor_total'],
                        'inter': prod_cons_TE_inter['valor_total'],
                        'fp': prod_cons_TE_fp['valor_total']
                    },
                    'iluminacao_publica': prod_ilum_pub['valor_total'],
                    'icms_cde': prod_icms_CDE['valor_total'],
                    'multas': {
                        'nf': prod_multasNF['valor_total'],
                        'cosip': prod_multasCOSIP['valor_total'],
                        'parcelamentos': prod_parc['valor_total'],
                        'doacoes': prod_doacao['valor_total']
                    },
                    'valor_final_faturado': total_fat,
                    'imp_som_dim': prod_imp_som_dim['valor_total']
                },
                'outros': {
                    'aviso_de_corte': aviso_corte,
                    'possui_debitos': debitos
                }
            },
        },
    }

    # Convert the dictionary to a JSON string
    output = json.dumps(data, indent=4)

    return output
