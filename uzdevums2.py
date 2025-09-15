

print("Ievadiet ciparu un mēs maģiski noteiksim vai tas ir pāra/nepāra negatīvs/pozitīvs:")
a = int(input("Cipars: "))

paraskaitlis = a % 2

if paraskaitlis == 0 and a > 0:
    print(f"{a} ir pozitīvs un pāra skaitlis")
elif paraskaitlis == 0 and a < 0:
    print(f"{a} ir negatīvs un pāra skaitlis")
elif paraskaitlis != 0 and a > 0:
    print(f"{a} ir pozitīvs un nepāra skaitlis")
elif paraskaitlis != 0 and a < 0:
    print(f"{a} ir negatīvs un nepāra skaitlis")
else:
    print("Tev šis nebija jāredz OwO")

