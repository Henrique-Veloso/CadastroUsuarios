from Biblioteca.Interface import*

def arquivoExiste(aqr):
    try:
        a=open(aqr, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(arq):
    try:
        a=open(arq, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')
    
def lerArquivo(arq):
    try:
        a=open(arq, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        linhas=a.readlines()
        if not linhas:
            print('Arquivo vazio! Nenhum usuário cadastrado.')
        else:
            for pessoa in linhas:
                dado = pessoa.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'Nome: {dado[0]:<20}Idade: {dado[1]} anos')

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a=open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao cadstrar os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')

def excluir(arq, nome='desconhecido'):
    try:
        a=open(arq, 'rt')
        linhas=a.readlines()
        a.close()
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        if not linhas:
            print('Arquivo vazio! Nenhum usuário cadastrado.')
            return
        else:
            novasLinhas=[linha for linha in linhas if linha.split(';')[0].strip()!=nome.strip()]
            if len(novasLinhas) ==len(linhas):
                print(f'Usuário {nome} não encontrado.')
                return
            else:
                a=open(arq, 'wt')
                a.writelines(novasLinhas)
                a.close()
                print(f'Usuário {nome} excluído com sucesso!')
