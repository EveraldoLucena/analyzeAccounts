from src.controllers.dataFirestore import FirestoreDatabase
import json
db = FirestoreDatabase()

def updateDocument(doc_id, result_account, result_historic):
  print('\nSalvando Análise...')
  result_account = json.loads(result_account)
  output= {}
  output.update(result_account)
  
  try:
    result_historic = json.loads(result_historic)
    output.update(result_historic)
      
    print(output)
  except:
    print(output)
    
  response = db.update_document_analyzes(doc_id, output)
  print('\n', response)
  return 