from fastapi import APIRouter, HTTPException, status, Response, Query, Path
from typing import List, Optional

from datetime import date
from app.models import Funcionario, EstatisticasGerais, Cargo, Veiculo, Cliente, Venda
from app.database import db


router = APIRouter(prefix="/api", tags=["concessionaria"])


@router.get("/funcionarios", response_model=List[Funcionario])
def get_funcionarios(
    cargo: Optional[str] = None,
    salario_min: Optional[float] = None,
    salario_max: Optional[float] = None,
    data_contratacao_inicial: Optional[date] = None,
    data_contratacao_final: Optional[date] = None
):
    """
    Obtém a lista de funcionários da concessionária, com opções de filtragem
    
    - **cargo**: Filtra por cargo específico
    - **salario_min**: Filtra por salário mínimo
    - **salario_max**: Filtra por salário máximo
    - **data_contratacao_inicial**: Filtra por data de contratação inicial
    - **data_contratacao_final**: Filtra por data de contratação final
    """
    resultado = db.get_all_funcionarios()
    
    if cargo:
        resultado = [f for f in resultado if f.cargo.value == cargo]
    
    if salario_min is not None or salario_max is not None:
        resultado = db.filtrar_por_salario(salario_min, salario_max)
    
    if data_contratacao_inicial is not None or data_contratacao_final is not None:
        resultado = db.filtrar_por_data_contratacao(data_contratacao_inicial, data_contratacao_final)
    
    return resultado


@router.get("/funcionarios/{funcionario_id}", response_model=Funcionario)
def get_funcionario(funcionario_id: int = Path(..., description="ID do funcionário")):
    """
    Obtém os detalhes de um funcionário da concessionária pelo ID
    """
    funcionario = db.get_funcionario_by_id(funcionario_id)
    if funcionario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Funcionário com ID {funcionario_id} não encontrado"
        )
    return funcionario


@router.post("/funcionarios", response_model=Funcionario, status_code=status.HTTP_201_CREATED)
def create_funcionario(funcionario: Funcionario):
    """
    Cria um novo funcionário na concessionária
    """
    return db.add_funcionario(funcionario)


@router.put("/funcionarios/{funcionario_id}", response_model=Funcionario)
def update_funcionario(
    funcionario_id: int = Path(..., description="ID do funcionário"), 
    funcionario: Funcionario = ...
):
    """
    Atualiza os dados de um funcionário da concessionária
    """
    updated_funcionario = db.update_funcionario(funcionario_id, funcionario)
    if updated_funcionario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Funcionário com ID {funcionario_id} não encontrado"
        )
    return updated_funcionario


