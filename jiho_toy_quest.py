# list_question = [
#     "상품의 품질에 대해 어떻게 생각하시나요?",
#     "상품의 가격에 대해 어떻게 생각하시나요?",
#     "상품의 디자인에 대해 어떻게 생각하시나요?",
#     "상품에 대한 전반적인 만족도는 어떠신가요?"
# ]

# list_answer =  ["좋음", "중간", "좋아지길"]

# received_fi = (list_question[0])
# received_s = (list_question[1])
# received_t = (list_question[2])
# received_fo = (list_question[3])


# input("received_fi" + "---->")
# input("received_s" + "---->")
# input("received_t" + "---->")
# input("received_fo" + "---->")

# answer_fi = input("received_fi" + "---->")
# answer_se = input("received_s" + "---->")
# answer_th = input("received_t" + "---->")
# answer_fo = input("received_fo" + "---->")

# answer_list = [answer_fi, answer_se, answer_th, answer_fo]

# if answer_list == 1
#     return "좋음"
# elfi answer_list == 2
#     return "중간"
# else
#     return "좋아지길"



# pass

print("1. 상품의 품질에 대해 어떻게 생각하시나요?")
print("1. 좋음     2. 중간     3. 좋아지길")
print("-" * 10)  # 구분선

print("2. 상품의 가격에 대해 어떻게 생각하시나요?")
print("1. 좋음     2. 중간     3. 좋아지길")
print("-" * 10)

print("3. 상품의 디자인에 대해 어떻게 생각하시나요?")
print("1. 좋음     2. 중간     3. 좋아지길")
print("-" * 10)

print("4. 상품에 대한 전반적인 만족도는 어떠신가요?")
print("1. 좋음     2. 중간     3. 좋아지길")

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]

list_answer = ["좋음", "중간", "좋아지길"]

firstq = list_question[0]
secondq = list_question[1]
thirdq = list_question[2]
fourthq = list_question[3]

first_reply = input(firstq + "---->")
second_reply = input(secondq + "---->")
third_reply = input(thirdq + "---->")
fourth_reply = input(fourthq + "---->")

reply_list = [first_reply, second_reply, third_reply, fourth_reply]

def analyze_answer(reply_list):
    """
    리스트의 답변 > 결과 반환 함수.
    """
    for reply in reply_list:
        if reply == "1":
            return list_answer[0]
        elif reply == "2":
            return list_answer[1]
        elif reply == "3":
            return list_answer[2]
        else:                           # list_answer에 있는 답변을 찾으면 반환
            return "잘못된 답변입니다."  # list_answer에 없는 답변이면 오류 메시지 반환

result = analyze_answer(reply_list)
print(result)