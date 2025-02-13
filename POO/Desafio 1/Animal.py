class Animal:
    def __init__(self, nome):
        self.nome = nome

    def descricao(self):
        return f"________________________________________________________________________________________________________________________________\n Nome: {self.nome}\n"

class Reino(Animal):
    def __init__(self, nome, reino_animalia):
        super().__init__(nome)
        self.reino_animalia = reino_animalia

    def descricao(self):
        info = super().descricao()
        if self.reino_animalia == "Animalia":
            info+= "________________________________________________________________________________________________________________________________\n"
            info += "Reino: Animalia\n"
            info += "O reino da diversidade! Composto por seres multicelulares (exceto por algumas exceções como os protozoários unicelulares), eucariontes e heterotróficos, animais que não produzem seu próprio alimento (obtenção de nutrientes por ingestão). É dividido em dois grupos principais: vertebrados, seres vivos que possuem vértebras, coluna dorsal e crânio, e seres invertebrados, que não possuem vértebras, que são os animais também pluricelulares, mas que não possuem parede celular.\n"
        return info
    
class Filo(Reino):
    def __init__(self, nome, reino_animalia, filo):
        super().__init__(nome, reino_animalia)
        self.filo = filo

    def descricao(self):
        info = super().descricao()
        if self.filo == 'Chordata':
            info += "Filo: Chordata\n"
            info += "Animais com notocorda (estrutura de suporte dorsal), tubo nervoso dorsal, fendas faringianas em algum estágio de desenvolvimento e cauda pós-anal.\n"
        elif self.filo == 'Arthropoda':
            info += "Filo: Arthropoda\n"
            info += "Animais com exoesqueleto quitinoso, segmentação do corpo e apêndices articulados. São o grupo mais diversificado de animais.\n"
        elif self.filo == 'Mollusca':
            info += "Filo: Mollusca\n"
            info += "Animais geralmente com corpo mole, muitas vezes protegido por uma concha calcária. Podem ter cabeça bem definida e pé muscular.\n"
        elif self.filo == 'Echinodermata':
            info += "Filo: Echinodermata\n"
            info += "Animais com simetria radial secundária, endoesqueleto calcário, sistema vascular aquático (sistema ambulacrário).\n"
        elif self.filo == 'Amphibia':
            info += "Filo: Amphibia\n"
            info += "Animais geralmente com pele úmida e permeável, ovos sem casca e fase larval aquática. Podem ter respiração cutânea.\n"
        elif self.filo == 'Cnidaria':
            info += "Filo: Cnidaria\n"
            info += "Animais aquáticos com corpo em forma de pólipo ou medusa, possuem células urticantes (cnidócitos).\n"
        return info

class Classe(Filo):
    def __init__(self, nome, reino_animalia, filo, classe):
        super().__init__(nome, reino_animalia, filo)
        self.classe = classe

    def descricao(self):
        info = super().descricao()
        if self.classe == 'Mammalia':
            info += "Classe: Mammalia\n"
            info += "Animais vertebrados de sangue quente, possuem glândulas mamárias e geralmente pelos.\n"
        elif self.classe == 'Aves':
            info += "Classe: Aves\n"
            info += "Animais vertebrados de sangue quente, possuem penas, bico sem dentes e geralmente são capazes de voar.\n"
        elif self.classe == 'Reptilia':
            info += "Classe: Reptilia\n"
            info += "Animais vertebrados de sangue frio, possuem pele seca com escamas e geralmente põem ovos com casca.\n"
        elif self.classe == 'Amphibia':
            info += "Classe: Amphibia\n"
            info += "Animais vertebrados que vivem em ambientes aquáticos e terrestres, possuem pele permeável e geralmente passam por metamorfose.\n"
        elif self.classe == 'Pisces':
            info += "Classe: Pisces\n"
            info += "Animais vertebrados aquáticos, possuem nadadeiras e brânquias para respiração.\n"
        elif self.classe == 'Insecta':
            info += "Classe: Insecta\n"
            info += "Animais invertebrados com corpo segmentado em cabeça, tórax e abdômen, possuem três pares de pernas e geralmente asas.\n"
        return info

