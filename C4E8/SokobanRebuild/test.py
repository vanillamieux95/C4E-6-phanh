from models.gamemodel import GameModel

#units test

#test 1
game_model = GameModel(2, 3)
game_model.print()

#test 2
game_model.x = 1
game_model.y = 2
game_model.move(2, -3)
#assert: to test if there's anything wrong in code, testing if it's wrong => error immediately
assert (game_model.x == 3) and (game_model.y == -1)

#test 3
game_model.x = 2
game_model.y = 4
[next_x, next_y] = game_model.next_pos(2, 7)
#check to see if the equation is true
assert (next_x == 4) and (next_y == 11)
#check to see if value change or not
assert (game_model.x == 2) and (game_model.y == 4)