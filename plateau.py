from math import *
#plateau
widht,height = 8,8
plate = [["vide"for _ in range(widht)]for _ in range(height)]

# for element in plate:
#     print(element,"\n")


#pièce noires
blk_r = "bl_r"
blk_k = "bl_kn"
blk_b = "bl_b"
blk_ki = "bl_ki"
blk_q = "bl_q"

blk_p = "bl_p"

black_pieces = [blk_r,blk_k,blk_b,blk_ki,blk_q,blk_b,blk_k,blk_r]

black_pawn = [(blk_p)for _ in range(widht)]
# print(black_pawn)
# print(black_pieces)


#pièces blanches
wht_r = "wh_r"
wht_k = "wh_kn"
wht_b = "wh_b"
wht_ki = "wh_ki"
wht_q = "wh_q"

wht_p = "wh_p"
white_pieces = [wht_r,wht_k,wht_b,wht_ki,wht_q,wht_b,wht_k,wht_r]
white_pawn = [(wht_p)for _ in range(widht)]
# print(white_pawn)
# print(white_pieces)


#rangement du plateau
def plate_tidy():
    '''cette fonction attribue les pièces a leurs place d'origine'''
    plate[0] = black_pieces
    plate[1] = black_pawn
    plate[6] = white_pawn
    plate[7] = white_pieces
    
    return
plate_tidy()
#affiche le plateau 
for element in plate:
    print(element,"\n")

lettres = ["a","b","c","d","e","f","g","h"]
chiffres = [(8-i)for i in range(0,widht)]

# transfome les coordonnées courante en chiffres
def coordinate(co):
    coordinate = list(co)
    coordinate[1] = 8-int(coordinate[1])
    coordinate[3] = 8-int(coordinate[3])
    for element in range(len(lettres)):
        if lettres[element] == coordinate[0]:
            coordinate[0] = element
        if lettres[element] == coordinate[2]:
            coordinate[2] = element
    return coordinate

# vérifie le move du poneys ;)
def valid_mv_knight(coordinate):
    valid_mv_knight = False
    if coordinate[0] == coordinate[2]+1 or coordinate[0] == coordinate[2]-1:
        if coordinate[1] == coordinate[3]+2 or coordinate[1] == coordinate[3]-2:
            valid_mv_knight = True
            if valid_eat(coordinate) == False:
                valid_mv_knight = False
    return valid_mv_knight


# print(valid_mv_knight(coordinate(co)))

def valid_eat(coordinate):
    valid_eat = True
    for element in black_pieces:

        if plate[coordinate[1]][coordinate[0]] == element or plate[coordinate[1]][coordinate[0]] == blk_p:

            if plate[coordinate[3]][coordinate[2]] == element or plate[coordinate[3]][coordinate[2]] == blk_p:
                valid_eat = False

    for element in white_pieces:

        if plate[coordinate[1]][coordinate[0]] == element or plate[coordinate[1]][coordinate[0]] == wht_p:

            if plate[coordinate[3]][coordinate[2]] == element or plate[coordinate[3]][coordinate[2]] == wht_p:
                valid_eat = False

    return valid_eat

def valid_forward_or_backward_move(coordinate):
    valid_forward_move = True
    if coordinate[3] < coordinate[1]:
        for i in range(coordinate[3]+1,coordinate[1]):
            if plate[i][coordinate[0]] != "vide":
                valid_forward_move = False
    elif coordinate[3] > coordinate[1]:
        for i in range(coordinate[1]+1,coordinate[3]):
            if plate[i][coordinate[0]] != "vide":
                valid_forward_move = False
    return valid_forward_move



def valid_move_pawn(coordinate):
    valid_move_pawn = False
    if plate[coordinate[1]][coordinate[0]] == wht_p:
        if coordinate[1] == 6:
            if coordinate[1] == coordinate[3]-2 or coordinate[1] == coordinate[3]-1:
                if valid_forward_or_backward_move(coordinate) == True:
                    valid_move_pawn =   True
        if coordinate[1] == coordinate[3]+1:
            print(coordinate[1],coordinate[3])
            valid_move_pawn = True
    elif plate[coordinate[1]][coordinate[0]] == blk_p:
        if coordinate[1] == 5:
            if coordinate[1] == coordinate[3]+2 or coordinate[1] == coordinate[3]+1:
                if valid_forward_or_backward_move(coordinate) == True:
                    valid_move_pawn = True
        if coordinate[1] == coordinate[3]-1:
            print(coordinate[1],coordinate[3])
            valid_move_pawn = True
            
    return valid_move_pawn


coo = coordinate("e4e3")
print(coo)

print("\n \n")
plate[4][4] = "bl_p"

print(valid_move_pawn(coo))
