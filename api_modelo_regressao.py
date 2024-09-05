from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn 
import joblib

# Criar uma instância do FastAPI
app = FastAPI()

# Criar uma classe que terá os dados de request body para API
class request_body(BaseModel):
  time_study : float
  
# Carregar modelo para realizar a predição
modelo_pontuacao = joblib.load("./modelo_regressao.pkl")

@app.post("/predict")
def predict(data : request_body):
  # Prepara os dados para predição
  input_feature = [[data.time_study]]

  # Realizar a predição
  y_pred = modelo_pontuacao.predict(input_feature)[0].astype(int)

  return {"pontuacao_teste": y_pred.tolist()}