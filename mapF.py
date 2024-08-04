
def yell(*words):
    uppercase = map(str.upper,words)
    print(*uppercase)

yell('hello','Word','to','us')