class Ordem(Classe):
    def __init__(self, nome, reino_animalia, filo, classe, ordem):
        super().__init__(nome, reino_animalia, filo, classe)
        self.ordem = ordem

    def descricao(self):
        info = super().descricao()
        if self.ordem == 'Carnivora':
            info += "Ordem: Carnivora\n"
            info += "Mamíferos com dentes adaptados para cortar carne, muitos são predadores, incluindo leões, tigres e cães.\n"
        elif self.ordem == 'Primates':
            info += "Ordem: Primates\n"
            info += "Mamíferos com cérebros grandes, visão binocular e geralmente mãos com polegares oponíveis, incluindo humanos e macacos.\n"
        elif self.ordem == 'Cetacea':
            info += "Ordem: Cetacea\n"
            info += "Mamíferos aquáticos totalmente adaptados à vida na água, incluindo baleias e golfinhos.\n"
        elif self.ordem == 'Chiroptera':
            info += "Ordem: Chiroptera\n"
            info += "Mamíferos voadores, conhecidos como morcegos, com asas formadas por uma membrana de pele esticada entre os dedos.\n"
        elif self.ordem == 'Artiodactyla':
            info += "Ordem: Artiodactyla\n"
            info += "Mamíferos ungulados com número par de dedos nas patas, incluindo camelos, girafas e porcos.\n"
        elif self.ordem == 'Perissodactyla':
            info += "Ordem: Perissodactyla\n"
            info += "Mamíferos ungulados com número ímpar de dedos nas patas, incluindo cavalos, rinocerontes e zebras.\n"
        elif self.ordem == 'Monotremata':
            info += "Ordem: Monotremata\n"
            info += "Mamíferos ovíparos que põem ovos, incluindo o ornitorrinco e a equidna.\n"
        elif self.ordem == 'Diprotodontia':
            info += "Ordem: Diprotodontia\n"
            info += "Mamíferos marsupiais, incluindo cangurus, coalas e wombats, que possuem dois grandes dentes incisivos na mandíbula inferior.\n"
        elif self.ordem == 'Testudines':
            info += "Ordem: Testudines\n"
            info += "Répteis com corpos cobertos por uma carapaça, incluindo tartarugas e cágados.\n"
        elif self.ordem == 'Squamata':
            info += "Ordem: Squamata\n"
            info += "Répteis com escamas, incluindo lagartos e cobras, caracterizados por crânios cinéticos.\n"
        return info

