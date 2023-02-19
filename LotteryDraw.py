#不要修改
import pygame #这个软件包需要在终端执行“pip install pygame”进行安装
import sys
import random
import time

#不要修改
class BJ101IDMember:
    def __init__(self, name, group, number):
        self.name = name
        self.group = group
        self.number = number
    def CommandLinePrintPeopleInfo(self):
        print("**Name: ", self.name, "** **Group: ", self.group, "** **Number: ", self.number,"**")
    def GameWindowPrint(self):
        stringInfo = self.name + " (" + self.group + ")"
        return stringInfo

BJ101IDMembers = []

BJ101IDMembers.append(BJ101IDMember("张三","张三的班名",1)) #这里的第三个变量，这个序号，是为了抽到之后方便快速定位删除代码的
BJ101IDMembers.append(BJ101IDMember("李四","李四的班名",2)) #可以模仿这个形式，添加当前学校的所有老师和同学，序号可以跳，但是最好不要重复，否则后期删除已经获奖的同学会相对困难

BJ101IDMembersNumber = len(BJ101IDMembers) #不要修改
print(BJ101IDMembersNumber) #不要修改

#不要修改
def get_random_people(people_number):
    IDNumberList = []
    while len(IDNumberList) < people_number:
        this_random = random.randint(0, BJ101IDMembersNumber - 1)
        selectable = True
        for j in range (0, len(IDNumberList), 1):
            if this_random == IDNumberList[j]:
                selectable = False
        if selectable:
            IDNumberList.append(this_random)
    print("This Cycle Index: ", IDNumberList)
    for i in range (0, len(IDNumberList),1):
        BJ101IDMembers[IDNumberList[i]].CommandLinePrintPeopleInfo()
    print()
    return IDNumberList

pygame.init() #不要修改
mainClock = pygame.time.Clock() #不要修改
WINDOWWIDTH = 1602 #这里是屏幕横向分辨率，最好保留一些余地（例如1920*1080的屏幕不要把这个设置为1920）
WINDOWHEIGHT = 806 #这里是屏幕纵向分辨率，最好保留一些余地（例如1920*1080的屏幕不要把这个设置为1080）
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) #不要修改
bg = pygame.image.load("background.jpeg") #不要修改
font = pygame.font.SysFont("arialunicode", 48) #系统字体，如果出错可以联系我或者查询当前系统有哪些字体
pygame.display.set_caption("抽奖环节！") #不要修改

#不要修改
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, (0, 0, 0))
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#不要修改
def terminate():
    pygame.quit()
    sys.exit()

#不要修改
def ten_people():
    windowSurface.blit(bg,(0,0))
    winnerList = get_random_people(10)
    drawText(BJ101IDMembers[winnerList[0]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 50)
    drawText(BJ101IDMembers[winnerList[1]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 100)
    drawText(BJ101IDMembers[winnerList[2]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 150)
    drawText(BJ101IDMembers[winnerList[3]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 200)
    drawText(BJ101IDMembers[winnerList[4]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 250)
    drawText(BJ101IDMembers[winnerList[5]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 50)
    drawText(BJ101IDMembers[winnerList[6]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 100)
    drawText(BJ101IDMembers[winnerList[7]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 150)
    drawText(BJ101IDMembers[winnerList[8]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 200)
    drawText(BJ101IDMembers[winnerList[9]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 250)
    pygame.display.update()
    time.sleep(0.01)
    pygame.display.flip()

#不要修改
def eight_people():
    windowSurface.blit(bg,(0,0))
    winnerList = get_random_people(8)
    drawText(BJ101IDMembers[winnerList[0]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 50)
    drawText(BJ101IDMembers[winnerList[1]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 100)
    drawText(BJ101IDMembers[winnerList[2]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 150)
    drawText(BJ101IDMembers[winnerList[3]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) - 270, (WINDOWHEIGHT / 3) + 200)
    drawText(BJ101IDMembers[winnerList[4]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 50)
    drawText(BJ101IDMembers[winnerList[5]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 100)
    drawText(BJ101IDMembers[winnerList[6]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 150)
    drawText(BJ101IDMembers[winnerList[7]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 270, (WINDOWHEIGHT / 3) + 200)
    pygame.display.update()
    time.sleep(0.01)
    pygame.display.flip()

#不要修改
def five_people():
    windowSurface.blit(bg,(0,0))
    winnerList = get_random_people(5)
    drawText(BJ101IDMembers[winnerList[0]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 50)
    drawText(BJ101IDMembers[winnerList[1]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 100)
    drawText(BJ101IDMembers[winnerList[2]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 150)
    drawText(BJ101IDMembers[winnerList[3]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 200)
    drawText(BJ101IDMembers[winnerList[4]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 250)
    pygame.display.update()
    time.sleep(0.01)
    pygame.display.flip()

#不要修改
def three_people():
    windowSurface.blit(bg,(0,0))
    winnerList = get_random_people(5)
    drawText(BJ101IDMembers[winnerList[0]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 50)
    drawText(BJ101IDMembers[winnerList[1]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 100)
    drawText(BJ101IDMembers[winnerList[2]].GameWindowPrint(), font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3) + 150)
    pygame.display.update()
    time.sleep(0.01)
    pygame.display.flip()

while True:
    three_people() #是3个人就是three_people，是5个人就是five_people，这里灵活变通一下