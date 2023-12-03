def read_txt():
    # Abrimos o "Banco de dados" de maneira correta
    with open("words.txt", "r", encoding="utf-8") as arq:
        # Criamos uma lista com todas as palavras do txt, que é dividido por linhas
        words = arq.read().split()
        arq.close()
        return words

