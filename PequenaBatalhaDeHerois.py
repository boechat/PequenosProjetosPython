########################################## BATALHA RPG #################################
import random
import math
import time 

class Character:
    def __init__(self, nome, nivel, base_stats, moves):
        self.nome = nome
        self.nivel = nivel
        self.base_stats = base_stats
        self.hp = self.calcular_hp()
        self.attack = self.calcular_stat("Attack")
        self.defense = self.calcular_stat("Defense")
        self.speed = self.calcular_stat("Speed")
        self.special = self.calcular_stat("Special")
        self.moves = moves

    def calcular_hp(self):
        return math.floor(((self.base_stats["HP"] * 2) * self.nivel) / 100) + self.nivel + 10

    def calcular_stat(self, stat):
        return math.floor(((self.base_stats[stat] * 2) * self.nivel) / 100) + 5

    def escolher_move(self):
        return random.choice(self.moves)

    def __str__(self):
        return f"{self.nome} (HP: {self.hp})"


class Move:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder


def calcular_dano(atacante, defensor, move):
    # Fórmula simplificada de dano (Gen 1 aproximada)
    dano = (((2 * atacante.nivel / 5 + 2) * move.poder * atacante.attack / defensor.defense) / 50) + 2
    return int(dano)


def turno(char1, char2):
    print(f"\n--- Novo Turno ---")
    time.sleep(1)
    # Escolhem os movimentos
    move1 = char1.escolher_move()
    time.sleep(1)
    move2 = char2.escolher_move()
    
    # Ordem baseada na Speed
    if char1.speed >= char2.speed:
        ordem = [(char1, move1, char2), (char2, move2, char1)]
    else:
        ordem = [(char2, move2, char1), (char1, move1, char2)]

    # Executa os ataques
    for atacante, move, defensor in ordem:
        if atacante.hp <= 0:
            continue  # PERSONAGEM já derrotado não ataca
        dano = calcular_dano(atacante, defensor, move)
        defensor.hp -= dano
        print(f"{atacante.nome} usou {move.nome}! {defensor.nome} perdeu {dano} HP \n(Restante: {max(defensor.hp,0)})")
        time.sleep(2)
        if defensor.hp <= 0:
            print(f"{defensor.nome} desmaiou!")
            break


######################################## EXEMPLO BATALHA ####################################################################

spoiler_base = {"HP": 68, "Attack": 60, "Defense": 78, "Speed": 100, "Special": 85}
redphoenix_base = {"HP": 79, "Attack": 83, "Defense": 100, "Speed": 78, "Special": 90}

spoiler_moves = [Move("Soco Elétrico!", 120), Move("Chutes Consecutivos!", 110), Move("Eu Escolho Você: ORION!", 230), Move("Nunchaku!", 65), Move("VAI LA AVAREST, MORRE NO FLASHBACK!", 120)]
redphoenix_moves = [Move("Phoenix... SLASH!", 150), Move("Myth... CANNON!", 210), Move("Soco Dramático!", 100), Move("DORAGON... SHOOTO!", 90), Move("BATTO WIND!", 80)]

spoiler = Character("Spoiler", 50, spoiler_base, spoiler_moves)
redphoenix = Character("Red Phoenix", 50, redphoenix_base, redphoenix_moves)

# Loop de combate
while spoiler.hp > 0 and redphoenix.hp > 0:
    turno(spoiler, redphoenix)
    time.sleep(2)

print("\nBatalha encerrada!")
