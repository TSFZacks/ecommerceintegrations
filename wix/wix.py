import requests
# Credenciais do Aplicativo
client_id = "7909aa44-b7fe-49d4-ad45-3ff8a15c282b"  # Substitua pelo Client ID do seu aplicativo Wix
client_secret = "94f10e30-e446-4ddf-8be3-68ec6e5d595b"  # Substitua pelo Client Secret do seu aplicativo Wix
redirect_uri = "SEU_URL_DE_REDIRECIONAMENTO"  # Substitua pelo URL de redirecionamento do seu aplicativo
# Passo 1: Solicitar o Token de Acesso
def get_access_token(authorization_code):
    token_url = "https://www.wixapis.com/oauth/access"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": authorization_code,
        "redirect_uri": redirect_uri
    }

    response = requests.post(token_url, data=token_data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None

# Passo 2: Usar o Token de Acesso para Fazer uma Chamada à API do Wix
def call_wix_api(access_token):
    api_url = "https://www.wixapis.com/v1/..."
    
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    # Parâmetros da solicitação à API (exemplo)
    params = {
        "param1": "valor1",
        "param2": "valor2"
    }
    
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Autorização do usuário (exemplo)
authorization_code = "CODIGO_DE_AUTORIZACAO"  # Substitua pelo código de autorização recebido após a autorização do usuário

# Obtenha o token de acesso
access_token = get_access_token(authorization_code)

if access_token:
    # Use o token de acesso para fazer uma chamada à API do Wix
    response = call_wix_api(access_token)
    if response:
        print("Resposta da API do Wix:", response)
        data = response.json()
    else:
        print("Erro ao chamar a API do Wix.")
else:
    print("Erro ao obter o token de acesso.")

APIs = {
    'Site Properties - Informações Gerais': {
        'URL': 'https://www.wixapis.com/site-properties/v4/properties',
        'Descrição': '''Esta API recupera informações sobre o site, como idioma, 
        moeda de pagamento, fuso horário e outros detalhes. Isso pode ser útil 
        para rastrear as configurações e informações gerais do site.'''
    },
    'Site Properties - Perfil de Negócios': {
        'URL': 'https://www.wixapis.com/site-properties/v4/properties/business-profile',
        'Descrição': '''Esta API permite atualizar o perfil de negócios de um site, 
        incluindo informações como o nome da empresa, nome de exibição do site, 
        logotipo e descrição. Isso pode ser usado para manter as informações 
        comerciais atualizadas.'''
    },
    'Site Properties - Contato de Negócios': {
        'URL': 'https://www.wixapis.com/site-properties/v4/properties/business-contact',
        'Descrição': '''Esta API permite atualizar informações de contato de negócios, 
        como e-mail, telefone, fax e endereço. Isso pode ser útil para manter as informações 
        de contato da empresa atualizadas.'''
    },
    'Site Properties - Horário de Funcionamento': {
        'URL': 'https://www.wixapis.com/site-properties/v4/properties/business-schedule',
        'Descrição': '''Esta API atualiza o horário de funcionamento de um site, 
        incluindo horários regulares e especificações de funcionamento. Isso pode ser útil 
        para refletir as informações sobre o horário de funcionamento da empresa.'''
    },
    'Site Properties - Política de Assinatura': {
        'URL': 'https://www.wixapis.com/site-properties/v4/properties/policy',
        'Descrição': '''Esta API permite atualizar a política de assinatura padrão 
        de um site, que é relevante para questões de privacidade e conformidade. 
        Isso pode ser importante para o gerenciamento das escolhas de consentimento 
        dos visitantes do site.'''
    },
    'Locations - Recuperar Lista de Locais': {
        'URL': 'https://www.wixapis.com/locations/v1/locations',
        'Descrição': 'Recupera uma lista de locais.'
    },
    'Locations - Criar um Novo Local': {
        'URL': 'https://www.wixapis.com/locations/v1/locations',
        'Descrição': 'Cria um novo local.'
    },
    'Locations - Recuperar um Local por ID': {
        'URL': 'https://www.wixapis.com/locations/v1/locations/{id}',
        'Descrição': 'Recupera um local com base em um ID específico.'
    },
    'Locations - Atualizar um Local Existente': {
        'URL': 'https://www.wixapis.com/locations/v1/locations/{location.id}',
        'Descrição': 'Atualiza um local existente.'
    },
    'Contacts - Arquivar um Local': {
        'URL': 'https://www.wixapis.com/contacts/v4/contacts',
        'Descrição': 'Arquivo um local.'
    },
    'Contacts - Recuperar uma Lista de Contatos': {
        'URL': 'https://www.wixapis.com/locations/v1/locations/{id}/archive',
        'Descrição': 'Recupera uma lista de até 1.000 contatos por solicitação, com opções para classificação, filtrada e paginação.'
    },
    'Contacts - Criar um Novo Contato': {
        'URL': 'https://www.wixapis.com/contacts/v4/contacts',
        'Descrição': 'Crie um novo contato com base nas informações fornecidas no corpo da solicitação, incluindo nome, número de telefone ou endereço de e-mail.'
    },
    'Contacts - Recuperar um Contato por ID': {
        'URL': 'https://www.wixapis.com/contacts/v4/contacts/{contactId}',
        'Descrição': 'Recupera informações fornecidas de um contato com base no ID do contato fornecido, com opções para retornar campos específicos.'
    },
    'Contacts - Atualizar um Contato por ID': {
        'URL': 'https://www.wixapis.com/contacts/v4/contacts/{contactId}',
        'Descrição': 'Atualiza um contato com base no ID do contato fornecido e na revisão correspondente, evitando conflitos.'
    },
    'Contacts - Mesclar Contatos': {
        'URL': 'https://www.wixapis.com/contacts/v4/contacts/{targetContactId}/merge',
        'Descrição': 'Mescla contatos de origem no contato de destino, mantendo os dados do contato de destino e mesclando matrizes (e-mails, telefones, endereços e rótulos) dos contatos de origem.'
    },
    'Contacts - Excluir um Contato por ID': {
        'URL': 'https://www.wixapis.com/contacts/v4/contacts/{id}',
        'Descrição': 'Exclui um contato com base no ID do contato fornecido, use com cautela, pois a exclusão de contatos é uma ação irreversível.'
    },
    'Contacts - Listar Todas as Etiquetas de Contato': {
        'URL': 'https://www.wixapis.com/contacts/v4/labels',
        'Descrição': 'Esta API permite listar todas as tags de contato para um site. Ela oferece opções de filtragem e classificação, permitindo que seu aplicativo acesse e gerencie as etiquetas de contato.'
    },
    'Contacts - Recuperar ou Criar uma Etiqueta': {
        'URL': 'https://www.wixapis.com/contacts/v4/labels',
        'Descrição': 'Esta API permite recuperar ou criar uma etiqueta com base no nome especificado. Se uma etiqueta correspondente já existir, ela será devolvida. Caso contrário, uma nova etiqueta será criada e devolvida.'
    },
    'Contacts - Recuperar Detalhes de uma Etiqueta': {
        'URL': 'https://www.wixapis.com/contacts/v4/labels/{key}',
        'Descrição': 'Esta API recupera detalhes específicos de uma etiqueta com base na chave da etiqueta. Ela permite que você acesse informações detalhadas sobre uma etiqueta específica.'
    },
    'Contacts - Excluir uma Etiqueta': {
        'URL': 'https://www.wixapis.com/contacts/v4/labels/{key}',
        'Descrição': 'Esta API permite excluir uma etiqueta do site e remover os contatos aos quais ela se aplica. Use com cautela, pois a exclusão de etiquetas é uma ação irreversível.'
    },
    'Contacts - Atualizar Propriedades de uma Etiqueta': {
        'URL': 'https://www.wixapis.com/contacts/v4/labels/{label.key}',
        'Descrição': 'Esta API permite atualizar propriedades específicas de uma etiqueta existente. Você pode modificar o nome da etiqueta, mas a chave da etiqueta não pode ser alterada.'
    },
    'Contacts - Consultar Etiquetas de Contato': {
        'URL': 'https://www.wixapis.com/contacts/v4/labels/query',
        'Descrição': 'Esta API recupera uma lista de etiquetas de contato com base em uma consulta. Ela oferece suporte a filtragem e permite que você consulte etiquetas com base em critérios específicos.'
    },
    'Contacts - Listar Campos Estendidos': {
        'URL': 'https://www.wixapis.com/contacts/v4/extended-fields',
        'Descrição': 'Recupera uma lista de campos estendidos.'
    },
    'Contacts - Recuperar ou Criar Campo Estendido': {
        'URL': 'https://www.wixapis.com/contacts/v4/extended-fields',
        'Descrição': 'Recupera um campo personalizado com um determinado nome ou cria um se ele não existir.'
    },
    'Contacts - Recuperar Campo Estendido por Chave': {
        'URL': 'https://www.wixapis.com/contacts/v4/extended-fields/{key}',
        'Descrição': 'Recupera um campo estendido por sua chave.'
    },
    'Contacts - Excluir Campo Estendido': {
        'URL': 'https://www.wixapis.com/contacts/v4/extended-fields/{key}',
        'Descrição': 'Exclui um campo estendido.'
    },
    'Contacts - Atualizar Propriedades de Campo Estendido': {
        'URL': 'https://www.wixapis.com/contacts/v4/extended-fields/{field.key}',
        'Descrição': 'Atualiza as propriedades especificadas de um campo estendido.'
    },
    'Contacts - Consultar Campos Estendidos': {
        'URL': 'https://www.wixapis.com/contacts/v4/extended-fields/query',
        'Descrição': 'Recupera uma lista de campos estendidos com filtros e classificação opcionais.'
    }

    
}

create_coupon_endpoint = {
    "URL": "https://www.wixapis.com/stores/v2/coupons",
    "Descrição": "Cria um novo cupom"
}

update_coupon_endpoint = {
    "URL": "https://www.wixapis.com/stores/v2/coupons/{id}",
    "Descrição": "Atualiza um cupom"
}


delete_coupon_endpoint = {
    "URL": "https://www.wixapis.com/stores/v2/coupons/{id}",
    "Descrição": "Exclui um cupom pelo ID"
}

query_coupons_endpoint = {
    "URL": "https://www.wixapis.com/stores/v2/coupons/query",
    "Descrição": "Recupera uma lista de cupons com filtros e paginação"
}


bulk_delete_coupons_endpoint = {
    "URL": "https://www.wixapis.com/stores/v2/bulk/coupons/delete",
    "Descrição": "Exclui vários cupons em massa"
}


bulk_create_coupons_endpoint = {
    "URL": "https://www.wixapis.com/stores/v2/bulk/coupons/create",
    "Descrição": "Cria vários cupons em massa"
}

create_comment_payload = {
    "URL": "https://www.wixapis.com/comments/v1/comments",
    "Descrição": "Cria um novo comentário"
}

update_comment_payload = {
    "URL": "https://www.wixapis.com/comments/v1/comments/{comment.id}",
    "Descrição": "Atualiza um comentário"
}

api_details = {
    "List Messages": {
        "URL": "https://www.wixapis.com/inbox/v2/messages",
        "Método HTTP": "GET",
        
    },
    "Send Message": {
        "URL": "https://www.wixapis.com/inbox/v2/messages",
        "Método HTTP": "POST",
    }
}

apis1 = {
    "Email Subscriptions API": {
        "URL": "https://www.wixapis.com/email-marketing/v1/email-subscriptions",
        "Descrição": "API para criar, visualizar e atualizar assinaturas de e-mail para contatos em um site. Fornece informações sobre status de inscrição e entregabilidade."
    },
    "Query Email Subscriptions": {
        "URL": "https://www.wixapis.com/email-marketing/v1/email-subscriptions/query",
        "Descrição": "Operação da API de Email Subscriptions usada para recuperar informações sobre inscrições de e-mail com base em filtros específicos."
    },
    "Upsert Email Subscription": {
        "URL": "https://www.wixapis.com/email-marketing/v1/email-subscriptions",
        "Descrição": "Operação da API para atualizar ou criar uma assinatura de e-mail para um endereço de e-mail especificado."
    },
    "Bulk Upsert Email Subscription": {
        "URL": "https://www.wixapis.com/email-marketing/v1/email-subscriptions/bulk",
        "Descrição": "Operação da API para atualizar ou criar várias assinaturas de e-mail de uma só vez."
    },
    "Generate Unsubscribe Link": {
        "URL": "https://www.wixapis.com/email-marketing/v1/email-subscriptions/unsubscribe-link",
        "Descrição": "Operação da API para criar um link de cancelamento de inscrição a ser compartilhado com um destinatário."
    }
}

apis2 = {
    "Get Account Details": {
        "URL": "https://www.wixapis.com/email-marketing/v1/account-details",
        "Descrição": "Recupera detalhes da conta de marketing por e-mail, incluindo informações sobre status e pacote premium atual."
    },
    "Get Sender Details": {
        "URL": "https://www.wixapis.com/email-marketing/v1/sender-details",
        "Descrição": "Recupera detalhes do remetente, incluindo nome de exibição e endereço de e-mail do remetente."
    },
    "Update Sender Details": {
        "URL": "https://www.wixapis.com/email-marketing/v1/sender-details",
        "Descrição": "Atualiza os detalhes do remetente, permitindo a alteração do nome de exibição e do endereço de e-mail do remetente."
    },
    "Verify Email": {
        "URL": "https://www.wixapis.com/email-marketing/v1/sender-details/verify-email",
        "Descrição": "Verifica o endereço de e-mail do remetente usando um código de verificação enviado para o endereço de e-mail do usuário."
    },
    "Resolve Actual From Address": {
        "URL": "https://www.wixapis.com/email-marketing/v1/sender-details/actual-from-address",
        "Descrição": "Verifica se o endereço de e-mail do remetente será usado como endereço de origem ou se será substituído."
    }
}

apis = {
    "Get Campaign": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns/{campaignId}",
        "Descrição": "Recupera informações sobre uma campanha de e-mail."
    },
    "Delete Campaign": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns/{campaignId}",
        "Descrição": "Exclui permanentemente uma campanha."
    },
    "List Campaigns": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns",
        "Descrição": "Retorna uma lista de campanhas de e-mail."
    },
    "Publish Campaign": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns/{campaignId}/publish",
        "Descrição": "Publica/envia uma campanha especificada. Pode ser publicada como página de destino ou enviada por e-mail."
    },
    "Send Test": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns/{campaignId}/test",
        "Descrição": "Envia um e-mail de teste para fins de pré-visualização."
    },
    "Pause Scheduling": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns/{campaignId}/pause-scheduling",
        "Descrição": "Pausa o agendamento de uma campanha programada."
    },
    "Reuse Campaign": {
        "URL": "https://www.wixapis.com/email-marketing/v1/campaigns/{campaignId}/reuse",
        "Descrição": "Cria uma cópia (rascunho) de uma campanha existente."
    },
    "Email Activity Updated": {
        "URL": "Webhook - Não possui uma URL fixa",
        "Descrição": "Webhook acionado quando há uma nova atividade do destinatário em uma campanha de e-mail."
    }
}

api_dictionary = {
    "List Marketing Tags": {
        "URL": "https://www.wixapis.com/marketing/v1/tags",
        "Descrição": "Recupera as tags de marketing com base em filtros fornecidos.",
        "Informações Relevantes": "Método HTTP: GET\nPermissão Necessária: READ MARKETING TAGS"
    },
    "Upsert Marketing Tag": {
        "URL": "https://www.wixapis.com/marketing/v1/tags",
        "Descrição": "Cria ou atualiza uma tag de marketing.",
        "Informações Relevantes": "Método HTTP: POST\nPermissão Necessária: MANAGE MARKETING TAGS"
    },
    "Delete Marketing Tag": {
        "URL": "https://www.wixapis.com/marketing/v1/tags",
        "Descrição": "Exclui uma tag de marketing (Método obsoleto, substituído por DeleteMarketingTagV2).",
        "Informações Relevantes": "Método HTTP: DELETE\nPermissão Necessária: MANAGE MARKETING TAGS"
    },
    "Marketing Tag Created": {
        "Descrição": "Disparado quando uma tag de marketing é criada.",
        "Informações Relevantes": "Permissões Necessárias: MARKETING_TAGS.READ"
    },
    "Marketing Tag Updated": {
        "Descrição": "Disparado quando uma tag de marketing é atualizada.",
        "Informações Relevantes": "Permissões Necessárias: MARKETING_TAGS.READ"
    },
    "Marketing Tag Deleted": {
        "Descrição": "Disparado quando uma tag de marketing é excluída.",
        "Informações Relevantes": "Permissões Necessárias: MARKETING_TAGS.READ"
    }
}

# API de SEO Keyword Suggestions
seo_keyword_suggestions_api = {
    "URL": "https://www.provider.example.com/v1/list-suggested-keywords",
    "Descrição": "Solicita sugestões de palavras-chave para uma frase específica para análise de força de SEO.",
    "Campos de Solicitação":
    {
        "keyword": "string - Palavra-chave para análise de força de SEO.",
        "countryCode": "string - Código do país específico para análise. Formato ISO-3166 alpha-2."
    },
    "Campos de Resposta":
    {
        "data": "array - Análise da palavra-chave e lista de palavras-chave similares.",
        "quota": "object - Detalhes da cota do plano."
    }
}

