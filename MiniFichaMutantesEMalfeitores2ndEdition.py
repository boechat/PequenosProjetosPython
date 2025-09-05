class Character:
    def __init__(self,name,alt_id,power_level,strenght,dexterity,constitution, intelligence, wisdom, charism
    ,resistance, fortitude, reflex, willpower
    ,mod_str = None , mod_dex = None, mod_int = None, mod_wis = None, mod_char = None,
    pontos_poder = None, pontos_poder_inicial = None):
        self.name = name
        self.alt_id = alt_id
        self.power_level = power_level
        self.pontos_poder = self.power_level * 15
        self.pontos_poder_inicial = self.power_level * 15
        
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
        

    def __str__(self):
        msg = f'''
Nome Heroi: {self.alt_id}, Nome Civil: {self.name}, 
------------------------------------------------------------
Nivel de Poder : |{self.power_level}| Pontos Poder: |{self.pontos_poder_inicial}| Restantes: |{self.pontos_poder}|
------------------------------------------------------------
STR: {self.strenght} | DES: {self.dexterity} | CON: {self.constitution} | INT: {self.intelligence} | WIS: {self.wisdom} | CHA : {self.charism}
MOD: {self.mod_str}  | MOD: {self.mod_dex}  | MOD: {self.mod_con}  | MOD: {self.mod_int}  | MOD: {self.mod_int}| MOD: {self.mod_cha}| 

RESISTANCE: {self.resistance} | FORTITUDE: {self.fortitude} | REFLEX: {self.reflex} | WILL: {self.willpower}
------------------------------------------------------------
        '''
        return msg
    
    def calcula_mod(self):
        
        list_name = ['strenght','dexterity','constitution','intelligence','wisdom','charism']
        list_habilidades = [self.strenght, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charism]
        list_mod = []
        
        for v in list_habilidades:
            valor = (v - 10) // 2
            list_mod.append(valor)
            #print(list_mod)
        
        #dicionario_mod = {n: {"VALOR_HABILIDADE": v, "MODIFICADOR": m} for n, v, m in zip(list_name, list_habilidades, list_mod)}
        #print(dicionario_mod)

    
    def modificadores(self):
        pass
    
    def power_level_points_remaining(self):
        pontos_poder_nivel = self.power_level * 15
        self.pontos_poder = pontos_poder_nivel
        return pontos_poder_nivel
        
    def cria_ficha(self):
        pass
        
        
        
c1 = Character(name='Antonio',alt_id='Conselheiro',power_level = 10, strenght = 16, dexterity = 18, constitution =16,
intelligence = 8, wisdom = 18, charism = 18, resistance = 8, fortitude = 6, reflex = 10, willpower = 10)

#print(c1)
#print('PONTOS DE PODER: ',c1.power_level_points())
#print('-'*100)
print(c1)

#print(c1.calcula_mod())
