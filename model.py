import json

def read_state(animal_id):
    #返回动物的状态
    with open('animal.json', "r") as f:
        animal = json.load(f)
        if animal_id in animal:
            return animal[animal_id]['STATE']
        else:
            raise Exception('Sorry, the animal is not in our shop.')

def read_place(animal_id):
    #返回动物所在的器具
    with open('animal.json', "r") as f:
        animal = json.load(f)
        if animal_id in animal:
            return animal[animal_id]['PLACE']
        else:
           raise Exception('Sorry, the animal is not in our shop.')

def verify_availability(equipment_id):
    #返回器具的可用性
    with open('equipment.json', "r") as f:
        equipment = json.load(f)
        if equipment_id in equipment:
            return equipment[equipment_id]['AVAILABILITY']
        else:
            raise Exception('Sorry, we don\'t have that equipment in our shop.')

def find_occupant(equipment_id):
    #返回占用器具的动物（如果为砂盆则可以是复数）
    with open('animal.json', "r") as f:
        animal = json.load(f)
        with open('equipment.json', 'r') as g:
            equipment = json.load(g)
        if equipment_id in equipment:
            animal_list = []
            for i in animal:
                if animal[i]['PLACE'] == equipment_id:
                    animal_list.append(i)
            return animal_list
        else:
           raise Exception('Sorry, we don\'t have that equipment in our shop.')

def change_state(animal_id, state):
    #改变动物状态
    possible_state = ['hungry', 'asleep', 'bored', 'tired']
    with open('animal.json', "r") as f:
        animal = json.load(f)
        if state in possible_state:
            if animal_id in animal:
                #修改animal文件中对应动物的状态
                animal[animal_id]['STATE'] = state
            else:
                raise Exception('Sorry, the animal is not in our shop.')
        else:
            raise Exception('Your state is not valid.')
    with open('animal.json', 'w') as f:
        json.dump(animal, f, indent=4)

def change_place(animal_id, place):
    #修改动物所在器具
    with open('animal.json', "r") as f:
        animal = json.load(f)
        with open('equipment.json', 'r') as g:
            equipment = json.load(g)
            #检查三项（按顺序）：器具是否存在，动物是否存在，器具是否被占用
            if place in equipment:
                if animal_id in animal:
                    if equipment[place]['AVAILABILITY'] == 'vacant':
                        #动物离开的器具空出
                        equipment[animal[animal_id]['PLACE']]['AVAILABILITY'] = 'vacant'
                        #动物到达的器具被占用（除砂盆之外）
                        if place != 'litter':
                            equipment[place]['AVAILABILITY'] = 'occupied'
                        #动物的地点修改
                        animal[animal_id]['PLACE'] = place
                    else:
                        raise Exception('Sorry, the equipment is occupied.')
                else:
                    raise Exception('Sorry, the animal is not in our shop.')
            else:
                raise Exception('Sorry, we don\'t have that equipment in our shop.')
    with open('animal.json', 'w') as f:
        json.dump(animal, f, indent=4)
    with open('equipment.json', 'w') as f:
        json.dump(equipment, f, indent=4)
    