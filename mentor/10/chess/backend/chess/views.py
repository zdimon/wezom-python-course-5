from django.shortcuts import render
from backend.settings import BASE_DIR
import os
import json

# d = json.loads('{"ss": "dsdas"}')
# f = {}
# f = json.dumps(f)

def make_board():
    board = []
    for i in range(0,8):
        tmp = []
        for j in range(0,8):
            if j%2 == 0:
                tmp.append({"color": "black"})
            else:
                tmp.append({"color": "white"})
        board.append(tmp)

    return board

def create_board_json():
    board = make_board()
    path = os.path.join(BASE_DIR,'static', 'board.json')
    #if not os.path.isfile(path):
    with open(path, 'w') as f:
        f.write(json.dumps(board))
    return board

        

def index(request):
    board = create_board_json()
    return render(request,'index.html',{"board": board})
