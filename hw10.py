# 연습문제 12.2 (과제)

import pickle
import os
filepath = 'score.bin'

# 사용자 정의 함수부
def input_scores():
    scores = []
    i = 0
    while True:
        n = int(input(f'#{i+1}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

# save/load 기능 추가
def save_data (score, avg):
    with open (filepath, 'wb') as file:
        pickle.dump(score, file)
        pickle.dump(avg, file)

def load_data():
    with open(filepath, 'rb') as file:
        score = pickle.load(file)
        avg = pickle.load(file)
        return score, avg


if os.path.exists (filepath):
    print("[파일 읽기]\n")
    score, avg = load_data()
    print('[점수 출력]\n')
    print(f'개인점수:', end='')
    show_scores(score)
    
    print(f'평균:{avg:.1f}')

else:
    print("[점수입력]")
    S = input_scores()
    avg = get_average(S)
    print('[점수출력]\n')
    print(f'개인점수:', end='')
    show_scores(S)
    print(f'평균:{avg:.1f}')
    save_data(S, avg)