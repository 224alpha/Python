from itertools import product


def findPassword(chars, function, show=50, format_="%s"):
    """
    Essa função encontra e retorna uma senha e retorna o número de tentativas.
    
    Param chars: Dígitos que uma senha pode ter.
    
    Param function: Função que obrigatóriamente deve ter um parâmetro para
    receber um senha. Caso o retorna dessa função seja True, a senha tentada
    é considerada a correta.

    Param show: Mostra uma tentativa a cada X tentativas.

    Param format_: Formato em que a senha será impressa.
    """

    password = None
    attempts = 0
    size = 1
    stop = False

    while not stop:

        # Obtém todas as combinações possíveis com os dígitos do parâmetro "chars".
        for pw in product(chars, repeat=size):

            password = "".join(pw)

            # Imprime a senha que será tentada.
            if attempts % show == 0:
                print(format_ % password)

            # Verifica se a senha é a correta.
            if function(password):
                stop = True
                break
            else:
                attempts += 1
        size += 1

    return password, attempts


def getChars():
    """
    Método para obter uma lista contendo todas as
    letras do alfabeto e números.
    """
    chars = []

    # Acrescenta à lista todas as letras maiúsculas
    for id_ in range(ord("A"), ord("Z") + 1):
        chars.append(chr(id_))

    # Acrescenta à lista todas as letras minúsculas
    for id_ in range(ord("a"), ord("z") + 1):
        chars.append(chr(id_))

    # Acrescenta à lista todos os números
    for number in range(10):
        chars.append(str(number))

    return chars


# Se este módulo não for importado, o programa será testado.
# Para realizar o teste, o usuário deverá inserir uma senha para ser encontrada.

if __name__ == "__main__":

    import datetime
    import time

    # Pede ao usuário uma senha
    pw = input("\n Type a password: ")
    print("\n")


    def testFunction(password):
        """
        Função que será usada para fazer o teste.
        Podemos pensar nela por exemplo como uma função
        que tenta se conectar a um site utilizando a
        senha passada no parâmetro "password".
        """
        global pw
        if password == pw:
            return True
        else:
            return False


    # Obtém os dígitos que uma senha pode ter
    chars = getChars()

    t = time.process_time()

    # Obtém a senha encontrada e o múmero de tentativas
    password, attempts = findPassword(chars, testFunction, show=1000, format_=" Trying %s")

    t = datetime.timedelta(seconds=int(time.process_time() - t))
    input("\n\n Password found: {}\n Attempts: {}\n Time: {}\n".format(password, attempts, t))
