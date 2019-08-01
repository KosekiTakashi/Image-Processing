from darkflow.net.build import TFNet
import cv2
from matplotlib import pyplot as plt
import numpy as np
import glob
import os
import sys




if __name__ == "__main__":
    options = {"model": "cfg/yolo.cfg", "load": "yolo_weights/yolo.weights", "threshold": 0.1}
    tfnet = TFNet(options)

    files = sorted(glob.glob("soto/*.JPG"))
    for f in files:
        #名前の分割
        file,gazou_name = os.path.split(f)
        name,ext = os.path.splitext(gazou_name)
        imgcv = cv2.imread(f)
        output = imgcv.copy()
        output2 = imgcv.copy()
        test = imgcv.copy()
        height, width, channel = imgcv.shape
        image_size = height * width
        print(name)

        result = tfnet.return_predict(imgcv)

#最大面積とその時の位置を取得
        areas = []
        i=0
        for item in result:
            tlx = item['topleft']['x']
            tly = item['topleft']['y']
            brx = item['bottomright']['x']
            bry = item['bottomright']['y']

            # area
            area = np.abs(brx-tlx)*np.abs(bry-tly)
            if tlx > 200 and tly > 300 and brx < width-200 and bry < height-1000:
                areas.append(area)
                a_max = np.max(areas)
                i+=1
        if i>0:
            print(a_max)
            for item in result:
             tlx = item['topleft']['x']
             tly = item['topleft']['y']
             brx = item['bottomright']['x']
             bry = item['bottomright']['y']
             area = np.abs(brx-tlx)*np.abs(bry-tly)
             if a_max == area and i>0  :
                 ax = tlx
                 ay = tly
                 bx = brx
                 by = bry
        else:
            pass
        if i>0 :
            print('a')
            cv2.rectangle(imgcv, (ax, ay), (bx, by),(0,0,0),50)
            cv2.rectangle(imgcv,(ax, ay), (bx, by) , (0,0,0), cv2.FILLED)
            cv2.imwrite(file+"_cv/"+name+"_m5.jpg",imgcv)
            cut = output[ay :by , ax: bx]
            dst = cv2.rectangle(output2, (0,0), (width,height), (255,200,220), cv2.FILLED)
            output2[ay :by , ax: bx] = cut
            cv2.imwrite(file+"_output3/"+name+"_m5.jpg",output2)
#何もしないで終了
        else:
            pass
