# Análise de Desempenho Acadêmico com Regressão Linear

Este projeto tem como objetivo analisar a relação entre a pontuação dos alunos e suas respectivas horas de estudo utilizando um modelo de regressão linear. O modelo é desenvolvido e avaliado usando diversas bibliotecas de Python e disponibilizado através de uma API local.

## Tecnologias Utilizadas

- **Bibliotecas de Análise e Visualização:**
  - `scikit-learn`
  - `scipy`
  - `pandas`
  - `matplotlib`
  - `statsmodels`
  - `pingouin`
  - `seaborn`
  - `ipykernel`

- **Framework para API:**
  - `FastAPI`
  - `uvicorn`
  - `pydantic`

## Estrutura do Projeto

O projeto está dividido em dois principais componentes:

### 1. Jupyter Notebook (`.ipynb`)

O notebook está dividido nas seguintes seções:

1. **Carga dos Dados:** Importação dos dados e preparação para análise.
2. **Análise Exploratória dos Dados:** Análise inicial para entender as características e padrões dos dados. A análise dos dados procura confirmar a hipótese da relação entre a quantidade de horas de estudo e o desempnho em um exame de um conjunto de alunos.
3. **Treinamento do Modelo:** Construção e treinamento do modelo de regressão linear.
4. **Validação do Modelo com Métricas:** Avaliação do desempenho do modelo usando métricas apropriadas.
5. **Análise de Resíduos:** Análise dos resíduos para verificar a adequação do modelo.
6. **Predições com o Modelo:** Utilização do modelo para fazer previsões baseadas nos dados de entrada.
7. **Salvamento do Modelo:** Salvamento do modelo treinado para uso futuro.

### 2. API Local (`api.py`)

Na pasta raiz do projeto, você encontrará um arquivo Python (`api_modelo_regressao.py`) que utiliza o `FastAPI` para disponibilizar o modelo de regressão linear através de uma API local. Isso permite que o modelo seja acessado e utilizado para previsões de forma prática.

## Como Executar

### Requisitos

Certifique-se de ter todas as bibliotecas necessárias instaladas. No desenvolvimento do projeto, foi utilizado o ambiente virtual gerado pelo **pipenv**.

### Executando o jupyter Notebook
1. Após clonar o repositório, execute o comando
```bash
pipenv install
```

2. Rode o ambiente virtual
```bash
pipenv shell
```
3. Execute o ipynb

### Executando a API Local

1. Inicie o servidor FastAPI:
```bash
uvicorn api_modelo_regressao:app --reload
```

2. Acesse a API localmente no navegador ou através de ferramentas como curl ou Postman em:
```bash
http://127.0.0.1:8000
```

2. Faça um POST no formato JSON (substitua 0 pelo numero de horas de estudo):
```JSON
{
  "time_study": 0 
}
```
## Contribuições
Se você deseja contribuir para o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto é licenciado sob a Licença MIT.