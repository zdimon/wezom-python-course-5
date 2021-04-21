from django.shortcuts import render
from backend.settings import BASE_DIR
import os

def create_board_json():
    path = os.path.join(BASE_DIR,'static', 'board.json')
    if not os.path.isfile(path):
        with open(path, 'w') as f:
            f.write('asdasdas')

        

def index(request):
    create_board_json()
    return render(request,'index.html',{})
