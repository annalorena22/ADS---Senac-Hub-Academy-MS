# Criar um sistema de classificação de animais vertebrados usando programação orientada a objetos (POO) em Python, 
# representando subdivisões até chegar a classes específicas como Ornitorrinco, Morcego e Baleia.

# Criação das Classes Principais:

# Inicie com a classe geral Animal que conterá características comuns a todos os animais (ex: nome científico).
# Crie subclasses que representem Vertebrados e, a partir daí, vá subdividindo em classes menores (por exemplo, Mamíferos, Répteis, etc.).
# Características Específicas:

# Cada classe deve conter atributos e métodos específicos de cada subdivisão. Por exemplo:
# Mamíferos: método amamentar().
# Aves: método voar().
# Chegue até as classes mais específicas: Ornitorrinco, Morcego e Baleia.
# Atributos e Métodos:

# Atributos como esqueleto, habitat e alimentacao devem ser herdados pelas subclasses.
# Métodos devem ser implementados para ações comuns (ex: seMovimentar()) e específicas (ex: botarOvo() para algumas classes). 

from Animal import *

cachorro = Animal("Cachorro", "Canis lupus familiaris", "Casa")
cachorro.seMovimentar()

gato = Vertebrados("Gato", "Felis silvestris catus", "Caixa de papelão")
gato.mostrarColuna()

papagaio = Aves("Papagaio", "Amazona", "Natureza")
papagaio.seMovimentar()
papagaio.mostrarColuna()
papagaio.voar()

cobra = Repteis("Cobra", "Serpentes", "Terra")
cobra.seMovimentar()
cobra.mostrarColuna()
cobra.botarOvo()

sapo = Anfibios("Sapo", "Anura", "Lagoa")
sapo.seMovimentar()
sapo.mostrarColuna()
sapo.pular()

tubarao = Peixes("Tubarão", "Selachimorpha", "Oceano")
tubarao.seMovimentar()
tubarao.mostrarColuna()
tubarao.nadar()

leao = Mamiferos("Leão", "Panthera leo", "Selva")
leao.seMovimentar()
leao.mostrarColuna()
leao.amamentar()

ornitorrinco = Ornitorrinco("Ornitorrinco", "Ornithorhynchus anatinus", "Austrália")
ornitorrinco.seMovimentar()
ornitorrinco.mostrarColuna()
ornitorrinco.amamentar()
ornitorrinco.botarOvo()

morcego = Morcego("Morcego", "Chiroptera", "Lugar Escuro")
morcego.seMovimentar()
morcego.mostrarColuna()
morcego.morderPescoco()

baleia = Baleia("Baleia", "Cetacea", "Oceano")
baleia.mostrarColuna()
baleia.seMovimentar()
baleia.nadar()
