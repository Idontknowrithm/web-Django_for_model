from tensorflow import keras
import numpy as np

class Omok():
    def __init__(self):
        self.SIZE = 20
        self.path = 'alpha_O.h5'
        self.model = keras.models.load_model(self.path)
        self.board = [[0 for u in range(self.SIZE)] for i in range(self.SIZE)]
        self.status = 0
    
    def alpha_turn(self, player):
        x_test = np.array(player)
        x_test = x_test.reshape(-1, 20, 20, 1)

        y = model.predict(x_test)
        y = y.reshape(20, 20)
        
        max_val = -1
        max_r = -1
        max_c = -1
        
        for i in range(20):
            for u in range(20):
                if(max < y[i][u]):
                    max = y[i][u]
                    max_r = i
                    max_c = u
        x_test = reshape(20, 20)
        
        for i in range(20):
            for u in range(20):
                if(i == max_r and u == max_c):
                    x_test[i][u] = 1
        
        return x_test
        
    def status_check(self, board):
        for i in range(20):
            for u in range(20):
                if(i + 4 < 20):
                    alpha = 0
                    player = 0
                    
                    for k in range(5):
                        if(board[i + k][u] == 1):
                            alpha += 1
                        elif(board[i + k][u] == -1):
                            player += 1
                    if(alpha == 5):
                        return 1
                    elif(player == 5):
                        return -1
                    
                if(u + 4 < 20):
                    alpha = 0
                    player = 0
                    
                    for k in range(5):
                        if(board[i][u + k] == 1):
                            alpha += 1
                        elif(board[i][u + k] == -1):
                            player += 1
                    if(alpha == 5):
                        return 1
                    elif(player == 5):
                        return -1
                
                if(i + 4 < 20 and u + 4 < 20):
                    alpha = 0
                    player = 0
                    
                    for k in range(5):
                        if(board[i + k][u + k] == 1):
                            alpha += 1
                        elif(board[i + k][u + k] == -1):
                            player += -1
                    if(alpha == 5):
                        return 1
                    elif(player == 5):
                        return -1
                    
        return 0