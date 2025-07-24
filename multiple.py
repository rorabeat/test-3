"""
구구단 계산 모듈
"""

def print_multiplication_table(num):
    """
    특정 숫자의 구구단을 출력하는 함수
    
    Args:
        num (int): 구구단을 출력할 숫자 (1-9)
    """
    if not isinstance(num, int) or num < 1 or num > 9:
        print("1부터 9까지의 숫자만 입력해주세요.")
        return
    
    print(f"\n=== {num}단 ===")
    for i in range(1, 10):
        result = num * i
        print(f"{num} × {i} = {result}")

def print_all_multiplication_tables():
    """
    1단부터 9단까지 모든 구구단을 출력하는 함수
    """
    print("=== 전체 구구단 ===")
    for num in range(1, 10):
        print_multiplication_table(num)
        if num < 9:  # 마지막 단이 아니면 줄바꿈 추가
            print()

def get_multiplication_result(num1, num2):
    """
    두 숫자의 곱셈 결과를 반환하는 함수
    
    Args:
        num1 (int): 첫 번째 숫자
        num2 (int): 두 번째 숫자
    
    Returns:
        int: 곱셈 결과
    """
    return num1 * num2

def print_specific_range(start, end):
    """
    특정 범위의 구구단을 출력하는 함수
    
    Args:
        start (int): 시작 단
        end (int): 끝 단
    """
    if not (1 <= start <= 9) or not (1 <= end <= 9) or start > end:
        print("올바른 범위를 입력해주세요. (1-9)")
        return
    
    print(f"\n=== {start}단부터 {end}단까지 ===")
    for num in range(start, end + 1):
        print_multiplication_table(num)
        if num < end:
            print()
