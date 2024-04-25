from typing import Dict


class Cliente:
    def __init__(self, subgroup, modality, contract, document_data, request):
        self.document = document_data
        
        if subgroup in ['B1', 'B2', 'B3', 'A3', 'A4']:
            self.subgroup = subgroup
        else:
            raise ValueError("Subgrupo inválido")
        if modality in ['CONVENCIONAL', 'BRANCA', 'AZUL', 'VERDE']:
            self.modality = modality
        else:
            raise ValueError("Modalidade inválida")
        if contract in ['ML', 'GD', 'CT']:
            self.contract = contract
        else:
            raise ValueError("Opção inválida")
        self.action = request.get('action')

    def process_request(self):
            match self.action:
                case 'read':
                    cliente_req = self.__format_response()
                    return cliente_req
                case 'analyze':
                    cliente_req = self.__format_response()
                    return cliente_req
                case _:
                    raise ValueError("Ação inválida")

    def __format_response(self) -> Dict:
        return {
            "document": self.document,
            "subgroup": self.subgroup,
            "modality": self.modality,
            "contract": self.contract,
            "action": self.action
        }
