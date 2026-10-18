def knight_vs_rook(knight, rook):
    if knight[0] == rook[0] or knight[1] == rook[1]:
        return "Rook"
    elif (abs(knight[0] - rook[0]) == 2 and abs(ord(knight[1]) - ord(rook[1])) == 1) or (abs(knight[0] - rook[0]) == 1 and abs(ord(knight[1]) - ord(rook[1])) == 2):
        return "Knight"
    return "None"