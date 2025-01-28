# You need to have at least three levels of scenarios with possible choices.
# At least one of your scenarios must have more than two possible choices.
# In each prompt, write the choices in ALL CAPS, 
# # so that the user knows which words are possible responses to choose.
# When checking the users responses, you should match on the keyword, 
# regardless of the uppercase/lowercase used in the response (e.g., "match", "MATCH", "Match" should all work).
# Making different choices should take you to different scenarios. (You shouldn't have the same result for different choices.)
# Choices should only work for the correct question.

print ('You are Percy Jackson, a demigod, the son of Poseidon.')
print ('Please type the word that is bolded to make your decision.')

print ()

print ('You wake up in a dark forest and a Minotaur appears!')
answer = input ('Do you RUN or FIGHT the Minotaur? ').lower().strip()
#first level 1
if answer == 'run':
    print('\nYou start to run away and try to find a place to hide!')
    answer = input('Do you run to a CAVE, continue in the FORREST, or FIGHT the Minotaur? ').lower().strip()
    #second level 1
    if answer == 'cave':
        print ('\nYou run inside the cave but it is a deadend! And the Minotaur follows you!')
        answer = input('You are cornered and have nowhere to go. Do you FIGHT or try to ESCAPE? ').lower().strip()
        #third level 1
        if answer == 'fight':
            print ('\nYou fight the Minotaur off and escape safely back to Camp Half-Blood!')
            print ('You win!')
        elif answer == 'escape':
            #third level 2
            print ('\nYou try to escape but the Minotaur was too quick and he attacks you.')
            print ('You lose')
        else:
            print ("\nThat was not an option. The Minotaur sliced you in half. ")
            print ('Game Over')
            exit ()
    elif answer == 'forrest':
        #second level 2
        print ('\nYou keep running from the Minotaur in hopes to lose its trail.')
        answer = input ('As you are running, it starts to catch up to you. \nYou notice a shining light blinding your eyes. Do you decide to RUN, CLIMB a tree, or FOLLOW the shiny light? ').lower().strip()
        if answer == 'run':
            #third level 1
            print ('\nYou keep running but start to get tired and slow down.')
            print ('The Minotaur catches up and slays you')
            print ('Game Over')
            exit ()
        elif answer == 'climb':
            #third level 2
            print ('\nYou attempt to climb the tree and it holds onto your leg!')
            print ('But in comes Annabeth to save the day and draw away the Minotaur')
            print ('You won!')
            exit ()
        elif answer == 'follow':
            #third level 3
            print ("\nYou follow the bright light and it's your friend Grover!")
            print ('He calls you over and helps you sucessfully escape!')
            print ('You win!')
            exit ()
        else:
            print ("\nThat was not an option. The Minotaur sliced you in half. ")
            print ('Game Over')
            exit ()
    elif answer == 'bushes':
        #second level 3
        print ('\nYou try hiding in some bushes. The Minotaur slowly walks past you, trying to sense where you are.')
        answer = input("Do you keep QUIET or try to ESCAPE while it isn't looking? ")
        if answer == 'quiet':
            print ("You stay low and don't make any noise. The Minotaur doesn't sense you and leaves.")
            print ('You won!')
            exit ()
        elif answer == 'escape':
            print ('You make an attempt to escape but the Minotaur hears you and takes you down.')
            print ('Game Over')
            exit ()
        else:
            print ("\nThat was not an option. The Minotaur sliced you in half. ")
            print ('Game Over')
            exit ()
    else:
            print ("\nThat was not an option. The Minotaur sliced you in half. ")
            print ('Game Over')
            exit ()
elif answer == 'fight':
    #first level 2
    print ('\nYou take on the Minotaur and use Riptide to fight back!')
    answer = input ('Do you attack the HEAD, LEGS, or ARMS? ').lower().strip()
    if answer == 'head':
        #second 2 level 1
        print ('\nYou run up and JUMP to attack the Minotaurs head! But! It knocks you down before you could get close enough.')
        answer = input ("There's a locked chest next to you, do you OPEN it or LEAVE it be? ").lower().strip()
        if answer == 'open':
            #third level 1
            print ('\nYou open the locked chest by breaking the lock and it is a glowing seashell!')
            print ('It grants you power from the sun and turns the Minotaur into dust.')
            print ('You won')
            exit ()
        elif answer == 'leave':
            print ('\nYou leave the chest alone and try to fight back again. The Minotaur weakens you and you faint.')
            print ('Game Over')
            exit ()
            #third level 2
        else:
            print ('n/That was not an option. Two Cyclopse see you and take you away.')
            print ('Game Over')
            exit ()
    elif answer == 'legs':
        #second 2 level 2
        print ('\nYou try to be sneaky and go for the legs and give the Minotaur a nice slice!')
        answer = input('It tries to fight back to defend itself. Do you BLOCK the attack or try to HIT it back? ').lower().strip()
        if answer == 'block':
            #third level 1
            print ('\nYou block the attack and impale the Minotaur. Well done!')
            print ('You won')
            exit ()
        elif answer == 'hit':
            #third level 2
            print ('\nYou try slicing the Minotar again but he was too strong and overpowered you.')
            print ('The Minotaur slayed you.')
            print ('Game Over')
            exit ()
        else:
            print ('\nThat was not an option. A Gorgon comes into your sight and you turn into stone.')
            print ('Game Over')
            exit ()
    elif answer == 'arms':
        #second 2 level 3
        print ('\nYou try to swing at his arm and it worked! It gives you the opportunity to go for the head!')
        print ('You slayed the Minotaur!')
        print ('You won!')
        exit ()
    else:
        print ('\nThat was not an option. Three Furies sweep in and take you away.')
        print ('Game Over')
        exit ()
else:
    print ("\nThat was not an option. You froze and couldn't decide what to do. The Minotaur charged you and you died.")
    exit ()

