# json.dump e json.load com arquivos

import os 
import json


NOME_ARQUIVO = 'aula290.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),                  # __file__ retorna o caminho absoluto | dirname retorna so o diretorio
         NOME_ARQUIVO
    )
)

# DICIONARIO ABAIXO
filme = {
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": True,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": None
}

# print(filme)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)                       # o objeto + nome do arquivo json

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)

os.unlink(CAMINHO_ABSOLUTO_ARQUIVO)             # APAGA O ARQUIVO NO FINAL
