def turtle(coord, direction):
    x, y = coord
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    command = yield (x, y)
    
    while True:
        if command == "f":
            x += dx[direction]
            y += dy[direction]
        elif command == "l":  
            direction = (direction + 1) % 4
        elif command == "r":  
            direction = (direction - 1) % 4
        
        command = yield (x, y)

if __name__ == "__main__":
    robo = turtle((0, 0), 0)
    start = next(robo)
    for c in "flfrffrffr":
        print(*robo.send(c))
