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



# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_d):
                note_list.append([pygame.time.get_ticks() - current_time, 1])
                
            if(event.key == pygame.K_f):
                note_list.append([pygame.time.get_ticks() - current_time, 2])
                current_time = pygame.time.get_ticks()
            if(event.key == pygame.K_g):
                note_list.append([pygame.time.get_ticks() - current_time, 3])
                current_time = pygame.time.get_ticks()
            if(event.key == pygame.K_h):
                note_list.append([pygame.time.get_ticks() - current_time, 4])
                current_time = pygame.time.get_ticks()
            if(event.key == pygame.K_j):
                note_list.append([pygame.time.get_ticks() - current_time, 5])
                current_time = pygame.time.get_ticks()
        
            print(len(note_list))

    
    
    # 화면을 흰색으로 채우기ddk
    screen.fill(WHITE)
    
    # Pygame 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()

print(note_list)