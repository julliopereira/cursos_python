### ESCREVER FUNÇÃO CHAMADA describe_city() QUE RECEBA NOME DA CIDADE E PAÍS
### EXIBIR CIDADEX ESTÁ LOCALIZADO EM PAÍSX

def func_describe_city(cidade, pais='brasil'):
    print(cidade.title() + ' Está localizado em ' + pais.title())

func_describe_city('osasco')
func_describe_city('pindamonhangaba', 'brasil')
func_describe_city('paris', 'frança')