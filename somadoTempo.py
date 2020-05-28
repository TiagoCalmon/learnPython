hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

s_min = mins + dura
if s_min > 59:
    s_hour=hour + (s_min // 60)
    if s_hour > 23:
        s_hour = s_hour % 24
    s_min=s_min % 60
    print("teste")
else:
    s_hour = hour
print(s_hour,s_min, sep=":")
# put your code here