get_quota_api = {
    "URL": "https://www.provider.example.com/v1/get-quota",
    "Descrição": "Obtém informações sobre a cota restante no plano atual.",
    "Campos de Solicitação": {},
    "Campos de Resposta":
    {
        "quota": "object - Informações sobre o crédito restante no plano."
    }
}

# API Ads.txt
get_ads_txt_api = {
    "URL": "https://www.wix.com/_api/promote-seo-txt-file-server/v2/ads",
    "Descrição": "Recupera o arquivo Ads.txt.",
    "Campos de Solicitação":
    {
        "subdomain": "string - Subdomínio do Ads.txt (por exemplo, www, es, fr). O padrão é www."
    },
    "Campos de Resposta":
    {
        "adsTxt": "object - Objeto Ads.txt."
    }
}

update_ads_txt_api = {
    "URL": "https://www.wixapis.com/promote-seo-txt-file-server/v2/ads",
    "Descrição": "Atualiza o arquivo Ads.txt. Um objeto content vazio cria um arquivo Ads.txt vazio. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content.",
    "Campos de Solicitação":
    {
        "adsTxt": "object - O objeto content substituirá o arquivo Ads.txt existente. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content."
    },
    "Campos de Resposta":
    {
        "adsTxt": "object - Objeto Ads.txt atualizado."
    }
}

append_ads_txt_api = {
    "URL": "https://www.wixapis.com/promote-seo-txt-file-server/v2/ads",
    "Descrição": "Anexa o objeto content enviado ao Ads.txt. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content.",
    "Campos de Solicitação":
    {
        "adsTxt": "object - O objeto content será anexado ao arquivo Ads.txt existente. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content."
    },
    "Campos de Resposta":
    {
        "adsTxt": "object - Arquivo Ads.txt anexado."
    }
}

# API de SEO Keyword Suggestions
seo_keyword_suggestions_api = {
    "URL": "https://www.provider.example.com/v1/list-suggested-keywords",
    "Descrição": "Solicita sugestões de palavras-chave para uma frase específica para análise de força de SEO.",
    "Campos de Solicitação": {
        "keyword": "string - Palavra-chave para análise de força de SEO.",
        "countryCode": "string - Código do país específico para análise. Formato ISO-3166 alpha-2."
    }
}

get_quota_api = {
    "URL": "https://www.provider.example.com/v1/get-quota",
    "Descrição": "Obtém informações sobre a cota restante no plano atual.",
    "Campos de Solicitação": {}
}

# API Ads.txt
get_ads_txt_api = {
    "URL": "https://www.wix.com/_api/promote-seo-txt-file-server/v2/ads",
    "Descrição": "Recupera o arquivo Ads.txt.",
    "Campos de Solicitação": {
        "subdomain": "string - Subdomínio do Ads.txt (por exemplo, www, es, fr). O padrão é www."
    }
}

update_ads_txt_api = {
    "URL": "https://www.wixapis.com/promote-seo-txt-file-server/v2/ads",
    "Descrição": "Atualiza o arquivo Ads.txt. Um objeto content vazio cria um arquivo Ads.txt vazio. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content.",
    "Campos de Solicitação": {
        "adsTxt": "object - O objeto content substituirá o arquivo Ads.txt existente. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content."
    }
}

append_ads_txt_api = {
    "URL": "https://www.wixapis.com/promote-seo-txt-file-server/v2/ads",
    "Descrição": "Anexa o objeto content enviado ao Ads.txt. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content.",
    "Campos de Solicitação": {
        "adsTxt": "object - O objeto content será anexado ao arquivo Ads.txt existente. Para redefinir o Ads.txt para o padrão do Wix, envie default: true sem um objeto content."
    }
}

# API List Folders
list_folders_api = {
    "URL": "https://www.wixapis.com/site-media/v1/folders",
    "Descrição": "Retrieves a list of folders in the Media Manager.",
    "Campos de Solicitação": {
        "parentFolderId": "string - ID of the folder's parent folder.",
        "sort.fieldName": "string - Name of the field to sort by.",
        "sort.order": "string - Sort order (ASC or DESC).",
        "paging.limit": "integer - Number of items to load.",
        "paging.cursor": "string - Pointer to the next or previous page in the list of results."
    }
}

# API Create Folder
create_folder_api = {
    "URL": "https://www.wixapis.com/site-media/v1/folders",
    "Descrição": "Creates a new folder in the Media Manager.",
    "Campos de Solicitação": {
        "displayName": "string - Folder name that appears in the Media Manager.",
        "parentFolderId": "string - ID of the folder's parent folder."
    }
}

# API Get Folder
get_folder_api = {
    "URL": "https://www.wixapis.com/site-media/v1/folders/{folderId}",
    "Descrição": "Gets information from a specific folder in the Media Manager.",
    "Campos de Solicitação": {
        "folderId": "string - Folder ID."
    }
}

# API Search Folders
search_folders_api = {
    "URL": "https://www.wixapis.com/site-media/v1/folders/search",
    "Descrição": "Searches the Media Manager and returns a list of folders that match the terms specified in the parameters.",
    "Campos de Solicitação": {
        "rootFolder": "string - A root folder in the media manager to search in.",
        "sort": "object - Field name and order to sort by.",
        "paging": "object - Cursor and paging information.",
        "search": "string - Term to search for."
    }
}

# API Update Folder
update_folder_api = {
    "URL": "https://www.wixapis.com/site-media/v1/folders/{folder.id}",
    "Descrição": "Updates a folder.",
    "Campos de Solicitação": {
        "folder.id": "string - Folder ID.",
        "folder": "object - The folder to update."
    }
}

# API Generate Folder Download Url
generate_folder_download_url_api = {
    "URL": "https://www.wixapis.com/site-media/v1/folders/{folderId}/generate-download-url",
    "Descrição": "Generates a URL for downloading a compressed file containing a specific folder in the Media Manager.",
    "Campos de Solicitação": {
        "folderId": "string - Folder ID."
    }
}

# API Bulk Delete Folders
bulk_delete_folders_api = {
    "URL": "https://www.wixapis.com/site-media/v1/bulk/folders/delete",
    "Descrição": "Temporarily deletes the specified folders from the Media Manager.",
    "Campos de Solicitação": {
        "folderIds": "Array of strings - IDs of the folders to move to the Media Manager's trash bin.",
        "permanent": "boolean - Whether the specified folders are permanently deleted."
    }
}

# API Bulk Restore Folders From Trash Bin
bulk_restore_folders_api = {
    "URL": "https://www.wixapis.com/site-media/v1/bulk/trash-bin/folders/restore",
    "Descrição": "Restores the specified folders from the Media Manager's trash bin.",
    "Campos de Solicitação": {
        "folderIds": "Array of strings - IDs of the folders to restore from the Media Manager's trash bin."
    }
}

# API List Deleted Folders
list_deleted_folders_api = {
    "URL": "https://www.wixapis.com/site-media/v1/trash-bin/folders",
    "Descrição": "Retrieves a list of folders in the Media Manager's trash bin.",
    "Campos de Solicitação": {
        "parentFolderId": "string - ID of the folder's parent folder.",
        "sort.fieldName": "string - Name of the field to sort by.",
        "sort.order": "string - Sort order (ASC or DESC).",
        "paging.limit": "integer - Number of items to load.",
        "paging.cursor": "string - Pointer to the next or previous page in the list of results."
    }
}

# Dados para inserir um item
inserir_item = {
    "URL": "https://www.wixapis.com/wix-data/v2/items",
    "descrição": "Inserir um item em uma coleção",
    "parâmetros_corporais": {
        "dataCollectionId": "cidades",
        "Item de dados": {
            "dados": {
                "estado": "Califórnia",
                "ano": 2022,
                "cidade": "Los Angeles",
                "população": 3800000
            }
        }
    }
}

# Dados para atualizar um item
atualizar_item = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/5331fc15-9441-4fd4-bc7b-7f6870c69228",
    "descrição": "Atualizar um item em uma coleção",
    "parâmetros_corporais": {
        "dataCollectionId": "cidades",
        "Item de dados": {
            "dados": {
                "estado": "Califórnia",
                "ano": 2022,
                "cidade": "Los Angeles",
                "população": 3800000
            }
        }
    }
}

# Dados para obter um item
obter_item = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/5331fc15-9441-4fd4-bc7b-7f6870c69228?dataCollectionId=cities",
    "descrição": "Obter um item de uma coleção"
}

# Dados para excluir um item
excluir_item = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/5331fc15-9441-4fd4-bc7b-7f6870c69228?dataCollectionId=cities",
    "descrição": "Remover um item de uma coleção"
}

# Dados para consultar itens
consultar_itens = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/query",
    "descrição": "Consultar itens em uma coleção",
    "parâmetros_corporais": {
        "dataCollectionId": "cidades",
        "consulta": {
            "filtro": {
                "estado": "Califórnia"
            },
            "paginação": {
                "limite": 2
            }
        }
    }
}

# Dados para contar itens
contar_itens = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/count",
    "descrição": "Contar itens em uma coleção",
    "parâmetros_corporais": {
        "dataCollectionId": "cidades",
        "filtro": {
            "estado": "Califórnia"
        }
    }
}

# Dados para truncar itens
truncar_itens = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/truncate",
    "descrição": "Remover todos os itens de uma coleção",
    "parâmetros_corporais": {
        "dataCollectionId": "cidades"
    }
}

# Dados para itens agregados
itens_agregados = {
    "URL": "https://www.wixapis.com/wix-data/v2/items/agregado",
    "descrição": "Realizar uma agregação em uma coleção",
    "parâmetros_corporais": {
        "dataCollectionId": "cidades",
        "filtro inicial": {
            "ano": 2022
        },
        "agregação": {
            "groupingFields": ["estado"],
            "operações": [
                {
                    "resultFieldName": "população_total",
                    "soma": {
                        "itemFieldName": "população"
                    }
                }
            ]
        }
    }
}

# Dicionário de informações para as ações da API
api_info = {
    "Contar itens de dados": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/items/count",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "filtro": "estrutura (opcional)",
            "leitura consistente": "boolean (opcional)"
        },
        "objeto_de_resposta": {
            "contagem total": "número"
        }
    },
    "Consultar valores distintos": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/items/query-distinct-values",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "campoNome": "string (obrigatório)",
            "filtro": "estrutura (opcional)",
            "ordem": "string (opcional)",
            "retornarTotalCount": "boolean (opcional)",
            "leitura consistente": "boolean (opcional)",
            "paginação": "objeto (opcional)",
            "cursorPaging": "objeto (opcional)"
        },
        "objeto_de_resposta": {
            "valores distintos": "lista de strings",
            "paginaçãoMetadados": {
                "contagem": "número",
                "tooManyToCount": "boolean",
                "hasNext": "boolean"
            }
        }
    },
    "Inserir itens de dados em massa": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/bulk/items/insert",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "itens de dados": "matriz de objetos DataItem (obrigatório)",
            "retornarEntidade": "boolean (opcional)"
        },
        "objeto_de_resposta": {
            "resultados": "matriz de objetos BulkDataItemResult",
            "bulkActionMetadata": {
                "totalSucessos": "número",
                "total de falhas": "número"
            }
        }
    },
    "Atualizar itens de dados em massa": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/bulk/items/update",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "itens de dados": "matriz de objetos DataItem (obrigatório)",
            "retornarEntidade": "boolean (opcional)"
        },
        "objeto_de_resposta": {
            "resultados": "matriz de objetos BulkDataItemResult",
            "bulkActionMetadata": {
                "totalSucessos": "número",
                "total de falhas": "número"
            }
        }
    },
    "Salvar itens de dados em massa": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/bulk/items/save",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "itens de dados": "matriz de objetos DataItem (obrigatório)",
            "retornarEntidade": "boolean (opcional)"
        },
        "objeto_de_resposta": {
            "resultados": "matriz de objetos BulkDataItemResult",
            "bulkActionMetadata": {
                "total de sucessos": "número",
                "totalFalhas": "número"
            }
        }
    },
    "Remover itens de dados em massa": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/bulk/items/remove",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "dataItemIds": "matriz de strings (obrigatório)"
        },
        "objeto_de_resposta": {
            "resultados": "matriz de objetos BulkDataItemResult",
            "bulkActionMetadata": {
                "totalSucessos": "número",
                "total de falhas": "número"
            }
        }
    },
    "Consultar itens de dados referenciados": {
        "endpoint": "https://www.wixapis.com/wix-data/v2/items/query-referenced",
        "método": "POST",
        "parâmetros_corporais": {
            "dataCollectionId": "string (obrigatório)",
            "referindoItemId": "string (obrigatório)",
            "referindoItemFieldName": "string (obrigatório)",
            "ordem": "string (opcional)",
            "retornarTotalCount": "boolean (opcional)",
            "leitura consistente": "boolean (opcional)",
            "paginação": "objeto (opcional)",
            "cursorPaging": "objeto (opcional)"
        },
        "objeto_de_resposta": {
            "resultados": "matriz de objetos ReferencedResult",
            "paginaçãoMetadados": {
                "contagem": "número"
            }
        }
    }
}

# Verificar se um campo em um item de referência contém uma referência a um item especificado
is_referenced = {
    "method": "POST",
    "endpoint": "https://www.wixapis.com/wix-data/v2/items/is-referenced",
    "request_body": {
        "dataCollectionId": "string",
        "referencingItemFieldName": "string",
        "referencingItemId": "string",
        "referencedItemId": "string",
        "readConsistent": False  # Padrão é False
    }
}

# Inserir referência de item de dados
insert_reference = {
    "method": "POST",
    "endpoint": "https://www.wixapis.com/wix-data/v2/items/insert-reference",
    "request_body": {
        "dataCollectionId": "string",
        "dataItemReference": {
            "referringItemFieldName": "string",
            "referringItemId": "string",
            "referencedItemId": "string"
        }
    }
}

# Remover referência de item de dados
remove_reference = {
    "method": "POST",
    "endpoint": "https://www.wixapis.com/wix-data/v2/items/remove-reference",
    "request_body": {
        "dataCollectionId": "string",
        "dataItemReference": {
            "referringItemFieldName": "string",
            "referringItemId": "string",
            "referencedItemId": "string"
        }
    }
}

# Referências de itens de dados de inserção em massa
bulk_insert_references = {
    "method": "POST",
    "endpoint": "https://www.wixapis.com/wix-data/v2/bulk/items/insert-references",
    "request_body": {
        "dataCollectionId": "string",
        "dataItemReferences": [
            {
                "referringItemFieldName": "string",
                "referringItemId": "string",
                "referencedItemId": "string"
            }
        ],
        "returnEntity": False  # Padrão é False
    }
}

# Referências de itens de dados para remoção em massa
bulk_remove_references = {
    "method": "POST",
    "endpoint": "https://www.wixapis.com/wix-data/v2/bulk/items/remove-references",
    "request_body": {
        "dataCollectionId": "string",
        "dataItemReferences": [
            {
                "referringItemFieldName": "string",
                "referringItemId": "string",
                "referencedItemId": "string"
            }
        ]
    }
}

# Substituir referências de itens de dados
replace_references = {
    "method": "POST",
    "endpoint": "https://www.wixapis.com/wix-data/v2/items/replace-references",
    "request_body": {
        "dataCollectionId": "string",
        "referringItemFieldName": "string",
        "referringItemId": "string",
        "newReferencedItemIds": ["string"]
    }
}

api_info = {
    "URL": "https://example.com/api",
    "Descrição": "Esta é uma API de exemplo usada para ilustrar como acessar dados.",
    "Outro Dado Importante": "Chave de Autenticação: abc123",
}

apis = [
    {
        "url": "https://www.wixapis.com/wix-data/v2/collections/{dataCollectionId=**}",
        "descrição": "Obtenha coleta de dados",
        "importante_para_chamar_api": "Cabeçalho de autorização necessário - passe o Sintaxe PEGAR"
    },
    {
        "url": "https://www.wixapis.com/wix-data/v2/collections/{dataCollectionId=**}",
        "descrição": "Exclui uma coleta de dados",
        "importante_para_chamar_api": "Cabeçalho de autorização necessário - passe o Sintaxe EXCLUIR"
    },
    {
        "url": "https://www.wixapis.com/wix-data/v2/data-collections",
        "descrição": "Lista todas as coleções de dados disponíveis",
        "importante_para_chamar_api": "Cabeçalho de autorização necessário - passe o Sintaxe PEGAR"
    },
    {
        "url": "https://www.wixapis.com/wix-data/v2/collections/dataCollectionId={dataCollectionId=**}",
        "descrição": "Recupera uma coleção de dados por ID",
        "importante_para_chamar_api": "Cabeçalho de autorização necessário - passe o Sintaxe PEGAR"
    },
    {
        "url": "https://www.wixapis.com/wix-data/v2/collections/{dataCollectionId=**}",
        "descrição": "Exclui uma coleta de dados",
        "importante_para_chamar_api": "Cabeçalho de autorização necessário - passe o Sintaxe EXCLUIR"
    }
]

