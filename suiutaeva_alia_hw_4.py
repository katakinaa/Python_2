from enum import Enum
from random import randint, choice


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    HEAL = 2
    BOOST = 3
    BLOCK_DAMAGE_AND_REVERT = 4
    GET_DAMAGE = 5
    REVERT_HEALTH_HERO = 6
    STEALTH_MODE = 7
    DEFENCE = 8
    SAITAMA = 9


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if (value > 0):
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT \
                        and self.__defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT:
                    coeff = randint(1, 2)  # 1, 2
                    hero.blocked_damage = int(self.damage / (5 * coeff))  # 5, 10
                    hero.health -= (self.damage - hero.blocked_damage)
                elif hero.ability == SuperAbility.DEFENCE:
                    pass
                else:
                    hero.health -= self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 4)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hits critically: {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage, boost_amount):
        super().__init__(name, health, damage, SuperAbility.BOOST)
        self.boost_amount = boost_amount

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage += self.boost_amount


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted: {self.blocked_damage}')


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.GET_DAMAGE)

    def apply_super_power(self, boss, heroes):
        dead_heroes = [hero for hero in heroes if hero.health <= 0]
        if dead_heroes:
            revived_hero = dead_heroes[0]
            revived_hero.health = 1
            print(f'Witcher {self.name} revived {revived_hero.name}!')
            self.health = 0


class Hacker(Hero):
    def __init__(self, name, health, damage, steal_amount):
        super().__init__(name, health, damage, SuperAbility.REVERT_HEALTH_HERO)
        self.steal_amount = steal_amount

    def apply_super_power(self, boss, heroes):
        boss.health -= self.steal_amount
        target_hero = choice(heroes)
        target_hero.health += self.steal_amount
        print(
            f'Hacker {self.name} stole {self.steal_amount} health from {boss.name} and gave it to {target_hero.name}.')


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STEALTH_MODE)
        self.invisible = False
        self.invisible_rounds = 2

    def apply_super_power(self, boss, heroes):
        if not self.invisible:
            self.invisible = True
            print(f'Avrora {self.name} entered invisibility mode!')
        else:
            self.invisible = False
            print(f'Avrora {self.name} exited invisibility mode!')
            boss.damage -= self.damage


class Avenger(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.DEFENCE)
        self.protected = False

    def apply_super_power(self, boss, heroes):
        if not self.protected:
            if randint(1, 5) == 1:
                self.protected = True
                print(f'Avenger {self.name} protected the team from boss\'s attack!')
        else:
            self.protected = False
            print(f'Avenger {self.name} released the team from protection!')


class King(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAITAMA)
        self.summoned_saitama = False

    def apply_super_power(self, boss, heroes):
        if not self.summoned_saitama:
            if randint(1, 10) == 5:
                print(f'King {self.name} summoned Saitama!')
                boss.health = 0
                self.summoned_saitama = True


round_number = 0


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} ------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True

    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and boss.defence != hero.ability:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def start_game():
    boss = Boss('Sauron', 1000, 50)

    warrior_1 = Warrior('Arthur', 280, 10)
    warrior_2 = Warrior('Ahiles', 270, 15)
    magic = Magic('Maga', 290, 10, 2)
    doc = Medic('Aibolit', 250, 5, 15)
    assistant = Medic('Student', 300, 5, 5)
    berserk = Berserk('Guts', 260, 10)
    witcher = Witcher('Elia', 180, 10)
    hacker = Hacker('Geek', 220, 15, 10)
    avrora = Avrora('Rora', 150, 5)
    avenger = Avenger('Hulk', 280, 15)
    king = King('Hell', 250, 10)
    heroes_list = [warrior_1, doc, warrior_2, magic, assistant, berserk, witcher, hacker, avrora, avenger, king]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
