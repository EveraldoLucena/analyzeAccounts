import os
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore")

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
class FirestoreDatabase:
    def __init__(self, collection_name="bills"):
        # Set the database ID from parameter or environment variable
        self.db = self.firebase_init()
        self.collection_name = collection_name
        
    def firebase_init(self):
        project_id = os.getenv('PROJECT_ID')
        if not project_id:
            raise ValueError("PROJECT_ID is required but not set in the environment.")

        if not firebase_admin._apps:
            if os.getenv('USE_EMULATOR') == 'true':
                # Define a variável de ambiente para o host do emulador
                print(os.getenv('FIRESTORE_HOST'))
                os.environ['FIRESTORE_EMULATOR_HOST'] = os.getenv('FIRESTORE_HOST')
                # Inicializa o Firebase sem credenciais específicas, adequado para uso com o emulador
                initialize_app(options={'projectId': project_id})
            else:
                # Inicializa o Firebase para produção com credenciais padrão
                cred = credentials.ApplicationDefault()
                initialize_app(cred, {'projectId': project_id})

        return firestore.client()

    def get_document(self, doc_id):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None
        
    def get_documents_by_installation_code(self, installation_code):
        docs = self.db.collection(self.collection_name).stream()
        results = []

        for doc in docs:
            data = doc.to_dict()
            # Verificar se o caminho data/dados/unidade_consumidora/instalacao existe e corresponde ao código
            if (
                'data' in data and 
                'dados' in data['data'] and 
                'unidade_consumidora' in data['data']['dados'] and 
                'instalacao' in data['data']['dados']['unidade_consumidora']
            ):
                if data['data']['dados']['unidade_consumidora']['instalacao'] == installation_code:
                    results.append(doc.id)
        
        return results
    
    def update_document_analyzes(self, doc_id, result):
        doc_ref = self.db.collection(self.collection_name).document(doc_id)
        try:
            doc_ref.set(result, merge=True)
            return f"Document {doc_id} updated successfully."
        except:
            return "ERRO ao salvar análise"
