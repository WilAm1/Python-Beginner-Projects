"""99 Bottles of Beer Personal Project"""

def sing():
    """Sings the lyrics of 99 bottles of beer completely"""
    bottle99 = 99
    for n in range(bottle99,0,-1):
        if n != 1:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer. ")
            
            if n != 2:
                print(f"Take one down and pass it around, {n-1} bottles of beer on the wall.")
            else:
                print(f"Take one down and pass it around, {n-1} bottle of beer on the wall.")
        else:
            print(f'{n} bottle of beer on the wall, {n} bottle of beer.')
            print(f'Take one down and pass it around, no more bottles of beer on the wall.')
        

    print(f'No more bottles of beer on the wall, no more bottles of beer.\n'\
        f'Go to the store and buy some more, {bottle99} bottles of beer on the wall.')

sing()