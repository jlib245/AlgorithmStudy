# [Gold V] 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다 - 6568 

[문제 링크](https://www.acmicpc.net/problem/6568) 

### 성능 요약

메모리: 108080 KB, 시간: 92 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 10월 2일 00:39:51

### 문제 설명

<p>그래서 여러분도 크리스마스날 심심해서 컴퓨터를 하나 만들었다. 이 컴퓨터는 아주 적은 수의 명령어를 사용하는 하나의 프로세서, 32바이트 메모리, 8비트짜리 가산기, 5비트짜리 프로그램 카운터(pc)로 이루어져 있다. 폰 노이만 구조를 표방하여 이 컴퓨터는 메모리와 프로그램 구문을 공유한다.</p>

<p>프로그램 카운터는 다음에 실행되어야 하는 명령어의 주소를 갖고 있다. 각 명령어의 길이는 1바이트이며, 상위 3비트는 명령어의 종류를, 하위 5비트는 피연산자를 표현한다. 피연산자는 언제나 메모리 값(XXXXX)이다. 피연산자가 필요하지 않은 명령어도 있는데, 이때는 하위 5비트는 무의미하다(-----). 사용되는 명령어들의 의미는 다음과 같다.</p>

<blockquote><code>000xxxxx   STA x</code>   메모리 주소 x에 가산기의 값을 저장한다.<br>
<code>001xxxxx   LDA x</code>   메모리 주소 x의 값을 가산기로 불러온다.<br>
<code>010xxxxx   BEQ x</code>   가산기의 값이 0이면 PC 값을 x로 바꾼다.<br>
<code>011-----   NOP</code>     아무 연산도 하지 않는다.<br>
<code>100-----   DEC</code>     가산기 값을 1 감소시킨다.<br>
<code>101-----   INC</code>     가산기 값을 1 증가시킨다.<br>
<code>110xxxxx   JMP x</code>   PC 값을 x로 바꾼다.<br>
<code>111-----   HLT</code>     프로그램을 종료한다.</blockquote>

<p>초기엔 PC와 가산기 값은 모두 0이다. 명령어를 불러와 해독한 뒤, 그 명령어를 실행하기 전에 PC 값은 1 증가한다. 프로그램은 언제나 종료된다고 가정해도 좋다.</p>

### 입력 

 <p>입력은 여러 개의 테스트 케이스로 주어진다. 각 테스트 케이스는 32개의 줄에 걸쳐 각 메모리 값, 즉 코드가 순서대로 8비트 2진수의 형태로 주어진다. 왼쪽에 있는 비트일수록 상위 비트이다. 입력은 EOF와 함께 종료된다.</p>

### 출력 

 <p>각 테스트 케이스마다 한 줄에 걸쳐 프로그램이 종료되었을 때의 가산기 값을 역시 8비트 2진수 형태로 출력한다. 이때도 왼쪽에 출력될수록 상위 비트이다.</p>

