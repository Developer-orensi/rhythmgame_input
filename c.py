import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame 기본 틀")

# 색깔 정의
WHITE = (255, 255, 255)

note_list = []
current_time = pygame.time.get_ticks()

#0 : 쇼트
#1 : 동타
#2 : 롱



# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(event.type == pygame.KEYDOWN):
            print(pygame.time.get_ticks() - current_time)
            if(pygame.time.get_ticks() - current_time < 5):
                note_list[-1]['time'] += pygame.time.get_ticks() - current_time
                note_list[-1]['type'] = 1
                
                current_time = pygame.time.get_ticks()
                
            else:
                note_list.append({
                    'time' : pygame.time.get_ticks() - current_time,
                    'type' : 0,
                    'len' : 0
                })
                
                note_list.append(pygame.time.get_ticks() - current_time)
                current_time = pygame.time.get_ticks()
    
    
    
    
    # 화면을 흰색으로 채우기
    screen.fill(WHITE)
    
    # Pygame 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()

print(note_list)