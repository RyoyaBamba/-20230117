#
# TODO: (HW)
# 問１. power64aとpower64bの繰り返しは何回？
#答. power64aは63回、power64bは6回
#
# 問２.
# 1. next_matrixの計算量はnに対して何のオーダー？　答.O(n^3)
# 2. sp_lengthの計算量はnに対して何のオーダー？　答.O(n^4)
# 3. sp_lengthをより早い方法で書き直す．以下のコードに答える．
# 4. 考えた方法で，sp_lengthの計算量はnに対して何のオーダーとなった？　答.O(n^3logn)
# (optional) グラフのデータを弄って、再計算を行う
#   例：雪のため、溝の口から武蔵小杉の説速は通行止めになると、八王子から羽田までの最短距離はどのくらい影響がありますか？　答.影響なし
#   例：蒲田と京急蒲田の間に新しい接続ができた場合は、どこが羽田まで早くなりますか？　答.武蔵小杉、自由が丘、大岡山、川崎、大井町、横浜、菊名、すずかけ台、長津田、溝の口、二子玉川、多摩川、蒲田
#   ...
#
# TODO: (Quiz)
# 1. read the code of next_matrix() and find its complexity
# 2. read the code of sp_length() and find its complexity

INFTY       = 999999

VERTICES = [
        "武蔵小杉(Musashi-Kosugi)",
        "自由が丘(Jiyugaoka)",
        "大岡山(Ookayama)",
        "川崎(Kawasaki)",
        "渋谷(Shibuya)",
        "新宿(Shinjuku)",
        "目黒(Meguro)",
        "大井町(Oimachi)",
        "品川(Shinagawa)",
        "東京(Tokyo)",
        "池袋(Ikebukuro)",
        "大宮(Omiya)",
        "上野(Ueno)",
        "横浜(Yokohama)",
        "菊名(Kikuna)",
        "すずかけ台(Suzukakedai)",
        "長津田(Nagatsuta)",
        "溝の口(Mizonokuchi)",
        "八王子(Hachioji)",
        "立川(Tachikawa)",
        "二子玉川(Futakotamagawa)",
        "多摩川(Tamagawa)",
        "蒲田(Kamata)",
        "京急蒲田(Keikyu-Kamata)",
        "羽田空港(Haneda airport)"
]

DISTANCES = [
        [    0, INFTY, INFTY,    13, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    10, INFTY, INFTY,    10, INFTY, INFTY,   INFTY,     3, INFTY, INFTY, INFTY],
        [INFTY,     0,     2, INFTY,     9, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,       6,     4, INFTY, INFTY, INFTY],
        [INFTY,     2,     0, INFTY, INFTY, INFTY,     6,    12, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY,     5, INFTY, INFTY, INFTY],
        [   13, INFTY, INFTY,     0, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    12, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY,     6,    10, INFTY],
        [INFTY,     9, INFTY, INFTY,     0,     7,     5, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,      10, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY,     7,     0, INFTY, INFTY, INFTY,    13,    14, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    24,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY,     6, INFTY,     5, INFTY,     0,     8,     7, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY,    12, INFTY, INFTY, INFTY,     8,     0,     8, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY,     6, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,     7,     8,     0,    14, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY,     7, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY,    13, INFTY, INFTY,    14,     0, INFTY, INFTY,     8, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY,    14, INFTY, INFTY, INFTY, INFTY,     0,    26,    17, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    26,     0,    26, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,     8,    17,    26,     0, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY,    12, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,     0,     6, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [   10, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,     6,     0, INFTY,    16, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,     0,     4, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    16,     4,     0,    17,    32, INFTY,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [   10, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    17,     0, INFTY,    35,       2, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    32, INFTY,     0,    10,   INFTY, INFTY, INFTY, INFTY, INFTY],
        [INFTY, INFTY, INFTY, INFTY, INFTY,    24, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,    35,    10,     0,   INFTY, INFTY, INFTY, INFTY, INFTY],

        [INFTY,     6, INFTY, INFTY,    10, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,     2, INFTY, INFTY,       0, INFTY, INFTY, INFTY, INFTY],
        [    3,     4,     5, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY,     0,    11, INFTY, INFTY],
        [INFTY, INFTY, INFTY,     6, INFTY, INFTY, INFTY,     6, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY,    11,     0, INFTY, INFTY],
        [INFTY, INFTY, INFTY,    10, INFTY, INFTY, INFTY, INFTY,     7, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY,     0,    12],
        [INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY, INFTY,   INFTY, INFTY, INFTY,    12,     0]
]


#
# GRAPH CALCULATIONS
#

def next_matrix(matX, matY):
    n = len(matX)
    matZ = [ [0] * n for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            tmp = INFTY
            for k in range(n):
                d = matX[i][k] + matY[k][j]
                tmp = min(tmp, d)
            matZ[i][j] = tmp
    return matZ


def sp_length(matA):
    #
    # Minplus algorithm
    #
    # TODO: improve complexity
    n = len(matA)
    matD = [ [ matA[i][j] for j in range(n) ] for i in range(n) ]
    t = 1
    while t < n-1:
        matD = next_matrix(matD, matD)
        t = t * 2
    return matD


#
# OUTPUT
#

def print_distance_matrix(names, dist):
    # prints a distance matrix with node names
    # in:
    #    - names    string vector s.t. names[i] is the name of node i
    #    - dist     distance matrix of the graph
    for i, from_name in enumerate(names):
        print(f"{from_name}:")
        for j, to_name in enumerate(names):
            if (dist[i][j] != INFTY) and (i != j):
                print(f"    --( {dist[i][j]} )--> {to_name}")


#
# MAIN PROGRAM
#
all_pairs_distance = None

print("Adjacency distance matrix:")
print("-------------------------")
print_distance_matrix(VERTICES, sp_length(DISTANCES))

# TODO: remove comment below
# all_pairs_distance = sp_length(DISTANCES)

if all_pairs_distance:
    print()
    print()
    print("All pairs distance matrix:")
    print("-------------------------")
    print_distance_matrix(VERTICES, sp_length(DISTANCES))
