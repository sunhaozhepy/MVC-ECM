from appJar import gui
import model
import controller
app = gui()


def onpress_function():  # 可以换成switch但是很可惜Python里面好像没有
    if app.getRadioButton('actions') == 'feed':
        controller.feed(app.getRadioButton("animals"))
    elif app.getRadioButton('actions') == 'play':
        controller.play(app.getRadioButton("animals"))
    elif app.getRadioButton('actions') == 'sleep':
        controller.sleep(app.getRadioButton("animals"))
    elif app.getRadioButton('actions') == 'wake':
        controller.wake(app.getRadioButton("animals"))
    animal_name = app.getRadioButton('animals')  # 此处的animal_name是局部变量
    state = model.read_state(animal_name)
    place = model.read_place(animal_name)
    app.setLabel(animal_name, '{:<20}{:<20}'.format(animal_name, state+', '+place))


row = app.getRow()
app.addLabel("header", "Welcome to the animal shop!", row, 0, 2)
app.setLabelBg("header", "salmon")
app.setLabelFg("header", "white")

row = app.getRow()
app.addLabel("dashboard", "Dashboard", row, 0, 2)
app.setLabelBg("dashboard", "gray")
app.setLabelFg("dashboard", "white")

list_animals = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
list_actions = ['feed', 'play', 'sleep', 'wake']

row = app.getRow()
color = ['lavender', 'white']  # 储存颜色，计数器偶数蓝色，奇数白色，形成条纹
for i in range(len(list_animals)):
    animal_name = list_animals[i]
    state = model.read_state(animal_name)
    place = model.read_place(animal_name)
    app.addLabel(animal_name, '{:<20}{:<20}'.format(animal_name, state+', '+place), row+i, 0, 2)
    app.setLabelAlign(animal_name, "left")
    app.setLabelBg(animal_name, color[i % 2])

row = app.getRow()
app.addLabel("actionboard", "Actions", row, 0, 2)
app.setLabelBg("actionboard", "gray")
app.setLabelFg("actionboard", "white")

row = app.getRow()
for i in range(len(list_animals)):
    animal_name = list_animals[i]
    app.addRadioButton('animals', animal_name, row+i, 0, 1)
for j in range(len(list_actions)):
    action_name = list_actions[j]
    app.addRadioButton('actions', action_name, row+j, 1, 1)

row = app.getRow()
app.addButton("go", onpress_function, row, 1)

app.go()
