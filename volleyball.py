import math

year = input().lower()
holidays = int(input())
weekends_home = int(input())

sofia_weekends = 48 - weekends_home
play_sofia = 3/4 * sofia_weekends / 2 + 2/3 * holidays / 2
play_total = play_sofia + weekends_home

if year == 'leap':
    play_total = math.floor(play_sofia * 15/100 * play_total)
elif year == 'normal':
    play_total = math.floor(play_total)

print(play_total)