import json


def A4Verde_CT(document_data):
    distribuidora = document_data['data']['dados']['distribuidora']
    nome = document_data['data']['dados']['unidade_consumidora']['nome']
    contrato = document_data['data']['dados']['unidade_consumidora']['contrato']
    subgrupo = document_data['data']['dados']['unidade_consumidora']['subgrupo']
    modalidade_tarifaria = document_data['data']['dados']['unidade_consumidora']['modalidade_tarifaria']
    tipo_contrato = document_data['data']['dados']['unidade_consumidora']['tipo_contrato']
    demanda_contrat = document_data['data']['dados']['fatura']['demandas_contratadas'][0]['valor']
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
    demanda_med_np = func_leitura(document_data, 2)
    demanda_med_fp = func_leitura(document_data, 3)
    reativo_np = func_leitura(document_data, 4)
    reativo_fp = func_leitura(document_data, 5)
    reat_exc_np = func_leitura(document_data, 6)
    reat_exc_fp = func_leitura(document_data, 7)

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

    prod_dem = func_produto(document_data, "Demanda TUSD kW")
    prod_demand_ultrap = func_produto(
        document_data, "Ultrapassagem Demanda TUSD kW")
    prod_demand_reativo = func_produto(
        document_data, "Demanda Reativa Excedente kVAR")
    prod_cons_TUSD_np = func_produto(document_data, "Consumo TUSD kWh Ponta")
    prod_cons_TUSD_fp = func_produto(
        document_data, "Consumo TUSD kWh Fora Ponta")
    prod_cons_TE_np = func_produto(document_data, "Consumo TE kWh Ponta")
    prod_cons_TE_fp = func_produto(document_data, "Consumo TE kWh Fora Ponta")
    prod_reativo_exc_np = func_produto(
        document_data, "Consumo Reativo Excedente kVARh Ponta")
    prod_reativo_exc_fp = func_produto(
        document_data, "Consumo Reativo Excedente kVARh Fora Ponta")
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
    print(f'Demanda Contratada NP: {
          demanda_contrat}')
    print(f'Demanda Ultrap.: {prod_demand_ultrap['quantidade']}')
    print(f'Demanda Medida NP: {
          demanda_med_np}, Demanda Medida FP: {demanda_med_fp}')
    print(f'Consumo NP: {consumo_np}, Consumo FP: {consumo_fp}')
    print(f'Reativo NP: {reativo_np}, Reativo FP: {reativo_fp}')
    print(f'Reativo Excedente NP: {
          reat_exc_np}, Reativo Excedente FP: {reat_exc_fp}')

    print('\n ------------------------------------------------------------------------')
    print("TARIFAS, BANDEIRA E IMPOSTOS:")
    print(f'Bandeira Tarifária: {bandeira}')
    print(f'PIS: {pis}, COFINS: {cofins}, ICMS: {icms}')
    print(f'Tarifa Demanda S/Impost: {prod_dem['tarifa_sem_impostos']
                                      }, Tarifa Demanda C/Impost: {prod_dem['tarifa_com_impostos']}')
    print(f'Tarifa Demanda Ultrap. S/Impost: {prod_demand_ultrap['tarifa_sem_impostos']
                                              }, Tarifa Demanda Ultrap. C/Impost: {prod_demand_ultrap['tarifa_com_impostos']}')
    print(f'Tarifa Demanda Reativa S/Impost: {prod_demand_reativo['tarifa_sem_impostos']
                                              }, Tarifa Demanda Reativa C/Impost: {prod_demand_reativo['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TUSD NP S/Impost: {prod_cons_TUSD_np['tarifa_sem_impostos']
                                              }, Tarifa Consumo TUSD NP C/Impost: {prod_cons_TUSD_np['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TUSD FP S/Impost: {prod_cons_TUSD_fp['tarifa_sem_impostos']
                                              }, Tarifa Consumo TUSD FP C/Impost: {prod_cons_TUSD_fp['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TE NP S/Impost: {prod_cons_TE_np['tarifa_sem_impostos']
                                            }, Tarifa Consumo TE NP C/Impost: {prod_cons_TE_np['tarifa_com_impostos']}')
    print(f'Tarifa Consumo TE FP S/Impost: {prod_cons_TE_fp['tarifa_sem_impostos']
                                            }, Tarifa Consumo TE FP C/Impost: {prod_cons_TE_fp['tarifa_com_impostos']}')
    print(f'Tarifa Reativo EXC S/Impost: {prod_reativo_exc_np['tarifa_sem_impostos']
                                          }, Tarifa Reativo EXC C/Impost: {prod_reativo_exc_np['tarifa_com_impostos']}')

    print('\n ------------------------------------------------------------------------')
    print("DETALHAMENTO DO FATURAMENTO:")
    print(f'Demanda Reativa: {prod_demand_reativo['valor_total']}')
    print(f'Demanda: {prod_dem['valor_total']}')
    print(f'Consumo TUSD NP: {prod_cons_TUSD_np['valor_total']}, Consumo TUSD FP: {
          prod_cons_TUSD_fp['valor_total']}')
    print(f'Consumo TE NP: {prod_cons_TE_np['valor_total']}, Consumo TE FP: {
          prod_cons_TE_fp['valor_total']}')
    print(f'Reativo EXC NP: {prod_reativo_exc_np['valor_total']}, Reativo EXC FP: {
          prod_reativo_exc_fp['valor_total']}')
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
                    'demand_contr': {
                        'np': 0,
                        'fp': demanda_contrat
                    },
                    'demand_ultrap': {
                        'np': 0,
                        'fp': prod_demand_ultrap['quantidade']
                    },
                    'demand_Medida': {
                        'np': demanda_med_np * 1.025,
                        'fp': demanda_med_fp * 1.025
                    },
                    'demand_reatv':{
                        'np': 0,
                        'fp': prod_demand_reativo['quantidade']   
                    },
                    'cons': {
                        'np': consumo_np * 1.025,
                        'fp': consumo_fp * 1.025
                    },
                    'reat': {
                        'np': reativo_np * 1.025,
                        'fp': reativo_fp * 1.025
                    },
                    'reat_exc': {
                        'np': reat_exc_np * 1.025,
                        'fp': reat_exc_fp * 1.025
                    },
                },
                'tarifas': {
                    'demanda_np': {
                        's_impost': 0,
                        'c_impost': 0
                    },
                    'demanda_fp': {
                        's_impost': prod_dem['tarifa_sem_impostos'],
                        'c_impost': prod_dem['tarifa_com_impostos']
                    },
                    'demanda_ultrapassada_np': {
                        's_impost': 0,
                        'c_impost': 0
                    },
                    'demanda_ultrapassada_fp': {
                        's_impost': prod_demand_ultrap['tarifa_sem_impostos'],
                        'c_impost': prod_demand_ultrap['tarifa_com_impostos']
                    },
                    'demanda_reativa': {
                        's_impost': prod_demand_reativo['tarifa_sem_impostos'],
                        'c_impost': prod_demand_reativo['tarifa_com_impostos']
                    },
                    'consumo_tusd_np': {
                        's_impost': prod_cons_TUSD_np['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TUSD_np['tarifa_com_impostos']
                    },
                    'consumo_tusd_fp': {
                        's_impost': prod_cons_TUSD_fp['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TUSD_fp['tarifa_com_impostos']
                    },
                    'consumo_te_np': {
                        's_impost': prod_cons_TE_np['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TE_np['tarifa_com_impostos']
                    },
                    'consumo_te_fp': {
                        's_impost': prod_cons_TE_fp['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TE_fp['tarifa_com_impostos']
                    },
                    'reativo_exc_np': {
                        's_impost': prod_reativo_exc_np['tarifa_sem_impostos'],
                        'c_impost': prod_reativo_exc_np['tarifa_com_impostos']
                    }
                },
                'detalh_fat': {
                    'demanda_reativa': {
                        'np': 0,
                        'fp': prod_demand_reativo['valor_total']
                    },
                    'demanda': {
                        'np': 0,
                        'fp': prod_dem['valor_total']
                    },
                    'consumo_tusd': {
                        'np': prod_cons_TUSD_np['valor_total'],
                        'fp': prod_cons_TUSD_fp['valor_total']
                    },
                    'consumo_te': {
                        'np': prod_cons_TE_np['valor_total'],
                        'fp': prod_cons_TE_fp['valor_total']
                    },
                    'reativo_exc': {
                        'np': prod_reativo_exc_np['valor_total'],
                        'fp': prod_reativo_exc_fp['valor_total']
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
                    'desc': 0,
                    'ajuste_desconto_demand_np': 0,
                    'ajuste_desconto_demand_fp': 0,
                    'ajuste_desconto_cons': 0,
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
    print(output)
    return output
