def compruebaMail(MailUsuario):
    """ Esta función compruba la validez sintáctica de un string que debe contener un mail.
    Para ello comprobará si contiene el carácter @ y que este no esté al final. Si tiene una @, y esta
    no se encuentra al final será correcto, en cualquier otro caso será incorrecto.

    >>> compruebaMail('ahidalgo@')
    False
    
    >>> compruebaMail('ahidalgo@lop.es')
    True

    >>> compruebaMail('ahidalgo@@lio.com')
    False

    """

    arroba=MailUsuario.count('@')
    if arroba!=1 or MailUsuario.rfind('@')==(len(MailUsuario)-1):
        return False
    else:
        return True


import doctest
doctest.testmod()