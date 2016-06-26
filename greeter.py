#function that takes in a person name and prints 3 line long greeting
def greet(nome):
    print("Hey, " +  nome)
    print("How are you, ? " + nome.title())
    print("do not know:  " +  nome.title())
nomi = ["Name1", "Name2", "Name3"]
for nome in nomi:
    greet(nome)
