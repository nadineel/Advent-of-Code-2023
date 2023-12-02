#First Part
def is_game_possible(game):
    colour_max = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }
    
    for subset in game:
        cubes = subset.split(', ')
        for cube in cubes:
            count = int(cube.split(' ')[0])
            colour = cube.split(' ')[1]
            if count > colour_max[colour]:
                return False
        
    return True

#Seond Part
def power(game):
    colour_max = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }

    for subset in game:
        cubes = subset.split(', ')
        for cube in cubes:
            count = int(cube.split(' ')[0])
            colour = cube.split(' ')[1]
            if count > colour_max[colour]:
                colour_max[colour]=count

    product = 1
    for value in colour_max.values():
        product *= value
    return product

def main():

    with open('input.txt') as f:
        lines = f.read().splitlines()

    idSum = 0
    powerSum= 0

    for line in lines:
        game_id = int(line.split(': ')[0].split(" ")[1])
        game = line.split(': ')[1].split('; ')
        powerSum+=power(game)

        if is_game_possible(game):
            idSum += game_id
    print("Total:", idSum)
    print("Total Power:", powerSum)
    
if __name__ == '__main__':
    main()
