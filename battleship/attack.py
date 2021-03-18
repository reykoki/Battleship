'''
https://stackabuse.com/the-factory-method-design-pattern-in-python/
'''


class attack:
    def createAttack(self, name, coords):
        if name == 'c':
            cA = coordAttack(name, coords)
            return cA
        elif name == 's':
            sA = sonarAttack(name, coords)
            return sA
        elif name == 'l':
            lA = spaceLaserAttack(name, coords)
            return lA


class coordAttack(attack):
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords


class sonarAttack(attack):
    def __init__(self, name, coords):
        self.name = name
        self.coords = self.createCoords(coords)

    def createCoords(self, coords):
        '''Creates list of coordinates in sonar attack'''
        sonarCoords = []
        row = str(int(coords[0]))
        col = chr(ord(coords[1]))
        sonarCoords.append(coords)
        return coords

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords


class spaceLaserAttack(attack):
    def __init__(self, name, coords):
        self.name = name
        self.coords = coords

    def getName(self):
        return self.name

    def getCoords(self):
        return self.coords
