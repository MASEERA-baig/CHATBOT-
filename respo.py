import random

R_EATING = "I  eat BRAINS!"
R_HUNGRY = "YES... Baegopaa.."
R_SINGLE = "No,I am Married"
R_SONG = 'Umm... sorry'
R_ASKING = 'I AM SUZU'


def unknown():
    response = ["Could you please Ask Again? ",
                "...",
                "Please Speak Again.",
                "What does that mean?"][
        random.randrange(4)]
    return response


#                                          THANK YOU....!
