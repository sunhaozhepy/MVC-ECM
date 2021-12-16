import model

def feed(animal_id):
    if model.verify_availability('manger') == 'vacant':
        if model.read_state(animal_id) == 'hungry':
            model.change_place(animal_id, 'manger')
            model.change_state(animal_id, 'bored')
            print(animal_id + ' is at the manger and becomes bored.')
        else:
            print('Sorry, ' + animal_id + ' is not hungry.')
    else:
        print('Sorry, the manger is occupied by', model.find_occupant('manger'))

def play(animal_id):
    if model.verify_availability('roller') == 'vacant':
        if model.read_state(animal_id) == 'bored':
            model.change_place(animal_id, 'roller')
            model.change_state(animal_id, 'tired')
            print(animal_id + ' is at the roller and becomes tired.')
        else:
            print('Sorry, ' + animal_id + ' doesn\'t want to do sports.')
    else:
        print('Sorry, the roller is occupied by', model.find_occupant('roller'))

def sleep(animal_id):
    if model.verify_availability('nest') == 'vacant':
        if model.read_state(animal_id) == 'tired':
            model.change_place(animal_id, 'nest')
            model.change_state(animal_id, 'asleep')
            print(animal_id + ' is at the nest and is asleep.')
        else:
            print('Sorry, ' + animal_id +  ' isn\'t tired.')
    else:
        print('Sorry, the nest is occupied by', model.find_occupant('nest'))

def wake(animal_id):
    if model.read_state(animal_id) == 'asleep':
        model.change_place(animal_id, 'litter')
        model.change_state(animal_id, 'hungry')
        print(animal_id + ' is awake and goes to the litter.')
    else:
        print('Sorry, ' + animal_id + ' isn\'t sleeping.')
