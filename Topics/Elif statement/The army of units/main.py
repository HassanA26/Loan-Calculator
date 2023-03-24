army = int(input())

if army < 1:
    print("no army")
elif army <= 9:
    print("few")
elif army <= 49:
    print("pack")
elif army <= 499:
    print("horde")
elif army <= 999:
    print("swarm")
elif army >= 1000:
    print("legion")
