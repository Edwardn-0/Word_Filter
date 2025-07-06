Ban_word = ['마약', '불법', '폭탄', '약품 조제']
Ban_word = set(Ban_word)

ban_count = 0

def Word_Filter(input):
    global ban_count
    for words in Ban_word:
        if words == input:
            print(f'{words} 때문에 이 문장은 금지됩니다.')
            ban_count += 1
        elif words != input:
            pass
    if ban_count > 0:
        pass
    else:
        print('이 문장에는 금지어가 없습니다')

Input_word = (input("문장을 입력하세요: "))
Word_Filter(Input_word)