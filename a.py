Width, Height = map(int, input().split())
tmap, location, visted, arrive = []
x, y, cnt = 0


def corret(corret_y, corret_x):
    if location[corret_y][corret_x] == 2:
        arrive.append(cnt)

def right_move(Rmove_y, Rmove_x):
    temp_x = x
    temp_y = y
    if tmap[temp_y][temp_x + 1] == 0:
        temp_x += 1
        down_move(temp_y, temp_x)
    elif tmap[temp_y][temp_x + 1] == 1:
        


def down_move(down_y, down_x):





def nevi(location):
    for Plus_Width in range(Width):
        if tmap[y][x+1] == 0:
            if tmap[y-1][x+1] == 1:
        if tmap[y-1][x] == 0:
            y -= 1



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
