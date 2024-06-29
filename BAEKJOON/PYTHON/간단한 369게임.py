N = int(input())
clap = ['3', '6', '9']

for i in range(1, N + 1):
    word = str(i)
    clap_count = 0
    for j in clap:
        clap_count += word.count(j)

    if clap_count:
        for _ in range(clap_count):
            print("-", end="")

        print(end=" ")
    else:
        print(word, end=" ")
