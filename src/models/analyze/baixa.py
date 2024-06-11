import json

def fat_analyze(dados):
    cons = dados['leitura']['cons']
    reativo = dados['leitura']['reativo']
    taf = dados['tarifas']
    total_fat = dados['detalh_fat']['valor_final_faturado']
    aviso_corte = dados['outros']['aviso_de_corte']
    debito = dados['outros']['possui_debitos']
    multas = dados['detalh_fat']['multas']
    cde = dados['detalh_fat']['icms_cde']
    publ_light = dados['detalh_fat']['iluminacao_publica']
    imp_som_dim = dados['detalh_fat']['imp_som_dim']
    ger = dados['leitura']['ger']
    deb_servicos = dados['detalh_fat']['deb_servicos']
    
    if(cons['leitura_atual_fp'] - cons['leitura_ant_fp']) < 100:
         value_fp = 100
    else:
        value_fp = cons['leitura_atual_fp'] - cons['leitura_ant_fp']

    value_TUSD_np = (cons['leitura_atual_np'] - cons['leitura_ant_np'])*taf['consumo_tusd_np']['c_impost']
    value_TUSD_inter = (cons['leitura_atual_inter'] - cons['leitura_ant_inter'])*taf['consumo_tusd_inter']['c_impost']
    value_TUSD_fp = value_fp*taf['consumo_tusd_fp']['c_impost']
    value_TE_np = cons['np']*taf['consumo_te_np']['c_impost']
    value_TE_inter = cons['inter']*taf['consumo_te_inter']['c_impost']
    value_TE_fp = cons['fp']*taf['consumo_te_fp']['c_impost']
    value_reativo = reativo['fp'] * taf['reativo_exc']['c_impost']
    multas_nf = multas['nf']
    multas_cosip = multas['cosip']
    parc = multas['parcelamentos']
    doacoes = multas['doacoes']
    total = value_TUSD_np + value_TUSD_inter + value_TUSD_fp + value_TE_np + value_TE_inter + \
        value_TE_fp + multas_nf + multas_cosip + parc + \
        doacoes + cde + publ_light + imp_som_dim + value_reativo + deb_servicos
        
    if aviso_corte == "True":
        corte = True
    else:
        corte = False
        
    if debito == "True":
        debitos = True
    else:
        debitos = False

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
        'value_reativo': value_reativo,
        'multas_nf': multas_nf,
        'multas_cosip': multas_cosip,
        'parc': parc,
        'doacoes': doacoes,
        'deb_servicos': deb_servicos,
        'total': total,
        'aviso_corte': corte,
        'debito': debitos,
    }

    output_json = json.dumps(output, indent=4)
    return output_json

def analyse_Branca(input):
    data = json.loads(input)
    if data['cons']['np'] == data['cons']['fp'] or data['cons']['inter'] == data['cons']['fp'] or data['cons']['fp'] == 0:
        cons_error = True
    else:
        cons_error = False

    if data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total']:
        fat_error = True
    else:
        fat_error = False

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0 or data['value_reativo'] >= 0.1 * data['total']:
        multa = True
    else:
        multa = False
    

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
        cons_error = True
    else:
        cons_error = False

    if (data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total']):
        fat_error = True
    else:
        fat_error = False

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0 or data['value_reativo'] >= 0.1 * data['total']:
        multa = True
    else:
        multa = False

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
        cons_error = True
    else:
        cons_error = False

    if (data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total']) or data['ger'] == 0 or data['ger'] < 0.1 * (data['cons']['leitura_atual_fp'] - data['cons']['leitura_ant_fp']):
        fat_error = True
    else:
        fat_error = False

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0 or data['value_reativo'] >= 0.1 * data['total']:
        multa = True
    else:
        multa = False

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
