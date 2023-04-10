from pydantic import BaseModel
from sqlalchemy import Date
from typing import List
from modelo import Instrutor


class InstrutorSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """

    nome: str = "Teste"
    idade: int = 0
    endereco: str = "rua teste"
    telefone: str = "(00) 0000-0000"
    data_nascimento: Date
    agenda:Date

class InstrutorBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Teste"


class ListagemInstrutorSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    instrutores:List[InstrutorSchema]


def apresenta_instrutores(instrutores: List[Instrutor]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """

    result = []
    for instrutor in instrutores:
        result.append({
            "nome":instrutor.nome,
            "idade":instrutor.idade,
            "endereco": instrutor.endereco,
            "telefone":instrutor.telefone,
            "data_nascimento":instrutor.data_nascimento,
            "agenda":instrutor.agenda
        })

    return {"alunos": result}


class InstrutorViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    nome: str = "Teste"
    idade: int = 0
    endereco: str = "rua teste"
    telefone: str = "(00) 0000-0000"
    data_nascimento: Date
    agenda: Date


class InstrutorDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_instrutor(instrutor: Instrutor):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
            "id":id,
            "nome":instrutor.nome,
            "idade":instrutor.idade,
            "endereco": instrutor.endereco,
            "telefone":instrutor.telefone,
            "data_nascimento":instrutor.data_nascimento ,
            "agenda":instrutor.agenda
    }