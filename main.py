
WRONG_REPEAT = False

PATH = 'list.txt'

RANDLIST = [[0,6],[11,6],[43,6],[17,6],[47,6],[3,6],[5,6],[19,6]]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

str2green = lambda str : bcolors.OKGREEN + str + bcolors.ENDC
str2yellow = lambda str : bcolors.WARNING + str + bcolors.ENDC
str2red = lambda str : bcolors.FAIL + str + bcolors.ENDC

def Con2DictList(content):
    list = []
    dict = {}
    for i in content:
        if i[0] in '0123456789':
            if dict:
                list.append(dict)
            dict = {}
        else:
            index = i.index(' ')
            if i[-1] == '\n':
                i = i[:-1]
            dict[i[:index]] = i[index+1:]
    if dict:
        list.append(dict)
    return list


def read(PATH):
    with open(PATH, 'r', encoding='utf-8') as f:
        CONTENT = f.readlines()
        return CONTENT

def RanOrder(dict, option):
    [base, exp] = RANDLIST[option]
    KeyList = [i for i in dict]
    if WRONG_REPEAT:
        wrongs = []
    t = 0
    while KeyList:
        length = len(KeyList)
        i = KeyList.pop( (base)**(exp+t) % length )
        t += 1
        print(str2yellow(dict[i]))
        word = input()
        if i==word:
            print(str2green('正确！\n'))
        elif word == '!quit':
            return
        else:
            if WRONG_REPEAT:
                wrongs.append(i)
            print(str2red('错误，正确答案是') + i + '\n')
    if WRONG_REPEAT:
        while wrongs:
            i = wrongs.pop(0)
            print(str2yellow(dict[i]))
            word = input()
            if i==word:
                print(str2green('正确！\n'))
            elif word == '!quit':
                return
            else:
                if WRONG_REPEAT:
                    wrongs.append(i)
                print(str2red('错误，正确答案是') + i + '\n')





CONTENT = read(PATH)
LIST = Con2DictList(CONTENT)

def main():
    global WRONG_REPEAT
    while(1):
        u = input('选择单元(1-' + str(len(LIST)) + ')，选0结束：')
        if u == '0':
            return
        dict = LIST[int(u)-1]
        order = input('选择模式，顺序1，乱序2-9：')
        if not '0' == input('需要重复错误单词吗，不需要0，需要1：'):
            WRONG_REPEAT = True
        else:
            WRONG_REPEAT = False
        RanOrder(dict, int(order)-1)
        print('本单元结束\n')

if __name__ == '__main__':
    main()
# for i in list:
#     for key in i:
#         print(key, i[key])
#     print()