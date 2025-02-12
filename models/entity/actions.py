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
    SHOWLETTERS = 1 

class ThirdAction(Action):
    PASS = 0
    CHALLENGE = 1

class ProtectiveAction(Action):
    PASS = 0
    CHALLENGE = 1
    BLOCKKILLER = 2 #Condensa
    BLOCKTOSTEAL = 3 #capitao e embaixador


class BlockAction(Action):
    PASS = 0
    CHALLENGE = 1
    BLOCKEXHELP = 2 #Duque
    BLOCKBUY3COINS = 3 #Duque