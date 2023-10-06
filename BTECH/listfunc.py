def a():
    N = int(input())
    lt = []
    for _ in range(N):
        cmd = list(map(str,input().split()))
        if cmd[0]=="insert":
            lt.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=="print":
            print(lt)
        elif cmd[0]=="remove":
            lt.remove(int(cmd[1]))
        elif cmd[0]=="sort":
            lt.sort()
        elif cmd[0]=="pop":
            lt.pop()
        elif cmd[0]=="reverse":
            lt.reverse()
a()
