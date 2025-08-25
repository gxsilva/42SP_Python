import cowsay

def greeting(name: str = "luis") -> None:
    """
    receives a name and print a greeting from a cow, with a name is not passed the default name is called
    """
    final_string = ("Hey my friend, " + name + "!!!")
    cowsay.ghostbusters(final_string)