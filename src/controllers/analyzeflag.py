import json
import pandas

def flag(input): 
    data = json.loads(input)
    data['aviso_corte'] = data['aviso_corte']
    data['debito'] = data['debito']

    flag_color = 'green'
    if (data['aviso_corte'] == True or data['debito'] == True or
        data['consumo_error'] == True or data['faturamento_error'] == True):
        flag_color = 'red'
    elif data['multa'] == True:
        flag_color = 'yellow'

    print(f'Flag Color: {flag_color}')
    
    analyze_account = {
        'consumo_error': data['consumo_error'],
        'faturamento_error': data['faturamento_error'],
        'multa': data['multa'],
        'aviso_corte': data['aviso_corte'],
        'debito': data['debito'],
        'flag_account': flag_color     
    }
    
    analyze_account = json.dumps(analyze_account, indent=4)
    print(analyze_account)
    return analyze_account