apis = [
    {
        "url": "https://www.wixapis.com/wix-data/v2/indexes",
        "descrição": "Lista todos os índices definidos para uma coleção de dados.",
        "informações adicionais": {
            "Parâmetros de consulta": {
                "dataCollectionId": "ID da coleção de dados para listar índices.",
                "paginação.limit": "Número de itens a serem carregados.",
                "paginação.offset": "Número de itens a serem ignorados na ordem de classificação atual."
            }
        }
    },
    {
        "url": "https://www.wixapis.com/wix-data/v2/indexes",
        "descrição": "Cria um índice para uma coleção de dados.",
        "informações adicionais": {
            "Parâmetros Corporais": {
                "índice": "Detalhes do índice a ser criado.",
                "dataCollectionId": "ID da coleção de dados para a qual gerar o índice."
            }
        }
    },
    {
        "url": "https://www.wixapis.com/wix-data/v2/indexes",
        "descrição": "Remove um índice de uma coleção de dados.",
        "informações adicionais": {
            "Parâmetros de consulta": {
                "indexName": "Nome do índice a ser descartado.",
                "dataCollectionId": "ID da coleção de dados para a qual o índice a ser eliminado é definido."
            }
        }
    }
]

apis = [
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections/{nome}",
        "Descrição": "Recupera uma conexão de banco de dados externa por nome.",
        "Permissão Necessária": "LER CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "GET",
        "Exemplo de Corpo da Solicitação": None,
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections/{nome}",
        "Descrição": "Exclui uma conexão de banco de dados externo.",
        "Permissão Necessária": "GRAVAR CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "DELETE",
        "Exemplo de Corpo da Solicitação": None,
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections",
        "Descrição": "Recupera uma lista de todas as coleções de bancos de dados externos associadas ao site ou projeto.",
        "Permissão Necessária": "LER CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "GET",
        "Exemplo de Corpo da Solicitação": None,
    },
    {
        
   
"URL": "https://www.wixapis.com/wix-data/v1/external-database-connections",
        "Descrição": "Cria uma nova conexão de banco de dados externo.",
        "Permissão Necessária": "GRAVAR CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "POST",
        "Exemplo de Corpo da Solicitação": {
            "externalDatabaseConnection": {
                "nome": "MeuBancoDeDadosExterno",
                "endpoint": "https://example.com/my-external-database",
                "configuração": {
                    "secretKey": "74dbd6d6-ec5b-4668-8229-c77379bc6431"
                }
            },
        },
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections/{externalDatabaseConnection.name}",
        "Descrição": "Atualiza uma conexão de banco de dados externo.",
        "Permissão Necessária": "GRAVAR CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "PUT",
        "Exemplo de Corpo da Solicitação": {
            "externalDatabaseConnection": {
                "endpoint": "https://example.com/my-external-database",
                "configuração": {
                    "secretKey": "74dbd6d6-ec5b-4668-8229-c77379bc6431"
                }
            },
        },
    },
]

apis = [
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections/{nome}",
        "Descrição": "Recupera uma conexão de banco de dados externa por nome.",
        "Permissão Necessária": "LER CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "GET",
        "Exemplo de Corpo da Solicitação": None,
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections/{nome}",
        "Descrição": "Exclui uma conexão de banco de dados externo.",
        "Permissão Necessária": "GRAVAR CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "DELETE",
        "Exemplo de Corpo da Solicitação": None,
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections",
        "Descrição": "Recupera uma lista de todas as coleções de bancos de dados externos associadas ao site ou projeto.",
        "Permissão Necessária": "LER CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "GET",
        "Exemplo de Corpo da Solicitação": None,
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections",
        "Descrição": "Cria uma nova conexão de banco de dados externo.",
        "Permissão Necessária": "GRAVAR CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "POST",
        "Exemplo de Corpo da Solicitação": {
            "externalDatabaseConnection": {
                "nome": "MeuBancoDeDadosExterno",
                "endpoint": "https://example.com/my-external-database",
                "configuração": {
                    "secretKey": "74dbd6d6-ec5b-4668-8229-c77379bc6431"
                }
            },
        },
    },
    {
        "URL": "https://www.wixapis.com/wix-data/v1/external-database-connections/{externalDatabaseConnection.name}",
        "Descrição": "Atualiza uma conexão de banco de dados externo.",
        "Permissão Necessária": "GRAVAR CONEXÕES DE BANCO DE DADOS EXTERNAS",
        "Método": "PUT",
        "Exemplo de Corpo da Solicitação": {
            "externalDatabaseConnection": {
                "endpoint": "https://example.com/my-external-database",
                "configuração": {
                    "secretKey": "74dbd6d6-ec5b-4668-8229-c77379bc6431"
                }
            },
        },
    },
]

apis = {
    "Create Checkout Developer Preview": {
        "URL": "POST https://www.wixapis.com/ecom/v1/checkouts",
        "Descrição": "Cria uma finalização de compra.",
        "Campos Relevantes": {
            "Body Params": {
                "checkoutInfo": "Informações de checkout.",
                "cupomCode": "Código do cupom.",
                "lineItems": "Itens de linha a serem adicionados à finalização da compra.",
                "channelType": "Canal de vendas que enviou o pedido.",
                "giftCardCode": "Código do vale-presente.",
                "overrideCheckoutUrl": "Permite redirecionar os clientes para uma página de checkout personalizada."
            }
        }
    },
    "Get Checkout Developer Preview": {
        "URL": "GET https://www.wixapis.com/ecom/v1/checkouts/{id}",
        "Descrição": "Recupera um checkout.",
        "Campos Relevantes": {
            "Path Params": {
                "id": "Checkout ID."
            }
        }
    },
    "Get Checkout URL Developer Preview": {
        "URL": "GET https://www.wixapis.com/ecom/v1/checkouts/{id}/checkout-url",
        "Descrição": "Recupera o URL da página de checkout de um checkout especificado.",
        "Campos Relevantes": {
            "Path Params": {
                "id": "Checkout ID."
            }
        }
    },
    "Update Checkout Developer Preview": {
        "URL": "PATCH https://www.wixapis.com/ecom/v1/checkouts/{checkout.id}",
        "Descrição": "Atualiza um checkout.",
        "Campos Relevantes": {
            "Path Params": {
                "checkout.id": "ID de checkout."
            },
            "Body Params": {
                "checkoutInfo": "Informações de checkout.",
                "cupomCode": "Código do cupom.",
                "giftCardCode": "Código do vale-presente.",
                "overrideCheckoutUrl": "Permite redirecionar os clientes para uma página de checkout personalizada."
            }
        }
    }
}

order_api = {
    "Create and manage eCommerce orders": {
        "URL": "https://api.example.com/create_order",
        "Descrição": "Crie e gerencie pedidos de comércio eletrônico",
        "Campos necessários": {
            "id": "string (GUID)",
            "number": "number",
            "createdDate": "string (date-time)",
            "updatedDate": "string (date-time)",
            "lineItems": "array of OrderLineItem",
            "buyerInfo": "object (Buyer information)",
            "paymentStatus": "string (UNSPECIFIED, NOT_PAID, PAID, PARTIALLY_REFUNDED, FULLY_REFUNDED, PENDING, PARTIALLY_PAID)",
            "fulfillmentStatus": "string (NOT_FULFILLED, FULFILLED, PARTIALLY_FULFILLED)",
            "buyerLanguage": "string",
            "weightUnit": "string (UNSPECIFIED_WEIGHT_UNIT, KG, LB)",
            "currency": "string (CURRENCY)",
            "taxIncludedInPrices": "boolean",
            "siteLanguage": "string",
            "priceSummary": "object (Order price summary)",
            "billingInfo": "object (Billing address and contact details)",
            "shippingInfo": "object (Shipping info and selected shipping option details)",
            "buyerNote": "string (max length 1000)",
            "status": "string (INITIALIZED, APPROVED, CANCELED)",
            "archived": "boolean",
            "taxSummary": "object (Tax summary)",
            "appliedDiscounts": "array of AppliedDiscount",
            "activities": "array of Activity",
            "attributionSource": "string (UNSPECIFIED, FACEBOOK_ADS)",
            "createdBy": "object (ID of the order's initiator)",
            "channelInfo": "object (Information about the sales channel that submitted this order)",
            "seenByAHuman": "boolean",
            "checkoutId": "string (GUID)",
            "customFields": "array of CustomField",
            "additionalFees": "array of AdditionalFee",
            "purchaseFlowId": "string (GUID)",
        }
    }
}

api_get_order = {
    "URL": "https://www.wixapis.com/ecom/v1/orders/{id}",
    "Descrição": "Recupera um pedido com o ID fornecido.",
    "Dados Necessários": {
        "id": "string (REQUIRED) - ID do pedido a ser recuperado.",
    }
}

api_data = {
    "URL": "https://www.wixapis.com/ecom/v1/orders/{id}/cancel",
    "Descrição": "Cancel Order",
    "Método": "POST",
    "Cabeçalhos": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "Parâmetros de Caminho (Path Params)": {
        "id": {
            "Tipo": "string",
            "Obrigatório": "REQUIRED",
            "Descrição": "Order ID"
        }
    },
    "Parâmetros do Corpo (Body Params)": {
        "sendOrderCanceledEmail": {
            "Tipo": "boolean",
            "Descrição": "Whether to send an order canceled email to the buyer."
        },
        "customMessage": {
            "Tipo": "string",
            "Mínimo de caracteres": 1,
            "Máximo de caracteres": 1000,
            "Descrição": "Custom note to be added to the email (optional)."
        },
        "restockAllItems": {
            "Tipo": "boolean",
            "Descrição": "Whether to restock all items in the order. This will only apply to products in the Wix Stores inventory."
        }
    },
    "Objeto de Resposta (Response Object)": {
        "order": {
            "Tipo": "object",
            "Descrição": "Canceled order."
        }
    }
}

# Exemplo de chamada da API
api_call = {
    "URL": "https://www.wixapis.com/ecom/v1/orders/7001d34b-11a6-4a34-8746-dc8ababeca42/cancel",
    "Método": "POST",
    "Cabeçalhos": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
api = {
    "URL": "https://www.wixapis.com/ecom/v1/fulfillments/orders/265c7d98-a7c3-48c4-89cd-bbdc00921eab",
    "DESCRIÇÃO": "Listar atendimentos para pedido unico",
    "DADOS_NECESSÁRIOS": {
        "Método": "GET",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
        },
    }
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/fulfillments/list-by-ids",
    "DESCRIÇÃO": "Listar atendimentos para varios pedidos",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
        },
    }
}
api = {
    "URL": "https://www.wixapis.com/ecom/v1/fulfillments/orders/58c9a790-27b7-463f-a865-c7cb494f7c29/create-fulfillment",
    "DESCRIÇÃO": "Create Fulfillment",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            --data-binary: {
                    "fulfillment": {
                    "lineItems": [
                        {
                        "id": "00000000-0000-0000-0000-000000000001",
                        "quantity": 1
                        }
                    ],
                    "trackingInfo": {
                        "trackingNumber": "12345",
                        "shippingProvider": "fedex"
                    }
                    }
                }
                
    }
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/fulfillments/1d93cd8e-0de5-469b-b802-88bcd76cb222/orders/eb4b91d3-51f3-494d-94df-479ff2c6eb08",
    "DESCRIÇÃO": "uPDATE fULFILLMENT",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
                        --data-binary '{
                "fulfillment": {
                "lineItems": [
                    {
                    "id": "00000000-0000-0000-0000-000000000001",
                    "quantity": 1
                    }
                ],
                "trackingInfo": {
                    "trackingNumber": "12345",
                    "shippingProvider": "fedex"
                }
                }
  }'
        },
    }
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/fulfillments/0d824fc7-2621-4e97-a5c8-489ec1b43377/orders/4c51c360-399f-4276-96b1-d85f0963dbfd",
    "DESCRIÇÃO": "Delete fulfillment",
    "DADOS_NECESSÁRIOS": {
        "Método": "DELETE",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
                
    }
}
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/fulfillments/orders/bulk/create-fulfillments",
    "DESCRIÇÃO": "bulk create fulfillment",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
                
    }
}
}
api = {
    "URL": "https://www.wixapis.com/ecom/v1/payments/orders/8d009fbe-6600-4c7a-ad23-37e9f0477947",
    "DESCRIÇÃO": "list transactions for single order",
    "DADOS_NECESSÁRIOS": {
        "Método": "GET",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
                
    }
}
}
api = {
    "URL": "https://www.wixapis.com/ecom/v1/payments/list-by-ids",
    "DESCRIÇÃO": "list transactions for multiple orders",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            --data-binary '{
    "orderIds": [
      "4bab5870-7943-4a9e-8d4e-96719b3e4f38",
      "6ae38b2e-455b-4e20-b418-01fca82edaa8"
    ]
  }'
                
    }
}
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/abandoned-checkout/b4ebb0b8-4482-4693-ae09-7b47e977484c",
    "DESCRIÇÃO": "get abandoned checkout",
    "DADOS_NECESSÁRIOS": {
        "Método": "GET",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            
  }
                
    }
}
api = {
    "URL": "https://www.wixapis.com/ecom/v1/abandoned-checkout/query",
    "DESCRIÇÃO": "query abandoned checkout",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            """--data-binary '{
    "query": {
      "sort": [
        {
          "fieldName": "createdDate",
          "order": "DESC"
        }
      ],
      "filter": {
        "contactDetails.firstName": "John"
      },
      "paging": {
        "limit": 20,
        "offset": 0
      }
    }
  }'"""
            
  }
                
    }
}
api = {
    "URL": "https://www.wixapis.com/ecom/v1/discount-rules/create",
    "DESCRIÇÃO": "create discount rule",
    "DADOS_NECESSÁRIOS": {
        "Método": "POST",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            """ --data-binary '{
    "discountRule": {
      "active": true,
      "name": "15% on all products when buying more than 5 items",
      "trigger": {
        "itemQuantityRange": {
          "scopes": [
            {
              "id": "all_215238eb-22a5-4c36-9e7b-e7c08025e04e",
              "type": "CATALOG_ITEM",
              "catalogItemFilter": {
                "catalogAppId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
                "catalogItemIds": []
              }
            }
          ],
          "from": 5,
          "to": null
        },
        "triggerType": "ITEM_QUANTITY_RANGE"
      },
      "discounts": {
        "values": [
          {
            "targetType": "SPECIFIC_ITEMS",
            "specificItemsInfo": {
              "scopes": [
                {
                  "id": "all_215238eb-22a5-4c36-9e7b-e7c08025e04e",
                  "type": "CATALOG_ITEM",
                  "catalogItemFilter": {
                    "catalogItemIds": [],
                    "catalogAppId": "215238eb-22a5-4c36-9e7b-e7c08025e04e"
                  }
                }
              ]
            },
            "discountType": "PERCENTAGE",
            "percentage": 15
          }
        ]
      }
    }
  }'"""
            
  }
                
    }
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/discount-rules/15bac455-10d0-4478-8358-e06f697f6180",
    "DESCRIÇÃO": "get discount rule",
    "DADOS_NECESSÁRIOS": {
        "Método": "GET",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            
  }
                
    }
}

api = {
    "URL": "https://www.wixapis.com/ecom/v1/discount-rules/delete/c31f8d152077bab24065f01c0e3152b746c54ce0",
    "DESCRIÇÃO": "delete dicount rule",
    "DADOS_NECESSÁRIOS": {
        "Método": "DELETE",
        "Cabeçalhos": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_API_KEY>"
            
  }
                
    }
}

# Comando para atualizar uma regra de desconto
update_discount_rule = {
    "description": "Atualiza uma regra de desconto existente",
    "method": "PATCH",
    "url": "https://www.wixapis.com/ecom/v1/discount-rules/update/35120105-1327-4624-8f7f-2720dcbab4d6",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "discountRule": {
            "id": "35120105-1327-4624-8f7f-2720dcbab4d6",
            "name": "discount new name",
            "revision": "5"
        }
    }
}

# Comando para consultar regras de desconto
query_discount_rules = {
    "description": "Consulta regras de desconto com filtro de ativação e classificação",
    "method": "POST",
    "url": "https://www.wixapis.com/ecom/v1/discount-rules/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "sort": [
                {
                    "fieldName": "name",
                    "order": "ASC"
                }
            ],
            "filter": {
                "active": True,
                "activeTimeInfo.start": {
                    "$gt": "2021-08-01T00:00:00Z"
                }
            },
            "cursorPaging": {
                "limit": 2
            }
        }
    }
}

# Comando para calcular taxas adicionais
calculate_additional_fees = {
    "description": "Calcula taxas adicionais com base nas informações do pedido",
    "method": "POST",
    "url": "https://provider.example.com/v1/calculate-additional-fees",
    "headers": {
        "user-agent": "Wix",
        "accept-encoding": "gzip, deflate",
        "content-type": "text/plain; charset=utf-8"
    },
    "data": {
        "data": {
            "request": {
                "lineItems": [
                    {
                        "physicalProperties": {
                            "sku": "0043",
                            "shippable": True
                        },
                        "quantity": 1,
                        "price": "16.00",
                        "_id": "00000000-0000-0000-0000-000000000001",
                        "productName": "Set of bowls",
                        "catalogReference": {
                            "catalogItemId": "27ef9a44-74a6-a0dd-3e40-50c7d196f890",
                            "appId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
                            "options": {
                                "options": {},
                                "variantId": "00000000-0000-0000-0000-000000000000"
                            }
                        }
                    }
                ],
                "shippingAddress": {
                    "addressLine1": "123 Turnover Way",
                    "city": "Boston",
                    "subdivision": "US-MA",
                    "country": "US",
                    "postalCode": "02108"
                },
                "buyerDetails": {
                    "contactDetails": {
                        "phone": "6175551905",
                        "email": "bowlbuyer@example.com"
                    }
                },
                "shippingInfo": {
                    "selectedCarrierServiceOption": {
                        "code": "5336e031-4421-fdb5-08fa-45b777dbc488",
                        "title": "Standard shipping",
                        "logistics": {
                            "deliveryTime": ""
                        },
                        "cost": {
                            "price": "3"
                        }
                    }
                },
                "ecomId": "41abc90a-c82d-4e33-bbea-7e3494bc6522"
            }
        }
    }
}

