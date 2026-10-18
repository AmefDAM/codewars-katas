def deaf_grandma(you):
    grandma_says = []
    for said in you:
        if said != said.upper():
            grandma_says.append("HUH?! SPEAK UP, SONNY!")
        elif said == "BYE":
            grandma_says.append("OK, BYE!")
            break
        else:
            grandma_says.append("NO, NOT SINCE 1938!")
    return grandma_says