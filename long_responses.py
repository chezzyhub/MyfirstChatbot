import random
R_ADVICE="I would like to give you advice"
R_EATING="What would you eat!"

def unknown():
    response=['could you please re-phrase that?'
              "...",
              "Sounds about right",
             "What does it mean?"][random.randrange(4)]
    return response