class Familia(Ordem):
    def __init__(self, nome, reino_animalia, filo, classe, ordem, familia):
        super().__init__(nome, reino_animalia, filo, classe, ordem)
        self.familia = familia

    def descricao(self):
        info = super().descricao()
        if self.familia == 'Felidae':
            info += "Família: Felidae\n"
            info += "Mamíferos carnívoros conhecidos como felinos, incluindo gatos, leões e tigres.\n"
        elif self.familia == 'Canidae':
            info += "Família: Canidae\n"
            info += "Mamíferos carnívoros conhecidos como canídeos, incluindo cães, lobos e raposas.\n"
        elif self.familia == 'Elephantidae':
            info += "Família: Elephantidae\n"
            info += "Mamíferos herbívoros conhecidos como elefantes, com corpos grandes e trombas longas.\n"
        elif self.familia == 'Giraffidae':
            info += "Família: Giraffidae\n"
            info += "Mamíferos herbívoros conhecidos como girafas, com pescoços longos e corpos altos.\n"
        elif self.familia == 'Equidae':
            info += "Família: Equidae\n"
            info += "Mamíferos herbívoros conhecidos como equídeos, incluindo cavalos, zebras e asnos.\n"
        elif self.familia == 'Ursidae':
            info += "Família: Ursidae\n"
            info += "Mamíferos carnívoros conhecidos como ursos, com corpos grandes e pelagem densa.\n"
        elif self.familia == 'Phascolarctidae':
            info += "Família: Phascolarctidae\n"
            info += "Mamíferos herbívoros conhecidos como coalas, que vivem em árvores e se alimentam de folhas de eucalipto.\n"
        elif self.familia == 'Macropodidae':
            info += "Família: Macropodidae\n"
            info += "Mamíferos herbívoros conhecidos como cangurus, com patas traseiras grandes e caudas fortes.\n"
        elif self.familia == 'Ornithorhynchidae':
            info += "Família: Ornithorhynchidae\n"
            info += "Mamíferos monotremados conhecidos como ornitorrincos, com bicos de pato e hábitos aquáticos.\n"
        elif self.familia == 'Tachyglossidae':
            info += "Família: Tachyglossidae\n"
            info += "Mamíferos monotremados conhecidos como equidnas, com espinhos no corpo e hábitos escavadores.\n"
        elif self.familia == 'Delphinidae':
            info += "Família: Delphinidae\n"
            info += "Mamíferos marinhos conhecidos como golfinhos, com corpos hidrodinâmicos e inteligência avançada.\n"
        elif self.familia == 'Balaenopteridae':
            info += "Família: Balaenopteridae\n"
            info += "Mamíferos marinhos conhecidos como baleias, com corpos grandes e barbatanas para filtração de alimento.\n"
        elif self.familia == 'Vespertilionidae':
            info += "Família: Vespertilionidae\n"
            info += "Mamíferos voadores conhecidos como morcegos vespertilionídeos, com hábitos noturnos e alimentação variada.\n"
        elif self.familia == 'Rhinocerotidae':
            info += "Família: Rhinocerotidae\n"
            info += "Mamíferos herbívoros conhecidos como rinocerontes, com pele grossa e chifres no focinho.\n"
        elif self.familia == 'Hippopotamidae':
            info += "Família: Hippopotamidae\n"
            info += "Mamíferos herbívoros conhecidos como hipopótamos, com corpos robustos e hábitos aquáticos.\n"
        elif self.familia == 'Cheloniidae':
            info += "Família: Cheloniidae\n"
            info += "Répteis marinhos conhecidos como tartarugas marinhas, com corpos protegidos por carapaças ósseas.\n"
        elif self.familia == 'Elapidae':
            info += "Família: Elapidae\n"
            info += "Répteis venenosos conhecidos como elapídeos, incluindo cobras como a naja e a mamba.\n"
        return info

