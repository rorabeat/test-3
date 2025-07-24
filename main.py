"""
구구단 프로그램 메인 실행 파일
"""

import multiple

def display_menu():
    """
    메뉴를 출력하는 함수
    """
    print("\n" + "="*40)
    print("         구구단 프로그램")
    print("="*40)
    print("1. 특정 단 출력")
    print("2. 전체 구구단 출력 (1단~9단)")
    print("3. 범위 지정 출력")
    print("4. 곱셈 계산기")
    print("5. 프로그램 종료")
    print("="*40)

def get_user_input(prompt, input_type=int):
    """
    사용자 입력을 받고 유효성을 검사하는 함수
    
    Args:
        prompt (str): 입력 안내 메시지
        input_type (type): 입력받을 데이터 타입
    
    Returns:
        입력받은 값 또는 None (오류 시)
    """
    try:
        return input_type(input(prompt))
    except ValueError:
        print("올바른 형식으로 입력해주세요.")
        return None

def handle_specific_table():
    """
    특정 단 출력을 처리하는 함수
    """
    num = get_user_input("출력할 단을 입력하세요 (1-9): ")
    if num is not None:
        multiple.print_multiplication_table(num)

def handle_range_table():
    """
    범위 지정 출력을 처리하는 함수
    """
    print("출력할 구구단 범위를 입력하세요.")
    start = get_user_input("시작 단 (1-9): ")
    if start is None:
        return
    
    end = get_user_input("끝 단 (1-9): ")
    if end is None:
        return
    
    multiple.print_specific_range(start, end)

def handle_calculator():
    """
    곱셈 계산기를 처리하는 함수
    """
    print("곱셈 계산을 수행합니다.")
    num1 = get_user_input("첫 번째 숫자를 입력하세요: ")
    if num1 is None:
        return
    
    num2 = get_user_input("두 번째 숫자를 입력하세요: ")
    if num2 is None:
        return
    
    result = multiple.get_multiplication_result(num1, num2)
    print(f"\n계산 결과: {num1} × {num2} = {result}")

def main():
    """
    메인 함수
    """
    print("구구단 프로그램에 오신 것을 환영합니다!")
    
    while True:
        display_menu()
        choice = get_user_input("메뉴를 선택하세요 (1-5): ")
        
        if choice is None:
            continue
        
        if choice == 1:
            handle_specific_table()
        elif choice == 2:
            multiple.print_all_multiplication_tables()
        elif choice == 3:
            handle_range_table()
        elif choice == 4:
            handle_calculator()
        elif choice == 5:
            print("\n프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("올바른 메뉴 번호를 선택해주세요 (1-5).")
        
        # 계속 진행하기 위한 입력 대기
        input("\n계속하려면 Enter 키를 누르세요...")

if __name__ == "__main__":
    main()
