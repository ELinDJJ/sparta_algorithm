def count_down(number):
    if number < 0:
        return
    print(number)          # number를 출력하고

    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!
    # 한계없이 -로 쭉 출력하게된다 - 무한루프
    # 재귀함수를 사용할 때는, 언제 끝날지 꼭 지정해줘야횐다. 탈출조건 필수
    # 자기자신을 호출 -> 코드를 간결하고 깔끔하게 만들어 준다


count_down(60)