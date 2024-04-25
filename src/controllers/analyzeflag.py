import json


def flag(input):
    data = json.loads(input)

    if data['aviso_corte'] == 'true' or data['debito'] == 'true':
        flag_color = 'red'
    elif data['consumo_error'] == 'true' or data['faturamento_error'] == 'true':
        flag_color = 'red'
    elif data['multa'] == 'true':
        flag_color = 'yellow'
    else:
        flag_color = 'green'

    additional_fields = {
        'flag': flag_color
    }
    data.update(additional_fields)
    output = json.dumps(data, indent=4)
    print('Flag Analyze: OK')
    return output
