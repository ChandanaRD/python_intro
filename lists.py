def init():
    print("********************** LISTS **********************")

    fruitList = ['Apples','Bananas', 'Cherries', 'Dry fruits']
    print(fruitList)
    # ['Apples', 'Bananas', 'Cherries', 'Dry fruits']

    fruitList.insert(5,'e')
    print(fruitList)
    # ['Apples', 'Bananas', 'Cherries', 'Dry fruits', 'e']

    fruitList.append('f')
    print(fruitList)
    # ['Apples', 'Bananas', 'Cherries', 'Dry fruits', 'e', 'f']

    fruitList.__delitem__(5)
    fruitList.__delitem__(4)
    print(fruitList)
    # ['Apples', 'Bananas', 'Cherries', 'Dry fruits']

    fruitList[0] = 'Apricots'
    print(fruitList)
    # ['Apricots', 'Bananas', 'Cherries', 'Dry fruits']

    costList = [100, 40, 180, 300]
    print(costList)
    # [100, 40, 180, 300]

    print(max(costList))
    # 300

    print(min(costList))
    # 40

    print(sum(costList))
    # 620

    print("max of fruitlist => "+ max(fruitList) + '\nmin of fruitlist => ' +min(fruitList))
    # print(sum(fruitList)) --> not supported

init()