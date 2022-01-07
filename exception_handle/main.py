from classes import testar, ExceptionHandleError

if __name__ == '__main__':
    try:
        testar()
    except ExceptionHandleError as error:
        print(f'error: {error}')
