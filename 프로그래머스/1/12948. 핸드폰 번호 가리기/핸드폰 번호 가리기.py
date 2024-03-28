def solution(phone_number):
    number = int(phone_number)
    hidden_part = '*' * (len(phone_number) - 4)
    last_part = phone_number[-4:]
    answer = hidden_part + last_part
    
    return answer









