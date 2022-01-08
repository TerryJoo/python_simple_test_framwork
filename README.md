# 파이썬 테스트 프레임워크
## 목적
**I/O 통합 테스트가 필요한 사람을 위한 프레임워크**

보통 함수 테스트를 할 땐,
1. 테스트케이스를 작성하고,
2. pytest나 unittest를 이용하여 확인을 합니다.

하지만 가끔 `input`, `print` 함수를 이용하여 테스트해야만 하는 경우가 있는데, 그때 이 프레임워크가 도움이 될 것입니다.

## Quick start
1. Clone this project
2. Install pytest
    ```bash
    pip3 install -r requirements.txt
    ```
3. Test
    ```bash
   pytest
    ```
   or
   ```bash
    pytest test_p1.py
   ```

## Custom solution & I/O
```python
# test_p1.py
from io_test_function import io_test_function
from p1 import solution


def test_p1_1():
    """ 설명
    solution:
    작성된 함수(p1.py)

    INPUT - '6\n3':
    solution안의 input함수가 호출될 때 마다 입력할 값을 줄바꿈 문자(\n)로 구분하여 순서대로 작성합니다. 
    첫번째 인풋으로 6이, 다음 인풋으로 3이 들어갑니다.
    # ex
    n, m = input(), input()  # n='6', m='3'
 
    OUTPUT - '666':
    solution안의 print함수에 의해 출력되는 결과를 수신하여, '666'이 맞는지 확인합니다.
    """
    io_test_function(solution, '6\n3', '666')
```