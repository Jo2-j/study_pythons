"""deposit_my_list = [4500000, 9800000] # 원금
bank_rate_year = [0.024, 0.036, 0.042] # 이율
bank_tax_interest_rate = [0, 0.154, 0.154] # 세금
#Option : 어려운 경우 각 변수 값 아래 사용
deposit_my_list = 4500000
bank_rate_year = [0.024, 0.036]
bank_tax_interest_rate = [0, 0.154] """


# def total_deposit_withouttax():

#     for dml in deposit_my_list:
#         for bry in bank_rate_year:


# return dml*bry



# 원금*(1+(이자율*개월수)), (deposit_my_list)


# deposit_my_list = [4500000, 9800000]  # 원금
# bank_rate_year = [0.024, 0.036, 0.042]  # 이율
# bank_tax_interest_rate = [0, 0.154, 0.154]  # 세금

# def total_deposit_without_tax():
#     result = []  # 결과를 저장할 리스트
#     for dml in deposit_my_list:
#         for bry in bank_rate_year:
#             interest = dml * bry  # 이자 계산
#             result_without = interest[]  # 결과를 저장할 리스트
#             print(result_without)

deposit_my_list = [4500000, 9800000]  # 원금
bank_rate_year = [0.024, 0.036, 0.042]  # 이율
bank_tax_interest_rate = [0, 0.154, 0.154]  # 세금

def total_deposit_without_tax():
    result_without = []  # 결과를 저장할 리스트
    for dml in deposit_my_list:
        for bry in bank_rate_year:
            interest = dml * bry  # 이자 계산
            result_without.append(interest)  # 이자를 리스트에 추가
    return result_without  # 모든 계산 결과를 리스트로 반환

print(result_without)

def total_deposit_with_tax():
    result_with = []
    for dml_with in result_without:
        for bti in bank_tax_interest_rate:
            withtax = dml_with * bti
            result_with.append(withtax)
    return result_with

print(result_with)


tax = interest * bank_tax_interest_rate[bank_rate_year.index(bry)]  # 세금 계산
# result.append([interest, tax])  # 이자와 세금을 리스트에 추가
# #     return result  # 모든 계산 결과를 리스트로 반환

# # print(total_deposit_withouttax())

# 아래는 gpt 힘좀 빌렸습니다.
# 
# deposit_my_list = [4500000, 9800000]  # 원금
# bank_rate_year = [0.024, 0.036, 0.042]  # 이율
# bank_tax_interest_rate = [0, 0.154, 0.154]  # 세금
#
# def calculate_deposit(principal, interest_rate, tax_rate):
#     """원금, 이자율, 세율을 기반으로 이자와 세금을 계산하는 함수"""
#     interest = principal * interest_rate  # 이자 계산
#     tax = interest * tax_rate  # 세금 계산
#     return [interest, tax]  # 이자와 세금을 리스트로 반환
#
# def main():
#     """
#     원금 목록(deposit_my_list)과 이율 목록(bank_rate_year)을 순회하며
#     각 조합에 대한 이자와 세금을 계산하고 출력하는 함수
#     """
#     for principal in deposit_my_list:
#         for interest_rate in bank_rate_year:
#             # 이자율에 해당하는 세율 가져오기
#             tax_rate = bank_tax_interest_rate[bank_rate_year.index(interest_rate)]
#             # 이자와 세금 계산
#             result = calculate_deposit(principal, interest_rate, tax_rate)
#             # 결과 출력
#             print(f"원금: {principal}원, 이율: {interest_rate:.1%}, 이자: {result[0]}원, 세금: {result[1]}원")
#
# # main 함수 실행
# if __name__ == "__main__":
#     main()

# 이율에 1/4를 하고 range를 써서 11개의 단위(33개월)까지 하는건 생각하였음
# deposit_my_list = [4500000, 9800000]  # 원금
# bank_rate_year = [0.024, 0.036, 0.042]  # 이율
# bank_tax_interest_rate = [0, 0.154, 0.154]  # 세금

# def calculate_deposit(principal, quarterly_interest_rate, tax_rate, num_quarters):
#     """원금, 분기별 이자율, 세율, 분기 수를 기반으로 이자와 세금을 계산하는 함수"""
#     interest = principal * quarterly_interest_rate * num_quarters  # 이자 계산 (분기별)
#     tax = interest * tax_rate  # 세금 계산
#     return interest, tax  # 이자와 세금을 반환

# def main():
#     """
#     원금 목록(deposit_my_list)과 이율 목록(bank_rate_year)을 순회하며
#     3개월 단위로 33개월까지의 이자와 세금을 계산하고 출력하는 함수
#     """
#     for principal in deposit_my_list:
#         for annual_interest_rate in bank_rate_year:
#             tax_rate = bank_tax_interest_rate[bank_rate_year.index(annual_interest_rate)]  # 이자율에 해당하는 세율 가져오기
#             quarterly_interest_rate = annual_interest_rate / 4  # 연 이자율을 분기별 이자율로 변환
#             for num_quarters in range(1, 12):  # 1분기부터 11분기까지 반복 (총 33개월)
#                 interest, tax = calculate_deposit(principal, quarterly_interest_rate, tax_rate, num_quarters)  # 이자와 세금 계산
#                 period_months = num_quarters * 3  # 분기 수를 개월 수로 변환
#                 print(f"원금: {principal}원, 이율: {annual_interest_rate:.1%}, 기간: {period_months}개월, 이자: {interest:.0f}원, 세금: {tax:.0f}원")  # 결과 출력

# # main 함수 실행
# if __name__ == "__main__":
#     main()