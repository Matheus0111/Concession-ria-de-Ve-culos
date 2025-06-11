from app.models import Funcionario, EstatisticasCargo, EstatisticasGerais, Veiculo, Cliente, Venda
from typing import List, Optional, Dict
from datetime import date


class Database:
    def __init__(self):
        self.funcionarios: List[Funcionario] = []
        self.veiculos: List[Veiculo] = []
        self.clientes: List[Cliente] = []
        self.vendas: List[Venda] = []
        self.counter = 1
        self.veiculo_counter = 1
        self.cliente_counter = 1
        self.venda_counter = 1
    
    def get_all_funcionarios(self) -> List[Funcionario]:
        return self.funcionarios
    
    def get_funcionario_by_id(self, funcionario_id: int) -> Optional[Funcionario]:
        for funcionario in self.funcionarios:
            if funcionario.id == funcionario_id:
                return funcionario
        return None
    
    def add_funcionario(self, funcionario: Funcionario) -> Funcionario:
        funcionario.id = self.counter
        self.counter += 1
        self.funcionarios.append(funcionario)
        return funcionario
    
    def update_funcionario(self, funcionario_id: int, updated_funcionario: Funcionario) -> Optional[Funcionario]:
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == funcionario_id:
                updated_funcionario.id = funcionario_id
                self.funcionarios[i] = updated_funcionario
                return updated_funcionario
        return None
    
    def delete_funcionario(self, funcionario_id: int) -> bool:
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == funcionario_id:
                self.funcionarios.pop(i)
                return True
        return False
    
    def filtrar_por_salario(self, salario_min: Optional[float] = None, salario_max: Optional[float] = None) -> List[Funcionario]:
        """
        Filtra funcionários por faixa salarial
        """
        resultado = self.funcionarios.copy()
        
        if salario_min is not None:
            resultado = [f for f in resultado if f.salario >= salario_min]
        
        if salario_max is not None:
            resultado = [f for f in resultado if f.salario <= salario_max]
            
        return resultado
    
    def filtrar_por_data_contratacao(self, data_inicial: Optional[date] = None, data_final: Optional[date] = None) -> List[Funcionario]:
        """
        Filtra funcionários por período de contratação
        """
        resultado = self.funcionarios.copy()
        
        if data_inicial is not None:
            resultado = [f for f in resultado if f.data_contratacao >= data_inicial]
        
        if data_final is not None:
            resultado = [f for f in resultado if f.data_contratacao <= data_final]
            
        return resultado
    
    def filtrar_por_cargo(self, cargo: str) -> List[Funcionario]:
        """
        Filtra funcionários por cargo
        """
        return [f for f in self.funcionarios if f.cargo.value == cargo]
    
    def calcular_estatisticas(self) -> EstatisticasGerais:
        """
        Calcula estatísticas gerais e por cargo dos funcionários
        """
        if not self.funcionarios:
            return EstatisticasGerais(
                total_funcionarios=0,
                total_salarios=0,
                salario_medio=0,
                estatisticas_por_cargo=[]
            )
        
        # Agrupa funcionários por cargo
        funcionarios_por_cargo: Dict[str, List[Funcionario]] = {}
        for f in self.funcionarios:
            cargo = f.cargo.value
            if cargo not in funcionarios_por_cargo:
                funcionarios_por_cargo[cargo] = []
            funcionarios_por_cargo[cargo].append(f)
        
        # Calcula estatísticas por cargo
        estatisticas_por_cargo = []
        for cargo, funcionarios in funcionarios_por_cargo.items():
            qtd = len(funcionarios)
            salario_total = sum(f.salario for f in funcionarios)
            salario_medio = salario_total / qtd if qtd > 0 else 0
            
            estatisticas_por_cargo.append(EstatisticasCargo(
                cargo=cargo,
                quantidade=qtd,
                salario_total=salario_total,
                salario_medio=salario_medio
            ))
        
        # Calcula estatísticas gerais
        total_funcionarios = len(self.funcionarios)
        total_salarios = sum(f.salario for f in self.funcionarios)
        salario_medio = total_salarios / total_funcionarios if total_funcionarios > 0 else 0
        
        return EstatisticasGerais(
            total_funcionarios=total_funcionarios,
            total_salarios=total_salarios,
            salario_medio=salario_medio,
            estatisticas_por_cargo=estatisticas_por_cargo
        )

    # CRUD Veículos
    def get_all_veiculos(self) -> List[Veiculo]:
        return self.veiculos

    def get_veiculo_by_id(self, veiculo_id: int) -> Optional[Veiculo]:
        for veiculo in self.veiculos:
            if veiculo.id == veiculo_id:
                return veiculo
        return None

    def add_veiculo(self, veiculo: Veiculo) -> Veiculo:
        veiculo.id = self.veiculo_counter
        self.veiculo_counter += 1
        self.veiculos.append(veiculo)
        return veiculo

    def update_veiculo(self, veiculo_id: int, updated_veiculo: Veiculo) -> Optional[Veiculo]:
        for i, veiculo in enumerate(self.veiculos):
            if veiculo.id == veiculo_id:
                updated_veiculo.id = veiculo_id
                self.veiculos[i] = updated_veiculo
                return updated_veiculo
        return None

    def delete_veiculo(self, veiculo_id: int) -> bool:
        for i, veiculo in enumerate(self.veiculos):
            if veiculo.id == veiculo_id:
                self.veiculos.pop(i)
                return True
        return False

    # CRUD Clientes
    def get_all_clientes(self) -> List[Cliente]:
        return self.clientes

    def get_cliente_by_id(self, cliente_id: int) -> Optional[Cliente]:
        for cliente in self.clientes:
            if cliente.id == cliente_id:
                return cliente
        return None

    def add_cliente(self, cliente: Cliente) -> Cliente:
        cliente.id = self.cliente_counter
        self.cliente_counter += 1
        self.clientes.append(cliente)
        return cliente

    def update_cliente(self, cliente_id: int, updated_cliente: Cliente) -> Optional[Cliente]:
        for i, cliente in enumerate(self.clientes):
            if cliente.id == cliente_id:
                updated_cliente.id = cliente_id
                self.clientes[i] = updated_cliente
                return updated_cliente
        return None

    def delete_cliente(self, cliente_id: int) -> bool:
        for i, cliente in enumerate(self.clientes):
            if cliente.id == cliente_id:
                self.clientes.pop(i)
                return True
        return False

    # CRUD Vendas
    def get_all_vendas(self) -> List[Venda]:
        return self.vendas

    def get_venda_by_id(self, venda_id: int) -> Optional[Venda]:
        for venda in self.vendas:
            if venda.id == venda_id:
                return venda
        return None

    def add_venda(self, venda: Venda) -> Venda:
        venda.id = self.venda_counter
        self.venda_counter += 1
        self.vendas.append(venda)
        return venda

    def update_venda(self, venda_id: int, updated_venda: Venda) -> Optional[Venda]:
        for i, venda in enumerate(self.vendas):
            if venda.id == venda_id:
                updated_venda.id = venda_id
                self.vendas[i] = updated_venda
                return updated_venda
        return None

    def delete_venda(self, venda_id: int) -> bool:
        for i, venda in enumerate(self.vendas):
            if venda.id == venda_id:
                self.vendas.pop(i)
                return True
        return False


# Criando uma instância global do banco de dados
db = Database() 