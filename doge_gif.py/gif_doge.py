# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from PIL import Image,ImageSequence
from PIL import Image,ImageDraw,ImageFont
import imageio



gif = Image.open(r'sample.gif')
if os.path.exists("output") == False:         #判断该文件夹是否存在，如果存在再创建则会报错
    os.mkdir("output")
    for i,frame in enumerate(ImageSequence.Iterator(gif),1):
        frame.save(r'output/%d.png' % i)

def text_to_Image(text, image, position, font_size, font_color):
    img_PIL = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    font = ImageFont.truetype("simhei.ttf", font_size,encoding="utf-8")
    draw = ImageDraw.Draw(img_PIL)
    draw.text(position,text,fill = font_color,font = font)
    image = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    return image


def change_text(num1,num2,font,add_x,add_y,text):
    global x1, x2, y1, y2
    for i in range(num1,num2+1):
        # change_flag = 0
        img = cv2.imread("output/%d.png" % i)
        #去文字和写文字操作
        # roi = img[x1:x2,y1:y2]
        # roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
        print x1,y1,x2,y2
        for x in range(x1,x2):
            for y in range(y1,y2):
                img[y,x] = [200,200,200]
        #cv2.putText(img, text, (x1, y2), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0),2)

        image = text_to_Image(text,img,(x1+ add_x,y1+add_y),font,(0,0,0))
        cv2.imshow("ss",image)
        cv2.imwrite("output/%d.png" % i,image)


def resize_frames(path,wid,hig):
    for i in range(1,167):
        image = cv2.imread(path+"/%d.png" % i)
        res = cv2.resize(image,(int(image.shape[1]/wid), int(image.shape[0]/hig)), interpolation=cv2.INTER_AREA)
        cv2.imwrite("outputRES/%d.png" % i,res)
    print image.shape
    print res.shape



def MouseHandle(event,x,y,flags,param):
    global img
    global  click_num
    global change_flag
    global x1, x2, y1, y2
    if event == cv2.EVENT_LBUTTONDOWN:
        click_num += 1
        print "left click"
        if click_num == 1:
            x1,y1 = x,y
            print  click_num,'(',x1,y1,')'
        if click_num == 2:
            x2,y2 = x,y
            print click_num,'(',x2,y2,')'
    elif event == cv2.EVENT_RBUTTONDOWN:
        if click_num >= 2:
            click_num = 0
            change_flag += 1
            print change_flag
            if change_flag == 1:
                change_text(27, 36,20,8,2 ,u"就算你人头抢的再多")          #前面加 u 才不会乱码

                img = cv2.imread("output/44.png")
                cv2.imshow("img", img)
            if change_flag == 2:
                change_text(44, 60,20,8,2 , u"就算你经济再好")  # 少2

                img = cv2.imread("output/62.png")
                cv2.imshow("img", img)
            if change_flag == 3:
                change_text(62, 80,20,8,2 , u"我想举报就举报")  #少2

                img = cv2.imread("output/83.png")
                cv2.imshow("img", img)
            if change_flag == 4:
                change_text(82, 93,20,0,2, u"谁叫我是峡谷暴躁姜呢")  #少0

                img = cv2.imread("output/97.png")
                cv2.imshow("img", img)
            if change_flag == 5:
                change_text(97, 105,20,0,2 , u"那你了不起啊")  #少0

                img = cv2.imread("output/112.png")
                cv2.imshow("img", img)
            if change_flag == 6:
                change_text(112, 131,20,0,2 , u"呵！我在这真的可以为所欲为")  # 多1

                img = cv2.imread("output/146.png")
                cv2.imshow("img", img)
            if change_flag == 7:
                #change_text(146, 157,20,0,2 , u"以后就让他刷野")  # 少0
                change_text(146, 157,20,0,2 , u"等会全都举报了")  # 少0

                img = cv2.imread("output/158.png")
                cv2.imshow("img", img)
            if change_flag == 8:
     #           change_text(158, 167,20,0,2 , u"一直刷")  # 少0
                change_text(158, 167,20,0,2 , u"全部举报")  # 少0








def create_gif(gif_name, path, duration = 0.3):
    frames = []
    image_list = []
    for i in range(1,167):
        image_list.append(path+"/%d.png" % i)
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

x1 = 0
x2 = 0
y1 = 0
y2 = 0
change_flag = 0
click_num = 0

# cv2.namedWindow('img',cv2.WINDOW_NORMAL)
# cv2.setMouseCallback("img", MouseHandle)
# img = cv2.imread("output/%d.png" % 27)
# cv2.imshow("img",img)


# gif_name = 'created_gif_mini.gif'
# path = 'output'  # 指定文件路径
# duration = 0.1
# create_gif(gif_name, path, duration)

resize_frames("output",2,2)
create_gif("res.gif","outputRES",0.08)

cv2.waitKey(0)
cv2.destroyAllWindows()
