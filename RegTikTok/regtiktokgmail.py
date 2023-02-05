
from time import sleep, time
from CBAutoHelper import ADB
adb = ADB()
devices = adb.GetDevices()
index = 0
for i in devices:
    print(index, i)
ind = int(input('Chọn máy: '))
devices = devices[ind]
def CheckImg(count=10, device="", path=""):
    for i in range(count):
        if adb.TapImg(device, path): break
        sleep(1)

def Reg(mail, pwd):

    adb.DeleteCache(devices, 'com.zhiliaoapp.musically')
    adb.OpenLink(devices, 'tiktok://notification')
    sleep(5)
    adb.OpenLink(devices, 'tiktok://notification')
    adb.OpenLink(devices, 'tiktok://notification')
    adb.OpenLink(devices, 'tiktok://notification')
    adb.OpenLink(devices, 'tiktok://notification')
    adb.OpenLink(devices, 'tiktok://notification')
    sleep(5)
    CheckImg(count=3, device=devices, path="./images/google.png")
    sleep(1)
    CheckImg(count=20, device=devices, path="./images/google2.png")
    sleep(10)
    while True:
        adb.Swipe(devices, 300, 750, 300, -1000)
        if adb.TapImg(devices, "./images/them.png"): break
        sleep(1)
    sleep(5)
    CheckImg(count=10, device=devices, path="./images/mail.png")
    sleep(1)

    adb.InpuText(devices, mail)
    CheckImg(count=10, device=devices, path="./images/tieptheo.png")
    sleep(5)
    adb.InpuText(devices, pwd)
    CheckImg(count=10, device=devices, path="./images/tieptheo.png")
    sleep(5)
    adb.Swipe(devices, 300, 750, 300, -1000)
    CheckImg(count=10, device=devices, path="./images/tip.png")
    sleep(5)

    CheckImg(count=10, device=devices, path="./images/yes.png")
    sleep(10)
    CheckImg(count=20, device=devices, path="./images/ccc.png")

    adb.Swipe(devices, 200, 1057, 200, -1000)
    sleep(1)
    adb.Swipe(devices, 350, 1057, 200, -1000)
    sleep(1)

    adb.Swipe(devices, 500, 1057, 200, 3000)
    sleep(1)

    CheckImg(count=10, device=devices, path="./images/tiep.png")
    sleep(8)
    open("success.txt", "a+").write("%s|%s\n"%(mail, pwd))

for i in open(input("File Path: ")).read().splitlines():
    k = i.split('|')
    print(k)
    Reg(k[0], k[1])