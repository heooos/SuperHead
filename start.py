# coding:utf-8
import screenshot,os,time
from PIL import Image
import pytesseract 

# w = 1080
# h = 1920


def crop():
    '''
    将截图分割为各小部分并进行识别
    :return:
    '''
    for i in range(0, 49, 1):
        region = im.crop(h_loc[i])
        # region.save("./test{}.png".format(i))  #测试时可打开，检测截图是否成功
        mem_pic["test{}".format(i)] = region
        img_handle(i)


def touch(loc):
    '''
    adb操作手机屏幕方法
    :param loc:位置信息
    :return:
    '''
    cmd = 'adb shell input tap {x} {y}'.format(
        x=loc[0],
        y=loc[1],
    )
    os.system(cmd)


def img_handle(index):
    '''
    对单一图像进行识别 存储
    :param index:
    :return:
    '''
    global key_list
    m = mem_pic["test{}".format(index)]
    ltext = pytesseract.image_to_string(m, config="-psm 7 digits")
    print ltext              # 测试时打开，检测是否识别成功
    key_list[ltext] = h_px[index]


def start():
    for i in range(1,50,1):
        #print key_list[str(i)]
        touch(key_list[str(i)])


# 截图分割区域 共49个截图
h_loc = ((62,652,184,778),(200,652,324,778),(340,652,458,778),(480,652,598,778),(614,652,736,778),(754,652,872,778),(892,652,1012,778),
         (62,804,184,926),(200,804,324,926),(340,804,458,926),(480,804,598,926),(614,804,736,926),(754,804,872,926),(892,804,1012,926),
         (62,950,184,1070),(200,950,324,1070),(340,950,458,1070),(480,950,598,1070),(614,950,736,1070),(754,950,872,1070),(892,950,1012,1070),
        (62,1100,184,1220),(200,1100,324,1220),(340,1100,458,1220),(480,1100,598,1220),(614,1100,736,1220),(754,1100,872,1220),(892,1100,1012,1220),
        (62,1240,184,1360),(200,1240,324,1360),(340,1240,458,1360),(480,1240,598,1360),(614,1240,736,1360),(754,1240,872,1360),(892,1240,1012,1360),
        (62,1390,184,1510),(200,1390,324,1510),(340,1390,458,1510),(480,1390,598,1510),(614,1390,736,1510),(754,1390,872,1510),(892,1390,1012,1510),
        (62,1540,184,1660),(200,1540,324,1660),(340,1540,458,1660),(480,1540,598,1660),(614,1540,736,1660),(754,1540,872,1660),(892,1540,1012,1660))
# 截图位置中心 点击
h_px = ((128,722),(262,722),(404,722),(540,722),(680,722),(820,722),(956,722),
        (128,866),(262,866),(404,866),(540,866),(680,866),(820,866),(956,866),
        (128,1010),(262,1010),(404,1010),(540,1010),(680,1010),(820,1010),(956,1010),
        (128,1160),(262,1160),(404,1160),(540,1160),(680,1160),(820,1160),(956,1160),
        (128,1310),(262,1310),(404,1310),(540,1310),(680,1310),(820,1310),(956,1310),
        (128,1450),(262,1450),(404,1450),(540,1450),(680,1450),(820,1450),(956,1450),
        (128,1600),(262,1600),(404,1600),(540,1600),(680,1600),(820,1600),(956,1600))

'''
c_s_time = time.time()
# 截图并上传
screenshot.check_screenshot()
screenshot.pull_screenshot()
c_e_time = time.time()
print '截图耗时{}s'.format(c_e_time - c_s_time)
'''
im = Image.open(r"./screenshot.png")

# 截图存储dict
mem_pic ={}
# 存储数字与位置对应信息dict
key_list = {}
h_s_time = time.time()
# 截图并处理
crop()
h_e_time = time.time()
print '识别耗时{}s'.format(h_e_time - h_s_time)

a_s_time = time.time()
# 执行adb操作
start()
a_e_time = time.time()
print 'adb操作耗时{}s'.format(a_e_time - a_s_time)
