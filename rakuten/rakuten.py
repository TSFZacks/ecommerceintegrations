import requests

# Defina os parâmetros da solicitação
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
params = {
    "format": "json",
    "keyword": "楽天",  # Substitua pela palavra-chave desejada
    "genreId": 555086,  # Substitua pelo ID do gênero desejado
    "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
}

# Faça a solicitação GET para a API
response = requests.get(url, params=params)

# Verifique se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    data = response.json()  # Analise a resposta JSON
    # Agora você pode trabalhar com os dados retornados
    print(data)
else:
    print(f"Erro na solicitação: Código de status {response.status_code}")



# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?format=json&keyword=%E6%A5%BD%E5%A4%A9&genreId=555086&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar itens na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "keyword": "楽天",  # Substitua pela palavra-chave desejada
        "genreId": 555086,  # Substitua pelo ID do gênero desejado
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
    }
}
# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword=%E6%A5%BD%E5%A4%A9&genreId=555086&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar itens na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "keyword": "楽天",  # Substitua pela palavra-chave desejada
        "genreId": 555086,  # Substitua pelo ID do gênero desejado
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20140222?format=json&genreId=559887&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar gêneros na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "genreId": 559887,  # Substitua pelo ID do gênero desejado
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/IchibaTag/Search/20140222?format=json&tagId=1000317&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar tags na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "tagId": 1000317,  # Substitua pelo ID da tag desejada
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20220601?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Obter a classificação de itens na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Obter a classificação de itens na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu ID de aplicativo
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar produtos na API Rakuten Ichiba",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "keyword": "",  # Substitua pela palavra-chave desejada
        "genreId": "",  # Substitua pelo ID do gênero desejado
        "productId": ""  # Substitua pelo ID do produto desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404?format=json&keyword=%E6%9C%AC&booksGenreId=000&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar livros na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "keyword": "本",  # Substitua pela palavra-chave desejada
        "booksGenreId": "000",  # Substitua pelo ID do gênero de livros desejado
        "isbnjan": ""  # Substitua pelo ISBN ou JAN code se necessário
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&title=%E5%A4%AA%E9%99%BD&booksGenreId=001004008&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar livros específicos na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "太陽",  # Substitua pelo título do livro desejado
        "author": "",  # Substitua pelo nome do autor, se necessário
        "publisherName": "",  # Substitua pelo nome do editor, se necessário
        "size": 0,  # Substitua pelo tamanho do livro, se necessário
        "isbn": "",  # Substitua pelo ISBN do livro, se necessário
        "booksGenreId": "001004008"  # Substitua pelo ID do gênero de livros desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksCD/Search/20170404?format=json&artistName=%E3%82%AA%E3%83%BC%E3%83%AB%E3%82%B9%E3%82%BF%E3%83%BC&booksGenreId=002&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar CDs na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "",  # Substitua pelo título do CD desejado
        "artistName": "オールスター",  # Substitua pelo nome do artista
        "label": "",  # Substitua pelo nome da gravadora, se necessário
        "jan": "",  # Substitua pelo código JAN do CD, se necessário
        "booksGenreId": "002"  # Substitua pelo ID do gênero de CDs desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksDVD/Search/20170404?format=json&title=%E3%83%9D%E3%83%83%E3%82%BF%E3%83%BC&booksGenreId=003&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar DVDs/Blu-rays na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "ポッター",  # Substitua pelo título do DVD/Blu-ray desejado
        "artistName": "",  # Substitua pelo nome do artista/diretor, se necessário
        "label": "",  # Substitua pelo nome do estúdio, se necessário
        "jan": "",  # Substitua pelo código JAN do DVD/Blu-ray, se necessário
        "booksGenreId": "003"  # Substitua pelo ID do gênero de DVDs/Blu-rays desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksForeignBook/Search/20170404?format=json&title=Potter&booksGenreId=005407&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar livros estrangeiros na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "Potter",  # Substitua pelo título do livro estrangeiro desejado
        "author": "",  # Substitua pelo nome do autor, se necessário
        "publisherName": "",  # Substitua pelo nome do editor, se necessário
        "isbn": "",  # Substitua pelo ISBN do livro estrangeiro, se necessário
        "booksGenreId": "005407"  # Substitua pelo ID do gênero de livros estrangeiros desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksMagazine/Search/20170404?format=json&title=%E7%B5%8C%E6%B8%88&booksGenreId=007604001&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar revistas na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "経済",  # Substitua pelo título da revista desejada
        "author": "",  # Substitua pelo nome do autor, se necessário
        "publisherName": "",  # Substitua pelo nome da editora, se necessário
        "jan": "",  # Substitua pelo código JAN da revista, se necessário
        "booksGenreId": "007604001"  # Substitua pelo ID do gênero de revistas desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksGame/Search/20170404?format=json&title=%E3%83%A1%E3%82%BF%E3%83%AB&hardware=PS&booksGenreId=006&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar jogos de vídeo game na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "メタル",  # Substitua pelo título do jogo de vídeo game desejado
        "hardware": "PS",  # Substitua pela plataforma de hardware desejada (ex. PS, Xbox, etc.)
        "makerCode": "",  # Substitua pelo código do fabricante, se necessário
        "label": "",  # Substitua pelo nome do editor, se necessário
        "jan": "",  # Substitua pelo código JAN do jogo de vídeo game, se necessário
        "booksGenreId": "006"  # Substitua pelo ID do gênero de jogos de vídeo game desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksSoftware/Search/20170404?format=json&title=%E4%BC%9A%E8%A8%88&os=Win&booksGenreId=004&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar software de contabilidade na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "title": "会計",  # Substitua pelo título do software de contabilidade desejado
        "os": "Win",  # Substitua pelo sistema operacional desejado (ex. Win, Mac, etc.)
        "makerCode": "",  # Substitua pelo código do fabricante, se necessário
        "label": "",  # Substitua pelo nome do editor, se necessário
        "jan": "",  # Substitua pelo código JAN do software de contabilidade, se necessário
        "booksGenreId": "004"  # Substitua pelo ID do gênero de software desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/BooksGenre/Search/20121128?format=json&booksGenreId=000&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisar gênero de livros na API Rakuten Books",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu ID de aplicativo
        "booksGenreId": "000"  # Substitua pelo ID do gênero de livros desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/FavoriteBookmark/List/20170426?format=json",
    "Descrição": "Listar favoritos do marcador na API Rakuten Bookmark",
    "Parâmetros": {
        "format": "json",
        "access_token": "SEU_ACCESS_TOKEN_AQUI"  # Substitua pelo seu access token
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/FavoriteBookmark/Add/20120627?format=json",
    "Descrição": "Adicionar um item aos favoritos do marcador na API Rakuten Bookmark",
    "Parâmetros": {
        "format": "json",
        "access_token": "SEU_ACCESS_TOKEN_AQUI",  # Substitua pelo seu access token
        "itemCode": "CÓDIGO_DO_ITEM_AQUI"  # Substitua pelo código do item que você deseja adicionar aos favoritos
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/FavoriteBookmark/Delete/20120627?format=json",
    "Descrição": "Excluir um marcador favorito na API Rakuten Bookmark",
    "Parâmetros": {
        "format": "json",
        "access_token": "SEU_ACCESS_TOKEN_AQUI",  # Substitua pelo seu access token
        "bookmarkId": "ID_DO_MARCADOR_AQUI"  # Substitua pelo ID do marcador que deseja excluir
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Lista de categorias de receitas na API Rakuten Recipe",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Ranking de categorias de receitas na API Rakuten Recipe",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa simples de hotéis na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/HotelDetailSearch/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa detalhada de hotel na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/VacantHotelSearch/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de hotéis vagos na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID
        "checkinDate": "YYYY-MM-DD",  # Substitua com a data de check-in desejada
        "checkoutDate": "YYYY-MM-DD"  # Substitua com a data de check-out desejada
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/HotelRanking/20170426?format=json&genre=all&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Obter o ranking de hotéis na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/GetHotelChainList/20131024?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Obter a lista de cadeias de hotéis na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/GetAreaClass/20131024?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Obter informações de classes de área na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc"  # Substitua pelo seu próprio Application ID
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Travel/KeywordHotelSearch/20170426?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de hotéis com palavras-chave na API Rakuten Travel",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID,
        "keyword": "SEU_KEYWORD_AQUI"  # Substitua por suas palavras-chave
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Kobo/GenreSearch/20131010?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de gênero na API Rakuten Kobo",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID,
        "koboGenreId": "101"  # Substitua pelo gênero desejado
    }
}

# Dicionário com os dados do corpo da solicitação
request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Kobo/EbookSearch/20170426?format=json&keyword=%E6%9C%AC&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de eBooks na API Rakuten Kobo",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID,
        "keyword": "%E6%9C%AC",  # Substitua pelo seu próprio termo de pesquisa em UTF-8
        "title": "",  # Preencha com o título se desejar pesquisar por título
        "author": "",  # Preencha com o nome do autor se desejar pesquisar por autor
        "publisherName": "",  # Preencha com o nome da editora se desejar pesquisar por editora
        "itemNumber": "",  # Preencha com o número do item se desejar pesquisar por número do item
        "koboGenreId": "101"  # Substitua pelo gênero desejado
    }
}

