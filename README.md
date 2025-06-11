# API de Pessoas

Uma API simples em Python para gerenciamento de pessoas, construída com FastAPI.

## Funcionalidades

- Cadastro de pessoas
- Listagem de pessoas
- Busca de pessoa por ID
- Atualização de dados de pessoas
- Exclusão de pessoas

## Como executar

### Método 1: Diretamente com Python

1. Clone este repositório
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Execute a aplicação:
   ```
   python run.py
   ```
4. Acesse a documentação da API em http://localhost:8000/docs

### Método 2: Usando Docker

1. Clone este repositório
2. Construa e inicie o container usando Docker:
   ```
   docker build -t pessoas-api .
   docker run -d -p 8000:8000 --name pessoas-api pessoas-api
   ```
3. Acesse a documentação da API em http://localhost:8000/docs

Para parar o container:
```
docker stop pessoas-api
docker rm pessoas-api
```

## Endpoints disponíveis

- `GET /api/pessoas` - Lista todas as pessoas
- `GET /api/pessoas/{id}` - Obtém detalhes de uma pessoa pelo ID
- `POST /api/pessoas` - Cadastra uma nova pessoa
- `PUT /api/pessoas/{id}` - Atualiza os dados de uma pessoa
- `DELETE /api/pessoas/{id}` - Remove uma pessoa

## Exemplo de uso

### Criar uma pessoa
```bash
curl -X POST "http://localhost:8000/api/pessoas" \
     -H "Content-Type: application/json" \
     -d '{"name": "João Silva", "email": "joao@example.com", "birth_date": "1990-01-01", "phone": "(11) 98765-4321"}'
```

### Listar todas as pessoas
```bash
curl -X GET "http://localhost:8000/api/pessoas"
```