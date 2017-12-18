acao = str(input("Oi, Bom Dia!\nVocê que falar comigo?"))
if (acao=="sim"):
    print("Que bom! Entao vamos conversar!")
    nome=str(input("Qual seu nome?"))
    print ("Nome legal! O meu é Saori! Prazer em conhecê-lo", nome)
    print ("Então, ")
    assunto=str(input("sobre o que você quer conversar?"))
    if (assunto=="cinema"):
        print ("Show! Você assistiu Mulher Maravilha?")
    elif (assunto=="que tal política?"):
        print ("Não gosto de política!\nDe política, só sei que vão prender um tal de Lula kkkkkkkk")
        reposta=str(input(""))
elif (acao=="não"):
    print ("Que pena! Então, xau!")