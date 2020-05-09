#######################################################################################################################
# Выполнил: Иван Суханюк(Курс: Intro Python (07.04.2020))
# Последние изменения: 09.05.2020
#  -> task 1: Допишите класс Unit: добавьте проверку на здоровье таким образом, чтобы здоровье нельзя было
#  установить < 0 (например у юнита осталось 5 здоровья а его ударили на 10)
#  -> task 2: Напишите класс Knight. Реализуйте расчет значения урона для атаки и значения заблокированного
#  урона для защиты. Добавьте в атаку рыцаря игнорирование половины защиты врага.
#  -> task 3: Реализуйте всем классам юнитов в атаке проверку состояния здоровья врага (нельзя атаковать врага,
#  у которого здоровье = 0)
#  -> *task 4: Для мага - продумайте механику использования заклинаний. Вероятнее всего заклинание - обьект
#  отдельного класса (ООП всетаки))))
######################################################################################################################
from Module1 import Mage, Pocket, Item

mag = Mage("Gav", 100, 100)

example = {
    "brace": {
        "health": 100,
        "defence": 20,
        "dmg": 30
    },
    "sword": {
        "health": 0,
        "defence": 40,
        "dmg": 100
    },
    "helmet": {
        "health": 0,
        "defence": 100,
        "dmg": 0
    }
}


loot = Pocket()
loot.push_item(Item("gas", 100, 20, 30))
loot.push_item(Item("gav", 20, 30, 60))
loot.push_item(Item("helmet", 20, 30, 80))
print(loot)





