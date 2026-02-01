from fastmcp import FastMCP
import requests
import sys

mcp = FastMCP("BuscaCEP Server")

@mcp.tool
def busca_cep(cep: str) -> dict:
  """
  Buca informações de endereço a partie do CEp fornecido usando a api do ViaCEP.
  """
  try :
    url = f"https://viapcep.com.br/{cep}/json"
    r = requests.get(url, timeout=5)
    data = r.json()
    if "erro" in data:
      return {"error": "CEP não encontrado."}
    return data
  except requests.RequestException as e:
    return {"error": str(e)}

if (__name__ == "__main__"):
  #Criar um buffer para garantir as respostas no console em tempo real
  sys.stdout.reconfigure(line_buffering=True)
  #Iniciar servidor MCP
  mcp.run()

