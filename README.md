# 2D Chess GUI 

## written using python3 pygame

### pieces are from wiki commons, you can find them right [here](https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent)

### Piece Class

The piece class implements the following functions:
```
p = Piece (<img_path>, (x, y))

# methods
p.move (x, y)
p.clicked(True)
p.draw (screen)
p.capture(opp_x, opp_y)

# constant
p.origin

```
The Piece class implements the functions clicked, draw, capture, and move, because they will operate the same way for every piece.


### Pawn Class (Piece)



maintainer: ```local@kader.email```
