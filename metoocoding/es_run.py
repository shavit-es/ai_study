import pygame
from random import *
####################기본 초기화 (반드시 해야하는 것들)###################
pygame.init()

#화면 크기 설정
screen_width = 600 #가로 크기
screen_height = 800 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
#잠들어버렸습니다!
sleep = pygame.image.load("sleep.png")
sleep_size = sleep.get_rect().size
sleep_width = sleep_size[0]
sleep_height = sleep_size[1]
sleep_x_pos = 150
sleep_y_pos = 300
# 현희 캐릭터
character = pygame.image.load("HH.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height- character_height/2
character_speed = 1
#은서 캐릭터
es = pygame.image.load("ES1.png")
es_size = es.get_rect().size
es_width = es_size[0]
es_height = es_size[1]

es2 = pygame.image.load("ES2.png")
es2_size = es2.get_rect().size
es2_width = es2_size[0]
es2_height = es2_size[1]
es2_time = 30
#좌표 이동
character_to_x_LEFT = 0
character_to_x_RIGHT = 0
character_to_y_UP = 0
character_to_y_DOWN = 0
es_to_y = 0
#시간 기록
best_record = 0
sleep_time = 0
# 화면 타이틀 설정
pygame.display.set_caption("잠만자는 은서 피하기")

# FPS
clock = pygame.time.Clock()

##################################여기까지 기본 초기화

#1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트, 속도 등)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성

# 시간 계산


# 이벤트 루프
running = True
breaker = False
sleeper = False
while running:
    start_ticks = pygame.time.get_ticks()  # 첫 시작 시간 정보를 받아옴
    es_y_pos = 0
    es_x_pos = randint(es_width / 2, screen_width - es_width)
    es_speed = 10

    es2_y_pos = 0
    es2_x_pos = randint(es2_width / 2, screen_width - es2_width)
    es2_speed = 10
    screen.blit(sleep, (sleep_x_pos, sleep_y_pos))
    # print("fps : ", clock.get_fps())
    # 키보드, 마우스 등 이벤트 처리
    while running:
        if breaker is True:
            breaker = False
            sleeper = True
            break
        dt = clock.tick(30)  # 게임화면의 초당 프레임 수
        for event in pygame.event.get():  # event는 입력같은 이벤트를 받아들임

            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_to_x_LEFT -= character_speed
                elif event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT += character_speed
                elif event.key == pygame.K_UP:
                    character_to_y_UP -= character_speed
                elif event.key == pygame.K_DOWN:
                    character_to_y_DOWN += character_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    character_to_x_LEFT = 0
                elif event.key == pygame.K_RIGHT:
                    character_to_x_RIGHT = 0
                if event.key == pygame.K_UP:
                    character_to_y_UP=0
                elif event.key == pygame.K_DOWN:
                    character_to_y_DOWN = 0


        character_x_pos += character_to_x_LEFT * dt + character_to_x_RIGHT * dt
        # character_y_pos += character_to_y_UP * dt + character_to_y_DOWN * dt

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        if character_y_pos < 0 :
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height




        # 경계값 처리

        #. 게임 캐릭터 위치 정의

        # 4. 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        es_rect = es.get_rect()
        es_rect.left = es_x_pos
        es_rect.top = es_y_pos

        es2_rect = es2.get_rect()
        es2_rect.left = es2_x_pos
        es2_rect.top = es2_y_pos

        sleep_rect = sleep.get_rect()
        sleep_rect.left = sleep_x_pos
        sleep_rect.top = sleep_y_pos
        # 충돌 체크
        if character_rect.colliderect(es_rect) or character_rect.colliderect(es2_rect):
            sleep_ticks = pygame.time.get_ticks()
            if last_time>best_record:
                best_record = last_time
            character_x_pos = screen_width / 2 - character_width / 2
            character_y_pos = screen_height - character_height / 2
            breaker = True

            continue
        es_y_pos += es_speed
        if (pygame.time.get_ticks() - start_ticks)/1000 > es2_time:
            es2_y_pos += es2_speed
        if es_y_pos>screen_height - es_height:
            es_y_pos = 0
            es_x_pos = randint(es_width / 2, screen_width - es_width)
            es_speed = es_speed + 3
            if es_speed > 40:
                es_speed = 40
        if es2_y_pos>screen_height-es2_height:
            es2_y_pos = 0
            es2_x_pos = randint(es2_width/2, screen_width - es2_width)
            es2_speed += 3
            if es2_speed > 50 :
                es_speed = 50

        #5. 화면에 그리기

        screen.fill((255,255,255))


        while sleeper is True :
            screen.blit(sleep, (sleep_x_pos, sleep_y_pos))
            screen.blit(character, (character_x_pos, character_y_pos))
            screen.blit(es, (es_x_pos, es_y_pos))
            last_time = (pygame.time.get_ticks() - start_ticks) / 1000
            # timer = game_font.render(str(round(last_time, 2)), True, (255, 0, 0))
            best_recordf = game_font.render(str(round(best_record, 2)), True, (0, 0, 0))
            # screen.blit(timer, (10, 10))
            screen.blit(best_recordf, (525, 10))
            pygame.display.update()  # 게임화면을 다시 그리기(호출)
            if int(pygame.time.get_ticks() - start_ticks) > 1000:
                sleeper = False
        screen.blit(character, (character_x_pos, character_y_pos))
        screen.blit(es, (es_x_pos, es_y_pos))
        last_time = (pygame.time.get_ticks() - start_ticks) / 1000
        timer = game_font.render(str(round(last_time,2)), True, (255,0,0))
        best_recordf = game_font.render(str(round(best_record,2)), True, (0,0,0))
        screen.blit(timer, (10,10))
        screen.blit(best_recordf, (525, 10))
        if last_time > es2_time:
            screen.blit(es2, (es2_x_pos,es2_y_pos))

        pygame.display.update()   # 게임화면을 다시 그리기(호출)

# pygame 종료
pygame.quit()
