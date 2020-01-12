# Nordin Trifiro
# question 1
def diviseurs(l1, l2):
    dico = {}
    if len(l1) == 0:
        return dico
    else:
        for i in l1:
            div = []

            if len(l2) == 0:
                dico[i] = div

            else:
                for j in l2:
                    if i == 0:
                        dico[0] = []

                    elif j % i == 0:
                        div.append(j)
                dico[i] = div

        return dico


# question 2
def rle(l):
    comp = []
    a = 1
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            a += 1
        else:
            comp.append((l[i], a))
            a = 1
    if l[i + 1] == l[i]:
        comp.append((l[i], a))
    else:
        comp.append((l[i + 1], 1))
    return comp


# question 3
def checkline(l):
    l1 = l.split(",")
    print(l1)
    # check si ligne complète
    if len(l1) != 4:
        print("1")
        return False

    for i in l1:
        if i == []:
            print("2")
            return False

    # check si Noma correct
    if len(l1[0]) != 8:
        print("3")
        return False

    testchi = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in l1[0]:
        if i not in testchi:
            print("4")
            return False

    # check si email correct
    if "@" not in l1[3]:
        print("5")
        return False

    return True


def est_correct(f):
    try:
        with open(f, "r") as file:
            lines = file.readlines()
            cl = []
            for i in lines:
                cl.append(i.strip())

            if cl == []:
                return False

            for j in cl:
                if not checkline(i):
                    return False
            return True
    except:
        return False


# question 4
def oxo(g):
    ver = 0
    hor = 0
    mdia = 0
    ddia = 0
    lv = len(g)
    lh = len(g[0])

    if lv < 3 and lh < 3:
        return "aucune combinaison, matrice trop petite"

    # ligne
    for i in g:
        for j in range(lh - 2):
            if i[j] + i[j + 1] + i[j + 2] == "OXO":
                hor += 1
    # colonne
    for k in range(lh):
        for l in range(lv - 2):
            if g[l][k] + g[l + 1][k] + g[l + 2][k] == "OXO":
                ver += 1

    # diagonale montante
    for m in range(2, lv):
        for n in range(lh - 2):
            if g[m][n] + g[m - 1][n + 1] + g[m - 2][n + 2] == "OXO":
                mdia += 1

    # diagonale descendante
    for o in range(lv - 2):
        for p in range(lh - 2):
            if g[o][p] + g[o + 1][p + 1] + g[o + 2][p + 2] == "OXO":
                ddia += 1

    return (ver, hor, ddia, mdia)


# question 5
# code fourni
class PositionNode:

    def __init__(self, x, y, val, next_node=None):
        self.x = x
        self.y = y
        self.val = val
        self.next_node = next_node

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.val) + ")"


class PositionList:

    def __init__(self, x_lim, y_lim):
        self.head = None
        self.x_lim = x_lim
        self.y_lim = y_lim

    # à implémenter (q5)
    def existe(self, x, y):
        if x > self.x_lim or y > self.y_lim:
            return "out-of-bounds"

        elif self.head == None:
            return False

        else:
            node = self.head
            while node is not None:
                if node.x == x and node.y == y:
                    return node.val
                else:
                    node = node.next_node

            if node is None:
                return False

    # à implémenter (q6) Par Hugo Vandermosten
    def insert(self, x, y, val):

        if x >= self.x_lim or y >= self.y_lim or x < 0 or y < 0:
            return "out-of-bounds"

        # Note de B.W.: pour savoir si c'est None il est plus conseillé de faire "self.head is None"
        # Meme si visiblement les auteurs s'en sont battu les couilles ici
        if self.head == None:
            self.head = PositionNode(x, y, val)
            return True

        if self.head.x == x and self.head.y == y:
            self.head = PositionNode(x, y, val, self.head.next_node)
            return True

        if self.head.x > x or (self.head.x == x and self.head.y > y):
            self.head = PositionNode(x, y, val, self.head)
            return True

        precedent, suivant = self.head, self.head.next_node

        while True:
            if suivant == None:
                precedent.next_node = PositionNode(x, y, val)
                return True

            if suivant.x > x or (suivant.x == x and suivant.y > y):
                precedent.next_node = PositionNode(x, y, val, suivant)
                return True

            if suivant.x == x and suivant.y == y:
                precedent.next_node = PositionNode(x, y, val, suivant.next_node)
                return True

            precedent = precedent.next_node
            suivant = suivant.next_node

    # à implémenter (q6) Par Nordin Trifiro
    def insert(self, x, y, val):

        if self.existe(x, y) == val:
            return

        elif self.existe(x, y) == "out-of-bounds":
            print(str(x) + "," + str(y) + " out_of_bounds")


        else:
            node1 = None
            node2 = PositionNode(x, y, val)
            node3 = self.head

            if self.head == None:
                self.head = node2
                return True

            elif self.head.x > x:
                node2.next_node = self.head
                self.head = node2
                return True

            elif self.head.x == x:
                if self.head.y > y:
                    node2.next_node = self.head
                    self.head = node2
                    return True

                else:
                    while node3.y < y:
                        if node3.next_node != None:
                            node1 = node3
                            node3 = node3.next_node

                        else:
                            node3.next_node = node2
                            return True

                    node2.next_node = node3
                    node1.next_node = node2
                    return True

            else:
                while node3.x < x:
                    if node3.next_node != None:
                        node1 = node3
                        node3 = node3.next_node

                    else:
                        node3.next_node = node2
                        return True

                if node3.x > x:
                    node2.next_node = node3
                    node1.next_node = node2
                    return True

                else:
                    if node3.y > y:
                        node2.next_node = node3
                        node1.next_node = node2
                        return True

                    else:
                        while node3.y < y:
                            if node3.next_node != None:
                                node1 = node3
                                node3 = node3.next_node

                            else:
                                node3.next_node = node2
                                return True

                        node2.next_node = node3
                        node1.next_node = node2
                        return True

    def __str__(self):
        str = "["
        node = self.head
        while node is not None:
            str += node.__str__()
            node = node = node.next_node
        str += "]"
        return str
