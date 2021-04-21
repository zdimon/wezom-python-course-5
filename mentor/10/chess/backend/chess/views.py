from django.shortcuts import render
from backend.settings import BASE_DIR
import os
import json

# d = json.loads('{"ss": "dsdas"}')
# f = {}
# f = json.dumps(f)

def make_board():
    board = []
    for i in range(0,7):
        board.append({})

def create_board_json():
    board = [ {
         "color": "black|white",
         "active": "true|false",
         "figure": {
             "image": "1.png",
             "helth": "100%"
         }   
      }      
    ]
    path = os.path.join(BASE_DIR,'static', 'board.json')
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            f.write(json.dumps(board))

        

def index(request):
    create_board_json()
    return render(request,'index.html',{})
