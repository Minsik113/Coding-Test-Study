if __name__ == '__main__':
    a = {
        1:3
        ,4:5
        ,6:10
        ,2:1
        ,3:99
    }
    b = sorted(a, key=lambda x: a[x])

    print(b)
