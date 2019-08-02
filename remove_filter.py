import numpy as np

th = 10
r0 = 255
g0 = 150
b0 = 200

f = open("test_pink.ply", 'r')
lines = f.readlines()
f.close()

with open("test_color_pink.ply", mode='w') as f:
    lnum = 0
    point_num = 0
    for l in lines:
        lnum = lnum + 1
        #print(l)
        if lnum >= 14:
            item = l.split(" ")
            r = np.int(item[6])
            g = np.int(item[7])
            b = np.int(item[8])
            #print("r,g,b = ", r, g, b)
            if (np.abs(r-r0) < th) and (np.abs(g-g0) < th) and (np.abs(b-b0) < th):
                continue
            else:
                # 保存
                point_num = point_num + 1
                f.write(l)
                if lnum % 10000 == 0:
                    print(lnum)
        else:
            f.write(l)

f.close()
print(point_num)