@router.delete("/funcionarios/{funcionario_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_funcionario(funcionario_id: int = Path(..., description="ID do funcionário")):
    """
    Remove um funcionário da concessionária
    """
    success = db.delete_funcionario(funcionario_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Funcionário com ID {funcionario_id} não encontrado"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/funcionarios/filtro/salario", response_model=List[Funcionario])
def filtrar_por_salario(
    salario_min: Optional[float] = Query(None, description="Salário mínimo", ge=0),
    salario_max: Optional[float] = Query(None, description="Salário máximo", ge=0)
):
    """
    Filtra funcionários por faixa salarial
    """
    return db.filtrar_por_salario(salario_min, salario_max)


@router.get("/funcionarios/filtro/data-contratacao", response_model=List[Funcionario])
def filtrar_por_data_contratacao(
    data_inicial: Optional[date] = Query(None, description="Data inicial de contratação"),
    data_final: Optional[date] = Query(None, description="Data final de contratação")
):
    """
    Filtra funcionários por data de contratação
    """
    return db.filtrar_por_data_contratacao(data_inicial, data_final)


@router.get("/funcionarios/filtro/cargo/{cargo}", response_model=List[Funcionario])
def filtrar_por_cargo(cargo: str = Path(..., description="Cargo para filtrar")):
    """
    Filtra funcionários por cargo
    """
    return db.filtrar_por_cargo(cargo)


@router.get("/funcionarios/estatisticas", response_model=EstatisticasGerais)
def get_estatisticas():
    """
    Obtém estatísticas sobre os funcionários da concessionária
    
    Retorna:
    - Total de funcionários
    - Total de salários
    - Salário médio
    - Estatísticas detalhadas por cargo
    """
    return db.calcular_estatisticas()


@router.get("/cargos", response_model=List[str])
def get_cargos():
    """
    Retorna a lista de todos os cargos disponíveis
    """
    return [cargo.value for cargo in Cargo]


# Rotas de Veículos
@router.get("/veiculos", response_model=List[Veiculo])
def get_veiculos():
    """Obtém a lista de veículos cadastrados"""
    return db.get_all_veiculos()

@router.get("/veiculos/{veiculo_id}", response_model=Veiculo)
def get_veiculo(veiculo_id: int):
    """Obtém detalhes de um veículo pelo ID"""
    veiculo = db.get_veiculo_by_id(veiculo_id)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo

@router.post("/veiculos", response_model=Veiculo, status_code=status.HTTP_201_CREATED)
def create_veiculo(veiculo: Veiculo):
    """Cadastra um novo veículo"""
    return db.add_veiculo(veiculo)

@router.put("/veiculos/{veiculo_id}", response_model=Veiculo)
def update_veiculo(veiculo_id: int, veiculo: Veiculo):
    """Atualiza os dados de um veículo"""
    updated = db.update_veiculo(veiculo_id, veiculo)
    if updated is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return updated

@router.delete("/veiculos/{veiculo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_veiculo(veiculo_id: int):
    """Remove um veículo do cadastro"""
    if not db.delete_veiculo(veiculo_id):
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Rotas de Clientes
@router.get("/clientes", response_model=List[Cliente])
def get_clientes():
    """Obtém a lista de clientes cadastrados"""
    return db.get_all_clientes()

@router.get("/clientes/{cliente_id}", response_model=Cliente)
def get_cliente(cliente_id: int):
    """Obtém detalhes de um cliente pelo ID"""
    cliente = db.get_cliente_by_id(cliente_id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@router.post("/clientes", response_model=Cliente, status_code=status.HTTP_201_CREATED)
def create_cliente(cliente: Cliente):
    """Cadastra um novo cliente"""
    return db.add_cliente(cliente)

@router.put("/clientes/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, cliente: Cliente):
    """Atualiza os dados de um cliente"""
    updated = db.update_cliente(cliente_id, cliente)
    if updated is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return updated

@router.delete("/clientes/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(cliente_id: int):
    """Remove um cliente do cadastro"""
    if not db.delete_cliente(cliente_id):
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Rotas de Vendas
@router.get("/vendas", response_model=List[Venda])
def get_vendas():
    """Obtém a lista de vendas realizadas"""
    return db.get_all_vendas()

@router.get("/vendas/{venda_id}", response_model=Venda)
def get_venda(venda_id: int):
    """Obtém detalhes de uma venda pelo ID"""
    venda = db.get_venda_by_id(venda_id)
    if venda is None:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return venda

@router.post("/vendas", response_model=Venda, status_code=status.HTTP_201_CREATED)
def create_venda(venda: Venda):
    """Registra uma nova venda"""
    return db.add_venda(venda)

@router.put("/vendas/{venda_id}", response_model=Venda)
def update_venda(venda_id: int, venda: Venda):
    """Atualiza os dados de uma venda"""
    updated = db.update_venda(venda_id, venda)
    if updated is None:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return updated

@router.delete("/vendas/{venda_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_venda(venda_id: int):
    """Remove uma venda do cadastro"""
    if not db.delete_venda(venda_id):
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return Response(status_code=status.HTTP_204_NO_CONTENT) 