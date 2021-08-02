with open('molc','a+') as f:
    for i in range(10000,12377):
        for _ in range(1,4):
            f.write(f"{i}\n")
