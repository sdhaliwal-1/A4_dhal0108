import time


# Scene 1: Starting scene
def scene1():
    print("""WELCOME TO THE GHOST STORIES ADVENTURE!
        The night is eerily silent, except for the sound of the wind howling outside. 
        Suddenly, you and your friends hear a loud knock coming from the abandoned classroom in your school.
        Everyone looks at each other, unsure of what to do.

        Do you: Stay together in the hallway or investigate the sound?

        Type your choice: Stay or Investigate
    """)

    c1 = input()
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "STAY":
            print("\nYou and your friends decide to stay in the hallway, but the temperature suddenly drops.")
            print("Before you know it, a ghostly figure appears behind you and whispers, 'You can't run.'")
            time.sleep(2)
            print("The lights go out, and you hear a scream. You didn’t make it out alive.")
            ans = 'correct'
            print("\nGAME OVER!")
        elif c1.upper() == "INVESTIGATE":
            print("You and your friends muster the courage to approach the abandoned classroom. The door creaks open.")
            ans = 'correct'
            scene2()
        else:
            print("ENTER THE CORRECT CHOICE! Stay or Investigate?")
            c1 = input()


# Scene 2: The haunted classroom
def scene2():
    print("""
        Inside the classroom, you find an old diary on the teacher's desk. 
        It looks ancient, and the air feels heavier as you pick it up. 
        Suddenly, a ghostly figure materializes and screams, 'Leave this place!'

        Do you: Read the diary or Drop it and run?

        Type your choice: Read or Run
    """)

    time.sleep(2)
    c1 = input()
    ans = 'incorrect'
    while ans == 'incorrect':
        if c1.upper() == "READ":
            print("""
            As you flip through the diary, you discover it belongs to a teacher who vanished years ago. 
            The diary reveals a ritual to trap the ghost. You take note of the instructions.
            The ghost screams, but for some reason, it doesn’t attack you. You move forward cautiously.
            """)
            ans = 'correct'
            read = "True"
        elif c1.upper() == "RUN":
            print("""
            You drop the diary and bolt out of the classroom, but the ghost follows you. 
            It whispers curses, and you feel weaker with each step. 
            Eventually, you collapse and black out.
            """)
            ans = 'correct'
            read = "False"
        else:
            print("Wrong Input! Enter Read or Run?")
            c1 = input()
    time.sleep(2)
    scene3(read)


# Scene 3: Final confrontation with the ghost
def scene3(read_value):
    print("""\n\nYou and your friends reach the school courtyard, but the ghost blocks your path.
    It looks angrier than before, and the air feels oppressive.
    """)

    time.sleep(2)
    if read_value == "True":
        print("""
        Remembering the ritual from the diary, you quickly draw a protective symbol on the ground. 
        You chant the words from the diary, and the ghost lets out a deafening scream. 
        The ghost is sucked into a vortex of light and disappears. You and your friends escape safely!
        """)
        time.sleep(2)
        print("\nYOU SURVIVED!")
    elif read_value == "False":
        print("""
        Without the knowledge from the diary, you have no way to defend yourself. 
        The ghost engulfs you in darkness, and you feel your life force slipping away.
        """)
        time.sleep(2)
        print("\nGAME OVER!")


# Start the story
scene1()

print("\n\n")
print("=================================END OF THE STORY=================================")
