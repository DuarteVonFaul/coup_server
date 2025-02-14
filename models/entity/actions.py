from enum import Enum


class Action(Enum):
    ...



class PrimaryAction(Action):
    INCOME = 1 #Renda
    EXHELP = 2 #Ajuda Externa
    BUY3COINS = 3 #Duque
    KILLER = 4 #Assassino
    TOSTEAL = 5 #Capitao
    CHANGELETTERS = 6 #Embaixador

class ChallengedActions(Action): #Apenas se ele for Desafiado
    SHOWLETTERS = 7 

class ThirdAction(Action):
    PASS = 0
    CHALLENGE = 8

class ProtectiveAction(Enum):
    PASS = 0
    CHALLENGE = 8
    BLOCKKILLER = 9 #Condensa
    BLOCKTOSTEAL = 10 #capitao e embaixador


class BlockAction(Action):
    PASS = 0
    CHALLENGE = 8
    BLOCKEXHELP = 11 #Duque
    BLOCKBUY3COINS = 12 #Duque
