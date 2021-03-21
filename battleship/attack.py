class attack:
    '''Defines attack type class.'''
    def createAttack(self, name, coords):
        '''Return attack object depending on user input.'''
        if name == 'c':
            cA = coordAttack(name, coords)
            return cA
        elif name == 's':
            sA = sonarAttack(name, coords)
            return sA
        elif name == 'l':
            lA = spaceLaserAttack(name, coords)
            return lA
        elif name == 'm':
            mF = moveFleet(name, coords)
            return mF

class coordAttack(attack):
    '''Define coordinate attack type.
    Attributes:
        name: attack name
        coords: attack coords
    '''
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords


class sonarAttack(attack):
    '''Define sonar attack type.
    Attributes:
        name: attack name
        coords: attack coords
    '''
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    # def createCoords(self, coords):
    #     '''Creates list of coordinates in sonar attack'''
    #     sonarCoords = []
    #     row = str(int(coords[0]))
    #     col = chr(ord(coords[1]))
    #     sonarCoords.append(coords)
    #     return coords

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords

class spaceLaserAttack(attack):
    '''Define space laser attack type.
    Attributes:
        name: attack name
        coords: attack coords
    '''
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords


class moveFleet(attack):
    '''Define move fleet command.
    Attributes:
        name: moveFleet name
        direction: direction of fleet movement
    '''
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction

    def getName(self):
        return self.name

    def getDirection(self):
        return self.direction