class Genero(Familia):
    def __init__(self, nome, reino_animalia, filo, classe, ordem, familia, genero):
        super().__init__(nome, reino_animalia, filo, classe, ordem, familia)
        self.genero = genero

    def descricao(self):
        info = super().descricao()
        if self.genero == 'Canis':
            info += "Gênero: Canis\n"
            info += "Gênero que inclui várias espécies de canídeos, como os cães domésticos e lobos.\n"
        elif self.genero == 'Felis':
            info += "Gênero: Felis\n"
            info += "Gênero que inclui várias espécies de felinos, como os gatos domésticos e leopardos.\n"
        elif self.genero == 'Panthera':
            info += "Gênero: Panthera\n"
            info += "Gênero que inclui várias espécies de grandes felinos, como leões, tigres e leopardos.\n"
        elif self.genero == 'Loxodonta':
            info += "Gênero: Loxodonta\n"
            info += "Gênero que inclui elefantes africanos, mamíferos herbívoros de grande porte.\n"
        elif self.genero == 'Giraffa':
            info += "Gênero: Giraffa\n"
            info += "Gênero que inclui girafas, mamíferos herbívoros com pescoço longo.\n"
        elif self.genero == 'Equus':
            info += "Gênero: Equus\n"
            info += "Gênero que inclui cavalos, zebras e asnos, mamíferos herbívoros adaptados para correr.\n"
        elif self.genero == 'Ursus':
            info += "Gênero: Ursus\n"
            info += "Gênero que inclui vários tipos de ursos, mamíferos carnívoros de grande porte.\n"
        elif self.genero == 'Vulpes':
            info += "Gênero: Vulpes\n"
            info += "Gênero que inclui raposas, mamíferos carnívoros adaptados para caçar pequenos animais.\n"
        elif self.genero == 'Macropus':
            info += "Gênero: Macropus\n"
            info += "Gênero que inclui cangurus, mamíferos marsupiais adaptados para pular.\n"
        elif self.genero == 'Phascolarctos':
            info += "Gênero: Phascolarctos\n"
            info += "Gênero que inclui coalas, mamíferos herbívoros arbóreos com hábitos noturnos.\n"
        elif self.genero == 'Ornithorhynchus':
            info += "Gênero: Ornithorhynchus\n"
            info += "Gênero que inclui ornitorrincos, mamíferos monotremados com bico de pato.\n"
        elif self.genero == 'Tachyglossus':
            info += "Gênero: Tachyglossus\n"
            info += "Gênero que inclui equidnas, mamíferos monotremados com espinhos no corpo.\n"
        elif self.genero == 'Delphinus':
            info += "Gênero: Delphinus\n"
            info += "Gênero que inclui golfinhos, mamíferos marinhos com corpo hidrodinâmico.\n"
        elif self.genero == 'Balaenoptera':
            info += "Gênero: Balaenoptera\n"
            info += "Gênero que inclui baleias, mamíferos marinhos de grande porte com barbatanas para filtração de alimento.\n"
        elif self.genero == 'Myotis':
            info += "Gênero: Myotis\n"
            info += "Gênero que inclui morcegos vespertilionídeos, mamíferos voadores com hábitos noturnos.\n"
        elif self.genero == 'Rhinoceros':
            info += "Gênero: Rhinoceros\n"
            info += "Gênero que inclui rinocerontes, mamíferos herbívoros com pele grossa e chifres.\n"
        elif self.genero == 'Hippopotamus':
            info += "Gênero: Hippopotamus\n"
            info += "Gênero que inclui hipopótamos, mamíferos herbívoros com corpos robustos e hábitos aquáticos.\n"
        elif self.genero == 'Chelonia':
            info += "Gênero: Chelonia\n"
            info += "Gênero que inclui tartarugas marinhas, répteis marinhos com corpos protegidos por carapaças ósseas.\n"
        elif self.genero == 'Naja':
            info += "Gênero: Naja\n"
            info += "Gênero que inclui cobras elapídeas, répteis venenosos com presas fixas e veneno neurotóxico.\n"
        return info

