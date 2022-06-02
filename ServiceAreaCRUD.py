from CreateServiceArea import create
from ReadServiceArea import read
from UpdateServiceArea import update
from DeleteServiceArea import delete

class choice_s():

    def func_Service(self):
        print('Enter option C to Create\nEnter option R to Read\nEnter option U to Update\nEnter option D to Delete')
        choiceS = input('Choose your option: ')

        if choiceS == 'C':
            createObj = create()
            createObj.func_createData()

        elif choiceS == 'R':
            readObj = read()
            readObj.func_readData()

        elif choiceS == 'U':
            updateObj = update()
            updateObj.func_updateData()

        elif choiceS == 'D':
            deleteObj = delete()
            deleteObj.func_deleteData()

        else:
            print('Wrong choice, you are going to exist.')

choice_s()