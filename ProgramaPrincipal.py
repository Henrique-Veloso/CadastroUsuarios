from Biblioteca.Interface import*
from Biblioteca.Arquivo import*
from time import sleep

arq = 'BancoDeDados.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Usuários Cadastrados', 'Cadastrar Usuário', 'Excluir Usuário', 'Sair do Sistema'])
    if resposta==1:
        lerArquivo(arq)
    elif resposta==2:
        cabeçalho('NOVO CADASTRO')
        nome=leiaStr('Nome: ').capitalize()
        idade=leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta==3:
        nomeDel=leiaStr('Nome: ').capitalize()
        excluir(arq, nomeDel)
    elif  resposta==4:
        cabeçalho('Saindo do Sistema... Até Logo!')
        break
    else:
        print('\033[31mERRO! Por favor digite uma opção válida.\033[m')
    sleep(1)
