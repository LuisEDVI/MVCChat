from View.ViewSetter import ViewSetter
from Model.Model import Model
from Controller import Controller

model_instance = Model()
controller_instance = Controller()

def main():
    controller_instance.set_model(model_instance)
    view_instance = ViewSetter(controller_instance)
    controller_instance.set_view(view_instance)
    view_instance.start()
main()