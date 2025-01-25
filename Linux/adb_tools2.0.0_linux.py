import os
import time
os.system("clear")
cache = ''
a = 0
def clear(t):
    os.system(f'sleep {t}')
    os.system("clear")
toolkit = ["1.查看连接设备","2.高级重启","3.检查ADB版本","4.屏幕工具","5.软件包管理","6.一键激活Shizuku","7.模拟按键模式","8.模拟键盘输入(EN only)","9.文件管理","10.adb终端","11.无线调试设置","12.ADB录屏","13.ADB投屏"]
text = """               *****************************
               *搞机工具箱 on Python V2.0.0*
               *****************************"""
while True :
    os.system('clear')
    print(text)
    for p in range(0,len(toolkit)) :
        print(toolkit[p])
    print("直接按下回车退出")
    a = str(input("输入功能序号："))
    if a == '1' : #check device
        os.system("adb devices")
        clear(1)
        
        
    elif a == '2' : #reboot
        answer = input("1.fastboot 2.recovery 3.9008(其他输入将会正常重启）")
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


    elif a == '3' : #adb VER
        os.system("adb version")
        clear(2)
    
    
    elif a == '4' : #display
        b = int(input("1.分辨率2.dpi"))
        if b == 1 :
            wmanswer = int(input("1.设置分辨率 2.还原至默认分辨率"))
            if wmanswer == 1 :
                cache = os.popen('adb shell wm size').read()
                nr = ''
                for i in range(15,len(cache)):
                    nr = nr + cache[i]
                print('当前分辨率:' + nr)
                print("请输入")
                l = input("宽")
                s = input("高")
                cm = f"adb shell wm size {l}x{s}"
                os.system( cm )
                reset = input('是否保留设置y/n')
                if reset == 'n' :
                    os.system('adb shell wm size '+ nr)
                clear(1)
            elif wmanswer == 2 :
                os.system("adb shell wm size reset")
                clear(1)
        elif b == 2 :
            secwmanswer = int(input("1.设置dpi 2.恢复默认"))
            if secwmanswer == 1 :
                cache = os.popen('adb shell wm density').read()
                ndpi = ''
                for i in range(17,len(cache)):
                    ndpi = ndpi + cache[i]
                print('当前dpi:' + ndpi )
                dpi = str(input("输入"))
                os.system("adb shell wm density " + dpi)
                recover = input('是否保留设置y/n')
                if recover == 'n' :
                    os.system('adb shell wm density '+ ndpi)
                clear(1)
            elif secwmanswer == 2 :
                os.system("adb shell wm density reset")
                clear(1)
    
    elif a == '5' : #package manager
        inp = str(input("1.列出已安装的包,2.安装apk,3.卸载软件,4.禁用/解禁软件,5.提取APK,6.查看前台Activity\n"))
        if inp == "1" : #list packages
            os.system("adb shell pm list packages")
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
            os.system( c + u )
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
            os.system( c + u )
            clear(2)
        elif inp == "4" : #disable app
            print("已禁用的app:\n")
            disable = os.popen("adb shell pm list packages -d").read()
            print(disable)
            pn = str(input("要禁用/解禁的软件的包名:"))
            if pn in disable :
                os.system('adb shell pm enable ' + pn)
                print("已解禁")
            else :
                os.system("adb shell pm disable-user " + pn)
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
                        os.system("adb shell pm list packages")
                        input("按回车关闭")
                        clear(0)
                        continue
                    else:
                        path = os.popen(f"adb shell pm path {pn}").read()
                        apkpath = ""
                        for i in range(8, len(path)):
                            apkpath += path[i]
                        apkpath = apkpath.strip()
                        pts = input('保存到哪里:')
                        os.system(f"adb pull {apkpath} {pts}")
                        print(f"已保存至{pts}")
                        clear(2)
                        break
            apk()
            clear(0)
        elif inp == "6" : #activity
            def activity(): 
                clear(0)
                os.system('adb shell "dumpsys activity top | grep "ACTIVITY""')
            ex = ''
            while ex == '' :
                ex = str(input('按下回车刷新,输入任意字符退出'))
                if ex == '' :
                    activity()
            clear(0)
    elif a == '6' : #shizuku
        os.system("adb shell sh /sdcard/Android/data/moe.shizuku.privileged.api/start.sh")
        print("操作完成!")
        clear(1)
    
    
    elif a == '7' : #virtual key
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
    
    
    elif a == '8' : #virtual input
        keyinput = str(input("模拟输入:"))
        cmd = f"adb shell input text {keyinput}"
        os.system(cmd)
        clear(0)   
    

    elif a == '9' : #file_manager
        file_path = '/sdcard'
        selcted = []
        def correct (p) : #一个纠正路径的函数,p为输入变量,纠错完成后将会赋值回p
            global file_path
            if p[0] != '/' :
                if file_path[-1] != '/' :
                    file_path += '/'
                corrected_path = file_path + p
                print(f'selcted: {corrected_path}')
                return corrected_path
            else :
                return p
        while True :
            os.system("clear")
            print('''                    *******************
                    *ATRI file Manager*
                    *******************''')
            time.sleep(1)
            print("*your directory:",file_path)
            time.sleep(0.5)
            os.system('adb shell ls -a ' + file_path)
            if len(selcted) != 0 :
                print("*selected:",selcted)
            act = str(input("[cd]change directory   [cp]copy a file\n[mv]move a file   [rm]remove a file\n[rn]rename a file   [mf]make a folder\n[ed]edit/creat a file with vim   [sl]select a file\n[dl]download a file [ul]upload a file\npress enter to exit\n"))
            if act == "cd" :
                path = str(input("where do you want to go?\n"))
                corrected_path = correct (path)
                file_path = corrected_path
            elif act == "cp" : #copy
                fn = str(input("file:\n"))
                fn  = correct(fn)
                wh = input("where do you want to copy?\n")
                wh = correct(wh)
                os.system(f'adb shell cp -i  -r {fn} {wh}')
                print("Done!")
                clear(1)
            elif act == "mv" : #move
                fn = str(input("file:\n"))
                fn = correct(fn)
                wh = str(input("where do you want to move?\n"))
                wh = correct(wh)
                os.system(f'adb shell mv -i -f {fn} {wh}')
                print("Done!")
                clear(1)
            elif act == "rm" : #remove
                fn = str(input("what's the file name?\n"))
                fn = correct(fn)
                if fn == "/" :
                    print("you can't remove '/'!")
                    break
                os.system(f'adb shell rm -rf {fn}')
                print("Done!")
                clear(1)
            elif act == "mf" : #makefolder
                fdn = str(input("what's the new folder's name?\n"))
                fdn = correct(fdn)
                os.system(f'adb shell mkdir {fdn}')
                print("Done!")
                clear(1)

            elif act == "rn" : #rename
                fn = str(input("file:\n"))
                fdn = correct(fn)
                nfn = str(input("what's the new file name?\n"))
                nfn = correct(nfn)
                os.system(f'adb shell mv -i -rf {fn} {nfn}')
                print("Done!")
                clear(1)
            elif act == "dl" : #download file
                remote = str(input("file:\n"))
                remote = correct(remote)
                local = str(input('where do you want to save:'))
                os.system(f'adb pull {remote} {local}')
                print("Done!")
                clear(1)
            elif act == "ul" : #upload file
                local = str(input('local file:'))
                remote = str(input("devise file:\n"))
                remote = correct(remote)
                os.system(f'adb push {local} {remote}')
                print("Done!")
                clear(1)
            
            elif act == 'ed' : #edit file
                fn = str(input("file name:\n"))
                cache = fn
                fn = correct(fn)
                files  = os.popen('adb shell ls -a ' + file_path).read()
                if cache in files:
                    os.system(f'adb pull {fn} ~')                
                os.system(f'vim ~/{cache}')
                ul = str(input('upload?(y/n)'))
                if ul == 'y' :
                    os.system(f'adb push ~/{cache} {file_path}')
                os.system(f'rm -r ~/{cache}')
                clear(1)
                print("Done!")
            if act == 'sl' :
                while True :
                    print("*selected:",selcted)
                    act = str(input("[s]select   [u]unselect\n[mv]move these files [cp]copy these files\n[dl]download these files\n[rm]delete these files   [zip]make a zip\n[e]exit select mode\n"))
                    if act == 's' :
                        fn = str(input('file name:'))
                        fn = correct(fn)
                        selcted.append(fn)
                    if act == 'u' :
                        fn = str(input('file name(use * to clear):'))
                        if fn == "*" :
                            selcted=[]
                            continue
                        fn = correct(fn)
                        selcted.remove(fn)
                    if act == 'mv' :
                        wh = str(input('where do you want to move these files?\n'))
                        wh = correct(wh)
                        for i in selcted :
                            os.system(f'adb shell mv -i -f {i} {wh}')
                        print("Done!")
                        clear(1)
                    if act == 'cp' :
                        wh = str(input('where do you want to copy these files?\n'))
                        wh = correct(wh)
                        for i in selcted :
                            os.system(f'adb shell cp -i -r {i} {wh}')
                            print("Done!")
                            clear(1)
                    if act == 'dl' :
                        local = str(input('where do you want to save:'))
                        for i in selcted :
                            remote = correct(i)
                            os.system(f'adb pull {remote} {local}')
                            print("Done!")
                            clear(1)
                    if act == 'rm' :
                        for i in selcted :
                            os.system(f'adb shell rm -rf {i}')
                    if act == 'zip' :
                        os.system('mkdir -p ~/zip_cache')
                        name = str(input("zip name:"))
                        for i in selcted:
                            os.system(f'adb pull {i} ~/zip_cache')
                        os.system(f'cd ~/zip_cache && zip ~/{name} ./*')
                        os.system(f'adb push ~/{name} {file_path}')
                        os.system('rm -r ~/zip_cache')
                        os.system(f'rm -r ~/{name}')
                        print("Done!")
                        clear(1)
                    if act == 'e' :
                        break


            elif act == "" :
                clear(0)
                break
    
    
    elif a == '10' : #shell
        os.system("adb shell")
        clear(0)
    

    elif a == '11' : #wireless debug
        inp = str(input("1.开启  2.连接  3.配对设备\n"))
        if inp == "1" :
            os.system("adb tcpip 5555")
            print("成功在设备5555号端口上启用无线adb!")
            clear(1)
        if inp == "2" :
            ip = str(input("设备ip地址:"))
            os.system(f"adb connect {ip}")
            print("操作完成!")
            clear(1)
        if inp == "3" :
            ip = str(input("设备ip地址:"))
            os.system(f"adb pair {ip}")
            print("操作完成!")
            clear(1)
    elif a == '12' :#screenrecoed
        cmd = 'adb shell screenrecord '
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

    elif a == '13' :#screen
        cmd = 'scrcpy '
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
    if a == '':
        break
