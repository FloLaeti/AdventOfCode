if __name__ == '__main__':
    fichier = open('input.txt','r')
    data = [int(i) for i in fichier.read().split("\n")]

    cpt=0
    for k in range(2,len(data)):
        i = k-2
        j = k-1
        v0=data[i]+data[j]+data[k]
        v1=data[j]+data[k]+data[k+1]

        if v0 < v1:
            cpt=cpt+1

    print(cpt, data)