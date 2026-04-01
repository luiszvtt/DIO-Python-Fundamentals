#Validar dados do usuário

#Projeto fixando o aprendizado em condicionais, operadores lógicos, str(in, len) e funções




def ValidacaoCadastro():
    nome = input("Digite o seu nome(apenas o primeiro): ").strip().capitalize()
    if not nome :
        print("Preencha o seu nome corretamente.")
        return ValidacaoCadastro()

    idade = input("Digite sua idade: ")
    if not idade.isdigit() or int(idade) < 18:
        print("Você precisa ser maior de idade para realizar o cadastro.")
        return ValidacaoCadastro()
    idade = int(idade)
    
    email = input("Digite o seu e-mail: ")
    if "@" in email and ".com" in email:
        pass
    else:
        print("Preencha o seu email corretamente.")
        return ValidacaoCadastro()
    
    senha = input("Digite sua senha(de 8 a 12 caracteres): ").strip()
    if 8 <= len(senha) <= 12:
        print("Cadastro preenchido com sucesso!")
    else:
        print("Digite sua senha dentro do limite desejado.")       
        return ValidacaoCadastro()

ValidacaoCadastro()
        
        
            
        
            
        
            
        
