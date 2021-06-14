import random as rd
import time

progress = 1
while progress:
    try:
        num = int(input('자릿수 입력 : '))
    except ValueError:
        print('\n잘못된 입력\n')
        continue
    except KeyboardInterrupt:
        progress = 0

    if (((num / 10) > 0) or (num < 0)):
        print('\n잘못된 입력\n')
        continue
    break

time.sleep(0.5)

while progress:
    print('\n%d개의 숫자를 임의로 추출합니다.\n' % (num))
    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    time.sleep(0.5)
    i = 0
    answer = []
    while i < num:
        a = rd.sample(number_list, 1)
        if answer.count(a[0]) < 1:
            answer.append(a[0])
            i += 1
    
    times = 0
    time.sleep(0.5)
    
    while 1:
        strike = 0
        ball = 0

        answer_input = list(input('숫자 입력 : '))
        while len(answer_input) != num and answer_input != ['포', '기'] and answer_input != ['ㅈ', 'ㅈ']:
            print('\n잘못된 입력\n')
            time.sleep(0.5)
            answer_input = list(input('숫자 입력 : '))

        if answer_input == ['포', '기'] or answer_input == ['ㅈ', 'ㅈ']:
            print('\n포기 하였습니다.\n')
            time.sleep(0.5)
            
            print('정답 : ', end = '')
            for i in range(num):
                if i != num - 1:
                    print('%s' % answer[i], end = ' ')
                else:
                    print('%s' % answer[i])
            time.sleep(0.5)
            break
        

        for i in range(num):
            for j in range(num):
                if answer_input[i] == answer[j] and i == j:
                    strike += 1
                elif answer_input[i] == answer[j] and i != j:
                    ball += 1
                    
        if strike == num:
            print('\n정답입니다!\n')
            break
        else:
            if strike > 0 and ball == 0:
                print('\n%d 스트라이크\n' % (strike))
            elif strike == 0 and ball > 0:
                print('\n%d 볼\n' % (ball))
            elif strike > 0 and ball > 0:
                print('\n%d 스트라이크 %d 볼\n' % (strike, ball))
            else:
                print('\n아웃\n')

            times += 1

    time.sleep(0.5)
    print('\n시도 횟수 : %d\n' % (times))
    time.sleep(0.5)

    print('\n다시 하려면 1을, 끝내려면 엔터키를 입력하세요\n')
    re = str(input(''))
    while re != '1' and re != '':
        print('잘못된 입력')
        re = str(input(''))

    if re == '1':
        continue
    else:
        progress = 0
        

