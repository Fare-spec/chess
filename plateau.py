from math import *

# plateau
width, height = 8, 8
plate = [[(None) for _ in range(width)] for _ in range(height)]

# for element in plate:
#     print(element,"\n")


# pièce noires
blk_r = "bl_r"
blk_k = "bl_kn"
blk_b = "bl_b"
blk_ki = "bl_ki"
blk_q = "bl_q"

blk_p = "bl_p"

black_pieces = [blk_r, blk_k, blk_b,blk_q, blk_ki, blk_b, blk_k, blk_r]

black_pawn = [(blk_p) for _ in range(width)]
# print(black_pawn)
# print(black_pieces)


# pièces blanches
wht_r = "wh_r"
wht_k = "wh_kn"
wht_b = "wh_b"
wht_ki = "wh_ki"
wht_q = "wh_q"

wht_p = "wh_p"
white_pieces = [wht_r, wht_k, wht_b, wht_q,wht_ki,wht_b, wht_k, wht_r]
white_pawn = [(wht_p) for _ in range(width)]
# print(white_pawn)
# print(white_pieces)


# rangement du plateau
def plate_tidy():
    """cette fonction attribue les pièces a leurs place d'origine"""
    plate[0] = black_pieces
    plate[1] = black_pawn
    plate[6] = white_pawn
    plate[7] = white_pieces

    return


plate_tidy()
# affiche le plateau
for element in plate:
    print(element, "\n")

lettres = ["a", "b", "c", "d", "e", "f", "g", "h"]
chiffres = [(8 - i) for i in range(0, width)]


# transfome les coordonnées courante en chiffres
def coordinate(co):
    coordinate = list(co)
    coordinate[1] = 8 - int(coordinate[1])
    coordinate[3] = 8 - int(coordinate[3])
    for element in range(len(lettres)):
        if lettres[element] == coordinate[0]:
            coordinate[0] = element
        if lettres[element] == coordinate[2]:
            coordinate[2] = element
    return coordinate


# vérifie le move du poneys ;)
def valid_mv_knight(coordinate):
    valid_mv_knight = False
    if coordinate[0] == coordinate[2] + 1 or coordinate[0] == coordinate[2] - 1:
        if coordinate[1] == coordinate[3] + 2 or coordinate[1] == coordinate[3] - 2:
            valid_mv_knight = True
            if valid_eat(coordinate) == False:
                valid_mv_knight = False
    return valid_mv_knight


# print(valid_mv_knight(coordinate(co)))


def valid_eat(coordinate):
    valid_eat = True
    for element in black_pieces:
        if (
            plate[coordinate[1]][coordinate[0]] == element
            or plate[coordinate[1]][coordinate[0]] == blk_p
        ):
            if (
                plate[coordinate[3]][coordinate[2]] == element
                or plate[coordinate[3]][coordinate[2]] == blk_p
            ):
                valid_eat = False
    for element in white_pieces:
        if (
            plate[coordinate[1]][coordinate[0]] == element
            or plate[coordinate[1]][coordinate[0]] == wht_p
        ):

            if (
                plate[coordinate[3]][coordinate[2]] == element
                or plate[coordinate[3]][coordinate[2]] == wht_p
            ):
                valid_eat = False
    return valid_eat


def valid_forward_or_backward_move(coordinate):
    valid_forward_move = True
    if coordinate[3] < coordinate[1]:
        for i in range(coordinate[3] + 1, coordinate[1]):
            if plate[i][coordinate[0]] != None:
                valid_forward_move = False
    elif coordinate[3] > coordinate[1]:
        for i in range(coordinate[1] + 1, coordinate[3]):
            if plate[i][coordinate[0]] != None:
                valid_forward_move = False
    return valid_forward_move


# pour les mouvements divers des pions
def valid_move_pawn(coordinate):
    valid_move_pawn = False
    if plate[coordinate[1]][coordinate[0]] == wht_p:
        if coordinate[1] == 6:

            if coordinate[1] == coordinate[3] + 2 or coordinate[1] == coordinate[3] + 1:
                if valid_forward_or_backward_move(coordinate) == True:
                    valid_move_pawn = True
        if coordinate[1] == coordinate[3] + 1:
            valid_move_pawn = True
    elif plate[coordinate[1]][coordinate[0]] == blk_p:
        if coordinate[1] == 5:
            if coordinate[1] == coordinate[3] + 2 or coordinate[1] == coordinate[3] + 1:
                if valid_forward_or_backward_move(coordinate) == True:
                    valid_move_pawn = True
        if coordinate[1] == coordinate[3] - 1:
            valid_move_pawn = True
    return valid_move_pawn


# pour les mouvement horizontaux
def valid_left_rightward_move(coordinate):
    valid_left_rightward_move = True
    if coordinate[2] < coordinate[0]:
        for i in range(coordinate[2] + 1, coordinate[0]):
            if plate[coordinate[1]][i] != None:
                valid_left_rightward_move = False
    elif coordinate[2] > coordinate[0]:
        for i in range(coordinate[0] + 1, coordinate[2]):
            if plate[coordinate[1]][i] != None:
                valid_left_rightward_move = False
    return valid_left_rightward_move


def valid_move_rook(coordinate):
    valid_move_rook = False
    if plate[coordinate[1]][coordinate[0]] == blk_r or wht_r:
        if coordinate[1] == coordinate[3]:
            if valid_left_rightward_move(coordinate) == True:
                if plate[coordinate[2]][coordinate[3]] == None:
                    valid_move_rook = True
                else:
                    if valid_eat(coordinate) == True:
                        valid_move_rook = True
        elif coordinate[0] == coordinate[2]:
            if valid_forward_or_backward_move(coordinate) == True:
                if plate[coordinate[3]][coordinate[2]] == None:
                    valid_move_rook = True
                elif valid_eat(coordinate) == True:
                    valid_move_rook = True
    return valid_move_rook

def empty_case(coordinate_case):
    empty_case = True
    if plate[coordinate_case[0]][coordinate_case[1]] != None:
        empty_case = False
        print(plate[coordinate_case[0]][coordinate_case[1]])        
    return empty_case
def valid_move_diagonal(coordinate):
    valid_move_diagonal = False
    # si la hauteur de départ est supérieur a celle d'arrivée etc...
    if coordinate[1] > coordinate[3]:
        diff_hauteur = coordinate[1] - coordinate[3]

    elif coordinate[1] < coordinate[3]:
        
        diff_hauteur = coordinate[3] - coordinate[1]
    if coordinate[0] > coordinate[2]:
        
        diff_hor = coordinate[0] - coordinate[2]
    elif coordinate[0] < coordinate[2]:

        diff_hor = coordinate[2] - coordinate[0]
    if diff_hauteur == diff_hor:
        #si la hauteur de départ est inférieure a celle d'arrivé
        if coordinate[1]<coordinate[3]:
            # si la coordoné l de départ est inférieure a celle d'arrivée
            if coordinate[0]>coordinate[2]:
                for i in range(diff_hauteur+1):
                    #print(plate[coordinate[1]+i][coordinate[0]-i])
                    print(empty_case([coordinate[1]+i,coordinate[0]-i]))
                    print(coordinate[1]+i,coordinate[0]-i)
                    if empty_case([coordinate[1]+i,coordinate[0]-i]) == True :
                        valid_move_diagonal = True
    return valid_move_diagonal


coordinat = coordinate("h6c1")
print(valid_move_diagonal(coordinat))
# print([coordinat[3],coordinat[2]])
# print(empty_case([coordinat[3],coordinat[2]]))