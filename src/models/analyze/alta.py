import json

def fat_analyze(dados):
    demand_contr = dados['leitura']['demand_contr']
    demand_med = dados['leitura']['demand_Medida']
    demand_ultrap_np = dados['leitura']['demand_ultrap']['np']
    demand_ultrap_fp = dados['leitura']['demand_ultrap']['fp']
    demand_reatv_np = dados['leitura']['demand_reatv']['fp']
    demand_reatv_fp = dados['leitura']['demand_reatv']['np']
    cons = dados['leitura']['cons']
    reat_exc = dados['leitura']['reat_exc']
    taf = dados['tarifas']
    total_fat = dados['detalh_fat']['valor_final_faturado']
    aviso_corte = dados['outros']['aviso_de_corte']
    debito = dados['outros']['possui_debitos']
    multas = dados['detalh_fat']['multas']
    cde = dados['detalh_fat']['icms_cde']
    publ_light = dados['detalh_fat']['iluminacao_publica']
    desc = dados['detalh_fat']['desc']
    ajuste_desconto_demand_np = dados['detalh_fat']['ajuste_desconto_demand_np']
    ajuste_desconto_demand_fp = dados['detalh_fat']['ajuste_desconto_demand_fp']
    ajuste_desconto_cons = dados['detalh_fat']['ajuste_desconto_cons']
    imp_som_dim = dados['detalh_fat']['imp_som_dim']
    deb_servicos = dados['detalh_fat']['deb_servicos']
    
    value_demand_np = demand_med['np'] * taf['demanda_np']['c_impost']
    value_demand_fp = demand_med['fp'] * taf['demanda_fp']['c_impost']
    value_demand_utrap_np = demand_ultrap_np * taf['demanda_ultrapassada_np']['c_impost']
    value_demand_utrap_fp = demand_ultrap_fp * taf['demanda_ultrapassada_fp']['c_impost']
    value_demand_reatv_np = demand_reatv_np * taf['demanda_reativa']['c_impost']
    value_demand_reatv_fp = demand_reatv_fp * taf['demanda_reativa']['c_impost']
    value_TUSD_np = cons['np'] * taf['consumo_tusd_np']['c_impost']
    value_TUSD_fp = cons['fp'] * taf['consumo_tusd_fp']['c_impost']
    value_TE_np = cons['np'] * taf['consumo_te_np']['c_impost']
    value_TE_fp = cons['fp'] * taf['consumo_te_fp']['c_impost']
    value_reat_exc = (reat_exc['np'] + reat_exc['fp']) * taf['reativo_exc_np']['c_impost']
    multas_nf = multas['nf']
    multas_cosip = multas['cosip']
    parc = multas['parcelamentos']
    doacoes = multas['doacoes']
    total = value_demand_np + value_demand_fp + value_demand_utrap_np + value_demand_utrap_fp + value_demand_reatv_np + value_demand_reatv_fp + value_TUSD_np + value_TUSD_fp + value_TE_np + value_TE_fp + value_reat_exc + multas_nf + multas_cosip + parc + \
        doacoes + cde + publ_light + imp_som_dim + ajuste_desconto_demand_np + ajuste_desconto_demand_fp + ajuste_desconto_cons + deb_servicos

    if aviso_corte == "True":
        corte = True
    else:
        corte = False
        
    if debito == "True":
        debitos = True
    else:
        debitos = False
        
    output = {
        'demand_contr': demand_contr,
        'demand': demand_med,
        'demand_utrap_np': value_demand_utrap_np,
        'demand_reatv_fp': demand_reatv_fp,
        'demand_utrap_np': value_demand_utrap_np,
        'demand_reatv_fp': demand_reatv_fp,
        'cons': cons,
        'taf': taf,
        'total_fat': total_fat,
        'multas': multas,
        'cde': cde,
        'publ_light': publ_light,
        'imp_som_dim': imp_som_dim,
        'value_demand_np': value_demand_np,
        'value_demand_fp': value_demand_fp,
        'value_demand_utrap_np': value_demand_utrap_np,
        'value_demand_utrap_fp': value_demand_utrap_fp,
        'value_demand_reatv_np': value_demand_reatv_fp,
        'value_demand_reatv_fp': value_demand_reatv_np,      
        'value_TUSD_np': value_TUSD_np,
        'value_TUSD_fp': value_TUSD_fp,
        'value_TE_np': value_TE_np,
        'value_TE_fp': value_TE_fp,
        'value_reat_exc': value_reat_exc,
        'desc': desc,
        'ajuste_desconto_demand_np': ajuste_desconto_demand_np,
        'ajuste_desconto_demand_fp': ajuste_desconto_demand_fp,
        'ajuste_desconto_cons': ajuste_desconto_cons,
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
  
def analyse_CT(input):
    data = json.loads(input)
    if data['cons']['np'] == data['cons']['fp'] or data['cons']['fp'] == 0:
        cons_error = True
    else:
        cons_error = False

    if data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total']:
        fat_error = True
    else:
        fat_error = False

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0 or data['value_demand_utrap_np'] != 0 or data['value_demand_utrap_fp'] != 0 or data['value_demand_reatv_np'] != 0 or data['value_demand_reatv_fp'] != 0 or data['value_reat_exc'] != 0:
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
  
def analyse_ML(input):
    data = json.loads(input)
    if data['cons']['np'] == data['cons']['fp'] or data['cons']['fp'] == 0:
        cons_error = True
    else:
        cons_error = False

    if data['total'] != data['total_fat'] and data['total_fat'] > 1.05 * data['total'] or data['value_TE_fp'] != 0 or data['value_TE_np'] != 0 or data['desc'] == 0 or data['ajuste_desconto_demand_fp'] == 0 or data['ajuste_desconto_cons'] == 0:
        fat_error = True
    else:
        fat_error = False

    if data['multas_nf'] != 0 or data['multas_cosip'] != 0 or data['parc'] != 0 or data['value_demand_utrap_np'] != 0 or data['value_demand_utrap_fp'] != 0 or data['value_demand_reatv_np'] != 0 or data['value_demand_reatv_fp'] != 0 or data['value_reat_exc'] > 0.05 * data['total_fat']:
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
  
def analyze_alta(input):
    dados = json.loads(input)
    data_input = fat_analyze(dados['data']['read'])
    tipo_contrato = dados['data']['read']['tipo_contrato']
    
    match tipo_contrato:
      case 'CT':
        print('CONVENCIONAL')
        output_analyse = analyse_CT(data_input)
        return output_analyse
      case 'ML':
        print('ML')
        output_analyse = analyse_ML(data_input)
        return output_analyse