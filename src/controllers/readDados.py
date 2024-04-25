from src.models.read.read_B1Conv_CT import B1Conv_CT
from src.models.read.read_B3Conv_CT import B3Conv_CT
from src.models.read.read_B3Conv_GD import B3Conv_GD
from src.models.read.read_B1Conv_GD import B1Conv_GD
from src.models.read.read_B1Branc_CT import B1Branc_CT
from src.models.read.read_B3Branc_CT import B3Branc_CT
from src.models.read.read_A4Verde_CT import A4Verde_CT
from src.models.read.read_A4Verde_ML import A4Verde_ML
from src.models.read.read_A4Azul_CT import A4azul_CT
from src.models.read.read_A4azul_ML import A4azul_ML

def getDados(cliente_req):
    match cliente_req['subgroup']:
        case 'B1':
            match cliente_req['modality']:
                case 'CONVENCIONAL':
                    match cliente_req['contract']:
                        case 'CT':
                            data = B1Conv_CT(cliente_req['document'])
                            return data
                        case 'GD':
                            data = B1Conv_GD(cliente_req['document'])
                            return data
                case 'BRANCA':
                    data = B1Branc_CT(cliente_req['document'])
                    return data

        case 'B3':
            match cliente_req['modality']:
                case 'CONVENCIONAL':
                    match cliente_req['contract']:
                        case 'CT':
                            data = B3Conv_CT(cliente_req['document'])
                            return data
                        case 'GD':
                            data = B3Conv_GD(cliente_req['document'])
                            return data
                case 'BRANCA':
                    data = B3Branc_CT(cliente_req['document'])
                    return data

        case 'A4':
            match cliente_req['modality']:
                case 'AZUL':
                    match cliente_req['contract']:
                        case 'CT':
                            data = A4azul_CT(cliente_req['document'])
                            return data
                        case 'ML':
                            data = A4azul_ML(cliente_req['document'])
                            return data
                case 'VERDE':
                    match cliente_req['contract']:
                        case 'CT':
                            data = A4Verde_CT(cliente_req['document'])
                            return data
                        case 'ML':
                            data = A4Verde_ML(cliente_req['document'])
                            return data
