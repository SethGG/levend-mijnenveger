import random

RIJEN = 10
KOLOMMEN = 10

def maakTak(rij, vakje, bewandeld):
    buren = [(rij+1, vakje), (rij-1, vakje), (rij, vakje+1), (rij, vakje-1)]
    for buur in buren:
        if buur in bewandeld:
            buren.remove(buur)
            break
    if rij >= RIJEN-1 or rij <= 0 or vakje >= KOLOMMEN or vakje <= -1 or (rij, vakje) in bewandeld or any(x in bewandeld for x in buren):
        return bewandeld

    bewandeld.insert(0, (rij, vakje))
    random.shuffle(buren)
    for buurman in buren:
        oude_lengte = len(bewandeld)
        nieuw_bewandeld = maakTak(buurman[0], buurman[1], bewandeld)
        if len(nieuw_bewandeld) > oude_lengte:
            break
        
    return nieuw_bewandeld    
    
def maakPad(rij, vakje, bewandeld):
    buren = [(rij+1, vakje), (rij-1, vakje), (rij, vakje+1), (rij, vakje-1)]
    if bewandeld:
        buren.remove((bewandeld[-1]))
    if rij >= RIJEN or rij <= -1 or vakje >= KOLOMMEN or vakje <= -1 or (rij, vakje) in bewandeld or any(x in bewandeld for x in buren):
        return bewandeld

    bewandeld.append((rij, vakje))
    if (rij-1, vakje) in buren and (rij == 1 or rij == RIJEN-1):
        buren.remove((rij-1, vakje))
    
    random.shuffle(buren)
    for buurman in buren:
        nieuw_bewandeld = maakPad(buurman[0], buurman[1], bewandeld)
        if nieuw_bewandeld[-1][0] == RIJEN-1:
            for buurman in buren:
                nieuw_bewandeld = maakTak(buurman[0], buurman[1], nieuw_bewandeld)
            return nieuw_bewandeld

    bewandeld.remove((rij, vakje))
    return bewandeld
        
def maakBoard():
    pad = maakPad(0, random.randint(0, KOLOMMEN-1), [])
    board = [[1] * KOLOMMEN for x in range(RIJEN)]
    for stap in pad:
        board[stap[0]][stap[1]] = 0
    
    return board

def main():
    board = maakBoard()
    line = "   "
    for i in range(KOLOMMEN):
        line += "%d "%i
    print(line)
    for i, rij in enumerate(board):
        line = "%d |"%i
        for vakje in rij:
            if vakje:
                line += "X|"
            else:
                line += " |"
        print(line)


if __name__ == "__main__":
    main()
