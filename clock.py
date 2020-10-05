class Clock():
    """
    generate a clock
    """

    def __init__(self, lock_gen_array):

        # canvas
        canvas_array = [
            [False, False, False, False, False],  # i = 0 , j =  0 1 2 3 4
            [False, False, False, False, False],  # i = 1 , j =  0 1 2 3 4
            [False, False, False, False, False],  # i = 2 , j =  0 1 2 3 4
            [False, False, False, False, False],  # i = 3 , j =  0 1 2 3 4
            [False, False, False, False, False]   # i = 4 , j =  0 1 2 3 4
        ]

        # generate the lock
        for i in range(5):
            for j in range(5):
                if i + 1 <= lock_gen_array[j]:
                    canvas_array[i][j] = True

        # update the canvas to generate the lock
        self.lock = canvas_array

    def get_lock(self):
        # print(self.lock)
        return self.lock

    def print_lock(self):
        # print the lock in the terminal
        canvas = self.lock
        print(" A B C D E")
        for i in range(5):
            for j in range(5):
                if canvas[i][j] == True:
                    print(" #", end ="")
                else:
                    print(" -", end ="")
            print(" ")