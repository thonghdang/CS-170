def main():
    age = int(input('How old are you?'))
    if age <=13:
        print ('child')
    elif age <=18:
        print ('teenager')
    elif age <=30:
        print ('young adult')
    else:
        print ('adult')

    print(age)

main()
