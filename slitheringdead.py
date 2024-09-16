def makeChoice(prompt, options):
    print(prompt)
    print(options)
    choice = input("> ")
    return choice

story = """You find yourself in an old, abandoned mansion.
The air is thick with dust and the smell of mildew.
You hear a creaking sound from somewhere in the darkened hallway."""

print(story)

playerName = input("What is your name, explorer? > ")
print(f"Alright, {playerName}. The mansion seems eerily quiet. You hear a soft thump coming from the second floor.")
print(
    """
    What do you do next?
    1) Investigate the sound on the second floor.
    2) Stay on the ground floor and look around.
    """
)
firstChoice = input("> ")

if firstChoice == '1':
    print(""" 
    You ascend the creaky staircase, each step groaning under your weight.
    As you reach the top, you find a door slightly ajar, light flickering through the crack.
    You push the door open and see an old dusty room with an ornate mirror on the wall.
    """)
    print(
    """
    What do you do next?
    1) Examine the mirror closely.
    2) Investigate the shadows in the corner of the room.
    3) Search the dusty furniture in the room.
    4) Leave the room and explore another part of the mansion.
    """
    )
    secondChoice = input("> ")
    if secondChoice == '1':
        print("""
    As you approach the mirror, you see a strange reflection – a shadowy figure standing behind you.
    Before you can react, the figure reaches out from the mirror and pulls you into the glass.
    You find yourself in a strange dimension where the laws of physics no longer apply.
    """)
    elif secondChoice == '2':
        print("""
You notice a dark shape moving in the corner. As you move closer, a ghostly figure emerges from the shadows.
It lets out a chilling wail and reaches out to you. You feel a cold hand grab your arm, and everything goes dark.
        """)
    elif secondChoice == '3':
        print("""
    You rummage through the dusty furniture and find an old, leather-bound book. 
    Opening it reveals an ancient map of the mansion with secret passages marked in red.
    You now have a clue on how to navigate the mansion’s hidden areas.
    """)
    else:
        print("""
    You decide to leave the room and explore another part of the mansion.
    In the hallway, you find a staircase leading to the attic. 
    Curiosity gets the better of you, and you decide to climb up.
    """)
    print(
    """
    What do you do in the attic?
    1) Examine the old trunk in the corner.
    2) Investigate the strange noises coming from the far side of the attic.
    3) Look for any old documents or artifacts.
    4) Head back down to the ground floor.
    """
    )
    thirdChoice = input("> ")
    if thirdChoice == '1':
        print("""
    You open the old trunk and discover a collection of old, ornate jewelry.
    Among the jewelry is a peculiar locket that seems to radiate a faint glow.
    When you touch the locket, you hear a whisper that leads you to a hidden room.
    """)
    elif thirdChoice == '2':
        print("""
    You follow the strange noises and find an old rocking chair moving by itself.
    As you approach, the chair stops and a spectral figure appears, offering you a choice: 
    join them in their eternal rest or leave the mansion and never return.
    """)
    elif thirdChoice == '3':
        print("""
    Among the old documents, you find a letter revealing the tragic history of the mansion.
    The letter speaks of a family curse and hints at a way to break it.
    This newfound knowledge might help you escape the mansion.
    """)
    else:
        print("""
    You head back down to the ground floor, feeling a bit overwhelmed by the mansion’s mysteries.
    As you wander, you find a hidden door behind a bookshelf that leads to a basement filled with old machinery and strange symbols.
    """)

else:
    print('You decide to stay on the ground floor. You search through the dusty furniture and find an old journal.')
    print('The journal is filled with strange symbols and cryptic messages. As you read through it, you start to feel a sense of dread.')
    print(
    """
    What do you do with the journal?
    1) Try to decode the cryptic messages.
    2) Keep the journal and continue searching the ground floor.
    3) Look for a place to hide in case of danger.
    4) Leave the mansion to find help.
    """
    )
    thirdChoice = input("> ")
    if thirdChoice == '1':
        print("""
    You spend time trying to decode the messages in the journal. 
    Some of the symbols start to make sense, revealing hidden passages in the mansion.
    You now have a better understanding of the mansion's layout.
    """)
    elif thirdChoice == '2':
        print("""
    You keep the journal and continue your search. 
    You find an old key hidden in a drawer that might unlock one of the mansion's doors.
    """)
    elif thirdChoice == '3':
        print("""
    You find a small, hidden alcove behind a bookshelf. 
    It seems like a safe place to hide if you hear any strange noises.
    """)
    else:
        print("""
    You leave the mansion, feeling the weight of its secrets and curses. 
    As you step outside, you see a figure watching you from the shadows. 
    You might have escaped, but the mansion's mystery remains unresolved.
    """)
