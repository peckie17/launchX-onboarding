
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print('No se puede leer el directorio')


if __name__ == '__main__':
    main()