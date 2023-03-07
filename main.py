import re, requests
from validate_docbr import CPF, CNPJ


def cpf_pattern():
    padrao_cpf = re.compile(r'[\d]{3}.?\d{3}.?\d{3}-?\d{2}')
    check_cpf = CPF()
    cpfs = '''
    123.456.789-00
    702.672.580-70
    10020030040
    260079340-20
    '''
    busca = padrao_cpf.findall(cpfs)
    for item in busca:
        if check_cpf.validate(item) is True:
            print(f'CPF válido: {item}')
        else:
            print(f'CPF não é válido: {item}')


def cnpj_pattern():
    padrao_cnpj = re.compile(r'\d{2}.\d{3}.\d{3}/\d{4}-\d{2}')
    check_cnpj = CNPJ()
    cnpjs = '''
    00.000.000/0001-91
    99111222000133
    10.200.300/4000-01
    46193013036415
    '''
    busca = padrao_cnpj.findall(cnpjs)
    for item in busca:
        if check_cnpj.validate(item) is True:
            print(f'CNPJ válido: {item}')
        else:
            print(f'CNPJ não é válido: {item}')


def date_pattern():
    padrao_data = re.compile("([0-2][1-9]|[1-3][0-1])(-|_)?([0][1-9]|[1][0-2])(-|_)?(20[\d]{2})")
                            # 0_____________________ 1____ 2_________________ 3___  4__________
    lista_data = [
        '21062088',
        '15-12-2087',
        '31_03_2000',
        '34-33-2019'
    ]

    for item in lista_data:
        busca = padrao_data.search(item)
        if busca is not None:
            fatias = busca.groups()
            print(fatias)
            data_formatada = f"{fatias[0]}/{fatias[2]}/{fatias[4]}"
            print(f'Data: {data_formatada}')
        else:
            print("Data não localizada!")


def cep_pattern():
    padrao_cep = re.compile('([\d]{5})(-)?([\d]{3})')
                            # 0______ 1__ 2___________
    lista_cep = [
        '01001-000'
        ,'CEP 04534001'
        ,'01316-060'
        ,'666'
    ]

    for item in lista_cep:
        busca = padrao_cep.search(item)
        if busca is not None:
            fatias = busca.groups()
            cep_formatado = f"{fatias[0]}-{fatias[2]}"
            print(f"CEP encontrado: {cep_formatado}")
            url = f"https://viacep.com.br/ws/{busca.group().replace('-', '')}/json"
            r = requests.get(url).json()
            print(f"CEP: {r['cep']}\nLogradouro: {r['logradouro']}\nComplemento: {r['complemento']}\n"\
            f"Bairro: {r['bairro']}\nCidade: {r['localidade']} / {r['uf']}\n\n")
        else:
            print(f"Texto\n{item}\nnão possui um CEP válido!")


def phone_pattern():
    padrao_telefone = re.compile(r"([+\d]{1,3})?(\([0-9]{2}\)|[0-9]{2})( )?([0-9]{4,5})(-)?([0-9]{4})")
                                  #0_________  1_____________________ 2__ 3__________ 4__ 5_________
    lista_telefone = [
        "meu telefone é (11) 3390-1234"
        # ,"Telefone: +5511983322233"
        # ,"Segue o número 1125603000"
        # ,"+55173344"
    ]

    for item in lista_telefone:
        # remoção de parênteses na string
        string_limpa = re.sub(r'[()]', '', item)
        busca = padrao_telefone.search(string_limpa)
        if busca is not None:
            fatias = busca.groups()
            print(fatias)
            print(busca.group())
            telefone_formatado = f"({fatias[1]}) {fatias[3]}-{fatias[5]}"
            print(f"Telefone encontrado: {telefone_formatado}\n")
        else:
            print("Telefone não localizado!")


def custom_pattern():
    padrao = re.compile(r"a[ra]*")
    # padrao = re.compile(r"\d")
    # padrao = re.compile(r".orte")
    # padrao = re.compile(r"^Olá")
    # padrao = re.compile(r"efetivado$")
    # padrao = re.compile(r".*ar")
    # padrao = re.compile(r"[a-m]")
    # padrao = re.compile(r'[a-zA-Z]')
    # padrao = re.compile(r"cas+a")
    # padrao = re.compile(r"18?º andar")
    # padrao = re.compile(r"10{3}")
    # padrao = re.compile(r"1º|18º andar")
    
    texto = """
    a
    arara
    arararararara
    """
    
    busca = padrao.finditer(texto)
    for item in busca:
        print(item)
        print(item.span())
        print(item.group())


if __name__ == '__main__':
    cpf_pattern()
    cnpj_pattern()
    date_pattern()
    cep_pattern()
    phone_pattern()
    custom_pattern()
