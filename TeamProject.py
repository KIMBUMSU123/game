import random
import turtle
# import main
#
# #맵 그리기
# main.draw();

move=3    #터틀의 움직임 횟수
finish=False


# 각종 설정
#사용자(player)가 움직이는 거북이
player = turtle.Turtle()       #터틀의 함수를 가지고 옴
player.shape("turtle") #모양 정하기(거북이)
player.speed(3) #속도는 숫자가 작을수록 빠름
screen = player.getscreen()      #화면에 표시
# player.goto(0,0)          #터틀의 해당 죄표를 여기로 이동
player.penup() # 펜 들기 == 그림 그리지 않는 상태

#랜덤으로 움직이는 공(goal)
goal= turtle.Turtle() #터틀의 함수를 가지고 옴
goal.color("#FFBB00") #색깔 정하기 with RGB code
goal.shape("circle") #모양 정하기(원)
goal.speed(3) #속도는 숫자가 작을수록 빠름
goal.goto(random.randint(-50,50), random.randint(-50, 50)) #공의 위치가 랜덤으로 생성
goal.penup() # 펜 들기 == 그림 그리지 않는 상태

# 공의 랜덤이동
def goal_move():
    ang = goal.towards(player.pos())
    goal.setheading(-ang)
    print(goal.towards(player.pos()))
    # goal.setheading(a)          #랜덤으로 뽑은 위치를 바라보면서
    goal.fd(10)                 #20만큼 이동을 한다


#turtle 의 상하이동
def left() :
   player.left(90)            #왼쪽을 바라봄
def right():
   player.right(90)           #오른쪽을 바라봄

# !대각 이동도 필요!

def up() :
   player.forward(10)       #해당 방향으로 30만큼 이동
   global move              #move 함수를 가지고 와서
   move -= 1                #실행 시 값을 하나를 뻄
   if move == 0:            #move의 값이 0이 되면
       goal_move()          #공이 움직임
       goal_move()
       move+=3              #그리고 다시 move의 값을 3으로 고정
       return
   print(move,'번남았습니다.')
   return


def down() :
   player.backward(10)      #해당의 반대 방향으로 30만큼 이동
   global move              #move 함수를 가지고 와서
   move -= 1                #실행 시 값을 하나를 뻄
   if move == 0:            #move의 값이 0이 되면
       goal_move()          #공이 움직임
       goal_move()
       move += 3            #그리고 다시 move의 값을 3으로 고정
       return
   print(move,'번남았습니다.')
   return

# onkeypress(함수명, 키보드버튼명) :
# 어떤 버튼을 눌렀을 때, 이 함수가 동작하도록 하겠다
screen.onkeypress(left, "Left")        #왼쪽 방향키눌렀을 때 left 함수 실행
screen.onkeypress(right, "Right")      #오른쪽 방향키눌렀을 때 right 함수 실행
screen.onkeypress(up, "Up")            #위쪽 방향키눌렀을 때 up 함수 실행
screen.onkeypress(down, "Down")        #아래쪽 방향키눌렀을 때 down 함수 실행

#게임 플레이 내용
# def play():
#     global finish
#     if player.distance(goal)<10:   #플레이어가 목표에 근접 or 도달할시
#                                    #게임을 멈춤 그리고 재시작 

screen.listen() # 프로그램 활성화
screen.mainloop() # 프로그램이 계속 동작하는 상태를 유지하겠다!
