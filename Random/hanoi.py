
def move(start, end):
    print(f'Move from {start} to {end}')

def hanoiTower(size,start,through,end):
    if size == 0:
        return
    
    else:
        hanoiTower(size - 1, start, end, through)
        move(start,end)
        hanoiTower(size - 1, through, start, end)
