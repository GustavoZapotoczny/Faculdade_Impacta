# ATIVIDADE CONTÍNUA 03

# NOMES DOS ALUNOS (máximo 6 alunos)
# ALUNO 1: Aléxia Vitória Melhado Pereira           RA:2101221
# ALUNO 2: Gustavo Zapotoczny Leite de Ciqueira     RA:2101260
# ALUNO 3: Jaques Braz Bitencourt                   RA:2101231
# ALUNO 4: Henrique Yda Yamamoto                    RA:2101786
# ALUNO 5: Guilherme Sousa Domingues                RA:2100071


class SuperPoder:
    def __init__(self, nome, categoria):
        self.__nome = nome
        self.__categoria = categoria

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria


class Personagem:
    def __init__(self, nome, nome_vida_real):
        self.__nome = nome
        self.__nome_vida_real = nome_vida_real
        self.__poderes = []

    def adicionar_super_poder(self, superpoder):
        if len(self.__poderes) < 4:
            self.__poderes.append(superpoder)
        else:
            raise ValueError

    def get_poder_total(self):
        acm_poderes = 0
        for poder in self.__poderes:
            acm_poderes += poder.get_categoria()
        return acm_poderes


class SuperHeroi(Personagem):
    def get_poder_total(self):
        acm = super().get_poder_total() * 1.1
        return acm


class Vilao(Personagem):
    def __init__(self, nome, nome_vida_real, tempo_de_prisao):
        super().__init__(nome, nome_vida_real)
        self.tempo_de_prisao = tempo_de_prisao


class Confronto:
    def lutar(self, superheroi, vilao):
        if superheroi.get_poder_total() > vilao.get_poder_total():
            return 1
        elif superheroi.get_poder_total() < vilao.get_poder_total():
            return 2
        else:
            return 0
