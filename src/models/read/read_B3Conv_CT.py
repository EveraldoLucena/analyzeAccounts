import json


def B3Conv_CT(document_data):
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
    def func_leitura(document_data, target_description):
        leituras = document_data['data']['dados']['fatura']['leitura']['medidores'][0]['leituras']
        for leitura in leituras:
            if leitura["ativa_ou_reativa"] == target_description:
                return {
                    "valor_leitura": leitura.get("valor_leitura", 0),
                    "valor_anterior": leitura.get("valor_anterior", 0),
                    "valor_atual": leitura.get("valor_atual", 0)
                }
        return {
            "valor_leitura": 0,
            "valor_anterior": 0,
            "valor_atual": 0
        }

    consumo = func_leitura(document_data, "ATIVA")
    reativo = func_leitura(document_data, "REATIVA")

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

    prod_cons_TUSD = func_produto(document_data, "Consumo TUSD kWh")
    prod_cons_TE = func_produto(document_data, "Consumo TUSD kWh")
    prod_reat_exc = func_produto(document_data, "Consumo Reativo Excedente kVARh")
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
    prod_deb_servicos = func_produto(
        document_data, "Débitos de Serviços Cobráveis pela Distribuidora")
    try:
        aviso_corte = document_data['data']['dados']['outros']['aviso_corte']
    except:
        aviso_corte = 'false'

    print(' ------------------------------------------------------------------------')
    print("INFORMAÇÕES GERAIS:")
    print("Distribuidora:", distribuidora)
    print(f'Dias: {dias}, Mês de Referência: {mes_ref}')
    print(f'Cliente: {nome}, Contrato: {contrato}, Subgrupo: {subgrupo}, Modalidade: {modalidade_tarifaria}, Tipo: {tipo_contrato}')

    print(' ------------------------------------------------------------------------')
    print("DETALHAMENTO DA LEITURA:")
    print(f'Consumo Ativo: {consumo["valor_leitura"]}, Leitura Anterior: {consumo["valor_anterior"]}, Leitura Atual: {consumo["valor_atual"]}')
    print(f'Consumo Reativo: {reativo["valor_leitura"]}, Leitura Anterior: {reativo["valor_anterior"]}, Leitura Atual: {reativo["valor_atual"]}')
    print(f'Geração Compensada: 0')

    print(' ------------------------------------------------------------------------')
    print("TARIFAS, BANDEIRA E IMPOSTOS:")
    print(f'Bandeira Tarifária: {bandeira}')
    print(f'PIS: {pis}, COFINS: {cofins}, ICMS: {icms}')
    print(f'Tarifa Consumo TUSD S/Impost: {prod_cons_TUSD["tarifa_sem_impostos"]}, Tarifa Consumo TUSD C/Impost: {prod_cons_TUSD["tarifa_com_impostos"]}')
    print(f'Tarifa Consumo TE S/Impost: {prod_cons_TE["tarifa_sem_impostos"]}, Tarifa Consumo TE C/Impost: {prod_cons_TE["tarifa_com_impostos"]}')

    print(' ------------------------------------------------------------------------')
    print("DETALHAMENTO DO FATURAMENTO:")
    print(f'Consumo TUSD: {prod_cons_TUSD["valor_total"]}, Consumo TE: {prod_cons_TE["valor_total"]}')
    print(f'Iluminação Pública: {prod_ilum_pub["valor_total"]}')
    print(f'ICMS CDE: {prod_icms_CDE["valor_total"]}, Imp.Som/Dim.: {prod_imp_som_dim["valor_total"]}')
    print(f'Multas NF: {prod_multasNF["valor_total"]}, Multas COSIP: {prod_multasCOSIP["valor_total"]}, Parcelamentos: {prod_parc["valor_total"]}, Doações: {prod_doacao["valor_total"]}')
    print(f'Valor Final Faturado: {total_fat}')

    print(' ------------------------------------------------------------------------')
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
                        'np': 0,
                        'inter': 0,
                        'fp': consumo['valor_leitura'],
                        'leitura_ant_np': 0,
                        'leitura_atual_np': 0,
                        'leitura_ant_inter': 0,
                        'leitura_atual_inter': 0,
                        'leitura_ant_fp': consumo['valor_anterior'],
                        'leitura_atual_fp':consumo['valor_atual'],
                    },
                    'reativo': {
                        'np': 0,
                        'inter': 0,
                        'fp': reativo['valor_leitura'],
                        'leitura_ant': reativo['valor_anterior'],
                        'leitura_atual': reativo['valor_atual'],
                    },
                    'ger': 0,
                },
                'tarifas': {
                    'consumo_tusd_np': {
                        's_impost': 0,
                        'c_impost': 0
                    },
                    'consumo_tusd_inter': {
                        's_impost': 0,
                        'c_impost': 0
                    },
                    'consumo_tusd_fp': {
                        's_impost': prod_cons_TUSD['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TUSD['tarifa_com_impostos']
                    },
                    'consumo_te_np': {
                        's_impost': 0,
                        'c_impost': 0
                    },
                    'consumo_te_inter': {
                        's_impost': 0,
                        'c_impost': 0
                    },
                    'consumo_te_fp': {
                        's_impost': prod_cons_TE['tarifa_sem_impostos'],
                        'c_impost': prod_cons_TE['tarifa_com_impostos']
                    },
                    'reativo_exc': {
                        's_impost':prod_reat_exc['tarifa_sem_impostos'],
                        'c_impost': prod_reat_exc['tarifa_com_impostos']
                    },
                },
                'detalh_fat': {
                    'consumo_tusd': {
                        'np': 0,
                        'inter': 0,
                        'fp': prod_cons_TUSD['valor_total']
                    },
                    'consumo_te': {
                        'np': 0,
                        'inter': 0,
                        'fp': prod_cons_TE['valor_total']
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
                    'imp_som_dim': prod_imp_som_dim['valor_total'],
                    'deb_servicos': prod_deb_servicos['valor_total']
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
