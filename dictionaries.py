def init():
    print("********************** DICTIONARIES **********************")

    fruits = {'Apples':120, 'Oranges':50, 'Grapes':80 }
    print('cost of apple: ', fruits['Apples'])

    fruits['Grapes'] = 60
    print('updated cost of Grapes:', fruits['Grapes'])

    fruits = {'Apples': 120, 'Oranges': 50, 'Apples': 80}
    print('Cost of apple:', fruits['Apples'])
    # last entered value is taken when 2 same keys are assigned value

    fruits.__delitem__('Oranges')
    print(fruits)

init()