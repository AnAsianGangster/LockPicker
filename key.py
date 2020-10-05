class Key():
    """
    generate a key
    """

    def __init__(self, key_gen_array):

        # canvas
        canvas_array = [
            [False, False, False, False, False],  # i = 0 , j =  0 1 2 3 4
            [False, False, False, False, False],  # i = 1 , j =  0 1 2 3 4
            [False, False, False, False, False],  # i = 2 , j =  0 1 2 3 4
            [False, False, False, False, False],  # i = 3 , j =  0 1 2 3 4
            [False, False, False, False, False]   # i = 4 , j =  0 1 2 3 4
        ]

        # generate the key
        for i in range(5):
            for j in range(5):
                if i > 4 - key_gen_array[j]:
                    canvas_array[i][j] = True

        # update the canvas to generate the key
        self.key = canvas_array

    def get_key(self):
        # print(self.key)
        return self.key

    def print_key(self):
        # print the key in the terminal
        canvas = self.key
        for i in range(5):
            for j in range(5):
                if canvas[i][j] == True:
                    print(" #", end ="")
                else:
                    print(" -", end ="")
            print(" ")
        print(" A B C D E")