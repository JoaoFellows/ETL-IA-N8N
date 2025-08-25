# Orquestração de IA com n8n para Análise de Dados

## Descrição

Este projeto é um backend em Python utilizando FastAPI para gerenciar diferentes tipos de agendas (IA, Marketing, RH). O sistema é containerizado com Docker, utiliza PostgreSQL como banco de dados e integra automações via n8n.

## Estrutura do Projeto

```
PyBack/
├── app/
│   ├── models.py           # Modelos SQLAlchemy
│   ├── database.py         # Conexão e sessão do banco
│   ├── main.py             # Inicialização do FastAPI e routers
│   ├── routes/             # Endpoints organizados por recurso
│   ├── schemas/            # Schemas Pydantic para validação
│   └── services/           # Lógica de acesso ao banco (CRUD)
├── requirements.txt        # Dependências Python
├── docker-compose.yml      # Orquestração dos containers
├── dockerfile              # Build do container FastAPI
├── .env                    # Variáveis de ambiente
├── AgenteIA.json           # Workflow do AI Agent no n8n
├── ETL.json                # Workflow do ETL no n8n
└── n8n_data/               # Dados persistentes do n8n
```

## Principais Tecnologias

- **FastAPI**: Framework web moderno e rápido para APIs.
- **SQLAlchemy**: ORM para manipulação do banco de dados.
- **PostgreSQL**: Banco de dados relacional.
- **Docker**: Containerização dos serviços.
- **n8n**: Automação de workflows.
- **Pydantic**: Validação de dados.

## Como rodar o projeto

1. **Suba os containers com Docker Compose**
   ```sh
   docker-compose up --build
   ```

2. **Acesse os serviços**
   - FastAPI: [http://localhost:8000/docs] (Swagger)
   - n8n: [http://localhost:5678]

3. **Testes**
   - **ETL:**  
     [Webhook ETL](http://localhost:5678/webhook/68777c06-72ec-49fd-b0cd-ee87d6b47e51)  
     <sub>Faça uma requisição POST para o link acima.</sub>
   - **n8n (Agente IA):**  
     [Webhook Agente IA](http://localhost:5678/webhook/4d32b57a-33ae-4ec9-aee1-7ba54a6b9496)  
     <sub>Faça uma requisição POST para o link acima, com o seguinte JSON:</sub>
     ```json
     {
       "prompt": "/SEU PROMPT AQUI/"
     }
     ```



## Endpoints principais

- **Agenda IA**
  - `POST /agendaIA/` — Cria evento IA
  - `GET /agendaIA/` — Lista eventos IA
  - `PATCH /agendaIA/{id}` — Atualiza evento IA (parcial)
  - `DELETE /agendaIA/{id}` — Remove evento IA

- **Agenda MKT**
  - `POST /agendaMKT/` — Cria evento Marketing
  - `GET /agendaMKT/` — Lista eventos Marketing
  - `PATCH /agendaMKT/{id}` — Atualiza evento Marketing (parcial)
  - `DELETE /agendaMKT/{id}` — Remove evento Marketing

- **Agenda RH**
  - `POST /agendaRH/` — Cria evento RH
  - `GET /agendaRH/` — Lista eventos RH
  - `PATCH /agendaRH/{id}` — Atualiza evento RH (parcial)
  - `DELETE /agendaRH/{id}` — Remove evento RH

- **Agendas agrupadas**
  - `GET /agendas/` — Retorna todas as agendas agrupadas

## Observações

- O banco de dados é recriado do zero se você rodar `docker-compose down -v` (apaga todos os dados).
- Como é um desafio apenas para testes, subi a .env já completa no github, para facilitar o teste da aplicação.

## Licença

MIT
