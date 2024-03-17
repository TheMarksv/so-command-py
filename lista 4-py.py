import win32net

def listar_usuarios_windows():
    try:
        # Inicializa uma lista vazia para armazenar os nomes dos usuários
        usuarios = []
        # Variável para controlar a continuação da enumeração de usuários
        resume = 0
        # Loop para enumerar os usuários
        while True:
            # Chama a função NetUserEnum para obter um lote de usuários
            data, total, resume = win32net.NetUserEnum(None, 0, win32net.FILTER_NORMAL_ACCOUNT, resume)
            # Adiciona os nomes dos usuários à lista
            for usuario in data:
                usuarios.append(usuario['name'])
            # Se não houver mais usuários a serem enumerados, sai do loop
            if resume == 0:
                break
        # Retorna a lista de usuários
        return usuarios
    except Exception as e:
        # Retorna a mensagem de erro se algo der errado
        return str(e)

# Chama a função para listar os usuários do Windows
usuarios_windows = listar_usuarios_windows()

# Verifica se o resultado é uma lista e imprime os usuários
if isinstance(usuarios_windows, list):
    print("Lista de usuários do Windows:")
    for usuario in usuarios_windows:
        print(usuario)
# Se ocorrer um erro, imprime a mensagem de erro
else:
    print(f"Erro: {usuarios_windows}")
