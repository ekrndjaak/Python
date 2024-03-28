# a는 앨범에 수록된 곡의 개수
# b는 저작권이 있는 멜로디의 개수
# i는 평균
a ,i = map(int, input().split())
# i = b / a (이거에 반올림)
# b = a * (i-1) 왜 -1이냐 b
b = a * (i-1)
print(b+1)