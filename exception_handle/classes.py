class ExceptionHandleError(Exception):
    pass


def testar():
    raise ExceptionHandleError("aconteceu algum erro")
