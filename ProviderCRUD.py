from CreateProvider import create
from ReadProvider import read
from UpdateProvider import update
from DeleteProvider import delete

class choice_p():

    def func_Provider(self):
        print('Enter option C to Create\nEnter option R to Read\nEnter option U to Update\nEnter option D to Delete')
        choiceP = input('Choose your option: ')

        if choiceP == 'C':
            createObj = create()
            createObj.func_createData()

        elif choiceP == 'R':
            readObj = read()
            readObj.func_readData()

        elif choiceP == 'U':
            updateObj = update()
            updateObj.func_updateData()

        elif choiceP == 'D':
            deleteObj = delete()
            deleteObj.func_deleteData()

        else:
            print('Wrong choice, you are going to exist.')

choice_p()