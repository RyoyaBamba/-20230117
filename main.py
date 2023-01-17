from hanoi import HanoiBoard


def hanoi(n):
    """Solves the "Tower of Hanoi" puzzle for n disks."""

    # Create the board
    board = HanoiBoard(n)

    # Move the tower from peg 0 to peg 1
    move_tower(board, n, 0, 1)


def move_tower(board, height, source, dest):
    """Moves a whole tower of size 'height' from peg 'source' to peg 'dest'.
    Args:
        board (HanoiBoard): Object representing the board
        height (int): Height of the tower to move. It must be between 0 and n (included).
        source (int): Source peg (i.e., in which the tower is originally)
        dest (int):   Destination peg (i.e., where to put the tower)

    Note:
        `source` and `dest` are peg numbers and must be 0, 1, or 2
    """
    spare = 3 - (source + dest)
    if height == 1:
        board.move_disk(source, dest)
    else:
        move_tower(board, height - 1, source, spare)
        board.move_disk(source, dest)
        move_tower(board, height - 1, spare, dest)


    # こちらのコメントの代わりには自分のコードを書きます．
n = int(input("塔の高さを入力してください(自然数で): "))
hanoi(n)
