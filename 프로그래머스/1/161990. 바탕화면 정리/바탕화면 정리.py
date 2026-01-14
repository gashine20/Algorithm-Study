def solution(wallpaper):
    answer = []
    
    # 배열에 다시 담을까 
    # 뒤면 +1 
    
    file = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                file.append([i,j])
     
    lux = file[0][0] # x 좌표 최소
    rdx = file[len(file)-1][0] + 1 # x 좌표 최대 +1
    
    file.sort(key=lambda x: (x[1], x[0]))
    luy = file[0][1] # y좌표 최소 
    rdy = file[len(file)-1][1] +1 # y 좌표 최대 +1
    
    answer = [lux, luy, rdx, rdy]
    #print(file)
    
    return answer