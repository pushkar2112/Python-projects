from sample_madlibs import coding, hungergames, potter, zombie
# import sample_madlibs
import random

ch = None
story = ['coding','hungergames', 'potter','zombie']
LibModes = [coding, hungergames, potter, zombie]

if __name__ == "__main__":
    print("Welcome to MAD Lib")
    
    while True:
        print("Do you want to play in Random Mode or Custom Mode? (R/C) ")
        ch = input().lower()
        if ch in ["r",'c']:
            if ch == 'r':
                m = random.choice([coding, hungergames, potter, zombie])
                m.madlib()
                break
            elif ch == 'c':
                print(f'Modes: {story}')
                mode = input('Select a story mode: ')
                if mode in story:
                    index = story.index(mode)
                    lib = LibModes[index]
                    lib.madlib()
                    break
                else:
                    print('That  is not a valid input! Please try again...')
                    continue

        else:
            print('That  is not a valid input! Please try again...')
            continue