get_shipping_rates = {
    "description": "Obtém taxas de envio com base nas informações do pedido",
    "method": "POST",
    "url": "https://provider.example.com/v1/getRates",
    "headers": {
        "user-agent": "Wix",
        "accept-encoding": "gzip, deflate",
        "content-type": "text/plain; charset=utf-8"
    },
    "data": {
        "data": {
            "request": {
                "lineItems": [
                    {
                        "physicalProperties": {
                            "weight": 0.4,
                            "sku": "",
                            "shippable": True
                        },
                        "name": "coffee mug",
                        "quantity": 1,
                        "price": "100.00",
                        "catalogReference": {
                            "catalogItemId": "50b7223c-80e6-3539-325e-4ecfe99770dc",
                            "appId": "1380b703-ce81-ff05-f115-39571d94dfcd",
                            "options": {
                                "options": {
                                    "Size": "256",
                                    "Color": "blue"
                                },
                                "variantId": "9d1bc95e-d6ed-4546-b89b-c61e334e2d5e"
                            }
                        }
                    }
                ],
                "buyerContactDetails": {
                    "phone": "123456789",
                    "email": "janedoe@gmail.com"
                },
                "taxIncludedInPrices": False,
                "weightUnit": "LB",
                "shippingDestination": {
                    "country": "US",
                    "subdivision": "US-NY",
                    "city": "New York",
                    "postalCode": "10011",
                    "addressLine": "235 West 23rd Street",
                    "addressLine2": "3rd floor",
                    "countryFullname": "United States",
                    "subdivisionFullname": "New York"
                },
                "shippingOrigin": {
                    "addressLine1": "34 Elizabeth Street",
                    "addressLine2": "4th floor",
                    "city": "Boston",
                    "country": "US",
                    "postalCode": "02108",
                    "subdivision": "US-MA"
                }
            },
            "metadata": {
                "instanceId": "9698acde-2e44-4656-9db3-f48c91da9828",
                "languages": ["en"],
                "currency": "USD",
                "requestId": "1670756264.11667254865110420",
                "identity": {
                    "identityType": "ANONYMOUS_VISITOR",
                    "anonymousVisitorId": "a02f16af-6174-4f3e-a1e1-6eed2735d67d"
                }
            },
            "aud": "e6a6c88b-8ed1-465b-8c10-5bb0e9285e3f",
            "iss": "wix.com",
            "iat": 1670756264,
            "exp": 1674356264
        }
    }
}

get_validation_violation = {
    "description": "Obtém violações de validação com base nas informações do pedido e das regras de desconto aplicadas",
    "method": "POST",
    "url": "https://provider.example.com/v1/getValidationViolations",
    "headers": {
        "user-agent": "Wix",
        "accept-encoding": "gzip, deflate",
        "content-type": "text/plain; charset=utf-8"
    },
    "data": {
        "sourceInfo": {
            "source": "CART",
            "purchaseFlowId": "a22ebad0-11ef-4a4d-a567-691fa7cb264c"
        },
        "validationInfo": {
            "appliedDiscounts": [
                {
                    "lineItemIds": [],
                    "discountType": "GLOBAL",
                    "coupon": {
                        "id": "435409da-d374-4c44-b08b-6c703c546960",
                        "code": "couponCode",
                        "name": "couponName"
                    }
                }
            ],
            "billingInfo": {
                "address": {
                    "country": "USA",
                    "subdivision": "US-California",
                    "city": "Los Angeles",
                    "postalCode": "123456"
                },
                "contactDetails": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "phone": "12345678",
                    "company": "Wix",
                    "vatId": {
                        "id": "a35409de-d374-4c4b-bf8b-6c703c5b6960",
                        "type": "CPF"
                    }
                }
            },
            "buyerDetails": {
                "contactId": "f463b4ee-0545-45ac-a273-23bf02d38a07",
                "email": "Johnne@wix.com"
            },
            "customFields": {
                "fields": [
                    {
                        "name": "John",
                        "title": "Name",
                        "translatedTitle": "名前"
                    }
                ]
            },
            "giftCard": {
                "id": "e463b4ee-0145-45ac-a263-23bf02d38a07",
                "appId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
                "amount": {
                    "amount": "2"
                }
            },
            "lineItems": [
                {
                    "catalogReference": {
                        "appId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
                        "catalogItemId": "e35409da-d374-4c4b-b08b-6c703c5b6960"
                    },
                    "id": "00000000-0000-0000-0000-000000000001",
                    "itemType": {
                        "preset": "PHYSICAL"
                    },
                    "physicalProperties": {
                        "shippable": True,
                        "sku": "",
                        "weight": 11
                    },
                    "price": {
                        "amount": "1"
                    },
                    "productName": {
                        "original": "Cute Silk Worm",
                        "translated": "Cute Silk Worm"
                    },
                    "quantity": 4
                },
                {
                    "catalogReference": {
                        "appId": "215238eb-22a5-4c36-9e7b-e7c08025e04e",
                        "catalogItemId": "74bfa1c0-ce2a-49b7-8cd8-a4c0e0b2af6e"
                    },
                    "id": "00000000-0000-0000-0000-000000000002",
                    "itemType": {
                        "preset": "PHYSICAL"
                    },
                    "physicalProperties": {
                        "shippable": True,
                        "sku": "",
                        "weight": "12"
                    },
                    "price": {
                        "amount": "600"
                    },
                    "productName": {
                        "original": "Khat Leaves",
                        "translated": "Khat Leaves"
                    },
                    "quantity": 50
                }
            ],
            "priceSummary": {
                "additionalFees": {
                    "amount": "0"
                },
                "discount": {
                    "amount": "0"
                },
                "shipping": {
                    "amount": "0.41"
                },
                "subtotal": {
                    "amount": "3.72"
                },
                "tax": {
                    "amount": "0.87"
                },
                "total": {
                    "amount": "5.00"
                }
            },
            "shippingAddress": {
                "address": {
                    "country": "USA",
                    "subdivision": "US-California",
                    "city": "Los Angeles",
                    "postalCode": "123456"
                },
                "contactDetails": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "phone": "12345678",
                    "company": "Wix",
                    "vatId": {
                        "id": "a35409de-d374-4c4b-bf8b-6c703c5b6960",
                        "type": "CPF"
                    }
                }
            },
            "shippingInfo": {
                "selectedCarrierServiceOption": {
                    "code": "8d782b64-bda4-93f6-d9c4-e40b497b0ec3"
                },
                "weightUnit": "KG"
            }
        }
    }
}

list_available_algorithms = {
    "description": "Lista os algoritmos de recomendação disponíveis",
    "method": "GET",
    "url": "www.wixapis.com/ecom/v1/recommendations/algorithms",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}

get_recommendation = {
    "description": "Obtém recomendações com base em itens e algoritmos específicos",
    "method": "POST",
    "url": "www.wixapis.com/ecom/v1/recommendations/get",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "items": [
            {
                "catalogItemId": "ec7914e8-208b-0069-5850-1a965643508d",
                "appId": "f29c9b39-1090-4d9b-8e3a-a3a681a57970"
            }
        ],
        "algorithms": [
            {
                "id": "e33f5e32-d1a2-4944-b38f-d29b7d5ef4ef",
                "appId": "72454cb3-90b5-4cef-bbff-cc61aea02584"
            },
            {
                "id": "09dc98e8-8696-49f7-833a-bab57f516f88",
                "appId": "b0933968-e643-4835-a403-de8e1eb4d33c"
            }
        ],
        "minimumRelatedItems": 1
    }
}

