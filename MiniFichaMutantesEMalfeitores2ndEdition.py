class Character:
    def __init__(self,name,alt_id,power_level,strenght,dexterity,constitution, intelligence, wisdom, charism
    ,resistance, fortitude, reflex, willpower
    ,mod_str = None , mod_dex = None, mod_int = None, mod_wis = None, mod_char = None,
    altura = None, tamanho = None, peso = None,
    pontos_poder = None, pontos_poder_inicial = None):
        self.name = name
        self.alt_id = alt_id
        self.power_level = power_level
        self.pontos_poder = self.power_level * 15
        self.pontos_poder_inicial = self.power_level * 15
        
        self.altura = altura
        self.tamanho = tamanho
        
        self.strenght = strenght
        self.mod_str = (self.strenght - 10) //2
        
        self.dexterity = dexterity
        self.mod_dex = (self.dexterity - 10) //2

        self.constitution = constitution
        self.mod_con = (self.constitution - 10) //2

        self.intelligence = intelligence
        self.mod_int = (self.intelligence - 10) //2

        self.wisdom = wisdom
        self.mod_wis = (self.wisdom- 10) //2

        self.charism = charism
        self.mod_cha = (self.charism - 10) //2

        self.resistance = resistance
        self.fortitude = fortitude
        self.reflex = reflex
        self.willpower = willpower

    
    def calcula_tamanho(self):
        verifica_alt = self.altura 
        verifica_peso = self.peso
        if (verifica_alt > 0 and verifica_alt <= 0.075) or (verifica_peso > 0 and verifica_peso <= 0.03):
            self.tamanho = 'MINUSCULO'
            mod_atk_tam = 12
            mod_def_tam = 12
            mod_gra_tam = -20
            mod_ste_tam = 20
            mod_itm_tam = -10
            space = 0.0075
            range_alcance = 0
            cap_carga = cap_carga * (1.0/16.0)
            custo = 20
            
        elif verifica_alt > 0.075 and verifica_alt <= 0.15:
            self.tamanho = 'INFIMO'
            mod_atk_tam = 8
            mod_def_tam = 8
            mod_gra_tam = -16
            mod_ste_tam = 16
            mod_itm_tam = -8
            space = 0.015
            range_alcance = 0
            cap_carga = cap_carga * (1.0/8.0)
            custo = 16
            
        elif verifica_alt >0.15 and verifica_alt <=0.3:
            self.tamanho = 'DIMINUTO'
            mod_atk_tam = 12
            mod_def_tam = 12
            mod_gra_tam = -20
            mod_ste_tam = 20
            mod_itm_tam = -10
            space = 0.75
            range_alcance = 0
            cap_carga = cap_carga * (1.0/12.0)
            custo = 12       
        
        elif verifica_alt > 0.3 and verifica_alt <= 0.6:
            self.tamanho = 'MINIMO'
        elif verifica_alt >0.6 and verifica_alt <= 1.2:
            self.tamanho = 'PEQUENO'
        elif verifica_alt >1.2 and verifica_alt <= 2.4:
            self.tamanho = 'MEDIO'
        elif verifica_alt > 2.4 and verifica_alt <= 4.8:
            self.tamanho= 'GRANDE'
        elif verifica_alt >4.8 and verifica_alt <= 9.6:
            self.tamanho = 'ENORME'
        elif verifica_alt > 9.6 and verifica_alt <= 19.2:
            self.tamanho = 'DESCOMUNAL'
        elif verifica_alt >19.2 and verifica_alt <= 38.4:
            self.tamanho = 'COLOSSAL'
        elif verifica_alt > 38.4:
            self.tamanho = 'INCRIVEL'
        else:
            print('TAMANHO INVALIDO')
    
    def power_level_points_remaining(self):
        pontos_poder_nivel = self.power_level * 15
        self.pontos_poder = pontos_poder_nivel
        return pontos_poder_nivel
        
    def cria_ficha(self):
        pass
        
    def __str__(self):
        # CHAMA CALCULA TAMANHO #
        Character.calcula_tamanho(self),
        ####
        
        msg = f'''
Nome Heroi: {self.alt_id}, Nome Civil: {self.name}, 
Altura: {self.altura} | Tamanho: {self.tamanho}
------------------------------------------------------------
Nivel de Poder : |{self.power_level}| Pontos Poder: |{self.pontos_poder_inicial}| Restantes: |{self.pontos_poder}|
------------------------------------------------------------
STR: {self.strenght} | DES: {self.dexterity} | CON: {self.constitution} | INT: {self.intelligence} | WIS: {self.wisdom} | CHA : {self.charism}
MOD: {self.mod_str}  | MOD: {self.mod_dex}  | MOD: {self.mod_con}  | MOD: {self.mod_int}  | MOD: {self.mod_int}| MOD: {self.mod_cha}| 

RESISTANCE: {self.resistance} | FORTITUDE: {self.fortitude} | REFLEX: {self.reflex} | WILL: {self.willpower}
------------------------------------------------------------
        '''
        return msg        
        
c1 = Character(name='Antonio',alt_id='Conselheiro',power_level = 10, strenght = 16, dexterity = 18, constitution =16,
intelligence = 8, wisdom = 18, charism = 18, resistance = 8, fortitude = 6, reflex = 10, willpower = 10, altura = 1.78)


c2 = Character(name='Evil Li',alt_id='Destruidor',power_level = 10, strenght = 18, dexterity = 14, constitution =12,
intelligence = 14, wisdom = 20, charism = 18, resistance = 10, fortitude = 10, reflex = 10, willpower = 12, altura = 6.54)

#print(c1)
#print('PONTOS DE PODER: ',c1.power_level_points())
#print('-'*100)
print(c1)
print('\n')
print(c2)
#print(c1.calcula_mod())

print('\n')
print('------------------------ BATALHA ----------------------------')