class Especie(Genero):
    def __init__(self, nome, reino_animalia, filo, classe, ordem, familia, genero, especie):
        super().__init__(nome, reino_animalia, filo, classe, ordem, familia, genero)
        self.especie = especie

    def descricao(self):
        info = super().descricao()
        if self.especie == 'Canis lupus':
            info += "Espécie: Canis lupus\n"
            info += "Espécie que inclui lobos, carnívoros sociais que vivem em matilhas.\n"
        elif self.especie == 'Canis familiaris':
            info += "Espécie: Canis familiaris\n"
            info += "Espécie que inclui cães domésticos, domesticados há milhares de anos como animais de companhia.\n"
        elif self.especie == 'Felis catus':
            info += "Espécie: Felis catus\n"
            info += "Espécie que inclui gatos domésticos, pequenos felinos independentes e caçadores.\n"
        elif self.especie == 'Panthera leo':
            info += "Espécie: Panthera leo\n"
            info += "Espécie que inclui leões, grandes felinos sociais que vivem em grupos chamados de 'coalizões'.\n"
        elif self.especie == 'Loxodonta africana':
            info += "Espécie: Loxodonta africana\n"
            info += "Espécie que inclui elefantes africanos, os maiores mamíferos terrestres, conhecidos por suas presas enormes e orelhas grandes.\n"
        elif self.especie == 'Giraffa camelopardalis':
            info += "Espécie: Giraffa camelopardalis\n"
            info += "Espécie que inclui girafas, mamíferos herbívoros com pescoço longo adaptados para alcançar folhas em árvores altas.\n"
        elif self.especie == 'Equus ferus':
            info += "Espécie: Equus ferus\n"
            info += "Espécie que inclui cavalos, zebras e asnos, mamíferos herbívoros adaptados para correr em grandes áreas abertas.\n"
        elif self.especie == 'Ursus arctos':
            info += "Espécie: Ursus arctos\n"
            info += "Espécie que inclui ursos pardos, mamíferos robustos e poderosos que vivem em habitats variados.\n"
        elif self.especie == 'Vulpes vulpes':
            info += "Espécie: Vulpes vulpes\n"
            info += "Espécie que inclui raposas vermelhas, mamíferos carnívoros adaptados para caçar pequenos animais e sobreviver em diferentes ambientes.\n"
        elif self.especie == 'Macropus giganteus':
            info += "Espécie: Macropus giganteus\n"
            info += "Espécie que inclui cangurus gigantes, mamíferos marsupiais com fortes patas traseiras para saltar longas distâncias.\n"
        elif self.especie == 'Phascolarctos cinereus':
            info += "Espécie: Phascolarctos cinereus\n"
            info += "Espécie que inclui coalas, marsupiais arborícolas que se alimentam principalmente de folhas de eucalipto.\n"
        elif self.especie == 'Ornithorhynchus anatinus':
            info += "Espécie: Ornithorhynchus anatinus\n"
            info += "Espécie que inclui ornitorrincos, mamíferos monotremados únicos com bico de pato e capacidade de botar ovos.\n"
        elif self.especie == 'Tachyglossus aculeatus':
            info += "Espécie: Tachyglossus aculeatus\n"
            info += "Espécie que inclui equidnas, monotremados com espinhos no corpo e língua pegajosa para capturar insetos.\n"
        elif self.especie == 'Delphinus delphis':
            info += "Espécie: Delphinus delphis\n"
            info += "Espécie que inclui golfinhos comuns, mamíferos marinhos altamente inteligentes que vivem em grupos sociais chamados 'pods'.\n"
        elif self.especie == 'Balaenoptera physalus':
            info += "Espécie: Balaenoptera physalus\n"
            info += "Espécie que inclui a baleia-fin, mamífero marinho gigante que se alimenta de krill e pequenos peixes através de filtração.\n"
        elif self.especie == 'Myotis lucifugus':
            info += "Espécie: Myotis lucifugus\n"
            info += "Espécie que inclui morcegos marrom pequenos, mamíferos voadores que desempenham um papel vital no controle de insetos noturnos.\n"
        elif self.especie == 'Rhinoceros unicornis':
            info += "Espécie: Rhinoceros unicornis\n"
            info += "Espécie que inclui o rinoceronte indiano, mamífero herbívoro com um único chifre e pele grossa para defesa.\n"
        elif self.especie == 'Hippopotamus amphibius':
            info += "Espécie: Hippopotamus amphibius\n"
            info += "Espécie que inclui o hipopótamo comum, mamífero herbívoro semi-aquático com pele espessa e hábitos principalmente aquáticos.\n"
        elif self.especie == 'Chelonia mydas':
            info += "Espécie: Chelonia mydas\n"
            info += "Espécie que inclui a tartaruga-verde, réptil marinho que se alimenta de plantas e é encontrada em oceanos tropicais.\n"
        elif self.especie == 'Naja naja':
            info += "Espécie: Naja naja\n"
            info += "Espécie que inclui a cobra-naja indiana, réptil venenoso conhecido por seu capuz expandido e veneno neurotóxico.\n"
        return info 