get_cart = {
    "description": "Obtém os detalhes de um carrinho de compras específico",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/carts/6000dbd9-cb49-4066-820e-2d95cb1e228b",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

get_cart_checkout_url = {
    "description": "Obtém a URL de checkout de um carrinho de compras específico",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/carts/6000dbd9-cb49-4066-820e-2d95cb1e228b/checkoutUrl",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

create_product = {
    "description": "Cria um novo produto no sistema com informações específicas",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products",
    "data": {
        "product": {
            "name": "T-shirt",
            "productType": "physical",
            "priceData": {
                "price": 10.5
            },
            "costAndProfitData": {
                "itemCost": 7
            },
            "description": "nice summer t-shirt",
            "sku": "123df",
            "visible": False,
            "ribbon": "Sale",
            "brand": "Nice",
            "weight": 0.2,
            "discount": {
                "type": "AMOUNT",
                "value": 1
            },
            "manageVariants": True,
            "productOptions": [
                {
                    "name": "Size",
                    "choices": [
                        {
                            "value": "S",
                            "description": "S"
                        },
                        {
                            "value": "L",
                            "description": "L"
                        }
                    ]
                }
            ]
        }
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
update_product = {
    "description": "Atualiza as informações de um produto existente no sistema",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v1/products/83f41911-5375-4ede-aafa-68f8b6dee9e2",
    "data": {
        "product": {
            "name": "T-shirt",
            "productType": "physical",
            "priceData": {
                "price": 12.5
            },
            "description": "nice summer t-shirt",
            "sku": "123df",
            "visible": False,
            "weight": 0.2,
            "ribbon": "Sold Out",
            "brand": "Nice",
            "discount": {
                "type": "AMOUNT",
                "value": 2
            },
            "productOptions": [
                {
                    "name": "Size",
                    "choices": [
                        {
                            "value": "S",
                            "description": "Small"
                        }
                    ]
                }
            ]
        }
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
delete_product = {
    "description": "Exclui um produto existente do sistema com base no ID do produto",
    "method": "DELETE",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

update_product_variant = {
    "description": "Atualiza as informações de uma variante de produto específica",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/variants",
    "data": {
        "variants": [
            {
                "choices": {
                    "Size": 'S',
                    "Color": 'Blue'
                },
                "price": 100
            }
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
reset_product_variant_data = {
    "description": "Redefine todos os dados das variantes do produto para os valores padrão",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/variants/resetToDefault",
    "data": {},
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
add_products_for_collection = {
    "description": "Adiciona produtos a uma coleção específica",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/collections/1044e7e4-37d1-0705-c5b3-623baae212fd/productIds",
    "data": {
        "productIds": [
            "a60fef92-ee29-070f-a7ed-9bbc3cc1c2f4",
            "d9cd1d2f-8318-486b-a6f3-aa0c4e81ccd2"
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
remove_products_from_collection = {
    "description": "Remove produtos de uma coleção específica",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/collections/1044e7e4-37d1-0705-c5b3-623baae212fd/productIds/delete",
    "data": {
        "productIds": [
            "a60fef92-ee29-070f-a7ed-9bbc3cc1c2f4",
            "d9cd1d2f-8318-486b-a6f3-aa0c4e81ccd2"
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

add_product_media = {
    "description": "Adiciona mídia a um produto específico, como imagens ou vídeos",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/media",
    "data": {
        "media": [
            {
                "mediaId": "9cc22d8b8d5244aba9ed73fb1783fc26.jpg"
            },
            {
                "url": "https://your-site-url/image.jpeg",
                "choice": {
                    "option": "Color",
                    "choice": "Blue"
                }
            },
            {
                "mediaId": "11062b_382eeb350464462c8f9150e4d3e40f2b"
            }
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

remove_product_media = {
    "description": "Remove mídia de um produto específico",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/media/delete",
    "data": {
        "mediaIds": [
            "mediaId1",
            "mediaId2"
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

add_product_media_to_choices = {
    "description": "Adiciona mídia a opções de um produto, como cores ou tamanhos",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/choices/media",
    "data": {
        "option": "Color",
        "choice": "blue",
        "mediaIds": [
            "9cc22d8b8d5244aba9ed73fb1783fc26.jpg",
            "fljseif3l4ij3l4ijl3r32fwfwf23234.jpg"
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}

remove_product_media_from_choices = {
    "description": "Remove mídia de opções de um produto, como cores ou tamanhos",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/choices/media/delete",
    "data": {
        "option": "Color",
        "choice": "blue",
        "mediaIds": [
            "9cc22d8b8d5244aba9ed73fb1783fc26.jpg",
            "fljseif3l4ij3l4ijl3r32fwfwf23234.jpg"
        ]
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
delete_product_options = {
    "description": "Remove as opções de um produto específico",
    "method": "DELETE",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/options",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
remove_brand = {
    "description": "Remove a marca de um produto específico",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/remove-brand",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
create_collection = {
    "description": "Cria uma nova coleção no sistema",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/collections",
    "data": {
        "collection": {
            "name": "My New Collection"
        }
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
update_collection_properties = {
    "description": "Atualiza as propriedades de uma coleção existente",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v1/collections/81093e7d-a251-4a22-a238-df3aa816f3dc",
    "data": {
        "collection": {
            "name": "Updated name"
        }
    },
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
delete_collection = {
    "description": "Exclui uma coleção existente",
    "method": "DELETE",
    "url": "https://www.wixapis.com/stores/v1/collections/81093e7d-a251-4a22-a238-df3aa816f3dc",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
remove_ribbon = {
    "description": "Remove a faixa de um produto específico",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/remove-ribbon",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
bulk_update_product_property = {
    "description": "Atualiza uma propriedade em massa para vários produtos",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/bulk/products/update",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ids": [
            "80a584c3-78c1-4e2f-84f8-b8d0bf65b518",
            "e5419878-8284-4f02-98bb-087e1d8dc781",
            "cc30ba06-2b9a-4962-8b34-7a265d495d7e"
        ],
        "set": {
            "cost": 2
        }
    }
}
bulk_adjust_product_properties = {
    "description": "Ajusta propriedades de produtos em massa para vários produtos",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/bulk/products/adjust-properties",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ids": [
            "bfcafbe6-b671-4ebe-8e3d-49f242cef188",
            "e5419878-8284-4f02-98bb-087e1d8dc781"
        ],
        "adjust": {
            "price": {
                "percentage": {
                    "roundToInt": False,
                    "rate": 200
                }
            }
        }
    }
}
query_products = {
    "description": "Consulta produtos com opção de inclusão de variantes",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "includeVariants": True
    }
}
get_product = {
    "description": "Obtém informações sobre um produto específico",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/products/91f7ac8b-2baa-289c-aa50-6d64764f35d3?includeMerchantSpecificData=true",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
query_collections = {
    "description": "Consulta coleções com informações sobre o número de produtos e descrição",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/collections/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {},
        "includeNumberOfProducts": True,
        "includeDescription": True
    }
}
get_collection = {
    "description": "Obtém informações sobre uma coleção específica, incluindo o número de produtos",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/collections/32fd0b3a-2d38-2235-7754-78a3f819274a?includeNumberOfProducts=true",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
get_collection_by_slug = {
    "description": "Obtém informações sobre uma coleção específica por meio de um slug",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/collections/slug/coffee-products",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
get_product_options_availability = {
    "description": "Obtém a disponibilidade de opções de produto",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/1044e7e4-37d1-0705-c5b3-623baae212fd/productOptionsAvailability",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "options": {
            "Size": "S",
            "Color": "Green"
        }
    }
}
query_products_variants = {
    "description": "Consulta variantes de produtos com base nas escolhas",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/products/0614129c-8777-9f3b-4dfe-b80a54df10d5/variants/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "choices": {
            "Weight": "250g"
        },
        "includeMerchantSpecificData": True
    }
}
query_store_variants = {
    "description": "Consulta variantes de loja",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/variants/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
get_store_variant = {
    "description": "Obtém informações sobre uma variante de loja específica",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/variants/0614129c-8777-9f3b-4dfe-b80a54df10d5-00000000-0000-0020-0005-a316f7c67df7",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
get_inventory_variants = {
    "description": "Obtém as variantes de estoque para um item de inventário específico",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/inventoryItems/be547028-fb08-b962-75e8-3f3e56da9ee3/getVariants",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {}
}
query_inventory = {
    "description": "Consulta itens de inventário com base em um filtro",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/inventoryItems/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": "{\"lastUpdated\": {\"$gt\": [\"2020-01-29T09:22:00.000Z\"]}}"
        }
    }
}
update_inventory_variants = {
    "description": "Atualiza as variantes de estoque de um item de inventário específico",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v2/inventoryItems/0ff8f8b0-2857-5974-193e-8283c21fde00",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "inventoryItem": {
            "trackQuantity": False,
            "variants": [
                {
                    "variantId": "00000000-0000-0001-0005-9a596c8e6f10",
                    "inStock": True
                },
                {
                    "variantId": "00000000-0000-0002-0005-9a596c8e6f10",
                    "inStock": True
                }
            ],
            "numericId": 0,
            "preorderInfo": {
                "enabled": True,
                "limit": 6,
                "message": "Expected to ship on June"
            }
        }
    }
}
decrement_inventory = {
    "description": "Decrementa a quantidade de estoque de um item de inventário",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/inventoryItems/decrement",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "decrementData": [
            {
                "productId": "f007074f-d7a8-a68b-e6c1-7d7c3de021ff",
                "variantId": "00000000-0000-0001-0005-9ccb19c4e6f0",
                "decrementBy": 2
            }
        ]
    }
}
increment_inventory = {
    "description": "Incrementa a quantidade de estoque de um item de inventário",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/inventoryItems/increment",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "incrementData": [
            {
                "productId": "f007074f-d7a8-a68b-e6c1-7d7c3de021ff",
                "variantId": "00000000-0000-0001-0005-9ccb19c4e6f0",
                "incrementBy": 2
            }
        ]
    }
}
create_order = {
    "description": "Cria um novo pedido",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/orders",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "order": {
            "totals": {
                "subtotal": "10",
                "shipping": "3",
                "tax": "3",
                "discount": "1",
                "total": "15"
            },
            "billingInfo": {
                "paymentMethod": "PayPal",
                "paymentProviderTransactionId": "tx_1806",
                "address": {
                    "fullName": {
                        "firstName": "John",
                        "lastName": "Smith"
                    },
                    "country": "US",
                    "city": "New York",
                    "zipCode": "92544",
                    "phone": "+972 555234555",
                    "email": "Ivanushka@example.com"
                }
            },
            "shippingInfo": {
                "deliveryOption": "Express",
                "estimatedDeliveryTime": "Today",
                "shippingRegion": "Domestic",
                "shipmentDetails": {
                    "address": {
                        "fullName": {
                            "firstName": "John",
                            "lastName": "Smith"
                        },
                        "country": "US",
                        "city": "New York",
                        "zipCode": "92544",
                        "phone": "+972 555234555",
                        "email": "Ivanushka@example.com"
                    },
                    "tax": "1",
                    "priceData": {
                        "taxIncludedInPrice": False,
                        "price": "3"
                    }
                }
            },
            "paymentStatus": "PAID",
            "lineItems": [
                {
                    "quantity": 2,
                    "discount": "1",
                    "tax": "1",
                    "name": "my product",
                    "productId": "a1f9d337-f831-4529-31e6-67db8fd4e1aa",
                    "lineItemType": "PHYSICAL",
                    "weight": "15",
                    "sku": "12345678",
                    "priceData": {
                        "taxIncludedInPrice": False,
                        "price": "5"
                    }
                }
            ],
            "channelInfo": {
                "type": "WEB"
            }
        }
    }
}
update_order_email = {
    "description": "Atualiza o e-mail associado a um pedido",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v2/orders/4b070345-5813-49b6-b0ad-2125e5ca5b50/updateEmail",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "orderId": "4b070345-5813-49b6-b0ad-2125e5ca5b50",
        "email": "JohnSmith@example.com"
    }
}
update_order_shipping_address = {
    "description": "Atualiza o endereço de entrega de um pedido",
    "method": "PUT",
    "url": "https://www.wixapis.com/stores/v2/orders/4b070345-5813-49b6-b0ad-2125e5ca5b50/updateShippingAddress",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "orderId": "4b070345-5813-49b6-b0ad-2125e5ca5b50",
        "shippingAddress": {
            "fullName": {
                "firstName": "John",
                "lastName": "Smith"
            },
            "country": "US",
            "city": "New York",
            "zipCode": "92544",
            "phone": "+972 555234555"
        }
    }
}
get_order = {
    "description": "Obtém informações sobre um pedido específico",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v2/orders/7001d34b-11a6-4a34-8746-dc8ababeca42",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
query_orders = {
    "description": "Consulta pedidos com base em um filtro",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/orders/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": "{\"paymentStatus\": \"PAID\"}",
            "paging": {
                "limit": 1
            },
            "sort": "[{\"number\": \"desc\"}]"
        }
    }
}
create_fulfillment = {
    "description": "Cria uma nova entrega para um pedido",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v2/orders/fedb19f5-bd4c-4bfc-b2d1-212538319611/fulfillments",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "fulfillment": {
            "lineItems": [
                {
                    "index": 1,
                    "quantity": 1
                }
            ],
            "trackingInfo": {
                "shippingProvider": "fedex",
                "trackingNumber": "1234",
                "trackingLink": "https://www.fedex.com/apps/fedextrack/?action=track&trackingnumber=1234"
            }
        }
    }
}
update_fulfillment = {
    "description": "Atualiza informações de entrega para um pedido",
    "method": "PUT",
    "url": "https://www.wixapis.com/stores/v2/orders/fedb19f5-bd4c-4bfc-b2d1-212538319611/fulfillments/5945017a-bf19-414e-ae67-af3d2dbc66ff",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "fulfillmentTrackingInfo": {
            "shippingProvider": "fedex",
            "trackingNumber": "123"
        }
    }
}
delete_fulfillment = {
    "description": "Exclui uma entrega de um pedido",
    "method": "DELETE",
    "url": "https://www.wixapis.com/stores/v2/orders/fedb19f5-bd4c-4bfc-b2d1-212538319611/fulfillments/0175f0e8-f877-40a9-b980-0d336c64c726",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
create_subscription_options = {
    "description": "Cria uma nova opção de assinatura",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/subscription-options",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "subscriptionOption": {
            "title": "Monthly auto-renewal",
            "subscriptionSettings": {
                "frequency": "MONTH",
                "autoRenewal": True
            }
        }
    }
}
bulk_update_subscription_options = {
    "description": "Atualiza várias opções de assinatura em lote",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v1/subscription-options",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "subscriptionOptions": [
            {
                "id": "26334df1-9ea6-43d5-9a51-acbc9d82690f",
                "title": "Monthly auto-renewal",
                "subscriptionSettings": {
                    "frequency": "MONTH",
                    "autoRenewal": True
                }
            },
            {
                "id": "87d201b5-f8f6-4e60-905f-88815c2c84ec",
                "title": "weekly (for 1 month)",
                "description": "save 10%",
                "subscriptionSettings": {
                    "frequency": "WEEK",
                    "billingCycles": 4
                },
                "discount": {
                    "type": "PERCENT",
                    "value": 10
                }
            }
        ]
    }
}
update_subscription_option = {
    "description": "Atualiza uma opção de assinatura específica",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/87d201b5-f8f6-4e60-905f-88815c2c84ec",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "subscriptionOption": {
            "title": "weekly (for 1 month)",
            "description": "save 10%",
            "subscriptionSettings": {
                "frequency": "WEEK",
                "billingCycles": 4
            },
            "discount": {
                "type": "PERCENT",
                "value": 10
            }
        }
    }
}
delete_subscription_option = {
    "description": "Deleta uma opção de assinatura específica",
    "method": "DELETE",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/26334df1-9ea6-43d5-9a51-acbc9d82690f",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
bulk_create_subscription_options = {
    "description": "Cria várias opções de assinatura em lote",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/createBulk",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "subscriptionOptions": [
            {
                "title": "Monthly auto-renewal",
                "subscriptionSettings": {
                    "frequency": "MONTH",
                    "autoRenewal": True
                }
            },
            {
                "title": "weekly (for 1 month)",
                "description": "save 10%",
                "subscriptionSettings": {
                    "frequency": "WEEK",
                    "billingCycles": 4
                },
                "discount": {
                    "type": "PERCENT",
                    "value": 10
                }
            }
        ]
    }
}
bulk_delete_subscription_options = {
    "description": "Deleta várias opções de assinatura em lote",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/deleteBulk",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ids": [
            "26334df1-9ea6-43d5-9a51-acbc9d82690f",
            "87d201b5-f8f6-4e60-905f-88815c2c84ec"
        ]
    }
}
assign_subscription_options_to_product = {
    "description": "Associa opções de assinatura a um produto específico",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/product/17434d91-b0ad-6633-93d2-8c62b1e96b58/assign",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "assignedSubscriptionOptions": [
            {
                "id": "464e3b77-51bf-40d9-a604-771ffa38f70b"
            },
            {
                "id": "99041397-732e-448c-8fe2-5f1dbd91bb10",
                "hidden": False
            },
            {
                "id": "66542157-d20a-4525-9c23-b7ca4cadf2ee",
                "hidden": True
            }
        ]
    }
}
allow_one_time_purchases = {
    "description": "Permite compras únicas (sem assinatura) de um produto",
    "method": "PATCH",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/product/17434d91-b0ad-6633-93d2-8c62b1e96b58/allowOneTimePurchase",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "allowed": True
    }
}
get_subscription_option = {
    "description": "Obtém informações sobre uma opção de assinatura específica",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/99041397-732e-448c-8fe2-5f1dbd91bb10",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
get_subscription_options_for_product = {
    "description": "Obtém todas as opções de assinatura disponíveis para um produto específico",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/byProduct/17434d91-b0ad-6633-93d2-8c62b1e96b58?includeHiddenSubscriptionOptions=false",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
list_subscription_options = {
    "description": "Lista informações sobre várias opções de assinatura",
    "method": "POST",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/list",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ids": [
            "66542157-d20a-4525-9c23-b7ca4cadf2ee",
            "99041397-732e-448c-8fe2-5f1dbd91bb10"
        ]
    }
}
get_products_id_for_subscription_options = {
    "description": "Obtém IDs de produtos associados a uma opção de assinatura específica",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/99041397-732e-448c-8fe2-5f1dbd91bb10/productIds?includeHiddenProducts=false&paging.limit=2&paging.offset=0",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
get_product_one_time_purchase_status = {
    "description": "Obtém o status de compra única (sem assinatura) de um produto",
    "method": "GET",
    "url": "https://www.wixapis.com/stores/v1/subscription-options/product/17434d91-b0ad-6633-93d2-8c62b1e96b58/oneTimePurchasesStatus",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
list_currencies = {
    "description": "Lista todas as moedas disponíveis",
    "method": "GET",
    "url": "https://www.wixapis.com/currency_converter/api/v1/currencies",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
convert_currency = {
    "description": "Converte uma quantidade de uma moeda para outra",
    "method": "POST",
    "url": "https://www.wixapis.com/currency_converter/v1/currencies/amounts/USD/convert/EUR",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "amounts": [
            {
                "value": 30,
                "decimal_places": 0
            }
        ]
    }
}
get_conversion_rate = {
    "description": "Obtém a taxa de conversão entre duas moedas",
    "method": "GET",
    "url": "https://www.wixapis.com/currency_converter/v1/currencies/rate/USD/convert/EUR",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
connect_account = {
    "description": "Conectar a conta do PSP (Provedor de Serviços de Pagamento)",
    "method": "POST",
    "url": "https://psp.example.com/connect",
    "headers": {
        "Content-Type": "application/json",
        "Digest": "JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup"
    },
    "data": {
        "credentials": {
            "client_id": "MerchantClientId",
            "client_secret": "MerchantClientSecret",
            "price_includes_tax": "true",
            "tax_percentage": "20"
        },
        "country": "US",
        "currency": "USD",
        "mode": "live",
        "wixMerchantId": "000000-0000-0000-0000-000000000000"
    }
}
create_transaction = {
    "description": "Criar uma transação de pagamento",
    "method": "POST",
    "url": "https://psp.example.com/payment",
    "headers": {
        "Content-Type": "application/json",
        "Digest": "JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup"
    },
    "data": {
        "wixMerchantId": "fcd2655f-e261-4c5b-8129-72a241461a27",
        "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
        "paymentMethod": "creditCard",
        "merchantCredentials": {
            "client_id": "e89b-12d3-a456-42665",
            "client_secret": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
        },
        "order": {
            "id": "ce590272-87bf-428f-943a-0ff594059712",
            "description": {
                "totalAmount": 1000,
                "currency": "USD",
                "items": [
                    {
                        "id": "it_1",
                        "name": "Digital camera",
                        "quantity": 1,
                        "price": 1000,
                        "description": "Portable digital camera",
                        "category": "physical"
                    }
                ],
                "buyerInfo": {
                    "buyerId": "ffc0a971-60cb-4c63-8016-39b1bce41e8d",
                    "buyerLanguage": "en"
                }
            },
            "returnUrls": {
                "successUrl": "https://merchant.com/success",
                "errorUrl": "https://merchant.com/error",
                "cancelUrl": "https://merchant.com/cancel",
                "pendingUrl": "https://merchant.com/pending"
            }
        },
        "installments": 1,
        "mode": "live",
        "moto": True,
        "paymentMethodData": {
            "card": {
                "number": "4111111111111111",
                "year": 2030,
                "month": 12,
                "cvv": "777",
                "holderName": "John Smith"
            }
        }
    }
}
refund_transaction = {
    "description": "Solicitar reembolso de uma transação",
    "method": "POST",
    "url": "https://psp.example.com/refund",
    "headers": {
        "Content-Type": "application/json",
        "Digest": "JWT=ai0zIQqt71bmnkgEJ1CRJchjKJup"
    },
    "data": {
        "wixTransactionId": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1",
        "wixRefundId": "fcd2655f-e261-4c5b-8129-72a241461a27",
        "pluginTransactionId": "e89b-12d3-a456-42665",
        "merchantCredentials": {
            "client_id": "e89b-12d3-a456-42665",
            "client_secret": "a15a3ee3-22d3-4a3f-920e-2186e13a19d1"
        },
        "refundAmount": 1000,
        "mode": "live",
        "reason": "REQUESTED_BY_CUSTOMER"
    }
}
submit_event = {
    "description": "Enviar um evento de pagamento",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v1/provider-platform-events",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "event": {
            "refund": {
                "wixTransactionId": "11111111-1111-1111-1111-111111111111",
                "pluginRefundId": "22222222-2222-2222-2222-222222222222",
                "amount": "1000",
                "wixRefundId": "33333333-3333-3333-3333-333333333333",
                "reasonCode": "3025",
                "errorCode": "INSUFFICIENT_FUNDS_FOR_REFUND",
                "errorMessage": "Insufficient funds for refund"
            }
        }
    }
}
send_message = {
    "description": "Enviar uma mensagem em um canal de chat",
    "method": "POST",
    "url": "https://www.wixapis.com/chat/v1/channels/3762db18-9231-41db-bfc6-0adcdf01c41d/messages",
    "headers": {
        "authorization": "<AUTH>",
        "cache-control": "no-cache",
        "content-type": "application/json"
    },
    "data": {
        "channelId": "3762db18-9231-41db-bfc6-0adcdf01c41d",
        "type": "TEXT",
        "payload": {
            "text": "testing from rest"
        },
        "metadata": {}
    }
}
get_category = {
    "description": "Obter informações sobre uma categoria do fórum por ID",
    "method": "GET",
    "url": "https://www.wixapis.com/forum/v1/categories/5cacd5fe04976c0015f35362",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<ACCESS_TOKEN>"
    }
}
get_category_by_slug = {
    "description": "Obter informações sobre uma categoria do fórum por slug",
    "method": "GET",
    "url": "https://www.wixapis.com/forum/v1/categories/slugs/discussion-corner",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<ACCESS_TOKEN>"
    }
}
query_categories = {
    "description": "Consultar categorias do fórum com filtros e classificação",
    "method": "POST",
    "url": "https://www.wixapis.com/forum/v1/categories/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<ACCESS_TOKEN>"
    },
    "data": {
        "paging": {
            "offset": 0,
            "limit": 1
        },
        "filter": {
            "rank": {
                "$eq": 0
            }
        },
        "sort": [
            {
                "fieldName": "rank",
                "order": "ASC"
            }
        ]
    }
}
get_post = {
    "description": "Obter informações sobre uma postagem do fórum por ID",
    "method": "GET",
    "url": "https://www.wixapis.com/forum/v1/posts/5cacd5fe04976c0015f35363",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<ACCESS_TOKEN>"
    }
}
get_post_by_slug = {
    "description": "Obter informações sobre uma postagem do fórum por slug",
    "method": "GET",
    "url": "https://www.wixapis.com/forum/v1/posts/slugs/welcome-to-the-forum",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<ACCESS_TOKEN>"
    }
}
query_posts = {
    "description": "Consultar postagens do fórum com filtros e classificação",
    "method": "POST",
    "url": "https://www.wixapis.com/forum/v1/posts/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<ACCESS_TOKEN>"
    },
    "data": {
        "paging": {
            "offset": 0,
            "limit": 1
        },
        "filter": {
            "likeCount": {
                "$eq": 0
            }
        },
        "sort": [
            {
                "fieldName": "lastActivityDate",
                "order": "ASC"
            }
        ]
    }
}
list_groups = {
    "description": "Listar grupos da comunidade social",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/groups?limit=100",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
create_group = {
    "description": "Criar um novo grupo na comunidade social",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "group": {
            "privacyLevel": "PUBLIC",
            "title": "Group 1",
            "description": "Welcome to the group! You can connect with other members, get updates and share videos.",
            "details": {
                "membersTitle": "Friends",
                "logo": {
                    "mediaId": "4d6eab_666134ee68464d76aa838619344c4369~mv2.jpg",
                    "width": 1024,
                    "height": 150
                }
            },
            "settings": {
                "membersPermittedToInvite": False,
                "membersPermittedToApprove": False,
                "memberWelcomePostEnabled": True,
                "groupDetailsChangedPostEnabled": True,
                "showMemberList": True
            }
        },
        "creatorId": "f98e4407-15bf-43a3-87fb-a954c49bb20f"
    }
}
update_group = {
    "description": "Atualizar informações de um grupo na comunidade social",
    "method": "PATCH",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "group": {
            "title": "New Title!",
            "details": {
                "membersTitle": "Coworkers"
            }
        }
    }
}
get_group = {
    "description": "Obter informações sobre um grupo na comunidade social por ID",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
delete_group = {
    "description": "Excluir um grupo na comunidade social por ID",
    "method": "DELETE",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
get_group_by_slug = {
    "description": "Obter informações sobre um grupo na comunidade social por slug",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/groups/slugs/group-1",
    "headers": {
        "Content-Type": "application.json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
query_groups = {
    "description": "Consultar grupos na comunidade social com filtros e classificação",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "title": {
                    "$contains": "Test"
                }
            },
            "sort": [
                {
                    "fieldName": "createdDate",
                    "order": "DESC"
                }
            ],
            "paging": {
                "offset": 10,
                "limit": 15
            }
        }
    }
}
approve_group_requests = {
    "description": "Aprovar solicitações de membros para ingressar em grupos",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups-requests/approve",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "groupRequestIds": [
            "2447a832-09b9-448e-8051-71d5cdb1217b"
        ]
    }
}
reject_group_requests = {
    "description": "Rejeitar solicitações de membros para ingressar em grupos",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups-requests/reject",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "groupRequestIds": [
            "2447a832-09b9-448e-8051-71d5cdb1217b"
        ]
    }
}
list_group_requests = {
    "description": "Listar solicitações de membros para ingressar em grupos",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/group-requests?limit=100&ownershipFilter=CURRENT_MEMBER",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
query_group_requests = {
    "description": "Consultar solicitações de membros para ingressar em grupos com filtros e classificação",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/group-requests/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ownershipFilter": "CURRENT_MEMBER",
        "query": {
            "filter": {
                "status": {
                    "$eq": "PENDING"
                }
            },
            "sort": [
                {
                    "fieldName": "createdDate",
                    "order": "DESC"
                }
            ],
            "paging": {
                "offset": 0,
                "limit": 100
            }
        }
    }
}
list_group_members = {
    "description": "Listar membros de um grupo na comunidade social",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b/members?limit=100",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
add_group_members = {
    "description": "Adicionar membros a um grupo na comunidade social",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/a4caf853-c0d7-498e-8eaa-3db36522dcbf/members",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "siteMemberIds": [
            "e6674661-f294-4f1f-9f22-bc11fa8164e7"
        ]
    }
}
remove_group_members = {
    "description": "Remover membros de um grupo na comunidade social",
    "method": "DELETE",
    "url": "https://wixapis.com/social-groups/v2/groups/a4caf853-c0d7-498e-8eaa-3db36522dcbf/members",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "siteMemberIds": [
            "e6674661-f294-4f1f-9f22-bc11fa8164e7"
        ]
    }
}
query_group_members_by_role = {
    "description": "Consultar membros de um grupo por função",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b/members/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "role": {
                    "$eq": "ADMIN"
                }
            },
            "sort": [
                {
                    "fieldName": "joinedOn",
                    "order": "DESC"
                }
            ],
            "paging": {
                "offset": 0,
                "limit": 100
            }
        }
    }
}
list_memberships = {
    "description": "Listar associações de membros em grupos",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/members/223c37e0-3474-43c5-8d47-e374b414ef68/memberships?limit=100",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
query_memberships = {
    "description": "Consultar associações de membros em grupos com filtros",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/members/223c37e0-3474-43c5-8d47-e374b414ef68/memberships/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "status": {
                    "$eq": "JOINED"
                }
            },
            "paging": {
                "offset": 0,
                "limit": 100
            }
        }
    }
}
list_join_group_requests = {
    "description": "Listar solicitações de associação a grupos",
    "method": "GET",
    "url": "https://wixapis.com/social-groups/v2/groups/a4caf853-c0d7-498e-8eaa-3db36522dcbf/join-requests?limit=100&ownershipFilter=CURRENT_MEMBER",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    }
}
approve_join_group_requests = {
    "description": "Aprovar solicitações de associação a grupos",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/a4caf853-c0d7-498e-8eaa-3db36522dcbf/join-requests/approve",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "siteMemberIds": [
            "e6674661-f294-4f1f-9f22-bc11fa8164e7"
        ]
    }
}
reject_join_group_requests = {
    "description": "Rejeitar solicitações de associação a grupos",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/a4caf853-c0d7-498e-8eaa-3db36522dcbf/join-requests/reject",
    "headers": {
        "Content-Type": "application-json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "siteMemberIds": [
            "e6674661-f294-4f1f-9f22-bc11fa8164e7"
        ]
    }
}
query_join_group_requests = {
    "description": "Consultar solicitações de associação a grupos",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/a4caf853-c0d7-498e-8eaa-3db36522dcbf/join-requests/query",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ownershipFilter": "CURRENT_MEMBER",
        "query": {
            "filter": {
                "status": {
                    "$eq": "APPROVED"
                }
            },
            "paging": {
                "offset": 0,
                "limit": 100
            }
        }
    }
}
assign_role = {
    "description": "Atribuir função a membros de grupo",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b/roles/assign",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "siteMemberIds": [
            "e6674661-f294-4f1f-9f22-bc11fa8164e7"
        ],
        "role": {
            "value": "ADMIN"
        }
    }
}
unassign_role = {
    "description": "Desatribuir função de membros de grupo",
    "method": "POST",
    "url": "https://wixapis.com/social-groups/v2/groups/8a258cf5-49f3-41dc-b320-65ec2598315b/roles/unassign",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "siteMemberIds": [
            "e6674661-f294-4f1f-9f22-bc11fa8164e7"
        ],
        "role": {
            "value": "ADMIN"
        }
    }
}
notify_request = {
    "description": "Notificar usando um modelo de notificação",
    "method": "POST",
    "url": "https://www.wixapis.com/notifications/v3/notify",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "notificationTemplateId": "2664799d-49ad-417c-aab0-aba0c39a3951",
        "dynamicValues": {
            "recipientName": {
                "text": "Danny"
            },
            "companyName": {
                "text": "WIX"
            },
            "age": {
                "text": "34"
            }
        }
    }
}
report_event_request = {
    "description": "Relatar evento",
    "method": "POST",
    "url": "https://wixapis.com/automations/v1/events/report",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json;charset=UTF-8"
    },
    "data": {
        "triggerKey": "my_trigger",
        "payload": {
            "name": "John Doe"
        },
        "externalEntityId": "16ef8c9c-413e-4d5f-b77d-8c67c3c8ae0c"
    }
}
cancel_event_request = {
    "description": "Cancelar evento",
    "method": "POST",
    "url": "https://wixapis.com/automations/v1/events/cancel",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json;charset=UTF-8"
    },
    "data": {
        "triggerKey": "my_trigger",
        "externalEntityId": "16ef8c9c-413e-4d5f-b77d-8c67c3c8ae0c"
    }
}
get_service_request = {
    "description": "Obter informações sobre um serviço",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v2/services/353aa3b7-00ef-42bd-86ff-720d7ef60443",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
query_services_request = {
    "description": "Consultar serviços",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/services/query",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "limit": 15,
            "filter": {
                "hidden": {
                    "$eq": "false"
                }
            },
            "fields": ["name", "type", "description"]
        }
    }
}
list_categories_request = {
    "description": "Listar categorias",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/categories?includeDeleted=true",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
create_category_request = {
    "description": "Criar categoria",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v1/categories",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "category": {
            "name": "A new Category!"
        }
    }
}
update_category_request = {
    "description": "Atualizar categoria",
    "method": "PUT",
    "url": "https://www.wixapis.com/bookings/v1/categories/77dff5ea-792a-4a3c-a49d-8b19124083d1",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "category": {
            "name": "Updated Category"
        }
    }
}
delete_category_request = {
    "description": "Excluir categoria",
    "method": "DELETE",
    "url": "https://www.wixapis.com/bookings/v1/categories/5c272c84-f9c2-4bbb-b55d-1b88c4597bfe",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
get_form_request = {
    "description": "Obter informações sobre um formulário",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/forms",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
update_form_request = {
    "description": "Atualizar um formulário",
    "method": "PUT",
    "url": "https://www.wixapis.com/bookings/v1/forms",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "form": {
            "id": "a8119733-f872-4b0a-963b-09a95208474e",
            "header": {
                "description": "Updated!!! Tell us a bit about yourself",
                "title": "Add Your Info",
                "isDescriptionHidden": False
            },
            "actionLabels": {
                "offlinePaymentLabel": "Book It",
                "onlinePaymentLabel": "Pay Now",
                "bookingRequestApprovalLabel": "Request To Book"
            },
            "name": {
                "fieldId": "fbe7fc3b-c30e-4ebe-8699-b272a120b178",
                "valueType": "SHORT_TEXT",
                "label": "Name",
                "userConstraints": {
                    "required": True
                },
                "additionalLabels": []
            },
            "email": {
                "fieldId": "30c5f37d-e7c8-4c57-879b-bcd75252d668",
                "valueType": "SHORT_TEXT",
                "label": "Email",
                "userConstraints": {
                    "required": True
                },
                "additionalLabels": []
            },
            "phone": {
                "fieldId": "0691f056-ac53-48e1-a4d7-5f4a6509d8eb",
                "valueType": "SHORT_TEXT",
                "label": "Phone Number",
                "userConstraints": {
                    "required": False
                },
                "additionalLabels": []
            },
            "numberOfParticipants": {
                "fieldId": "9f362e51-461b-4f5c-85b1-d4fb355543b9",
                "valueType": "SHORT_TEXT",
                "label": "Number of Participants",
                "userConstraints": {
                    "required": True
                },
                "additionalLabels": []
            },
            "address": {
                "street": {
                    "fieldId": "c1e68eb8-bc6e-419f-b6c7-7e57d7ff968e",
                    "valueType": "SHORT_TEXT",
                    "label": "Street",
                    "userConstraints": {
                        "required": True
                    },
                    "additionalLabels": []
                },
                "city": {
                    "fieldId": "42337533-6fd6-4f7c-906f-beb69c63aa99",
                    "valueType": "SHORT_TEXT",
                    "label": "City",
                    "userConstraints": {
                        "required": True
                    },
                    "additionalLabels": []
                },
                "floorNumber": {
                    "fieldId": "3c258e9a-3fdd-4cd3-83f9-44b4f47a12de",
                    "valueType": "SHORT_TEXT",
                    "label": "Apt. / Floor No.",
                    "userConstraints": {
                        "required": False
                    },
                    "additionalLabels": []
                },
                "state": {
                    "fieldId": "b7957be3-0776-40da-9a47-7fbb0b832538",
                    "valueType": "SHORT_TEXT",
                    "label": "State",
                    "userConstraints": {
                        "required": False
                    },
                    "additionalLabels": []
                }
            },
            "customFields": [
                {
                    "fieldId": "fd57ad23-22c0-4049-b674-0c95512ca078",
                    "valueType": "LONG_TEXT",
                    "label": "Add Your Message",
                    "userConstraints": {
                        "required": False
                    },
                    "additionalLabels": []
                }
            ]
        }
    }
}
create_form_request = {
    "description": "Criar formulário",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v1/forms",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "form": {
            "header": {
                "description": "Tell us a bit about yourself",
                "title": "Add Your Info",
                "isDescriptionHidden": False
            },
            "actionLabels": {
                "offlinePaymentLabel": "Book It",
                "onlinePaymentLabel": "Pay Now",
                "bookingRequestApprovalLabel": "Request To Book"
            },
            "name": {
                "label": "Name"
            },
            "email": {
                "label": "Email"
            },
            "phone": {
                "label": "Phone Number"
            },
            "numberOfParticipants": {
                "label": "Number of Participants"
            },
            "address": {
                "street": {
                    "label": "Street"
                },
                "city": {
                    "label": "City"
                },
                "floorNumber": {
                    "label": "Apt. / Floor No.",
                    "userConstraints": {
                        "required": False
                    }
                },
                "state": {
                    "label": "State",
                    "userConstraints": {
                        "required": False
                    }
                }
            },
            "customFields": [
                {
                    "valueType": "LONG_TEXT",
                    "label": "Add Your Message",
                    "userConstraints": {
                        "required": False
                    }
                }
            ]
        }
    }
}
update_bookings_policy_request = {
    "description": "Atualizar a política de reservas",
    "method": "PUT",
    "url": "https://www.wixapis.com/bookings/v1/services/policy",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "policy": {
            "bookUpToXMinutesBefore": 0,
            "cancelRescheduleUpToXMinutesBefore": 0,
            "futureBookingsPolicy": {
                "shouldLimit": False,
                "limitXMinutesToTheFuture": 10080
            },
            "waitingListPolicy": {
                "isEnabled": False,
                "capacity": 10,
                "timeWindowMinutes": 10
            }
        }
    }
}
get_bookings_policy_request = {
    "description": "Obter a política de reservas",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/services/policy",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
create_service_options_and_variants_request = {
    "description": "Criar opções e variantes de serviço",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "serviceOptionsAndVariants": {
            "serviceId": "6072fbad-5c95-4bf6-a9bc-4280aadc1ae8",
            "options": {
                "values": [
                    {
                        "customData": {
                            "choices": ["Student", "Adult"],
                            "name": "Customer Type"
                        },
                        "id": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                        "type": "CUSTOM"
                    }
                ]
            },
            "variants": {
                "values": [
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Student"
                            }
                        ],
                        "price": {
                            "currency": "EUR",
                            "value": "3"
                        }
                    },
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Adult"
                            }
                        ],
                        "price": {
                            "currency": "EUR",
                            "value": "12"
                        }
                    }
                ]
            }
        }
    }
}
clone_service_options_and_variants_request = {
    "description": "Clonar opções e variantes de serviço",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/0cf0c708-58f0-408b-a10f-a6d9b6e2a6de/clone",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "targetServiceId": "cea2bc29-9f05-4523-a4d7-cd52983b43dc"
    }
}
get_service_options_and_variants_request = {
    "description": "Obter opções e variantes de serviço",
    "method": "GET",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/0cf0c708-58f0-408b-a10f-a6d9b6e2a6de",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
delete_service_options_and_variants_request = {
    "description": "Excluir opções e variantes de serviço",
    "method": "DELETE",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/cee77f8c-2ad3-11ed-a261-0242ac120002",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
get_service_options_and_variants_by_service_id_request = {
    "description": "Obter opções e variantes de serviço por ID de serviço",
    "method": "GET",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/service_id/33340481-e57e-4285-8e31-4f0b5ca0a6b5",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
update_service_options_and_variants_request = {
    "description": "Atualizar opções e variantes de serviço",
    "method": "PATCH",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/7e7eac53-21c9-41fd-844b-25b287aa38ce",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "serviceOptionsAndVariants": {
            "serviceId": "6072fbad-5c95-4bf6-a9bc-4280aadc1ae8",
            "options": {
                "values": [
                    {
                        "customData": {
                            "choices": ["Student", "Adult"],
                            "name": "Customer Type"
                        },
                        "id": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                        "type": "CUSTOM"
                    }
                ]
            },
            "variants": {
                "values": [
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Student"
                            }
                        ],
                        "price": {
                            "value": "8",
                            "currency": "EUR"
                        }
                    },
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Adult"
                            }
                        ],
                        "price": {
                            "value": "12",
                            "currency": "EUR"
                        }
                    }
                ],
                "revision": "1",
                "id": "7e7eac53-21c9-41fd-844b-25b287aa38ce"
            }
        }
    }
}
query_service_options_and_variants_request = {
    "description": "Consultar opções e variantes de serviço",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/query",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "sort": [
                {
                    "fieldName": "serviceId",
                    "order": "DESC"
                }
            ],
            "fieldsets": [],
            "fields": [],
            "cursorPaging": {
                "limit": 3
            }
        }
    }
}
list_services_request = {
    "description": "Listar serviços",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/catalog/services",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
query_services_catalog_request = {
    "description": "Consultar serviços no catálogo",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/catalog/services",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "category.name": {"$contains": "Services"},
                "service.paymentOptions.wixPayOnline": True
            },
            "includeDeleted": False
        }
    }
}
get_service_request = {
    "description": "Obter um serviço específico",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/catalog/services/4c0bae61-4599-4d02-a2f4-25e9222df416?fields=service.info.name&fields=service.id",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
list_resources_request = {
    "description": "Listar recursos",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/resources",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
create_resource_request = {
    "description": "Criar um recurso",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/resources",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "resource": {
            "name": "Rachel Green 3",
            "email": "rachel.mysite.info",
            "phone": "620-428-1741",
            "tags": ["staff"],
            "images": []
        },
        "schedules": [
            {
                "timeZone": "Asia/Jerusalem",
                "intervals": [
                    {
                        "start": "2020-04-18T21:00:00Z",
                        "interval": {
                            "daysOfWeek": "FRI",
                            "hourOfDay": 10,
                            "minuteOfHour": 0,
                            "duration": 480
                        },
                        "frequency": {
                            "repetition": 1
                        },
                        "affectedSchedules": []
                    },
                    {
                        "start": "2020-04-18T21:00:00Z",
                        "interval": {
                            "daysOfWeek": "SAT",
                            "hourOfDay": 9,
                            "minuteOfHour": 0,
                            "duration": 540
                        },
                        "frequency": {
                            "repetition": 1
                        },
                        "affectedSchedules": []
                    },
                    {
                        "start": "2020-04-18T21:00:00Z",
                        "interval": {
                            "daysOfWeek": "SUN",
                            "hourOfDay": 9,
                            "minuteOfHour": 0,
                            "duration": 540
                        },
                        "frequency": {
                            "repetition": 1
                        },
                        "affectedSchedules": []
                    }
                ],
                "tags": [],
                "availability": {
                    "start": "2020-04-18T21:00:00Z",
                    "linkedSchedules": []
                },
                "totalNumberOfParticipants": 0,
                "participants": [],
                "inheritedFields": ["timeZone"]
            }
        ]
    }
}
query_resource_request = {
    "description": "Consultar recursos",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v1/resources/query",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "query": {
            "filter": {
                "resource.tags": {"$in": "staff"},
                "resource.status": {"$in": ["DELETED", "UPDATED"]}
            },
            "fields": ["name", "tags", "status"],
            "paging": {"limit": 10, "offset": 3}
        }
    }
}
update_resource_request = {
    "description": "Atualizar um recurso",
    "method": "PATCH",
    "url": "https://www.wixapis.com/bookings/v1/resources",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "resource": {
            "name": "Sakura H. Tanaka",
            "email": "stanaka@test.info",
            "phone": "555 4337"
        }
    }
}
update_schedule_request = {
    "description": "Atualizar um agendamento de recurso",
    "method": "PATCH",
    "url": "https://www.wixapis.com/bookings/v1/resources/26a20115-6b1c-42d8-88cf-897e8fbaadb5/updateSchedule",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "schedule": {
            "id": "ac23ffec-83ee-4c84-8d67-c6bba9d9fabf",
            "availability": {
                "linkedSchedules": [
                    {
                        "scheduleId": "48ed1477-443b-40f4-bd71-7a04e863cafd",
                        "transparency": "BUSY",
                        "scheduleOwnerId": "e6b6108c-92bc-462b-937c-dab386909fd2"
                    }
                ]
            }
        }
    }
}
delete_resource_request = {
    "description": "Excluir um recurso",
    "method": "DELETE",
    "url": "https://www.wixapis.com/bookings/v1/resources/4c0bae61-4599-4d02-a2f4-25e9222df416",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
preview_price_request = {
    "description": "Prever o preço de um serviço com escolhas",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/pricing/preview",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "bookingLineItems": [
            {
                "serviceId": "dae13fbb-4314-4b1c-990d-1d82c280cb2f",
                "resourceId": "76570209-101f-409b-af97-b445bdb63125",
                "choices": [
                    {
                        "optionId": "68ea3e36-4a40-461d-81ef-349499d51c74",
                        "custom": "Adults"
                    }
                ],
                "numberOfParticipants": 2
            },
            {
                "serviceId": "dae13fbb-4314-4b1c-990d-1d82c280cb2f",
                "resourceId": "76570209-101f-409b-af97-b445bdb63125",
                "choices": [
                    {
                        "optionId": "68ea3e36-4a40-461d-81ef-349499d51c74",
                        "custom": "Child"
                    }
                ],
                "numberOfParticipants": 3
            }
        ]
    }
}
calculate_price_request = {
    "description": "Calcular o preço de uma reserva",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/pricing/calculate",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "booking": {
            "bookedEntity": {
                "slot": {
                    "serviceId": "dae13fbb-4314-4b1c-990d-1d82c280cb2f",
                    "resource": {
                        "id": "76570209-101f-409b-af97-b445bdb63125"
                    }
                }
            },
            "participantsChoices": {
                "serviceChoices": [
                    {
                        "numberOfParticipants": 1,
                        "choices": [
                            {
                                "optionId": "68ea3e36-4a40-461d-81ef-349499d51c74",
                                "custom": "Adults"
                            }
                        ]
                    }
                ]
            }
        }
    }
}
get_attendance_request = {
    "description": "Obter informações de atendimento",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v2/attendance/9fc7a1cc-55ba-4943-afac-5849f1a3cdd9",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
set_attendance_request = {
    "description": "Definir atendimento",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/attendance/set",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "attendance": {
            "bookingId": "88214716-6ed1-4273-b089-8015c4ab2f4b",
            "sessionId": "2mmoW0vwKcSFyxtOfCdMqTntk7dVhOyHRtg53bu4e0cvIFpCA9sAC0M0ZiAJcAcni80UUc0DZWeZiSWqQEpqEHzb6cLa99kNRZDp",
            "status": "ATTENDED",
            "numberOfAttendees": 1
        }
    }
}
query_attendance_request = {
    "description": "Consultar atendimento",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/attendance/query",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "status": "NOT_ATTENDED"
            }
        }
    }
}
list_waiting_list_request = {
    "description": "Listar entidades em lista de espera",
    "method": "GET",
    "url": "https://www.wixapis.com/bookings/v1/waitlist/list?waitingResources=193ZPR9ppP9emJUCLevcLf6orynNEIDt5nc0520xjGQILnPPaF5s62yK3BWz7ExgIRM1VRioAcbF7zzwvoBTEIScx8fykHVtU2r5GoJrd7PuRidnB3zvYGeB6vu46SF7RN6M20Jg3OP1PZhRjhbotC5iz5mBXEncK2sHCaVgGczVpDEUts19ULscMtZ8dzmp6Hd6caRs6g5UcGtKSnvH5KJPYdojijsgantqsSTmGCItRoTcYi0dBhYzvxxB6Sv51iSs7tupi36hkw6Eau5FhC7P8jBQfZ0eFi7tZIeGUyoV39wexfMbu0kLn5nRTUVx5r0eSzENSJcV7F",
    "headers": {
        "Authorization": "<AUTH>"
    }
}

