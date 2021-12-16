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
    app.setLabel(animal_name, '{:<20}{:<20}'.format(animal_name,
                                                   model.read_state(animal_name)+', '+model.read_place(animal_name)))


row = app.getRow()
app.startFrame('headerframe', row, 0, colspan=2)
app.addLabel("header", "Welcome to the animal shop!")
app.setLabelBg("header", "salmon")
app.setLabelFg("header", "white")
app.addLabel("dashboard", "Dashboard")
app.setLabelBg("dashboard", "gray")
app.setLabelFg("dashboard", "white")
app.stopFrame()

list_animals = ['Tic', 'Tac', 'Totoro', 'Patrick', 'Pocahontas']
list_actions = ['feed', 'play', 'sleep', 'wake']

row = app.getRow()
color = ['lavender', 'white']  # 储存颜色，计数器偶数蓝色，奇数白色，形成条纹
app.startFrame('animalframeleft', row, 0, colspan=2)
for i in range(len(list_animals)):
    animal_name = list_animals[i]
    app.addLabel(animal_name, '{:<20}{:<20}'.format(animal_name,
                                                   model.read_state(animal_name)+', '+model.read_place(animal_name)))
    app.setLabelAlign(animal_name, "left")
    app.setLabelBg(animal_name, color[i % 2])
app.stopFrame()

row = app.getRow()
app.startFrame('actionframe', row, 0, colspan=2)
app.addLabel("actionboard", "Actions")
app.setLabelBg("actionboard", "gray")
app.setLabelFg("actionboard", "white")
app.stopFrame()

row = app.getRow()
app.startFrame('leftframe', row, 0)
for animal_name in list_animals:
    app.addRadioButton('animals', animal_name)
app.stopFrame()

app.startFrame('rightframe', row, 1)
for action_name in list_actions:
    app.addRadioButton('actions', action_name)
app.stopFrame()

row = app.getRow()
app.addButton("go", onpress_function, row, 0, 2)
app.stopFrame()

app.go()
