import getpass

try: 
    import msvcrt
except ImportError:
    msvcrt = None


def input_senha(prompt="Senha: "):
    if msvcrt is None:
        return getpass.getpass(prompt)

    print(prompt, end="", flush=True)
    senha = ""
    while True:
        tecla = msvcrt.getwch()
        if tecla in ("\r", "\n"):
            print()
            break
        elif tecla == "\x08":
            if senha:
                senha = senha[:-1]
                print("\b \b", end="", flush=True)
        elif tecla == "\x03":
            raise KeyboardInterrupt
        elif tecla in ("\x00", "\xe0"):
            msvcrt.getwch()
        else:
            senha += tecla
            print("*", end="", flush=True)
    return senha