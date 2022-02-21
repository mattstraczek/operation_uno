import pygame



def main():
    run = True
    # instantiate our needed classes here

    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()\
        
        # ongoing checks (controls, etc)


# run main
main()
