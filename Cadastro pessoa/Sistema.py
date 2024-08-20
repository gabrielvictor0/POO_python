
from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():
    lista_pf = []
    while True:
        opcao = int(input("Escolha uma opção: 1 - Pessoa física / 2 - Pessoa juridica / 0 - Sair"))

        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar pessoa física / 2 - Listar pessoa física / 0 - Voltar ao menu anterior: "))

                if opcao_pf == 1:
                    novaPessoa = PessoaFisica()
                    novoEndereco = Endereco()
                    
                    novaPessoa.nome = input("Digite o nome da pessoa física: ")
                    novaPessoa.cpf = input("Digite o cpf: ")
                    novaPessoa.rendimento = float(input("Digite o rendimento (somente numeros): "))

                    data_nascimento = input("Digite a date de nascimento (dd/mm/aaaa): ")
                    novaPessoa.dataNascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                    idade = (date.today() - novaPessoa.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue
                    
                    novoEndereco.logradouro = input("Informe o logradouro: ")
                    novoEndereco.numero = input("Informe o numero: ")
                    enderecoComercial = input("Este endereço é comercial: S/N: ")
                    novoEndereco.endereco_Comercial = enderecoComercial.strip().upper() == 'S'
                    
                    novaPessoa.endereco = novoEndereco

                    lista_pf.append(novaPessoa)

                    print("Cadastro realizado com sucesso!!")
                elif opcao_pf == 2:
                    if lista_pf:
                        for pessoa in lista_pf:
                            print(pessoa.nome)
                            print(pessoa.cpf)
                            print(f"Endereço: {pessoa.endereco.logradouro}, {pessoa.endereco.numero}")
                            print(f"Imposto a ser pago: {pessoa.calcular_imposto(pessoa.rendimento)}")
                            print("Digite 0 para sair: ")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao == 0: 
                    print("Voltando ao menu interior")
                    break
                else: 
                    print("Opção inválida, por favor digite uma das opções inidicadas: ")
        elif opcao == 2: 
            pass
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema! Valeu!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()
                            


                    