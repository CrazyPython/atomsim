## [subcode]
import atoms
class molecule:
    def __init__(self,bonds,elements,stable = True):
        self.bonds = bonds
        self.elements = elements
        self.stable = stable
    def update(self):
        if not self.stable:
            self.unstable()
    def unstable(self):
        for bond in bonds:
            del bond
class bond:
    def __init__(self,a,b,num = 1):
        if a.bond == False:
            a.bond = []
        if b.bond == False:
            b.bond = []
        a.bond.append(self)
        b.bond.append(self)
        self.a = a
        self.b = b
        a.bondneed -= num
        b.bondneed -= num
        if num != 1:
            global bond
            bond(a,b,num-1)
class atom:
    def __init__(self,bonds,name,abbr,joinable = True):
        self.bond = False
        self.bondneed = bonds
        self.joinable = joinable
        self.bonds = bonds
        self.name = name
        self.abbr = abbr
class nojoinatom(atom):
    def __init__(self,bonds,name,abbr):
        super.__init__(bonds,name,abbr,joinable = False)


def join(elements,unstable = False):
    "join(elements,[unstable]) -> [bool,molecule]"
    """
    Takes in the elements needed to bond
    and if an unstable molecule is allowed.

    Puts out if the elements were joinable
    and the molecule that was formed.
    """
    for i in elements:
        if not i.joinable:
            return False,[]
    if len(elements) == 2:
        a = element[0]
        b = element[1]
        if a.bond == False and \
           b.bond == False:
           if a.bonds ==  b.bonds:
             return True,molecule([bond(a,b)],[a,b])
           elif unstable == True:
                return True,molecule([bond(a,b)],[a,b],stable = False)
        elif a.bondneed == b.bondneed:
            return True,molecule([bond(a,b)],[a,b])
        else:
            return False,None
    if len(elements) == 3:
        #recursive
        a = element[0]
        b = element[1]
        c = element[2]
        #try to join a-b-c or a-c-b or b-a-c or b-c-a or c-a-b or c-b-a
        actions = [[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,a,b],[c,b,a]]
        for i in actions:
            join(i[0],i[1],unstable = True)
            sucseed,molecule = join(i[1],i[2])
            if sucseed:
                return sucseed,molecule
        #try to join in a triangle
        join(a,b,unstable = True)
        join(c,b,unstable = True)
        return join(c,a)
            
