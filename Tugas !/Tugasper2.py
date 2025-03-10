import random  # Mengimpor modul random untuk mengacak damage dan peluang serangan

class Robot:
    def __init__(self, name, hp, attack_power, special_skill):
        self.name = name 
        self.hp = hp 
        self.attack_power = attack_power 
        self.attack_accuracy = 0.8  
        self.special_skill = special_skill  
        self.special_used = False  

    def attack_enemy(self, enemy):
        if random.random() <= self.attack_accuracy: 
            damage = random.randint(self.attack_power - 2, self.attack_power + 2) 
            enemy.hp -= damage  # Kurangi HP musuh
            print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage!")  
        else:
            print(f"{self.name} gagal menyerang {enemy.name}!") 

    def use_special_skill(self, enemy):
        if not self.special_used:  #mengecek apakah skill spesial sudah digunakan
            print(f"{self.name} menggunakan skill spesial: {self.special_skill['name']}!")  
            enemy.hp -= self.special_skill['damage']  
            print(f"{enemy.name} menerima {self.special_skill['damage']} damage!")  
            self.special_used = True  #menandai skill sudah digunakan
        else:
            print(f"{self.name} sudah menggunakan skill spesial sebelumnya!")  

    def defend(self):
        self.hp += 5  
        print(f"{self.name} bertahan dan memulihkan 5 HP!")  

    def is_defeated(self):
        return self.hp <= 0  #mengembalikan True jika HP robot habis (<= 0)

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1  
        self.robot2 = robot2  
        self.round_number = 1  

    def start(self):
        while not self.robot1.is_defeated() and not self.robot2.is_defeated():  #looping sampai ada yang kalah
            print(f"\nRound-{self.round_number} ============================================")
            print(f"{self.robot1.name} [{self.robot1.hp}] vs {self.robot2.name} [{self.robot2.hp}]")  
            
            for robot, enemy in [(self.robot1, self.robot2), (self.robot2, self.robot1)]:  
                if robot.is_defeated(): 
                    continue
                
                print("\n1. Attack  2. Special Skill  3. Defense  4. Give up") 
                choice = int(input(f"{robot.name}, pilih aksi: "))  
                
                if choice == 1:
                    robot.attack_enemy(enemy)  
                elif choice == 2:
                    robot.use_special_skill(enemy) 
                elif choice == 3:
                    robot.defend()  
                elif choice == 4:
                    print(f"{robot.name} menyerah!")  
                    robot.hp = 0
                    break

            self.round_number += 1 

        winner = self.robot1 if not self.robot1.is_defeated() else self.robot2  
        print(f"\n{winner.name} menang!")  

robot1 = Robot("Luffy", 500, 12, {"name": "Gomu Gomu no Red Hawk", "damage": 30}) 
robot2 = Robot("Zoro", 500, 11, {"name": "Santoryu Ougi: Sanzen Sekai", "damage": 40}) 

game = Game(robot1, robot2) 
game.start()  
