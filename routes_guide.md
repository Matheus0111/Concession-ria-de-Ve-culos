# Guia de Execução das Rotas - API de Funcionários

Este documento apresenta um guia detalhado sobre como utilizar cada uma das rotas disponíveis na API de Funcionários.

## Pré-requisitos

- A API deve estar em execução (comando `python run.py`)
- O servidor estará disponível em: http://localhost:8000

## Ferramentas para Teste

Você pode testar as rotas usando:
- A interface Swagger disponível em: http://localhost:8000/docs
- Ferramentas como cURL, Postman ou Insomnia
- Qualquer biblioteca HTTP em suas aplicações

## Endpoints Disponíveis

### 1. Obter lista de funcionários

**URL:** `/api/funcionarios`  
**Método:** `GET`  
**Autenticação:** Não requerida  
**Filtros opcionais:**
- `cargo`: Filtra por cargo específico
- `salario_min`: Filtra por salário mínimo
- `salario_max`: Filtra por salário máximo
- `data_contratacao_inicial`: Filtra por data de contratação inicial (formato YYYY-MM-DD)
- `data_contratacao_final`: Filtra por data de contratação final (formato YYYY-MM-DD)

**Exemplo cURL (sem filtros):**
```bash
curl -X GET "http://localhost:8000/api/funcionarios"
```

**Exemplo cURL (com filtros):**
```bash
curl -X GET "http://localhost:8000/api/funcionarios?cargo=Desenvolvedor&salario_min=5000&data_contratacao_inicial=2021-01-01"
```

**Resposta de sucesso (200 OK):**
```json
[
  {
    "id": 2,
    "nome": "Carlos Oliveira",
    "email": "carlos@exemplo.com",
    "data_nascimento": "1992-08-22",
    "telefone": "(11) 91234-5678",
    "cargo": "Desenvolvedor",
    "data_contratacao": "2020-07-15",
    "salario": 7800.0
  },
  ...
]
```

### 2. Obter funcionário específico

**URL:** `/api/funcionarios/{id}`  
**Método:** `GET`  
**Autenticação:** Não requerida

**Parâmetros:**
- `id`: ID do funcionário (número inteiro)

**Exemplo cURL:**
```bash
curl -X GET "http://localhost:8000/api/funcionarios/1"
```

**Resposta de sucesso (200 OK):**
```json
{
  "id": 1,
  "nome": "Maria Santos",
  "email": "maria@exemplo.com",
  "data_nascimento": "1985-05-15",
  "telefone": "(21) 99876-5432",
  "cargo": "Gerente",
  "data_contratacao": "2018-03-10",
  "salario": 12500.0
}
```

**Resposta de erro (404 Not Found):**
```json
{
  "detail": "Funcionário com ID 999 não encontrado"
}
```

### 3. Criar novo funcionário

**URL:** `/api/funcionarios`  
**Método:** `POST`  
**Autenticação:** Não requerida  
**Content-Type:** `application/json`

**Corpo da requisição:**
```json
{
  "nome": "Paulo Roberto",
  "email": "paulo@exemplo.com",
  "data_nascimento": "1987-10-20",
  "telefone": "(11) 98888-7777",
  "cargo": "Analista",
  "data_contratacao": "2022-03-15",
  "salario": 6800.00
}
```

**Exemplo cURL:**
```bash
curl -X POST "http://localhost:8000/api/funcionarios" \
     -H "Content-Type: application/json" \
     -d '{
           "nome": "Paulo Roberto",
           "email": "paulo@exemplo.com",
           "data_nascimento": "1987-10-20",
           "telefone": "(11) 98888-7777",
           "cargo": "Analista",
           "data_contratacao": "2022-03-15",
           "salario": 6800.00
         }'
```

**Resposta de sucesso (201 Created):**
```json
{
  "id": 11,
  "nome": "Paulo Roberto",
  "email": "paulo@exemplo.com",
  "data_nascimento": "1987-10-20",
  "telefone": "(11) 98888-7777",
  "cargo": "Analista",
  "data_contratacao": "2022-03-15",
  "salario": 6800.00
}
```

### 4. Atualizar funcionário existente

**URL:** `/api/funcionarios/{id}`  
**Método:** `PUT`  
**Autenticação:** Não requerida  
**Content-Type:** `application/json`

**Parâmetros:**
- `id`: ID do funcionário (número inteiro)

**Corpo da requisição:**
```json
{
  "nome": "Maria Santos Silva",
  "email": "maria.silva@exemplo.com",
  "data_nascimento": "1985-05-15",
  "telefone": "(21) 99876-5432",
  "cargo": "Gerente",
  "data_contratacao": "2018-03-10",
  "salario": 13200.00
}
```

**Exemplo cURL:**
```bash
curl -X PUT "http://localhost:8000/api/funcionarios/1" \
     -H "Content-Type: application/json" \
     -d '{
           "nome": "Maria Santos Silva",
           "email": "maria.silva@exemplo.com",
           "data_nascimento": "1985-05-15",
           "telefone": "(21) 99876-5432",
           "cargo": "Gerente",
           "data_contratacao": "2018-03-10",
           "salario": 13200.00
         }'
```

