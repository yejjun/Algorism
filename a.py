Width, Height = map(int, input().split())
tmap, location, visited, arrive = []
x, y, cnt = 0

def corret(corret_y, corret_x): # 도착지점 도착시 arrive에 추가
    if location[corret_y][corret_x] == 2:
        arrive.append(cnt)

def right_move(Rmove_y, Rmove_x): 
    temp_x = x
    temp_y = y
    if tmap[temp_y][temp_x + 1] == 0:
        temp_x += 1
        down_move(temp_y, temp_x)
    elif tmap[temp_y][temp_x + 1] == 1:
        if tmap[temp_y+1][temp_x + 1] == 0:
            temp_y += 1
            temp_x += 1
        elif tmap[temp_y][temp_x + 1] == 1:
            visited.append(tmap[temp_y][temp_x+1])

def down_move(down_y, down_x):
    while True:
        if tmap[down_y-1][down_x] == 0: # 만약 아래 블록이 0이면 아래로 한 칸
            down_y -= 1
        elif tmap[down_y-1][down_x] == 1:


def nevi(location):
    for Plus_Width in range(Width):
        if tmap[y][x+1] == 0:
            if tmap[y-1][x+1] == 1:
        if tmap[y-1][x] == 0:
            y -= 1

def move(temp_x, temp_y)
    
    if d=
    



for a in range(Height): 
    save = list(map(int, input().split())) # 지도 입력
    tmap.append(save)

for y in range(Height):  # 현재 위치
    for x in range(Width):
        if tmap[x][y] == 3:
            location.append(x)
            location.append(y)
            break

while True: # 만약 시작지점 밑이 0이면 바닥까지 내려감
    if location[0] == 0:
        location[0] -= 1
        y -= 1
    elif location[0] == 1:
        break
print(location)
