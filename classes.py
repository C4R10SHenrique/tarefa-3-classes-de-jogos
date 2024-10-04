name = input("Digite o nome da sua classe (Guerreiro,Arqueiro,Mago,Assasino): ").strip().lower()
#classificando classes
if name == "guerreiro":
    print ("Seu personagem serve para combates de curta distancia, e serve para aguentar muitos ataques.")
elif name == "Arqueiro":
    print ("Seu personagem serve para ataques de longa e media distancia. ")
elif name == "mago":
    print ("Seu personagem serve para ataques de media e longa distancia, e ele aprenta pouca quantidade de vida e precisa de mana para usar seus ataques.")
elif name == "assasino":
    print ("Seu personagem serve para ataques furtivos de longa e pouca distancia, e pode uasr uma adaga ou um arco.")           
else:
    print ("classe não reconhecida")