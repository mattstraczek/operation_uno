# functions -------------------------

def redrawWindow(window):
    window.fill(background_color) # change color if you want

def displayMessage(msg, color, dest, display):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, dest)