request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Kobo/EbookSearch/20170426?format=json&keyword=%E6%9C%AC&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de eBooks na API Rakuten Kobo",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID
        "keyword": "%E6%9C%AC",  # Substitua pelo seu próprio termo de pesquisa em UTF-8
        "title": "",  # Preencha com o título se desejar pesquisar por título
        "author": "",  # Preencha com o nome do autor se desejar pesquisar por autor
        "publisherName": "",  # Preencha com o nome da editora se desejar pesquisar por editora
        "itemNumber": "",  # Preencha com o número do item se desejar pesquisar por número do item
        "koboGenreId": "101"  # Substitua pelo gênero desejado
    }
}

request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Kobo/EbookSearch/20170426?format=json&keyword=%E6%9C%AC&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de eBooks na API Rakuten Kobo",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID,
        "keyword": "%E6%9C%AC",  # Substitua pelo seu próprio termo de pesquisa em UTF-8
        "title": "",  # Preencha com o título se desejar pesquisar por título
        "author": " ",  # Preencha com o nome do autor se desejar pesquisar por autor
        "publisherName": "",  # Preencha com o nome da editora se desejar pesquisar por editora
        "itemNumber": "",  # Preencha com o número do item se desejar pesquisar por número do item
        "koboGenreId": "101"  # Substitua pelo gênero desejado
    }
}

request_data = {
    "URL": "https://app.rakuten.co.jp/services/api/Gora/GoraPlanSearch/20170623?format=json&applicationId=e06e2a5afcf14b52139c1fb6c58e9dbc",
    "Descrição": "Pesquisa de planos de golfe na API Rakuten Gora",
    "Parâmetros": {
        "format": "json",
        "applicationId": "e06e2a5afcf14b52139c1fb6c58e9dbc",  # Substitua pelo seu próprio Application ID
        "playDate": "YYYY-MM-DD"  # Substitua com a data de jogo no formato YYYY-MM-DD
    }
}


