def solution(s):
    answer = []
    s2 = s.lstrip('{').rstrip('}').split('},{') # 감탄..
    
    s3 = []
    for element in s2:
        s3.append(list(map(int,element.split(','))))
    
    s3.sort(key=len)
    
    for collection in s3:
        for element in collection:
            if element not in answer:
                answer.append(element)
    
    return answer




# 처음 풀은 방식
# def solution(s):
#     answer = []
#     s = s[1:len(s)-1]
#     s_list = list(s)
    
#     #print(s_list)
    
#     # string -> array
#     s1 = []
#     s_array = []
#     operand = ''
#     for element in s_list:
#         if element == '{':
#             s_array = [] # 초기화
#             operand = ''
#         elif element == '}':
#             s_array.append(int(operand))
#             s1.append(s_array)
#             operand = '' # 초기화
#         elif element == ',':
#             if operand != '':
#                 s_array.append(int(operand))
#                 operand = '' # 초기화
#         else: # 피연산자일 때
#             operand += element
    
#     #print(s1)
    
#     s1.sort(key=len)
#     #print(s1)
    
#     # 순서대로 넣기
#     for collection in s1:
#         #print(collection)
#         for element in collection:
#             if element not in answer:
#                 answer.append(element)
    
#     return answer