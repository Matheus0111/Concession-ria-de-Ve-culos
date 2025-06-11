from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import date
from enum import Enum


class Cargo(str, Enum):
    DESENVOLVEDOR = "Desenvolvedor"
    ANALISTA = "Analista"
    GERENTE = "Gerente"
    DIRETOR = "Diretor"
    ESTAGIARIO = "Estagiário"
    ADMINISTRATIVO = "Administrativo"
    RECURSOS_HUMANOS = "Recursos Humanos"
    FINANCEIRO = "Financeiro"
    SUPORTE = "Suporte"
    OUTROS = "Outros"


class Funcionario(BaseModel):
    id: Optional[int] = None
    nome: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    data_nascimento: Optional[date] = None
    telefone: Optional[str] = Field(None, max_length=20)
    
    # Novos campos para funcionários
    cargo: Cargo = Field(..., description="Cargo do funcionário na empresa")
    data_contratacao: date = Field(..., description="Data de contratação do funcionário")
    salario: float = Field(..., ge=0, description="Salário mensal do funcionário em reais")
    
    class Config:
        json_schema_extra = {
            "example": {
                "nome": "João Silva",
                "email": "joao@example.com",
                "data_nascimento": "1990-01-01",
                "telefone": "(11) 98765-4321",
                "cargo": "Desenvolvedor",
                "data_contratacao": "2021-03-15",
                "salario": 5000.00
            }
        }


class EstatisticasCargo(BaseModel):
    cargo: str
    quantidade: int
    salario_total: float
    salario_medio: float


class EstatisticasGerais(BaseModel):
    total_funcionarios: int
    total_salarios: float
    salario_medio: float
    estatisticas_por_cargo: List[EstatisticasCargo]


class TipoVeiculo(str, Enum):
    CARRO = "Carro"
    MOTO = "Moto"
    CAMINHAO = "Caminhão"
    SUV = "SUV"
    OUTRO = "Outro"


class Veiculo(BaseModel):
    id: Optional[int] = None
    marca: str = Field(..., min_length=1, max_length=50)
    modelo: str = Field(..., min_length=1, max_length=50)
    ano: int = Field(..., ge=1900, le=2100)
    tipo: TipoVeiculo = Field(...)
    preco: float = Field(..., ge=0)
    disponivel: bool = Field(default=True)

    class Config:
        json_schema_extra = {
            "example": {
                "marca": "Toyota",
                "modelo": "Corolla",
                "ano": 2022,
                "tipo": "Carro",
                "preco": 120000.00,
                "disponivel": True
            }
        }


class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    telefone: Optional[str] = Field(None, max_length=20)
    cpf: str = Field(..., min_length=11, max_length=14)

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Carlos Souza",
                "email": "carlos@cliente.com",
                "telefone": "(11) 99999-8888",
                "cpf": "123.456.789-00"
            }
        }


class Venda(BaseModel):
    id: Optional[int] = None
    veiculo_id: int = Field(..., description="ID do veículo vendido")
    cliente_id: int = Field(..., description="ID do cliente comprador")
    funcionario_id: int = Field(..., description="ID do funcionário responsável")
    data_venda: date = Field(...)
    valor_venda: float = Field(..., ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "veiculo_id": 1,
                "cliente_id": 2,
                "funcionario_id": 3,
                "data_venda": "2024-06-01",
                "valor_venda": 115000.00
            }
        } 