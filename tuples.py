def init():
    print("********************** TUPLES **********************")
    print('- Tuples are mutable')
    print('- values of tuples can be read, added, tuples itself can be added but values cannot be deleted \n\n')

    tuple1 = ('Apples', 'Oranges', 'Grapes')
    print('Tuple 1 ', tuple1)

    tuple2 = ('pineapple', 'muskmelon', 'watermelon')
    print('tuple1+tuple2 ', tuple1+tuple2)

    print('tuple1*3',tuple1*3)

    del tuple1
    # print(tuple1) --> Error

init()