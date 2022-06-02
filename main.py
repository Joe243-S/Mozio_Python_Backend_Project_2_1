from ProviderCRUD import choice_p
from ServiceAreaCRUD import choice_s

def main():
    print('Enter P for Provider\nEnter S for Service Area')

    file = input('Choose your file: ')

    if file == 'P':
        providerObj = choice_p()
        providerObj.func_Provider()

    elif file == 'S':
        serviceObj = choice_s()
        serviceObj.func_Service()
    else:
        print('Wrong choice, you are going to exist.')

main()