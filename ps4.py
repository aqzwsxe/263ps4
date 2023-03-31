'''
CSC263 Winter 2023
Problem Set 4 Starter Code
University of Toronto Mississauga
'''


# # Do NOT add any "import" statements
def T_move_helper(nrows, ncols, tingting_cur_row, tingting_cur_col):
    move_option = []
    horizontal_move1 = [-1, 1] # Those are the options that Tingting can move
    horizontal_move2 = [-2, 2]
    vertical_move1 = [-1, 1]
    vertical_move2 = [-2, 2]
    for i in vertical_move1:   # Since Tingting's move are (1, 2) (2, 1) (-1, -2) (-2, -1) (-1, 2) (1, -2)
                               # (-2, 1) (2, -1), so there are 2 for loop to generate those move
        test_row = tingting_cur_row + i
        if test_row > nrows - 1 or test_row < 0:
            continue
        for j in horizontal_move2:
            test_col = tingting_cur_col + j
            if test_col > ncols - 1 or test_col < 0:
                continue
            move_option.append((test_row, test_col))

    for i in vertical_move2:
        test_row = tingting_cur_row + i
        if test_row > nrows - 1 or test_row < 0:
            continue
        for j in horizontal_move1:
            test_col = tingting_cur_col + j
            if test_col > ncols - 1 or test_col < 0:
                continue
            move_option.append((test_row, test_col))
    return move_option


def catch_me_if_you_can(nrows, ncols, bahar_row, bahar_col, tingting_row, tingting_col):
    '''
    Return the appropriate string, as described in the handout.
    nrows: number of rows in the board
    ncols: number of columns in the board
    bahar_row/bahar_col: Bahar's starting location
    tingting_row/tingting_col: Tingting's starting location
    '''
    counter = 0

    if_visited = {}  # TingTing should not go to tha position that she has already visited
    b_position = []  # store all the location that Bahar will go to.
    queue = []
    #level = 0
    test_row = bahar_row
    test_col = bahar_col
    while test_row < nrows - 1:
        test_row += 1
        if test_col < ncols - 1:
            test_col += 1
        b_position.append((test_row, test_col))


    # now b_position contains all location that Bahar will go to.
    steps = 0
    queue.append((tingting_row, tingting_col, steps))   # The program terminate iff the queue is empty
    if_visited[(tingting_row, tingting_col)] = True

    while queue != []:
        curr_t = queue.pop(0) # The current position of Tingting
        steps = curr_t[-1]

        # The queue is empty when dequeue the source node. In addition, queue[0][3] != steps when all the node
        # in the current level of the graph are dequeued from the graph.
        if queue == [] or queue[0][-1] != steps:
            temp1 = b_position.pop(0)
            ba_row = temp1[0]
            ba_col = temp1[1]
            if ba_row == (nrows - 1):
                b = "Bahar wins in {} moves".format(steps)
                return b
        steps += 1 # Tingting moves after bahar
        T_option = T_move_helper(nrows, ncols, curr_t[0], curr_t[1])
        # a list contain the row and col that TingTing can move to from the current position

        while len(T_option) != 0:
            temp = T_option.pop(0)
            ting_row = temp[0]
            ting_col = temp[1]
            if (ting_row, ting_col) == (ba_row, ba_col):
                a = "Tingting wins in {} moves".format(steps)
                return (a)
            if (ting_row, ting_col) not in if_visited:
                queue.append((ting_row, ting_col, steps))
                if_visited[(ting_row, ting_col)] = True
    b = "Bahar wins in {} moves".format(steps)
    return b





if __name__ == '__main__':

  # some small test cases
  # Case 1, Tingting wins in 2 moves
  s = catch_me_if_you_can(50, 50, 10, 10, 10, 12)
  print(s)
  assert s == 'Tingting wins in 2 moves'
  # Case 2, Bahar wins in 1 moves
  s = catch_me_if_you_can(6, 8, 3, 3, 0, 0)
  print(s)
  assert s == 'Bahar wins in 1 moves'

  s = catch_me_if_you_can(100, 100, 10, 10, 10, 12)
  print(s)
  assert s == 'Tingting wins in 2 moves'