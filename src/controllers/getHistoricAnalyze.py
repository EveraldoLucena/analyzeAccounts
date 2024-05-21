from src.controllers.dataFirestore import FirestoreDatabase
from src.controllers.getInfoaccount import Cliente
from src.controllers.readDados import getDados
from src.controllers.analyzeDados import getHistoric
from src.controllers.analyzeDados import getleituraHistoric
from datetime import datetime
import json
db = FirestoreDatabase()

def getHistoricAnalyze(result, cod_inst, document_id):
  print(f'Código de instalção: {cod_inst}')
  accounts = db.get_documents_by_installation_code(cod_inst)
  accounts.remove(document_id)
  print(f'Contas encontradas: {accounts}')
  
  try:
    historic = []
    for account in accounts:
      request = {
      'document_id': 'account',
      'action': 'read'
    }
      document_data = db.get_document(account)
      subgrupo = document_data['data']['dados']['unidade_consumidora']['subgrupo']
      modalidade_tarifaria = document_data['data']['dados']['unidade_consumidora']['modalidade_tarifaria']
      tipo_contrato = document_data['data']['dados']['unidade_consumidora']['tipo_contrato']
      client  = Cliente(subgrupo, modalidade_tarifaria,tipo_contrato, document_data, request)
      response = client.process_request()
      result_read = getDados(response)
      historic.append(result_read)
    
    # Parse the JSON strings into dictionaries
    parsed_historic = [json.loads(entry) if isinstance(entry, str) else entry for entry in historic]
      
    # Function to convert date string to datetime object
    def parse_date(date_str):
          return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
      
    # Sorting the historic list by 'mes_ref' in descending order
    sorted_historic = sorted(parsed_historic, key=lambda x: parse_date(x['data']['read']['mes_ref']), reverse=True)
      
    # Creating a new list with the organized data
    organized_historic = [entry for entry in sorted_historic]
      
    merged_data = []
    for i,account_data in enumerate(organized_historic,1):
      output = getleituraHistoric(account_data)
      obj = {str(i): {"account": output}}
      merged_data.append(obj)

    new_entry = {"0": {"account": result}}
    merged_data.insert(0, new_entry)
    json_output = json.dumps(merged_data, indent=2)
    print(json_output)
    
    analyze_historic = getHistoric(json_output, subgrupo, modalidade_tarifaria, tipo_contrato)
    return analyze_historic
  except:
    print('Não há histórico!')
    return {}