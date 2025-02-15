from enum import Enum


class Action(Enum):
    INCOME = 1 #Renda
    EXHELP = 2 #Ajuda Externa
    BUY3COINS = 3 #Duque
    KILLER = 4 #Assassino
    TOSTEAL = 5 #Capitao
    CHANGELETTERS = 6 #Embaixador
    SHOWLETTERS = 7
    CHALLENGE = 8
    BLOCKKILLER = 9 #Condensa
    BLOCKTOSTEAL = 10 #capitao e embaixador
    BLOCKEXHELP = 11 #Duque
    BLOCKBUY3COINS = 12 #Duque
 

    ...



PrimaryAction = [
    {'name':'INCOME'        , 'code': 1 },#Renda
    {'name':'EXHELP'        , 'code': 2 },#Ajuda Externa 
    {'name':'BUY3COINS'     , 'code': 3 },#Duque
    {'name':'KILLER'        , 'code': 4 },#Assassino -- Ação Contra Alguem
    {'name':'TOSTEAL'       , 'code': 5 },#Capitão   -- Ação Contra Alguem
    {'name':'CHANGELETTERS' , 'code': 6 } #Embaixador
    ]

ChallengedActions=[
    {'name':'SHOWLETTERS', 'code': 7 }
    ] 

EmbaixadorAction = [
    {'name':'PASS'      , 'code': 0},
    {'name':'CHALLENGE' , 'code': 8}
    ]

KillerAction = [
    {'name':'SHOWLETTERS' , 'code':7}, 
    {'name':'CHALLENGE '  , 'code':8},
    {'name':'BLOCKKILLER' , 'code':9} #Condensa
   ]

TOSTEALAction = [
    {'name':'pay2coins' , 'code':13}, 
    {'name':'CHALLENGE '  , 'code':8},
    {'name':'BLOCKTOSTEAL' , 'code':10} #capitao e embaixador
   ]

BlockDuqueAction = [
    {'name':'PASS'            , 'code':0},
    {'name':'CHALLENGE'       , 'code':8},
    {'name':'BLOCKEXHELP'     , 'code':11}, #Duque
    {'name':'BLOCKBUY3COINS'  , 'code':12} #Duque
]



