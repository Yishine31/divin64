import random
import numpy as np
import os
import time


'''
三個皆正：老陽（。－）

一正二反：少陽（－）

二正一 反：少陰（- -)

三個皆反：老陰（。- -)
'''
def welcome():
    logo = ''
    with open('divin64/logo.txt','r') as file:
        for i in file.readlines():
            logo += i
    print(logo)
    print()
    text1 = '歡迎使用卜卦app\n本程式資料都來源於 易學網 : https://www.eee-learning.com/\n\n'
    text2 = '使用前請先閱讀規則:\n\n1.一事不二問，也不可用不同問法問同一個問題。\n\n'
    text3 = '2.發問前先調整心態，平心靜氣。\n\n3.卜卦不準是常有的事，不要太過於期待。\n\n準備好就開始吧!\n\n'
    text1 += text2+text3
    print(text1)

def count_coins(coin):
    coinn = np.array(coin)
    index_yang = np.where(coinn=='1')
    index_yin = np.where(coinn=='0')
    count_yang = len(coinn[index_yang])
    count_yin = len(coinn[index_yin])
    
    if count_yang == 3:
        s = "三個皆反：老陽（⚊ )"
        coins = '⚊'
    elif count_yin == 3:
        s = "三個皆正：老陰（⚋ )"
        coins = '⚋'
    elif count_yang == 1:
        s = "一反二正：少陽（⚊ )"
        coins = '⚊'
    elif count_yin == 1:
        s = "二反一正：少陰（⚋ )"
        coins = '⚋'
    
    count_coins = f"正面:{count_yin}次, 反面:{count_yang}次"
    return coins,count_coins,s

def read_yao(yaos):
    yao_num = []
    yaocode = ''
    for i in yaos:
        match i:
            case '⚊':
                num = '1'
            case '⚋':
                num = '0'
        yao_num.append(num)
    for i in yao_num:
        yaocode += i
    return yaocode


def throw_coins():
    yaos = []
    print('--start--')
    print('1 代表硬幣反面(人頭面)為 陽,\n0 代表硬幣正面(數字面)為 陰\n')
    for i in range(6):
        print(f'第 {i+1} 次擲銅板 :')
        os.system("pause")
        coin = []
        for j in range(3):
            res = random.randint(0,1)
            coin += str(res)
        print(coin)
        tem_coins,tem_count,tem_s = count_coins(coin)
        print(tem_count)
        print(tem_s)
        yaos += tem_coins
        print('\n')
    print(f"六次擲銅板結果 : 6.\'{yaos[5]} \' 5.\'{yaos[4]} \' 4.\'{yaos[3]} \' 3.\'{yaos[2]} \' 2.\'{yaos[1]} \' 1.\'{yaos[0]} \'")
    yaos = yaos[::-1]
    os.system("pause")
    print()
    return yaos

def question():
    q = input('請輸入一個想問的問題 :')
    print("開始卜卦...")
    os.system("pause")
    return q

def get_fT_yC_yS(lists):
    file_titles = []
    yao_code_list = []
    yao_symbol_list = []
    for i in lists[1:]:
        ftitle = i[0]+' '+i[1]
        ynum = i[2].split('-')[1]
        ynum = ynum.replace('\n','')
        ysym = i[2].split('-')[0]
        file_titles.append(ftitle)
        yao_code_list.append(ynum)
        yao_symbol_list.append(ysym)
    return file_titles,yao_code_list,yao_symbol_list

def get_titletext():
    filetext = []
    name = '掛名與卦象1'
    path = f"divin64/simple64/{name}.txt"
    # path = "simple64/a.txt"
    with open(path,'r',encoding='utf-8') as file:
        for i in file.readlines():
            filetext.append(i)
    lists = []
    for i in filetext:
        lists.append(i.split(' '))
    return lists

def answer(file_titles,yao_code_list,yao_symbol_list,yaocode):
    for i in range(64):
        if(yao_code_list[i] == yaocode):
            # print(f'這次卜卦結果是 : {file_titles[i]} {yao_symbol_list[i]}\n')
            file_open = file_titles[i]
            break

    text = ""
    text += f"這次卜卦結果是 : {file_titles[i]} {yao_symbol_list[i]}\n\n"
    with open(f"divin64/simple64/{file_open}.txt",'r',encoding='utf-8') as file:
        for i in file.readlines():
            text+=i
    return text

def save_file(text):
    if not os.path.isdir("divin64/answers64"):
        os.mkdir("divin64/answers64")
    now = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    filename = f"算掛結果_{now}"
    f = open(f"divin64/answers64/{filename}.txt",'w',encoding='utf8')
    f.write('\ufeff')
    f.write(text)
    f.close()

def anstext(questiontitle,answer):
    text = ''
    text += questiontitle + '\n' + answer
    return text



'''q = question()
yaos = throw_coins()
yaocode = read_yao(yaos)

questiontitle = f'關於你的問題 :  {q}'
print(questiontitle)

titletext = get_titletext()
file_titles,yao_code_list,yao_symbol_list = get_fT_yC_yS(titletext)

answer = answer(file_titles,yao_code_list,yao_symbol_list,yaocode)
print(answer)

text = anstext(questiontitle,answer)
save_file(text)'''


# 3 list text
'''
titletext = get_titletext()
file_titles,yao_code_list,yao_symbol_list = get_fT_yC_yS(titletext)
print(file_titles)
print()
print(yao_code_list)
print()
print(yao_symbol_list)

'''
