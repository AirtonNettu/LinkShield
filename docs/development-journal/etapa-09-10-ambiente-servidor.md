# Etapas 09-10 — Ambiente e Servidor

## Objetivo

Garantir que a aplicação FastAPI pudesse ser executada localmente de forma consistente, utilizando ambiente isolado e servidor ASGI.

Nesta fase o objetivo principal foi validar que o backend do LinkShield estava preparado para execução, testes e desenvolvimento contínuo.

---

## Servidor da aplicação

O LinkShield passou a utilizar o **Uvicorn** como servidor da aplicação.

O FastAPI é responsável pela construção da aplicação e definição das rotas, enquanto o Uvicorn realiza a comunicação entre o cliente HTTP e a aplicação Python.

Fluxo da aplicação:

```text
Cliente
   |
   v
Uvicorn
   |
   v
FastAPI
   |
   v
Rotas da aplicação
```

O Uvicorn atua como servidor ASGI (*Asynchronous Server Gateway Interface*), permitindo que aplicações Python web recebam e processem requisições HTTP.

---

## Execução do projeto

O servidor passou a ser iniciado utilizando:

```bash
uvicorn app.main:app --reload
```

Onde:

- `app.main` representa o módulo Python onde está localizada a aplicação;
- `app` representa o objeto FastAPI criado dentro do arquivo `main.py`;
- `--reload` permite reiniciar automaticamente o servidor durante o desenvolvimento quando alterações são detectadas.

Exemplo:

```python
from fastapi import FastAPI

app = FastAPI()
```

O Uvicorn procura esse objeto `app` para iniciar a aplicação.

---

## Documentação automática

Foi validada a documentação automática gerada pelo FastAPI através do Swagger UI.

A documentação fica disponível em:

```
/docs
```

Essa funcionalidade permite:

- visualizar endpoints existentes;
- testar requisições;
- analisar contratos da API;
- verificar respostas retornadas pelo backend.

---

## Testes realizados

A aplicação foi testada utilizando:

```bash
curl http://127.0.0.1:8000/
```

Resultado esperado:

```json
{
    "message": "LinkShield API running"
}
```

Também foi validado o carregamento da documentação:

```bash
curl http://127.0.0.1:8000/docs
```

Confirmando que o FastAPI estava gerando corretamente a interface Swagger.

---

## Problemas encontrados

Durante o desenvolvimento ocorreram problemas relacionados ao ambiente Python.

Principais causas identificadas:

- terminal utilizando um interpretador Python diferente do ambiente virtual;
- ambiente virtual contendo caminhos antigos após movimentação da pasta do projeto;
- executáveis internos do `.venv` apontando para uma localização que não existia mais.

Exemplo do problema encontrado:

```
/home/airton/Área de trabalho/LinkShield/LinkShield/.venv/bin/python
```

O projeto posteriormente passou a utilizar outro caminho:

```
/home/airton/Área de trabalho/LinkShield/.venv
```

---

## Soluções aplicadas

Foram utilizadas validações para identificar o ambiente correto:

```bash
which python
```

```bash
which python3
```

```bash
python --version
```

Também foi validado o funcionamento direto do interpretador do ambiente:

```bash
./.venv/bin/python --version
```

Quando o ambiente virtual apresentou referências inválidas, foi necessário recriar o `.venv`.

Após a correção, o ambiente voltou a executar normalmente:

- FastAPI instalado;
- Uvicorn funcionando;
- servidor iniciando corretamente.

---

## Conceitos aprendidos

Nesta fase foram consolidados conceitos importantes:

- diferença entre framework web e servidor de aplicação;
- funcionamento básico do ASGI;
- execução de aplicações FastAPI;
- ambiente virtual Python;
- gerenciamento de dependências;
- documentação automática de APIs;
- diagnóstico de problemas relacionados ao ambiente.

---

## Resultado da etapa

Ao final das etapas 09-10 o LinkShield possuía:

- ambiente Python funcional;
- servidor Uvicorn configurado;
- aplicação FastAPI executando localmente;
- endpoint inicial respondendo corretamente;
- documentação Swagger disponível;
- processo básico de teste definido.

Esta etapa preparou a base para a organização das rotas da API realizada posteriormente na Etapa 11.