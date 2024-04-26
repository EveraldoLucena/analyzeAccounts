import json


def fat_analyze(dados):
    cons = dados['leitura']['cons']
    taf = dados['tarifas']
    total_fat = dados['detalh_fat']['valor_final_faturado']
    aviso_corte = dados['outros']['aviso_de_corte']
    debito = dados['outros']['possui_debitos']
    multas = dados['detalh_fat']['multas']
    cde = dados['detalh_fat']['icms_cde']
    publ_light = dados['detalh_fat']['iluminacao_publica']
    imp_som_dim = dados['detalh_fat']['imp_som_dim']
    ger = dados['leitura']['ger']

    value_TUSD_np = cons['np']*taf['consumo_tusd_np']['c_impost']
    value_TUSD_inter = cons['inter']*taf['consumo_tusd_inter']['c_impost']
    value_TUSD_fp = cons['fp']*taf['consumo_tusd_fp']['c_impost']
    value_TE_np = cons['np']*taf['consumo_te_np']['c_impost']
    value_TE_inter = cons['inter']*taf['consumo_te_inter']['c_impost']
    value_TE_fp = cons['fp']*taf['consumo_te_fp']['c_impost']
    multas_nf = multas['nf']
    multas_cosip = multas['cosip']
    parc = multas['parcelamentos']
    doacoes = multas['doacoes']
    total = value_TUSD_np + value_TUSD_inter + value_TUSD_fp + value_TE_np + value_TE_inter + \
        value_TE_fp + multas_nf + multas_cosip + parc + \
        doacoes + cde + publ_light + imp_som_dim

    output = {
        'cons': cons,
        'ger': ger,
        'taf': taf,
        'total_fat': total_fat,
        'multas': multas,
        'cde': cde,
        'publ_light': publ_light,
        'imp_som_dim': imp_som_dim,
        'value_TUSD_np': value_TUSD_np,
        'value_TUSD_inter': value_TUSD_inter,
        'value_TUSD_fp': value_TUSD_fp,
        'value_TE_np': value_TE_np,
        'value_TE_inter': value_TE_inter,
        'value_TE_fp': value_TE_fp,
        'multas_nf': multas_nf,
        'multas_cosip': multas_cosip,
        'parc': parc,
        'doacoes': doacoes,
        'total': total,
        'aviso_corte': aviso_corte,
        'debito': debito,
    }
    output_json = json.dumps(output, indent=4)
    return output_json


def analyse_Branca(input):
    data = json.loads(input)
    if data['cons']['np'] == data['cons']['fp'] or data['cons']['inter'] == data['cons']['fp'] or data['cons']['fp'] == 0:
        cons_error = 'true'
    else:
        cons_error = 'false'

    if data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total']:
        fat_error = 'true'
    else:
        fat_error = 'false'

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0:
        multa = 'true'
    else:
        multa = 'false'

    additional_fields = {
        'consumo_error': cons_error,
        'faturamento_error': fat_error,
        'multa': multa
    }
    data.update(additional_fields)
    output = data
    output_analyse = json.dumps(output, indent=4)
    return output_analyse


def analyse_Convencional(input):
    data = json.loads(input)
    if data['cons']['np'] != 0 or data['cons']['inter'] != 0 or data['cons']['fp'] == 0:
        cons_error = 'true'
    else:
        cons_error = 'false'

    if data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total']:
        fat_error = 'true'
    else:
        fat_error = 'false'

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0:
        multa = 'true'
    else:
        multa = 'false'

    additional_fields = {
        'consumo_error': cons_error,
        'faturamento_error': fat_error,
        'multa': multa
    }
    data.update(additional_fields)
    output = data
    output_analyse = json.dumps(output, indent=4)
    return output_analyse


def analyse_GD(input):
    data = json.loads(input)
    if data['cons']['np'] != 0 or data['cons']['inter'] != 0 or data['cons']['fp'] == 0:
        cons_error = 'true'
    else:
        cons_error = 'false'

    if data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total'] or data['ger'] == 0:
        fat_error = 'true'
    else:
        fat_error = 'false'

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0:
        multa = 'true'
    else:
        multa = 'false'

    additional_fields = {
        'consumo_error': cons_error,
        'faturamento_error': fat_error,
        'multa': multa
    }
    data.update(additional_fields)
    output = data
    output_analyse = json.dumps(output, indent=4)
    return output_analyse


def analyze_baixa(input):
    dados = json.loads(input)
    data_input = fat_analyze(dados['data']['read'])
    modalidade = dados['data']['read']['modalidade']
    tipo_contrato = dados['data']['read']['tipo_contrato']

    match modalidade:
        case 'CONVENCIONAL':
            match tipo_contrato:
                case 'CT':
                    print('CONVENCIONAL')
                    output_analyse = analyse_Convencional(data_input)
                    return output_analyse
                case 'GD':
                    print('GD')
                    output_analyse = analyse_GD(data_input)
                    return output_analyse

        case 'BRANCA':
            print('BRANCA')
            output_analyse = analyse_Branca(data_input)
            return output_analyse
