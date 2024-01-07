while True:
    height = 0
    index = 0

    for i in range(8):
        mountain_h = int(input())  
        if mountain_h > height:
            height = mountain_h
            index = i
           
    print(index)  