**Resposta de sucesso (200 OK):**
```json
{
  "id": 1,
  "nome": "Maria Santos Silva",
  "email": "maria.silva@exemplo.com",
  "data_nascimento": "1985-05-15",
  "telefone": "(21) 99876-5432",
  "cargo": "Gerente",
  "data_contratacao": "2018-03-10",
  "salario": 13200.00
}
```

### 5. Excluir funcionário

**URL:** `/api/funcionarios/{id}`  
**Método:** `DELETE`  
**Autenticação:** Não requerida

**Parâmetros:**
- `id`: ID do funcionário (número inteiro)

**Exemplo cURL:**
```bash
curl -X DELETE "http://localhost:8000/api/funcionarios/3"
```

**Resposta de sucesso (204 No Content):**
```
(Sem corpo na resposta)
```

### 6. Filtrar funcionários por salário

**URL:** `/api/funcionarios/filtro/salario`  
**Método:** `GET`  
**Autenticação:** Não requerida  
**Parâmetros de consulta:**
- `salario_min`: Salário mínimo (opcional)
- `salario_max`: Salário máximo (opcional)

**Exemplo cURL:**
```bash
curl -X GET "http://localhost:8000/api/funcionarios/filtro/salario?salario_min=7000&salario_max=10000"
```

**Resposta de sucesso (200 OK):**
```json
[
  {
    "id": 2,
    "nome": "Carlos Oliveira",
    "email": "carlos@exemplo.com",
    "data_nascimento": "1992-08-22",
    "telefone": "(11) 91234-5678",
    "cargo": "Desenvolvedor",
    "data_contratacao": "2020-07-15",
    "salario": 7800.0
  },
  ...
]
```

### 7. Filtrar funcionários por data de contratação

**URL:** `/api/funcionarios/filtro/data-contratacao`  
**Método:** `GET`  
**Autenticação:** Não requerida  
**Parâmetros de consulta:**
- `data_inicial`: Data inicial de contratação (formato YYYY-MM-DD, opcional)
- `data_final`: Data final de contratação (formato YYYY-MM-DD, opcional)

**Exemplo cURL:**
```bash
curl -X GET "http://localhost:8000/api/funcionarios/filtro/data-contratacao?data_inicial=2020-01-01&data_final=2022-12-31"
```

**Resposta de sucesso (200 OK):**
```json
[
  {
    "id": 2,
    "nome": "Carlos Oliveira",
    "email": "carlos@exemplo.com",
    "data_nascimento": "1992-08-22",
    "telefone": "(11) 91234-5678",
    "cargo": "Desenvolvedor",
    "data_contratacao": "2020-07-15",
    "salario": 7800.0
  },
  ...
]
```

### 8. Filtrar funcionários por cargo

**URL:** `/api/funcionarios/filtro/cargo/{cargo}`  
**Método:** `GET`  
**Autenticação:** Não requerida  
**Parâmetros:**
- `cargo`: Cargo para filtrar (string)

**Exemplo cURL:**
```bash
curl -X GET "http://localhost:8000/api/funcionarios/filtro/cargo/Desenvolvedor"
```

**Resposta de sucesso (200 OK):**
```json
[
  {
    "id": 2,
    "nome": "Carlos Oliveira",
    "email": "carlos@exemplo.com",
    "data_nascimento": "1992-08-22",
    "telefone": "(11) 91234-5678",
    "cargo": "Desenvolvedor",
    "data_contratacao": "2020-07-15",
    "salario": 7800.0
  },
  ...
]
```

### 9. Obter estatísticas de funcionários

**URL:** `/api/funcionarios/estatisticas`  
**Método:** `GET`  
**Autenticação:** Não requerida

**Exemplo cURL:**
```bash
curl -X GET "http://localhost:8000/api/funcionarios/estatisticas"
```

**Resposta de sucesso (200 OK):**
```json
{
  "total_funcionarios": 10,
  "total_salarios": 78400.0,
  "salario_medio": 7840.0,
  "estatisticas_por_cargo": [
    {
      "cargo": "Desenvolvedor",
      "quantidade": 3,
      "salario_total": 22500.0,
      "salario_medio": 7500.0
    },
    {
      "cargo": "Gerente",
      "quantidade": 1,
      "salario_total": 12500.0,
      "salario_medio": 12500.0
    },
    ...
  ]
}
```

### 10. Obter lista de cargos disponíveis

**URL:** `/api/cargos`  
**Método:** `GET`  
**Autenticação:** Não requerida

**Exemplo cURL:**
```bash
curl -X GET "http://localhost:8000/api/cargos"
```

**Resposta de sucesso (200 OK):**
```json
[
  "Desenvolvedor",
  "Analista",
  "Gerente",
  "Diretor",
  "Estagiário",
  "Administrativo",
  "Recursos Humanos",
  "Financeiro",
  "Suporte",
  "Outros"
]
```

## Códigos de Resposta HTTP

- `200 OK`: Requisição bem-sucedida
- `201 Created`: Recurso criado com sucesso
- `204 No Content`: Requisição bem-sucedida, sem conteúdo na resposta
- `404 Not Found`: Recurso não encontrado
- `422 Unprocessable Entity`: Falha na validação dos dados enviados 