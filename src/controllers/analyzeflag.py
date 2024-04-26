import json
import pandas

def flag(input):
    data = json.loads(input)
    data['aviso_corte'] = str(data['aviso_corte'])
    data['debito'] = str(data['debito'])

    flag_color = 'green'
    if (data['aviso_corte'] == 'True' or data['debito'] == 'True' or
        data['consumo_error'] == 'true' or data['faturamento_error'] == 'true'):
        flag_color = 'red'
    elif data['multa'] == 'true':
        flag_color = 'yellow'

    additional_fields = {
        'flag': flag_color
    }
    data.update(additional_fields)
    output = json.dumps(data, indent=4)
    print('Flag Analyze: OK')
    return output
