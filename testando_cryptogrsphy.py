from typing import Any

from cryptography.fernet import Fernet


def gerar_token(local="cryptography/"):
    """Gera um numero de token de criptografia e guarda o mesmo no arquivo
    token.key

    Args:
        local (Str): pasta com a localização da token.key.
        Default cryptography/
    """
    token = Fernet.generate_key()
    arquivo = local + "token.key"
    with open(arquivo, "wb") as token_file:
        token_file.write(token)
        print(f"Gerado token = {token}")


def read_token(local="cryptography/"):
    """Ler token de criptografia no arquivo token.key

    Args:
        local (Str): pasta com a localização da token.key.
        Default cryptography/

    Returns:
        str: chave token
    """
    arquivo = local + "token.key"
    file = open(arquivo, "r")
    token = file.read()
    file.close()
    return token


def encrypt_message(dados: Any):
    """Criptografa dados com cryptography.

    Args:
        dados (Any): Informação a ser criptografada

    Returns:
        [str]: Informação criptografada
    """
    token = read_token()
    encoded_msg = dados.encode()
    f = Fernet(token)
    encrypt_msg = f.encrypt(encoded_msg)
    return encrypt_msg


def decrypt_message(data: Any):
    """Descriptografa dados com cryptography.

    Args:
        dados (Any): Informação a ser descriptografada

    Returns:
        [str]: Informação descriptografada
    """
    token = read_token()
    f = Fernet(token)
    decrypt_msn = f.decrypt(data)
    return decrypt_msn.decode()


# .Testando o código.
if __name__ == "__main__":

    """mensagem_secreta = "Hello Word!!!"

    mensagem_secreta_encrypt = encrypt_message(mensagem_secreta)

    mensagem_secreta_decrypt = decrypt_message(mensagem_secreta_encrypt)

    print(f"\nMensagem a ser criptografada = {mensagem_secreta}")

    print("-" * 50)

    print(f"Mensagem encrypt = {mensagem_secreta_encrypt}")

    print("-" * 50)

    print(f"Mensagem decrypt = {mensagem_secreta_decrypt}")"""

    # . Gerar um token de criptografia.
    """token = Fernet.generate_key()
    print(f"\n{token = }\n\n{type(token) = }\n")

    # transformando em texto
    token_txt = token.decode()
    print(f"\n{token_txt = }\n\n{type(token_txt) = }\n")

    # transformando em bytes
    token_b = token_txt.encode()
    print(f"\n{token_b = }\n\n{type(token_b) = }\n")"""

    token = Fernet.generate_key()
    msg = 1
    encoded_msg = str(msg).encode()
    f = Fernet(token)
    encrypt_msg = f.encrypt(encoded_msg).decode()
    print(f"\n{msg = }\n\n{encrypt_msg = }\n\n{type(encrypt_msg) = }\n")
