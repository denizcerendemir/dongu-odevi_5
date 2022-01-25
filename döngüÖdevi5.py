"""Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın."""

list1 = range(1,100)

for i in list1 :
    if (i in list1 and i%3 == 0) :
        print(i)
        continue