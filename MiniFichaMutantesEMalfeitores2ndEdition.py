class Character:
    def __init__(self,name,alt_id,power_level,strenght,dexterity,constitution, intelligence, wisdom, charism
    ,resistance, fortitude, reflex, willpower
    ,mod_str = None , mod_dex = None, mod_int = None, mod_wis = None, mod_char = None,
    altura = None, tamanho = None, peso = 0, cap_carga = 0,
    pontos_poder = None, pontos_poder_inicial = None):
        self.name = name
        self.alt_id = alt_id
        self.power_level = power_level
        self.pontos_poder = self.power_level * 15
        self.pontos_poder_inicial = self.power_level * 15
        
        self.altura = altura
        self.tamanho = tamanho
        self.peso = peso
        self.cap_carga = cap_carga
        
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


    def capacidade_carga(self):
        nivel_forca = self.strenght
        carga_max = 10
        carga_leve = 1.5 
        carga_med = 3
        carga_pes = 5
        empurra = 25
        
        if nivel_forca > 0 and nivel_forca <= 10:
            carga_max = nivel_forca * 10
            carga_leve = carga_leve + 1.5
            
            if nivel_forca % 2 == 0:
                carga_med = carga_med + 3.5
            else:
                carga_med = carga_med + 2.5
            
            carga_pes = carga_pes + 5
        
        elif nivel_forca > 10 and nivel_forca <= 12:
            carga_max = 
            carga_leve = carga_leve + 1.5
            
            if nivel_forca % 2 == 0:
                carga_med = carga_med + 3.5
            else:
                carga_med = carga_med + 2.5
            
            carga_pes = carga_pes + 5
            
        

###### CONFORME TABELA DE TAMANHO PG 34 #######    
    def calcula_tamanho(self):
        verifica_alt = self.altura 
        verifica_peso = self.peso
        cap_carga = 
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
            mod_atk_tam = 4
            mod_def_tam = 4
            mod_gra_tam = -12 
            mod_ste_tam = 12
            mod_itm_tam = -6
            space = 0.03
            range_alcance = 0
            cap_carga = cap_carga * (1.0/4.0)
            custo = 12       
        
        elif verifica_alt > 0.3 and verifica_alt <= 0.6:
            self.tamanho = 'MINIMO'
            mod_atk_tam = 2
            mod_def_tam = 2
            mod_gra_tam = -8
            mod_ste_tam = 8
            mod_itm_tam = -4
            space = 0.075
            range_alcance = 0
            cap_carga = cap_carga * (1.0/2.0)
            custo = 8   
            
        elif verifica_alt >0.6 and verifica_alt <= 1.2:
            self.tamanho = 'PEQUENO'
            mod_atk_tam = 1
            mod_def_tam = 1
            mod_gra_tam = -4
            mod_ste_tam = 4
            mod_itm_tam = -2
            space = 1.5
            range_alcance = 1.5
            cap_carga = cap_carga * (3.0/4.0)
            custo = 4   
            
        elif verifica_alt >1.2 and verifica_alt <= 2.4:
            self.tamanho = 'MEDIO'
            mod_atk_tam = 0
            mod_def_tam = 0
            mod_gra_tam = 0
            mod_ste_tam = 0
            mod_itm_tam = 0
            space = 1.5
            range_alcance = 1.5
            cap_carga = cap_carga * 1
            custo = 0
            
        elif verifica_alt > 2.4 and verifica_alt <= 4.8:
            self.tamanho= 'GRANDE'
            mod_atk_tam = -1
            mod_def_tam = -1
            mod_gra_tam = 4
            mod_ste_tam = -4
            mod_itm_tam = 2
            space = 3
            range_alcance = 3
            cap_carga = self.strenght + 5
            custo = 12   
            
        elif verifica_alt >4.8 and verifica_alt <= 9.6:
            self.tamanho = 'ENORME'
            mod_atk_tam = -2
            mod_def_tam = -2
            mod_gra_tam = 8
            mod_ste_tam = -8
            mod_itm_tam = 4
            space = 4.5
            range_alcance = 3
            cap_carga = self.strenght + 10
            custo = 24  
            
        elif verifica_alt > 9.6 and verifica_alt <= 19.2:
            self.tamanho = 'DESCOMUNAL'
            mod_atk_tam = -4
            mod_def_tam = -4
            mod_gra_tam = 12
            mod_ste_tam = -12
            mod_itm_tam = 6
            space = 6
            range_alcance = 4.5
            cap_carga = self.strenght + 15
            custo = 36 
            
        elif verifica_alt >19.2 and verifica_alt <= 38.4:
            self.tamanho = 'COLOSSAL'
            mod_atk_tam = -8
            mod_def_tam = -8
            mod_gra_tam = 16
            mod_ste_tam = -16
            mod_itm_tam = 8
            space = 9
            range_alcance = 4.5
            cap_carga = self.strenght + 20
            custo = 48  
            
        elif verifica_alt > 38.4:
            self.tamanho = 'INCRIVEL'
            mod_atk_tam = -12
            mod_def_tam = -12
            mod_gra_tam = 20
            mod_ste_tam = -20
            mod_itm_tam = 10
            space = 12
            range_alcance = 6
            cap_carga = self.strenght + 25
            custo = 60
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
