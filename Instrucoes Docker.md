# Guia de Uso da API com Docker

Este documento apresenta instruções detalhadas sobre como executar a API de Pessoas usando Docker.

## Pré-requisitos

- Docker instalado na sua máquina.


## Execução

### Construir a imagem

```bash
docker build -t pessoas-api .
```

### Iniciar o container

```bash
docker run -d -p 8000:8000 --name pessoas-api pessoas-api
```

Parâmetros:
- `-d`: Executa o container em segundo plano
- `-p 8000:8000`: Mapeia a porta 8000 do container para a porta 8000 do host
- `--name pessoas-api`: Define um nome para o container

### Visualizar logs

```bash
docker logs -f pessoas-api
```

### Parar e remover o container

```bash
docker stop pessoas-api
docker rm pessoas-api
```

## Acessar a API

Após iniciar o container, a API estará disponível em:

- Documentação Swagger: http://localhost:8000/docs
- Documentação ReDoc: http://localhost:8000/redoc
- Endpoints da API: http://localhost:8000/api/...