register_to_waitlist_request = {
    "description": "Registrar-se na lista de espera",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v1/waitlist/register",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "waitingResource": "193ZPR9ppP9emJUCLevcLf6orynNEIDt5nc0520xjGQILnPPaF5s62yK3BWz7ExgIRM1VRioAcbF7zzwvoBTEIScx8fykHVtU2r5GoJrd7PuRidnB3zvYGeB6vu46SF7RN6M20Jg3OP1PZhRjhbotC5iz5mBXEncK2sHCaVgGczVpDEUts19ULscMtZ8dzmp6Hd6caRs6g5UcGtKSnvH5KJPYdojijsgantqsSTmFokncR3Y5PHqiIRaLeERqoPVfZbwXR7nJIOAe5EjjoMPFhRTOoczpbq9zjDLsREsYtStLaYvO2zhufHEWlp5Gq7mB9cXh1UmPbR7rp"
    }
}
leave_waitlist_request = {
    "description": "Sair da lista de espera",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v1/waitlist/leave",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "registrationId": "f0213bd9-a663-40d4-9b07-25832d17d33e",
        "waitingResource": "193ZPR9ppP9emJUCLevcLf6orynNEIDt5nc0520xjGQILnPPaF5s62yK3BWz7ExgIRM1VRioAcbF7zzwvoBTEIScx8fykHVtU2r5GoJrd7PuRidnB3zvYGeB6vu46SF7RN6M20Jg3OP1PZhRjhbotC5iz5mBXEncK2sHCaVgGczVpDEUts19ULscMtZ8dzmp6Hd6caRs6g5UcGtKSnvH5KJPYdojijsgantqsSTmFokncR3Y5PHqiIRaLeERqoPVfZbwXR7nJIOAe5EjjoMPFhRTOoczpbq9zjDLsREsYtStLaYvO2zhufHEWlp5Gq7mB9cXh1UmPbR7rp"
    }
}
book_from_waitlist_request = {
    "description": "Reservar da lista de espera",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v1/waitlist/enroll",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "registrationId": "2724acf6-fedd-402b-8cbc-48bc784481d9"
    }
}
create_booking_request = {
    "description": "Criar uma reserva",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bookings",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "booking": {
            "bookedEntity": {
                "slot": {
                    "serviceId": "8ee826a3-64c4-416d-a22c-e01d39f56931",
                    "scheduleId": "844772a6-ad31-49fb-b3d9-7aef1e559b7e",
                    "startDate": "2022-12-26T12:00:00.000Z",
                    "endDate": "2022-12-26T13:00:00.000Z",
                    "timezone": "Europe/Dublin",
                    "resource": {
                        "id": "5fa50f19-4c94-4c42-a72b-289505ba2028",
                        "name": "Tom Jones",
                        "scheduleId": "a4166c1f-728c-4895-8a6e-1942bb321315"
                    },
                    "location": {
                        "id": "9de094d5-8985-484e-9218-d020d9d17953",
                        "name": "Location Name",
                        "formattedAddress": "Location Address",
                        "locationType": "OWNER_BUSINESS"
                    }
                },
                "title": "In-person Appointment",
                "tags": ["INDIVIDUAL"]
            },
            "contactDetails": {
                "firstName": "John",
                "email": "john@example.com"
            },
            "additionalFields": [],
            "totalParticipants": 1,
            "selectedPaymentOption": "ONLINE"
        },
        "sendSmsReminder": False,
        "participantNotification": {
            "notifyParticipants": True
        },
        "flowControlSettings": {
            "skipAvailabilityValidation": False,
            "skipBusinessConfirmation": False,
            "skipSelectedPaymentOptionValidation": False
        }
    }
}
bulk_create_booking_request = {
    "description": "Criar várias reservas em lote",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bulk/bookings/create",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "create_bookings_info": [
            {
                "booking": {
                    "additional_fields": [],
                    "contact_details": {
                        "first_name": "John",
                        "last_name": "Smith",
                        "email": "john@example.com"
                    },
                    "number_of_participants": 101,
                    "selected_payment_option": "OFFLINE",
                    "booked_entity": {
                        "tags": [],
                        "slot": {
                            "session_id": "2mmoW0vwKcSFyxtOfCdMtcdSxR9eP0QJxQJQWTXGy0Al6QeAcX8ZIDsZHTX9Ac3S1JsWouwU09anSiLIogKIAPnLFithTcTBx111"
                        }
                    }
                }
            },
            {
                "booking": {
                    "additional_fields": [],
                    "contact_details": {
                        "first_name": "John2",
                        "last_name": "Smith2",
                        "email": "john2@example.com"
                    },
                    "number_of_participants": 1,
                    "selected_payment_option": "OFFLINE",
                    "booked_entity": {
                        "tags": [],
                        "slot": {
                            "session_id": "2mmoW0vwKcSFyxtOfCdMtcdSxR9eP0QJxQJQWTXGy0Al6QeAcX8ZIDsZHTX9Ac3S1JsWouwU09anSiLIogKIAPnLFithTcTBx111"
                        }
                    }
                }
            }
        ],
        "returnFullEntity": True
    }
}
reschedule_booking_request = {
    "description": "Remarcar uma reserva",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bookings/a80daf61-41f2-4195-b592-978321e969b9/reschedule",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "slot": {
            "sessionId": "2mmoW0vwKcSFyxtOfCdKTATfNXY9sBJdc35TZCXaVhrOWCsHv0e8sE2dEIzNOeRWb2SMLNjSrwQk557YdfycK5OGQaOicTerujnR",
            "startDate": "2022-11-03T11:00:00.000Z",
            "endDate": "2022-11-04T12:00:00.000Z",
            "timezone": "Europe/Dublin",
            "resource": {
                "name": "Dodly",
                "id": "64bb860a-eda5-4992-9fc6-538d58e818ec",
                "scheduleId": "64bb860a-eda5-4992-9fc6-538d58e818ec"
            },
            "scheduleId": "14c80105-2dac-42fd-b901-e7109dee47f9",
            "serviceId": "032cd844-18fe-4ffc-86cc-e6e47f4243f0",
            "location": {
                "locationType": "OWNER_CUSTOM"
            }
        },
        "bookingId": "a80daf61-41f2-4195-b592-978321e969b9",
        "revision": "7",
        "participantNotification": {
            "notifyParticipants": False
        },
        "totalParticipants": 1
    }
}
update_extended_fields_request = {
    "description": "Atualizar campos estendidos",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bookings/9caabb6a-2ad0-4947-b38f-77a10433baf4/update_extended_fields",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "namespace": "@accountName/appName",
        "namespaceData": {
            "boatType": "kayak"
        }
    }
}
decline_booking_request = {
    "description": "Recusar uma reserva",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bookings/17411c29-cfcb-4c07-9437-b673764781dd/decline",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "participantNotification": {
            "notifyParticipants": False
        },
        "bookingId": "17411c29-cfcb-4c07-9437-b673764781dd",
        "revision": "2"
    }
}
cancel_booking_request = {
    "description": "Cancelar uma reserva",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bookings/b4d80fb5-2e8f-4174-91fd-dfededcb50d2/cancel",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "participantNotification": {
            "notifyParticipants": False
        },
        "bookingId": "b4d80fb5-2e8f-4174-91fd-dfededcb50d2",
        "revision": "2"
    }
}
update_number_of_participants_request = {
    "description": "Atualizar o número de participantes",
    "method": "POST",
    "url": "https://www.wixapis.com/bookings/v2/bookings/66882b7a-9e8c-4834-89bb-6eb98ca88b65/update_number_of_participants",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "totalParticipants": 3,
        "participantNotification": {
            "notifyParticipants": False
        },
        "bookingId": "66882b7a-9e8c-4834-89bb-6eb98ca88b65",
        "revision": "17"
    }
}
query_availability_request = {
    "description": "Consultar a disponibilidade",
    "method": "POST",
    "url": "https://www.wixapis.com/availability-calendar/v1/availability/query",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "serviceId": ["832adc1f-d6cc-412d-894d-f04455baec68"],
                "startDate": "2023-05-20T12:00:00.000Z",
                "endDate": "2023-05-20T13:00:00.000Z",
                "location.businessLocation.id": ["3dd710bd-3480-49b4-a549-0522b035a8d7"]
            }
        }
    }
}
create_service_options_variants_request = {
    "description": "Criar serviços, opções e variantes",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "serviceOptionsAndVariants": {
            "serviceId": "6072fbad-5c95-4bf6-a9bc-4280aadc1ae8",
            "options": {
                "values": [
                    {
                        "customData": {
                            "choices": ["Student", "Adult"],
                            "name": "Customer Type"
                        },
                        "id": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                        "type": "CUSTOM"
                    }
                ]
            },
            "variants": {
                "values": [
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Student"
                            }
                        ],
                        "price": {
                            "currency": "EUR",
                            "value": "3"
                        }
                    },
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Adult"
                            }
                        ],
                        "price": {
                            "currency": "EUR",
                            "value": "12"
                        }
                    }
                ]
            }
        }
    }
}
clone_service_options_variants_request = {
    "description": "Clonar opções e variantes de serviços",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/0cf0c708-58f0-408b-a10f-a6d9b6e2a6de/clone",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "targetServiceId": "cea2bc29-9f05-4523-a4d7-cd52983b43dc"
    }
}
get_service_options_variants_request = {
    "description": "Obter opções e variantes de serviços",
    "method": "GET",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/0cf0c708-58f0-408b-a10f-a6d9b6e2a6de",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
delete_service_options_variants_request = {
    "description": "Excluir opções e variantes de serviços",
    "method": "DELETE",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/cee77f8c-2ad3-11ed-a261-0242ac120002",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
update_service_options_variants_request = {
    "description": "Atualizar opções e variantes de serviços",
    "method": "PATCH",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/7e7eac53-21c9-41fd-844b-25b287aa38ce",
    "headers": {
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "serviceOptionsAndVariants": {
            "serviceId": "6072fbad-5c95-4bf6-a9bc-4280aadc1ae8",
            "options": {
                "values": [
                    {
                        "customData": {
                            "choices": ["Student", "Adult"],
                            "name": "Customer Type"
                        },
                        "id": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                        "type": "CUSTOM"
                    }
                ]
            },
            "variants": {
                "values": [
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Student"
                            }
                        ],
                        "price": {
                            "value": "8",
                            "currency": "EUR"
                        }
                    },
                    {
                        "choices": [
                            {
                                "optionId": "0b78af72-0ba0-4e71-ba39-b4386555a353",
                                "custom": "Adult"
                            }
                        ],
                        "price": {
                            "value": "12",
                            "currency": "EUR"
                        }
                    }
                ]
            },
            "revision": "1",
            "id": "7e7eac53-21c9-41fd-844b-25b287aa38ce"
        }
    }
}
query_service_options_variants_request = {
    "description": "Consultar opções e variantes de serviços",
    "method": "POST",
    "url": "https://wixapis.com/bookings/v1/serviceOptionsAndVariants/query",
    "headers": {
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "sort": [
                {
                    "fieldName": "serviceId",
                    "order": "DESC"
                }
            ],
            "fieldsets": [],
            "fields": [],
            "cursorPaging": {
                "limit": 3
            }
        }
    }
}
create_submission_request = {
    "description": "Criar submissão",
    "method": "POST",
    "url": "http://www.wixapis.com/form-submission/v4/submissions",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "submission": [
            {
                "formId": "e62e3011-55cf-4de3-a497-e097b52d86b8",
                "submissions": {
                    "first_name": "Adam",
                    "last_name": "Fisher"
                }
            }
        ]
    }
}
get_submission_request = {
    "description": "Obter submissão",
    "method": "GET",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/e62e3011-55cf-4de3-a497-e097b52d86b7",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
delete_submission_request = {
    "description": "Excluir submissão",
    "method": "DELETE",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/e62e3011-55cf-4de3-a497-e097b52d86b7",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
update_submission_request = {
    "description": "Atualizar submissão",
    "method": "PATCH",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/e62e3011-55cf-4de3-a497-e097b52d86b7",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "submission": {
            "id": "e62e3011-55cf-4de3-a497-e097b52d86b7",
            "seen": true
        }
    }
}
confirm_submission_request = {
    "description": "Confirmar submissão",
    "method": "POST",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/e62e3011-55cf-4de3-a497-e097b52d86b7/confirm",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    }
}
query_submissions_by_namespace_request = {
    "description": "Consultar submissões por namespace",
    "method": "POST",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/namespace/query",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "query": {
            "filter": {
                "formId": "e62e3011-55cf-4de3-a497-e097b52d86b8",
                "namespace": "wix.form_app.form"
            }
        },
        "onlyYourOwn": True
    }
}
count_submissions_request = {
    "description": "Contar submissões",
    "method": "POST",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/count",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "formIds": ["e62e3011-55cf-4de3-a497-e097b52d86b8"],
        "namespace": "wix.form_app.form"
    }
}
get_media_upload_url_request = {
    "description": "Obter URL de envio de mídia",
    "method": "POST",
    "url": "http://www.wixapis.com/form-submission/v4/submissions/media-upload-url",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "form_id": "e62e3011-55cf-4de3-a497-e097b52d86b8",
        "filename": "cats.mp4",
        "mimeType": "video/mp4"
    }
}
bulk_mark_submission_as_seen_request = {
    "description": "Marcar submissões em massa como vistas",
    "method": "POST",
    "url": "http://www.wixapis.com/form-submission/v4/bulk/submissions/mark-as-seen",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "<AUTH>"
    },
    "data": {
        "ids": ["e62e3011-55cf-4de3-a497-e097b52d86b7"],
        "formId": "e62e3011-55cf-4de3-a497-e097b52d86b8"
    }
}
create_transaction_request = {
    "description": "Criar transação",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions",
    "headers": {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "items": [
            {
                "id": "3f2939f3-cbb3-46c7-9682-dbacaa52d3ca",
                "title": "Product#1",
                "unitPrice": "100",
                "quantity": 1,
                "category": "DIGITAL"
            }
        ],
        "metadata": {
            "metadataKey": "metadataValue"
        },
        "accountId": "6f82b2ce-2a15-4bd7-84b5-392c74b3719c",
        "amount": "100",
        "currency": "USD",
        "externalInvoiceId": "4a3f71e5-9c20-4aca-b994-3b5bbd57a2bd",
        "externalOrderId": "4a3f71e5-9c20-4aca-b994-3b5bbd57a2bd",
        "returnUrl": "https://wix.com/3ds",
        "paymentMethodTypeId": "creditCard",
        "card": {
            "numberToken": "675f55ed-adfe-4411-b4cf-aaa8e614a715",
            "expiryMonth": 12,
            "expiryYear": 2025,
            "holderName": "PAYMENTS TESTS",
            "securityCodeToken": "46cc9574-cf5f-4e47-bfc8-f833e1bfddb3"
        },
        "externalBuyerId": "4a3f71e5-9c20-4aca-b994-3b5bbd57a2bd",
        "billingAddress": {
            "address": {
                "country": "US",
                "city": "New York",
                "postalCode": "10003",
                "streetAddress": {
                    "number": "20",
                    "name": "Cooper Square"
                }
            },
            "contactDetails": {
                "firstName": "John",
                "lastName": "Doe",
                "phone": "12345675432",
                "company": "Company wix.com",
                "email": "john.doe@test.com",
                "vatId": {
                    "id": "134424234",
                    "type": "UNSPECIFIED"
                }
            }
        },
        "idempotencyKey": "9f5a2e55-b0ec-484e-8247-460de104f3ba",
        "externalTransactionId": "d44150d8-1cbe-4ead-9f1d-c9a673698a7f",
        "setupCofOnSession": {}
    }
}
get_transaction_request = {
    "description": "Obter transação",
    "method": "GET",
    "url": "https://www.wixapis.com/payments/v3/transactions/4f68983f-9b70-438e-8130-4fff0b97cf48?accountId=6f82b2ce-2a15-4bd7-84b5-392c74b3719c",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
capture_transaction_request = {
    "description": "Capturar transação",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions/29298cc4-43b1-4ae9-bd52-be5e35cd114b/capture",
    "headers": {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "accountId": "6f82b2ce-2a15-4bd7-84b5-392c74b3719c"
    }
}
void_or_refund_transaction_request = {
    "description": "Anular ou reembolsar transação",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions/4c37853b-79d5-4f0a-aadc-e8c3c4f2c322/refund",
    "headers": {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "<AUTH>"
    },
    "data": {
        "accountId": "6f82b2ce-2a15-4bd7-84b5-392c74b3719c",
        "reason": "DUPLICATE_PAYMENT"
    }
}
accept_dispute_request = {
    "description": "Aceitar disputa",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions/bdba15b3-e931-4877-ae98-ce4f3f37b233/disputes/786f68e5-fa4a-45ef-a2c8-1edfb27dd5a6/accept",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json; charset=utf-8"
    },
    "data": {
        "account_id": "c94b4b44-4523-4826-a6ce-5fed1cc19d59"
    }
}
generate_evidence_upload_url_request = {
    "description": "Gerar URL de upload de evidências",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions/bb4188b7-1779-44d6-961d-e3db25a6bea0/disputes/0a6f4f4a-407f-4892-836c-ad968708c679/generate-evidence-upload-url",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json; charset=utf-8"
    },
    "data": {
        "account_id": "c94b4b44-4523-4826-a6ce-5fed1cc19d59"
    }
}
add_evidence_request = {
    "description": "Adicionar evidências",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions/bb4188b7-1779-44d6-961d-e3db25a6bea0/disputes/0a6f4f4a-407f-4892-836c-ad968708c679/add-evidence",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json; charset=utf-8"
    },
    "data": {
        "account_id": "c94b4b44-4523-4826-a6ce-5fed1cc19d59",
        "evidence": {
            "type": "ACCESS_ACTIVITY_LOG",
            "file_id": "7017b89bdd9b443c8e39fe7ba12cd197"
        }
    }
}
submit_evidence_request = {
    "description": "Submeter evidências",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/transactions/bb4188b7-1779-44d6-961d-e3db25a6bea0/disputes/0a6f4f4a-407f-4892-836c-ad968708c679/submit-evidence",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json; charset=utf-8"
    },
    "data": {
        "account_id": "c94b4b44-4523-4826-a6ce-5fed1cc19d59"
    }
}
generate_card_token_request = {
    "description": "Gerar token de cartão de crédito",
    "method": "POST",
    "url": "https://www.wixapis.com/payments/v3/card-tokens",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json; charset=utf-8"
    },
    "data": {
        "cardNumber": "1234567890123456",  # Número do cartão
        "securityCode": "123"  # Código de segurança (CVV)
    }
}
insert_data_item_request = {
    "description": "Inserir item de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItem": {
            "data": {
                "state": "California",
                "year": 2022,
                "city": "Los Angeles",
                "population": 3800000
            }
        }
    }
}
update_data_item_request = {
    "description": "Atualizar item de dados",
    "method": "PUT",
    "url": "https://www.wixapis.com/wix-data/v2/items/5331fc15-9441-4fd4-bc7b-7f6870c69228",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItem": {
            "data": {
                "state": "California",
                "year": 2022,
                "city": "Los Angeles",
                "population": 3800000
            }
        }
    }
}
save_data_item_request = {
    "description": "Salvar item de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/save",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItem": {
            "data": {
                "state": "California",
                "year": 2022,
                "city": "Los Angeles",
                "population": 3800000
            }
        }
    }
}
get_data_item_request = {
    "description": "Obter item de dados",
    "method": "GET",
    "url": "https://www.wixapis.com/wix-data/v2/items/5331fc15-9441-4fd4-bc7b-7f6870c69228?dataCollectionId=cities",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
remove_data_item_request = {
    "description": "Remover item de dados",
    "method": "DELETE",
    "url": "https://www.wixapis.com/wix-data/v2/items/5331fc15-9441-4fd4-bc7b-7f6870c69228?dataCollectionId=cities",
    "headers": {
        "Authorization": "<AUTH>"
    }
}
truncate_data_items_request = {
    "description": "Esvaziar itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/truncate",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities"
    }
}
query_data_items_request = {
    "description": "Consultar itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/query",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "query": {
            "filter": {
                "state": "California"
            },
            "paging": {
                "limit": 2
            }
        }
    }
}
aggregate_data_items_request = {
    "description": "Agrupar itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/aggregate",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "initialFilter": {
            "year": 2022
        },
        "aggregation": {
            "groupingFields": ["state"],
            "operations": [
                {
                    "resultFieldName": "totalPopulation",
                    "sum": {
                        "itemFieldName": "population"
                    }
                }
            ]
        }
    }
}
count_data_items_request = {
    "description": "Contar itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/count",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "filter": {
            "state": "California"
        }
    }
}
query_distinct_values_request = {
    "description": "Consultar valores distintos",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/query-distinct-values",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "fieldName": "city"
    }
}
bulk_insert_data_items_request = {
    "description": "Inserir vários itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/bulk/items/insert",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItems": [
            {
                "data": {
                    "state": "California",
                    "year": 2022,
                    "city": "Los Angeles",
                    "population": 3800000
                }
            },
            {
                "data": {
                    "state": "California",
                    "year": 2022,
                    "city": "San Francisco",
                    "population": 840000
                }
            }
        ],
        "returnEntity": True
    }
}
bulk_update_data_items_request = {
    "description": "Atualizar vários itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/bulk/items/update",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItems": [
            {
                "id": "40877d18-c5fe-4ed5-b495-d84bb4c027bd",
                "data": {
                    "state": "California",
                    "year": 2022,
                    "city": "Los Angeles",
                    "population": 3800000
                }
            },
            {
                "id": "6c38b4f7-7b8d-4702-9283-66a5889f8e17",
                "data": {
                    "state": "California",
                    "year": 2022,
                    "city": "San Francisco",
                    "population": 840000
                }
            }
        }
    }
}


