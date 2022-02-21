import Ruleset, Game, Deck, pygame

# changable constants -----

aspect_ratio = (800, 600)
background_color = (0,0,0)

# -------------------------

def redrawWindow(window):
    window.fill(background_color) # change color if you want
    pygame.display.update()

window = pygame.display.set_mode(aspect_ratio)
pygame.display.set_caption("uno game")

if __name__ == '__main__':
    run = True
    # instantiate our needed classes here
    d = Deck.Deck()
    d.init_deck()
    d.print()
    d.shuffle()
    d.print()

    
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
        
        # ongoing checks (controls, etc)
        redrawWindow(window) # this should be after all the game logic
# run main

