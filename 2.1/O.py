# Интересное сложение

N, M, T = int(input()), int(input()), int(input())

T_hour = T // 60
T_min = T % 60

new_min = M + T_min
min_for_new_hour = new_min // 60
real_new_min = new_min % 60
new_hour = (N + T_hour + min_for_new_hour) % 24

print(f"{new_hour:0>2}:{real_new_min:0>2}")