bulk_save_data_items_request = {
    "description": "Salvar vários itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/bulk/items/save",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItems": [
            {
                "data": {
                    "state": "California",
                    "year": 2022,
                    "city": "Los Angeles",
                    "population": 3800000
                }
            },
            {
                "data": {
                    "state": "California",
                    "year": 2022,
                    "city": "San Francisco",
                    "population": 840000
                }
            }
        ]
    }
}

bulk_remove_data_items_request = {
    "description": "Remover vários itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/bulk/items/remove",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "cities",
        "dataItemIds": [
            "6d717171-6f4d-4794-b6ea-7aea0071a76b",
            "6c38b4f7-7b8d-4702-9283-66a5889f8e17"
        ]
    }
}

query_referenced_data_items_request = {
    "description": "Consultar itens de dados referenciados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/query-referenced",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "referringItemFieldName": "songs",
        "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
        "order": "ASC",
        "paging": {
            "limit": 1
        }
    }
}
is_referenced_data_items_request = {
    "description": "Verificar se um item de dados é referenciado",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/is-referenced",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "referringItemFieldName": "songs",
        "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
        "referencedItemId": "99cb26d5-dd42-4384-af30-3bb6e4026bd0"
    }
}
insert_data_item_reference_request = {
    "description": "Inserir referência de item de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/insert-reference",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "dataItemReference": {
            "referringItemFieldName": "songs",
            "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
            "referencedItemId": "aafeaaf4-6192-4cc2-a79b-97ce0f1b3646"
        }
    }
}
remove_data_item_reference_request = {
    "description": "Remover referência de item de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/remove-reference",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "dataItemReference": {
            "referringItemFieldName": "songs",
            "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
            "referencedItemId": "aafeaaf4-6192-4cc2-a79b-97ce0f1b3646"
        }
    }
}
bulk_insert_data_items_reference_request = {
    "description": "Inserir várias referências de itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/bulk/items/insert-references",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "dataItemReferences": [
            {
                "referringItemFieldName": "songs",
                "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
                "referencedItemId": "aafeaaf4-6192-4cc2-a79b-97ce0f1b3646"
            },
            {
                "referringItemFieldName": "songs",
                "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
                "referencedItemId": "e7fe3827-5102-470a-a10a-b6221dd0b4a9"
            }
        ]
    }
}
bulk_remove_data_items_reference_request = {
    "description": "Remover várias referências de itens de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/bulk/items/remove-references",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "dataItemReferences": [
            {
                "referringItemFieldName": "songs",
                "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
                "referencedItemId": "aafeaaf4-6192-4cc2-a79b-97ce0f1b3646"
            },
            {
                "referringItemFieldName": "songs",
                "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
                "referencedItemId": "e7fe3827-5102-470a-a10a-b6221dd0b4a9"
            }
        ]
    }
}
replace_data_item_reference_request = {
    "description": "Substituir referência de item de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/items/replace-references",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "albums",
        "referringItemFieldName": "songs",
        "referringItemId": "37de298e-026d-4b2e-b87f-fbec11d53105",
        "newReferencedItemIds": ["aafeaaf4-6192-4cc2-a79b-97ce0f1b3646"]
    }
}
update_data_collection_request = {
    "description": "Atualizar coleção de dados",
    "method": "PUT",
    "url": "https://www.wixapis.com/wix-data/v2/collections",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "id": "my-first-collection",
        "revision": "1",
        "displayName": "Author Collection",
        "fields": [
            {"key": "first_name", "displayName": "First Name", "type": "TEXT"},
            {"key": "last_name", "displayName": "Last Name", "type": "TEXT"}
        ],
        "permissions": {
            "insert": "ADMIN",
            "update": "ADMIN",
            "remove": "ADMIN",
            "read": "ANYONE"
        }
    }
}
list_data_collections_request = {
    "description": "Listar coleções de dados",
    "method": "GET",
    "url": "https://www.wixapis.com/wix-data/v2/collections?include_referenced_collections=true&sort.field=NAME&sort.direction=ASC",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
create_data_collection_request = {
    "description": "Criar coleção de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/collections",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "id": "my-favorite-artists",
        "displayName": "My Favorite Artists",
        "fields": [
            {
                "key": "name",
                "displayName": "Artist Name",
                "type": "TEXT"
            },
            {
                "key": "date_of_birth",
                "displayName": "Date of birth",
                "type": "DATE"
            },
            {
                "key": "songs_multi_ref",
                "displayName": "Songs",
                "type": "MULTI_REFERENCE",
                "typeMetadata": {
                    "multiReference": {
                        "referencedCollection": "songs-collection",
                        "referencingFieldKey": "my-favorite-artists",
                        "referencingDisplayName": "Performed by"
                    }
                }
            }
        ]
    }
}
get_data_collection_request = {
    "description": "Obter coleção de dados",
    "method": "GET",
    "url": "https://www.wixapis.com/wix-data/v2/collections/Stores/Products",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
delete_data_collection_request = {
    "description": "Excluir coleção de dados",
    "method": "DELETE",
    "url": "https://www.wixapis.com/wix-data/v2/collections/my-first-collection",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
list_indexes_request = {
    "description": "Listar índices de coleção de dados",
    "method": "GET",
    "url": "https://www.wixapis.com/wix-data/v2/indexes?collectionName=my-collection",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
create_index_request = {
    "description": "Criar índice de coleção de dados",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v2/indexes",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "my-collection",
        "index": {
            "name": "my-index",
            "fields": [
                {
                    "path": "my-field",
                    "order": "ASC"
                }
            ],
            "unique": False,
            "caseInsensitive": False
        }
    }
}
drop_index_request = {
    "description": "Excluir índice de coleção de dados",
    "method": "DELETE",
    "url": "https://www.wixapis.com/wix-data/v2/indexes",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "dataCollectionId": "my-collection",
        "indexName": "my-index"
    }
}
get_external_database_connection_request = {
    "description": "Obter conexão com banco de dados externo",
    "method": "GET",
    "url": "https://www.wixapis.com/wix-data/v1/external-database-connections/MyExternalDatabase",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
delete_external_database_connection_request = {
    "description": "Excluir conexão com banco de dados externo",
    "method": "DELETE",
    "url": "https://www.wixapis.com/wix-data/v1/external-database-connections/MyExternalDatabase",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    }
}
list_external_database_connections_request = {
    "description": "Listar conexões com bancos de dados externos",
    "method": "GET",
    "url": "https://www.wixapis.com/wix-data/v1/external-database-connections",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application.json"
    }
}
create_external_database_connection_request = {
    "description": "Criar conexão com banco de dados externo",
    "method": "POST",
    "url": "https://www.wixapis.com/wix-data/v1/external-database-connections",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "externalDatabaseConnection": {
            "name": "MyExternalDatabase",
            "endpoint": "https://example.com/my-external-database",
            "configuration": {
                "secretKey": "74dbd6d6-ec5b-4668-8229-c77379bc6431"
            }
        }
    }
}
update_external_database_connection_request = {
    "description": "Atualizar conexão com banco de dados externo",
    "method": "PUT",
    "url": "https://www.wixapis.com/wix-data/v1/external-database-connections/MyExternalDatabase",
    "headers": {
        "Authorization": "<AUTH>",
        "Content-Type": "application/json"
    },
    "data": {
        "externalDatabaseConnection": {
            "endpoint": "https://example.com/my-external-database",
            "configuration": {
                "secretKey": "74dbd6d6-ec5b-4668-8229-c77379bc6431"
            }
        }
    }
}






# Exemplo de como acessar os dados para inserir um item


