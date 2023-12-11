errors = {
    'success': "Sucesso!",
    'user_exists': "Usuário já existe!",
    'invalid_credentials': "Credenciais inválidas!",
    'password_mismatch': "Senhas não conferem"
}

def get_error(name):
    return errors[name]