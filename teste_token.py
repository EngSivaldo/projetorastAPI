from security import criar_token, verificar_token

dados = {"usuario": "admin"}
token = criar_token(dados)
print("Token:", token)

decoded = verificar_token(token)
print("Decodificado:", decoded)
