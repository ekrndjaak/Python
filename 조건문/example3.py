while True:
    print("메뉴를 입력하세요")
    selcet = int(input("1.게임시작  2.랭킹보기  3.게임종료>>>"))

    if selcet == 1:
        print("->게임을시작합니다")
        break
    elif selcet == 2:
        print("->랭킹보기")
        break
    elif selcet == 3:
        print("->게임을종료합니다")
        break
    else:
        print("->다시입력해주세요")

