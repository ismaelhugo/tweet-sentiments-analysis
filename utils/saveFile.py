def saveFile(tweets, nome_arquivo):
    try:
        # Verificar se o arquivo já existe e adicioná-los ao final
        with open(nome_arquivo, 'a') as arquivo:
            for tweet in tweets:
                arquivo.write(tweet + "\n \n")  # Adicionar cada tweet ao arquivo
        print("Tweets salvos com sucesso no arquivo.")
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo e salvar os tweets
        with open(nome_arquivo, 'w') as arquivo:
            for tweet in tweets:
                arquivo.write(tweet + "\n \n")  # Adicionar cada tweet ao arquivo
        print("Arquivo criado e tweets salvos com sucesso.")