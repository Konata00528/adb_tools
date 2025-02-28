import os
import time
os.system("cls")
cache = ''
a = 0
file_path = '/sdcard'
adb = 'cd ./tools && '
def clear(t):
    timeout = 'timeout /T '+ str(t) + ' /nobreak'
    os.system(timeout)
    os.system("cls")
toolkit = ["1.查看连接设备","2.高级重启","3.检查ADB版本","4.屏幕工具","5.软件包管理","6.一键激活Shizuku","7.模拟按键模式","8.模拟键盘输入(EN only)","9.文件管理","10.adb终端","11.无线调试设置","12.ADB录屏","13.ADB投屏"]
text = """               *****************************
               *搞机工具箱 on Python V2.0.0*
               *****************************"""
while True :
    os.system('cls')
    print(text)
    for p in range(0,len(toolkit)) :
        print(toolkit[p])
    print("输入其他数字重启ADB服务\n直接按下回车退出")
    print("您正在使用Windows移植版,当前内置ADB版本1.0.41")
    a = int(input("输入功能序号："))
    if a == 1 : #check device
        os.system(adb + "adb devices")
        clear(1)
        
        
    elif a == 2 : #reboot
        answer = input("1.fastboot 2.recovery 3.9008(其他输入将会正常重启）")
        if answer == 1 :
            os.system(adb + "adb reboot bootloader")
            clear(1)
        elif answer == 2 :
            os.system(adb + "adb reboot bootloader")
            clear(1)
        elif answer == 3 :
            os.system(adb + "adb reboot edl")
            clear(1)
        else :
            os.system(adb + "adb reboot")
            clear(1)


    elif a == 3 : #adb VER
        os.system(adb + "adb version")
        clear(2)
    
    
    elif a == 4 : #display
        b = int(input("1.分辨率2.dpi"))
        if b == 1 :
            wmanswer = int(input("1.设置分辨率 2.还原至默认分辨率"))
            if wmanswer == 1 :
                cache = os.popen(adb + 'adb shell wm size').read()
                nr = ''
                for i in range(15,len(cache)):
                    nr = nr + cache[i]
                print('当前分辨率:' + nr)
                print("请输入")
                l = input("宽")
                s = input("高")
                cm = "adb shell wm size " + l + "x" + s
                os.system( adb +  cm )
                recover = input('是否保留设置y/n')
                if recover == 'n' :
                    os.system(adb + 'adb shell wm size '+ nr)
                clear(1)
            elif wmanswer == 2 :
                os.system(adb + "adb shell wm size reset")
                clear(1)
        elif b == 2 :
            secwmanswer = int(input("1.设置dpi 2.恢复默认"))
            if secwmanswer == 1 :
                cache = os.popen(adb + 'adb shell wm density').read()
                ndpi = ''
                for i in range(17,len(cache)):
                    ndpi = ndpi + cache[i]
                print('当前dpi:' + ndpi )
                dpi = str(input("输入"))
                os.system(adb + "adb shell wm density " + dpi)
                recover = input('是否保留设置y/n')
                if recover == 'n' :
                    os.system(adb + 'adb shell wm density '+ ndpi)
                clear(1)
            elif secwmanswer == 2 :
                os.system(adb + "adb shell wm density reset")
                clear(1)
    
    elif a == 5 : #package manager
        inp = str(input("1.列出已安装的包,2.安装apk,3.卸载软件,4.禁用/解禁软件,5.提取APK,6.查看前台Activity\n"))
        if inp == "1" : #list packages
            os.system(adb + "adb shell pm list packages")
            input("按下回车退出")
            clear(0)
        
        elif inp == "2" : #install package
            u = input("输入APK包所在的路径(例如D:/):")
            c = "adb install "
            r = str(input("是否允许覆盖安装y/n:")) #cover
            if r == "y" :
                c += "-r "
            d = str(input("是否降级安装y/n:")) #up to down
            if d == "y" :
                c += "-d "
            os.system(adb +  c + u )
            clear(1)
        elif inp == "3" :#uninstall package
            u = input("输入包名")
            c = "adb shell pm uninstall "
            r = str(input("是否为系统应用y/n:")) #sys app
            if r == "y" :
                c += "-- user 0 "
            d = str(input("是否保数据卸载y/n:")) #save data
            if d == "y" :
                c += "-k "
            os.system(adb +  c + u )
            clear(2)
        elif inp == "4" : #disable app
            print("已禁用的app:\n")
            disable = os.popen(adb + "adb shell pm list packages -d").read()
            print(disable)
            pn = str(input("要禁用/解禁的软件的包名:"))
            if pn in disable :
                os.system(adb + 'adb shell pm enable ' + pn)
                print("已解禁")
            else :
                os.system(adb + "adb shell pm disable-user " + pn)
                print("已禁用")
            clear(1)
        elif inp == "5" : #pull apk
            def apk():
                while True:
                    pn = input("要提取的app包名:\n(按回车查看已安装的app,输入0退出)")
                    if pn == "0":
                        print('已退出')
                        break
                    elif pn == "":
                        os.system(f"{adb}adb shell pm list packages")
                        input("按回车关闭")
                        clear(0)
                        continue
                    else:
                        path = os.popen(f"{adb}adb shell pm path {pn}").read()
                        apkpath = ""
                        for i in range(8, len(path)):
                            apkpath += path[i]
                        apkpath = apkpath.strip()
                        pts = input('保存到哪里:')
                        os.system(f"{adb}adb pull {apkpath} {pts}")
                        print(f"已保存至{pts}")
                        clear(2)
                        break
            apk()
            clear(0)
        elif inp == "6" : #activity
            def activity(): 
                clear(0)
                os.system(adb + 'adb shell "dumpsys activity top | grep "ACTIVITY""')
            ex = ''
            while ex == '' :
                ex = str(input('按下回车刷新,输入任意字符退出'))
                if ex == '' :
                    activity()
            clear(0)
    elif a == 6 : #shizuku
        os.system(adb + "adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh")
        print("操作完成!")
        clear(1)
    
    
    elif a == 7 : #virtual key
        while True :
            key = input("1.返回 2.home 3.多任务 输入其他以退出模拟按键模式")
            if key == "1" :
                os.system(adb + "adb shell input keyevent KEYCODE_BACK")
                clear(0)
            elif key == "2" :
                os.system(adb + "adb shell input keyevent KEYCODE_HOME")
                clear(0)
            elif key == "3" :
                os.system(adb + "adb shell input keyevent KEYCODE_APP_SWITCH")
                clear(0)
            else:
                print("已退出")
                clear(1)
                break
    
    
    elif a == 8 : #virtual input
        k = str(input("模拟输入:"))
        kk = "adb shell input text " + k
        os.system(adb + kk)
        clear(0)   
    

    elif a == 9 : #file_manager
        def correct (v,f) : #一个纠正路径的函数,v为输入变量,f是否将输出重新赋值(关闭会直接将正确路径赋值给filepath)
            global file_path
            if v[0] != '/' :
                if f == 1:
                    v = file_path + v
                else :
                    file_path += v
            else :
                if f == 0 :
                    file_path = v
                else :
                    v = v
                    print(2)
            if file_path[len(file_path) - 1] != '/' :
                file_path += '/'
        while True :
            os.system("cls")
            print('''                    *****************
                    *konata file MGR*
                    *****************''')
            time.sleep(1)
            if file_path[len(file_path) - 1] != '/' :
                file_path += '/'
            print("*your dir:",file_path)
            time.sleep(0.5)
            os.system(adb + 'adb shell ls -a ' + file_path)
            act = str(input("[c]change dir   [cp]copy a file\n[m]move a file   [r]remove a file\n[rn]rename a file   [mf]make a folder\n [e]edit with vim\n[dl]download a file [ul]upload a file\npress enter to exit\n"))
            if act == "c" :
                path = str(input("where do you want to go?\n"))
                correct (path,0)
            elif act == "cp" : #copy
                fn = str(input("file:\n"))
                if fn[0] != '/' :
                    fn = file_path + fn
                else :
                    fn = fn
                wh = str(input("where do you want to copy?\n"))
                if wh[0] != '/' :
                    wh = file_path + wh
                else :
                    wh =wh
                os.system(adb + 'adb shell cp -i  -r ' + fn + " " + wh)
                print("Done!")
                time.sleep(0.5)
                os.system("cls")
            elif act == "m" : #move
                fn = str(input("file:\n"))
                if fn[0] != '/' :
                    fn = file_path + fn
                else :
                    fn = fn
                wh = str(input("where do you want to move?\n"))
                if wh[0] != '/' :
                    wh = file_path + wh
                else :
                    wh = wh
                os.system(adb + 'adb shell mv -i -f ' + fn + " " + wh)
                time.sleep(0.5)
                os.system("cls")
            elif act == "r" : #remove
                fn = str(input("what's the file do you want  to remove?\n"))
                if fn[0] != '/' :
                    fn = file_path + fn
                else :
                    fn = fn
                if fn == "/" :
                    print("you can't remove \"/\"!")
                os.system(adb + 'adb shell rm -rf ' + fn)
                time.sleep(0.5)
                os.system("cls")
            elif act == "mf" : #makefolder
                fdn = str(input("what's the new folder's name?\n"))
                if fdn[0] != '/' :
                    fdn = file_path + fdn
                else :
                    fdn = fdn
                os.system(adb + 'adb shell mkdir ' + fdn)
                print("Done!")
                time.sleep(0.5)
                os.system("cls")

            elif act == "rn" : #rename
                fn = str(input("file:\n"))
                if fn[0] != '/' :
                    fn = file_path + fn
                else : 
                    fn = fn
                nfn = str(input("what's the new file name?\n"))
                if nfn[0] != '/' :
                    nfn = file_path + nfn
                else : 
                    nfn = nfn
                os.system(adb + 'adb shell mv -i -f ' + fn + ' ' + nfn)
                time.sleep(1)
                print("Done!")
                time.sleep(0.5)
                os.system("cls")
            elif act == "dl" : #download file
                fn = fn = str(input("file:\n"))
                if fn[0] != '/' :
                    fn = file_path + fn
                else : 
                    fn = fn
                wh = str(input('where do you want to save:'))
                os.system(adb + 'adb pull ' + fn + ' ' + wh)
            elif act == "ul" : #upload file
                wh = str(input('local file:'))
                fn = fn = str(input("devise file:\n"))
                if fn[0] != '/' :
                    fn = file_path + fn
                else : 
                    fn = fn
                os.system(adb + 'adb push ' + wh + ' ' + fn)
            
            elif act == 'e' : #edit file
                fn = fn = str(input("file:\n"))
                if fn[0] != '/' :
                    cache = fn
                    fn = file_path + fn
                else : 
                    fn = fn
                os.system(adb + 'adb pull ' + fn + ' ' + '.')                
                os.system('cd ./tools/Vim/vim90 && vim ./../../' + cache )
                ul = str(input('upload?(y/n)'))
                if ul == 'y' :
                    os.system(adb + 'adb push ./../tools/' + cache + " " + fn )
                os.system('cd ./tools && del .\\' + cache )
            elif act == "" :
                clear(0)
                break
    
    
    elif a == 10 : #shell
        os.system(adb + "adb shell")
        clear(0)
    

    elif a == 11 : #wireless debug
        inp = str(input("1.开启2.连接\n"))
        if inp == "1" :
            os.system(adb + "adb tcpip 5555")
            print("成功在设备5555号端口上启用无线adb!")
            clear(1)
        if inp == "2" :
            ip = str(input("设备ip地址:"))
            os.system(adb + "adb connect " + ip + ":5555")
            print("操作完成!")
            clear(1)
    
    elif a == 12 :#screenrecoed
        cmd = adb + 'adb shell screenrecord '
        savepath = str(input('保存到(设备目录+文件名):'))
        size = str(input('可选:分辨率(1920*1080):'))
        if size == '' :
            None
        else :
            cmd +=  ' --size ' + size + ' '
        bit = str(input('可选:比特率(M):'))
        if bit == '' :
            None
        else :
            cmd +=  ' --bit-rate ' + str(int(bit) * 1000000) + ' '
        t = str(input('录制时间(s):'))
        if t == '' :
            None
        else :
            cmd +=  '--time-limit ' + t + ' '
        input('一切准备就绪,按下回车将会开始录制并保存到设备的' + savepath + '下')
        cmd += savepath
        print('按下ctrl+c提前结束录制')
        os.system(cmd)
        clear(0)

    elif a == 13 :#screen
        cmd = adb + 'scrcpy '
        bit = str(input('可选:比特率(M):'))
        if bit == '' :
            None
        else :
            cmd +=  ' --video-bit-rate ' + bit + 'M '
        size = str(input('可选:最大尺寸:'))
        if size == '' :
            None
        else :
            cmd +=  ' --max-size ' + size + ' '
        scr = str(input('可选:是否关闭物理屏幕(y/n)'))
        if scr != 'y' :
            None
        else :
            cmd +=  ' --turn-screen-off'
        os.system(cmd)
        clear(0)
    else : #reboot adb
        os.system("taskkill /f /IM adb.exe")
        print("成功杀死sADB服务!")
        clear(2)
