size = width, height = 1500, 843

with open("images.txt", encoding="utf-8") as file:
    all_images = file.readlines()
    bird_image_path = all_images[0][:-1]
    bg = all_images[1][:-1]
    start_bg = all_images[2][:-1]
    choose_level_bg = all_images[3][:-1]
    slingshot_image_path = all_images[4][:-1]
    column_vertical_image_path = all_images[5][:-1]
    column_horizontal_image_path = all_images[6][:-1]
    pig_image_path = all_images[7][:-1]
    start_button_image_path = all_images[8][:-1]
    logout_button_image_path = all_images[9][:-1]
    block_level_image_path = all_images[10][:-1]
    pause_button = all_images[11][:-1]
    next_level_button = all_images[12][:-1]
    continue_button = all_images[13][:-1]
    go_to_menu_button = all_images[14][:-1]
    start_over_button = all_images[15][:-1]
    victory = all_images[16]


bird_rect_x = 150
bird_rect_y = 550

slingshot_rect_x = 125
slingshot_rect_y = 540

column_vertical_rect_x = 1100
column_vertical_rect_y = 660

column_horizontal_rect_x = 1100
column_horizontal_rect_y = 645

pig_rect_x = 1140
pig_rect_y = 600

start_button_rect_x = 640
start_button_rect_y = 220

logout_button_rect_x = 700
logout_button_rect_y = 420

levels_base_x = 50
levels_y = 50

levels_space = 30

image_width = 92

levels_acessibility = [1, 0, 0, 0]
levels_points = [0, 0, 0]

pause_button_rect_x = 40
pause_button_rect_y = 40

next_level_button_rect_x = 700
next_level_button_rect_y = 200

continue_button_rect_x = 300
continue_button_rect_y = 40

go_to_menu_button_rect_x = 320
go_to_menu_button_rect_y = 200

start_over_button_rect_x = 720
start_over_button_rect_y = 40

victory_rect_x = 580
victory_rect_y = 40
