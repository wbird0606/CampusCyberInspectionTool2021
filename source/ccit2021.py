import argparse
import os
# Demo
from functions.ClockFunc import ClockFunc
# 綺娟
from functions.Netstat import Netstat  # (初級)
from functions.Tracert import Traceip  # (中級)
# 豔婕
from functions.Openyt import Openyt  # (初級)
from functions.Bypassuac import Bypassuac  # (中級)
from functions.Changepassword import Changepassword  # (中級)
# benson871229
# from functions.LetterFrequency import LetterFrequency # (中級)
# from functions.nmap import nmap # (初級)
from functions.Notepad import Notepad  # (中級)
# 東東
from functions.Path import Path  # (初級)
# from functions.tcp_syn_flood import syn_flood # (高級)
# Kung-327
# from functions.reptile_movie import reptile_movie  # (高級)
# Kiritorian
# from functions.Func import ST  #(未完整->初級)
# tims871031
# (未完整->初級)
# 庭維
from functions.Ping import Ping  # (中級)
from functions.Ping import Ping2  # (中級)
from functions.Ping import Ping3  # (中級)
# 永翰
from functions.encryption import Cryto  # (中級*n)
@ 家維 wbird0606
from functions.Nslookup import Nslookupoption
from functions.PortScanner import thread_job


def main():
    # 準備參數解析
    app_description = "校園資安測試常用工具集合"
    epilog_text = "歡迎至https://github.com/TwMoonBear-Arsenal/BetterCalculator/issues提供建議"
    parser = argparse.ArgumentParser(
        description=app_description, epilog=epilog_text)
    args = parser.parse_args()

    # 準備選單
    optionList = []
    optionList.append(ClockFunc())
    optionList.append(Netstat())
    optionList.append(Traceip())
    optionList.append(Openyt())
    optionList.append(Bypassuac())
    optionList.append(Changepassword())
    # optionList.append(LetterFrequency())
    # optionList.append(nmap())
    optionList.append(Notepad())
    optionList.append(Path())
    # optionList.append(syn_flood())
    # optionList.append(reptile_movie())
    optionList.append(Ping())
    optionList.append(Ping2())
    optionList.append(Ping3())
    optionList.append(Cryto())
    optionList.append(Cryto())
    optionList.append(Cryto())
    print()

    # 以下持續循環直到使用者結束
    while(True):

        # 顯示選單
        os.system('cls')
        print(app_description)
        print(epilog_text)
        print("--------")
        for i in range(len(optionList)):
            print('[ {:>2} ]'.format(i+1), optionList[i].Description)
        print("[", 99, "]", "結束程式")

        # 詢問使用者
        selection = int(input("請輸入需要的功能：").strip())
        print()
        # 依使用者選號找出功能項
        if((selection - 1) < len(optionList)):
            func = optionList[selection-1]
            func.Run()
        elif(selection == 99):
            print("See you next time...")
            print()
            return
        else:
            print("輸入錯誤")

        # 開始下一循環
        print()
        input("按任意鍵繼續...")


if __name__ == "__main__":
    main()
