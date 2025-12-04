import sys
import Modules.ui as ui
import Modules.tasks as tasks

window, app = ui.openui()
input = ui.setupinput(window)
buttons, labels = ui.setuptasks(window)

tasks.labels = labels
tasks.buttons = buttons

input.editingFinished.connect(lambda: tasks.addtask(window, input))

window.show()
sys.exit(app.exec())
