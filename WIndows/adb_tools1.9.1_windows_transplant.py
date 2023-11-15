import os
import time
os.system("cls")
a = 0
def clear(t):
    time.sleep(t)
    os.system("cls")
toolkit = ["1.查看连接设备","2.高级重启","3.检查ADB版本","4.屏幕工具","5.软件包管理","6.一键激活Shizuku","7.模拟按键模式","8.模拟键盘输入(EN only)","9.推送/拉取文件","10.adb终端","11.无线调试设置"]
text = """               ****************************
               *搞机工具箱 on Python V1.9.1*
               ****************************"""
while True :
    print(text)
    for p in range(0,len(toolkit)) :
        print(toolkit[p])
    print("输入其他数字重启ADB服务\n直接按下回车退出")
    print("您正在使用Windows移植版,请确保ADB环境变量已正确设置")
    print("输入233查看环境变量配置帮助")
    a = int(input("输入功能序号："))
    if a == 1 : #check device
        os.system("adb devices")
        clear(1)
        
        
    elif a == 2 : #reboot
        answer = input("1.fastboot 2.recovery 3.9008（其他输入将会正常重启）")
        if answer == 1 :
            os.system("adb reboot bootloader")
            clear(1)
        elif answer == 2 :
            os.system("adb reboot bootloader")
            clear(1)
        elif answer == 3 :
            os.system("adb reboot edl")
            clear(1)
        else :
            os.system("adb reboot")
            clear(1)


    elif a == 3 : #adb VER
        os.system("adb version")
        clear(2)
    
    
    elif a == 4 : #display
        b = int(input("1.分辨率2.dpi"))
        if b == 1 :
            wmanswer = int(input("1.设置分辨率 2.还原至默认分辨率"))
            if wmanswer == 1 :
                print("请输入：")
                l = input("长")
                s = input("宽")
                cm = "adb shell wm size " + l + "x" + s
                os.system( cm )
                clear(1)
            elif wmanswer == 2 :
                os.system("adb shell wm size reset")
                clear(1)
        elif b == 2 :
            secwmanswer = int(input("1.设置dpi 2.恢复默认"))
            if secwmanswer == 1 :
                dpi = str(input("输入"))
                os.system("adb shell wm density " + dpi)
                clear(0)
            elif secwmanswer == 2 :
                os.system("adb shell wm density")
                clear(0)
    
    elif a == 5 : #package manager
        inp = str(input("1.列出已安装的包,2.安装apk,3.卸载软件,4.禁用软件,5.提取APK\n"))
        if inp == "1" : #list packages
            os.system("adb shell pm list packages")
            input("")
            clear(0)
        
        elif inp == "2" : #install package
            u = input("输入APK包所在的路径:")
            c = "adb install "
            r = str(input("是否允许覆盖安装y/n:")) #cover
            if r == "y" :
                c += "-r "
            d = str(input("是否降级安装y/n:")) #up to down
            if d == "y" :
                c += "-d "
            os.system( c + u )
            clear(1)
        elif inp == "3" :#uninstall package
            u = input("输入包名:")
            c = "adb shell pm uninstall "
            r = str(input("是否为系统应用y/n:")) #sys app
            if r == "y" :
                c += "-- user 0 "
            d = str(input("是否保数据卸载y/n:")) #save data
            if d == "y" :
                c += "-k "
            os.system( c + u )
            clear(1)
        elif inp == "4" : #disable app
            print("已禁用的app:\n")
            os.system("adb shell pm list packages -d")
            print("")
            pn = str(input("要禁用的软件的包名:"))
            os.system("adb shell pm disable-user " + pn)
            print("完成")
            clear(1)
        if inp == "5" : #pull apk
            def apk() :
                pn = str(input("要提取的app包名:\n(按回车查看已安装的app,输入0退出)"))
                if inp == "0" :
                    print('已退出')
                    clear(1)
                elif pn == "" :
                    os.system("adb shell pm list packages")
                    input("按回车关闭")
                    clear(0)
                    apk()
                elif pn != '0' or '' :
                    path = os.popen("adb shell pm path " + pn ).read()
                    apkpath = ""
                    for i in range(8,len(path)):
                        apkpath += path[i]
                    os.system("adb pull " + apkpath + " ~")
                    print("已保存至用户目录!")
                    clear(2)
            apk()
            clear(0)

            
    elif a == 6 : #shizuku
        os.system("adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh")
        print("操作完成!")
        clear(1)
    
    
    elif a == 7 : #virtual key
        while True :
            key = input("1.返回 2.home 3.多任务 输入其他以退出模拟按键模式")
            if key == "1" :
                os.system("adb shell input keyevent KEYCODE_BACK")
                clear(0)
            elif key == "2" :
                os.system("adb shell input keyevent KEYCODE_HOME")
                clear(0)
            elif key == "3" :
                os.system("adb shell input keyevent KEYCODE_APP_SWITCH")
                clear(0)
            else:
                print("已退出")
                clear(1)
                break
    
    
    elif a == 8 : #virtual input
        k = str(input("模拟输入:（空格使用“%s”代替）"))
        kk = "adb shell input text" + k
        os.system(kk)
        os.system("clear")    
    

    elif a == 9 : #file
        pu = str(input("1.推送 2.拉取:"))
        if pu == "1" :
            ptc = str(input("文件绝对路径:"))
            ptp = str(input("推送到哪里:"))
            cmd = "adb push " + ptc+ " " + ptp
            os.system(cmd)
            clear(2)
            
        elif pu == "2" :
            ptc = str(input("文件绝对路径:"))
            ptp = str(input("保存到哪里:"))
            cmd = "adb pull " + ptp+ " " + ptc
            os.system(cmd)
            clear(2)
    
    
    elif a == 10 : #shell
        os.system("adb shell")
        clear(0)
    
    elif a == 233 : #ENV 
        print("环境变量配置帮助\n按下Windows徽标键,搜索环境变量并打开,点击环境变量.在下方框框内单击path,点击右下角的编辑,在新窗口内点击新建,粘贴你的platform-tool路径,三个窗口都点击确定即可\n按下回车关闭...")
        input('')
        clear(0)

    elif a == 11 : #wireless debug
        inp = str(input("1.开启2.连接\n"))
        if inp == "1" :
            os.system("adb tcpip 5555")
            print("成功在设备5555号端口上启用无线adb!")
            clear(1)
        if inp == "2" :
            ip = str(input("设备ip地址:"))
            os.system("adb connect " + ip + ":5555")
            print("操作完成!")
            clear(1)
    
    else : #reboot adb
        os.system("taskkill /f /IM adb.exe")
        print("成功重启ADB服务！")
        clear(2)
