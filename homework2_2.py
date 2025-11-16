boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
if len(boys) != len(girls):
    print("Внимание! Кто-то может остаться без пары.")
else:
    print("Идеальные пары:")
    for i in range(len(boys)):
        print(f"{boys[i]} и {girls[i]}")
