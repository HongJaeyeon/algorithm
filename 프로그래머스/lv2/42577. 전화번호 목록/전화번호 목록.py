def solution(phone_book):
    # n == 1,000,000, n의 차승 안됨
    
    if len(phone_book) == 1: return False
    
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]:
            return False
    return True