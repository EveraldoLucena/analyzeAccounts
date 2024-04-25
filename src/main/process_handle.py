from src.controllers.dataFirestore import FirestoreDatabase
from src.controllers.getInfoaccount import Cliente
from src.main.action_constructor import action_type
import warnings
warnings.filterwarnings("ignore")


def main(request):
    print(request)

    print("Iniciando o script...")
    db = FirestoreDatabase()
    print("Banco de dados inicializado")

    print(f"Tentando recuperar o documento com ID: {request['document_id']}")
    document_data = db.get_document(request['document_id'])

    # Acessando diretamente os valores
    try:
        arquivo_id = document_data.get('arquivoId')
        processo_id = document_data.get('processoId')
        fatura_id = document_data['data']['dados']['fatura_id']
        subgrupo = document_data['data']['dados']['unidade_consumidora']['subgrupo']
        modalidade_tarifaria = document_data['data']['dados']['unidade_consumidora']['modalidade_tarifaria']
        tipo_contrato = document_data['data']['dados']['unidade_consumidora']['tipo_contrato']
        print(f'Arquivo ID: {arquivo_id}, Processo ID: {processo_id}, Fatura ID: {fatura_id}')
        client  = Cliente(subgrupo, modalidade_tarifaria,tipo_contrato, document_data, request)
        response = client.process_request()
        dados = action_type(response)
        print(dados)
        
        return dados
    except Exception as e:
        print(f'Error: {e}')
        return 'ERROR'
    
