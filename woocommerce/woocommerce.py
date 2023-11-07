import requests

product_list_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=product_list',
    'descrição': 'Retorna uma lista exclusiva e ordenada de IDs de produtos, títulos de produtos, IDs de pedidos e subIDs se o produto for uma assinatura WooCommerce.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Substitua 'sua_api_key' pelo valor real da sua chave de API
api_key = 'sua_api_key'

# Adicione a chave de API ao cabeçalho
product_list_api['header']['api_key'] = api_key

# Realiza a chamada de API
response = requests.get(product_list_api['url'], headers=product_list_api['header'])

# Processa a resposta
if response.status_code == 200:
    data = response.json()
    print("Resposta da API:")
    print(data)
    # Faça algo com os dados da resposta
else:
    print(f'Erro na chamada de API: {response.status_code}')


# Dicionário para a API de ativação
activate_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=activate',
    'descrição': 'Ativar uma chave de API para acessar recursos específicos.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de desativação
deactivate_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=deactivate',
    'descrição': 'Desativar uma chave de API.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de status
status_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=status',
    'descrição': 'Verificar o status de uma chave de API.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

product_list_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=product_list',
    'descrição': 'Retorna uma lista exclusiva e ordenada de IDs de produtos, títulos de produtos, IDs de pedidos e subIDs se o produto for uma assinatura WooCommerce.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de verificação da chave de API ativa
verify_api_key_is_active_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=verify_api_key_is_active',
    'descrição': 'Retorna sucesso verdadeiro se a chave de API existir e for atribuída a um recurso de API ativo.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de informações do plugin
information_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=information',
    'descrição': 'Retorna informações sobre um plugin ou tema WooCommerce.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de verificação de atualização
update_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=update',
    'descrição': 'Retorna se uma atualização de software está disponível. Se autenticado, o URL para download do arquivo será retornado.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de informações do plugin (serializado)
plugin_information_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=plugininformation',
    'descrição': 'Retorna informações sobre um plugin ou tema WooCommerce em formato serializado.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}

# Dicionário para a API de verificação de atualização (serializado)
plugin_update_check_api = {
    'url': 'https://wc/?wc-api=wc-am-api&wc_am_action=pluginupdatecheck',
    'descrição': 'Retorna se uma atualização de software está disponível em formato serializado.',
    'header': {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
}