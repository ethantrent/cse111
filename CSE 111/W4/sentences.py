"""
Write a Python program named sentences.py that generates simple English sentences. 
During this prove milestone, you will write functions that generate sentences with three parts:

a determiner (sometimes known as an article)
a noun
a verb
"""

import random

def main():
    # Generate and print six sentences one each for these grammar combinations: single past, single present, 
    # single future, plural past, plural present, plural future.
    combinations = [
        (1, "past"),
        (1, "present"),
        (1, "future"),
        (2, "past"),
        (2, "present"),
        (2, "future")
    ]
    # Generate and print a sentence for each combination.
    for quantity, tense in combinations:
        sentence = make_sentence(quantity, tense)
        print(sentence)

def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird","boy", "car", "cat", "child",
                  "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    
    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        "accidentally", "always", "angrily", "anxiously", "awkwardly",
        "badly", "blindly", "boastfully", "boldly", "bravely",
        "brightly", "calmly", "carefully", "cautiously", "cheerfully",
        "clearly", "correctly", "courageously", "crossly", "cruelly",
        "curiously", "deftly", "deliberately", "doubtfully", "eagerly",
        "elegantly", "enormously", "enthusiastically", "equally", "evenly",
        "eventually", "exactly", "faithfully", "finally", "fondly",
        "foolishly", "fortunately", "frankly", "frantically", "gently",
        "gladly", "gracefully", "greedily", "happily", "hastily",
        "honestly", "hourly", "hungrily", "innocently", "inquisitively",
        "irritably", "jealously", "justly", "kindly", "lazily",
        "loosely", "madly", "merrily", "mortally", "mysteriously",
        "nervously", "never", "obediently", "obnoxiously", "occasionally",
        "often", "only", "painfully", "perfectly", "politely",
        "poorly", "powerfully", "promptly", "quickly",

    Return: a randomly chosen adverb.
    """
    words = ["accidentally", "always", "angrily", "anxiously", "awkwardly",
             "badly", "blindly", "boastfully", "boldly", "bravely",
             "brightly", "calmly", "carefully", "cautiously", "cheerfully",
             "clearly", "correctly", "courageously", "crossly", "cruelly",
             "curiously", "deftly", "deliberately", "doubtfully", "eagerly",
             "elegantly", "enormously", "enthusiastically", "equally", "evenly",
             "eventually", "exactly", "faithfully", "finally", "fondly",
             "foolishly", "fortunately", "frankly", "frantically", "gently",
             "gladly", "gracefully", "greedily", "happily", "hastily",
             "honestly", "hourly", "hungrily", "innocently", "inquisitively",
             "irritably", "jealously", "justly", "kindly", "lazily",
             "loosely", "madly", "merrily", "mortally", "mysteriously",
             "nervously", "never", "obediently", "obnoxiously", "occasionally",
             "often", "only", "painfully", "perfectly", "politely",
             "poorly", "powerfully", "promptly", "quickly"]

    # Randomly choose and return an adverb.
    word = random.choice(words)
    return word

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
             "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for",
             "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over",
             "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    # Get a preposition, determiner, and noun.
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    # Build and return the prepositional phrase.
    phrase = preposition + " " + determiner + " " + noun
    return phrase

def make_sentence(quantity, tense):
    """Build and return a sentence with four parts:
    a determiner, a noun, a verb, and a prepositional phrase. 
    The grammatical quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    # Call the determiner, noun, verb, and prepositional phrase.
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    adverb = get_adverb()
    prepositional_phrase = get_prepositional_phrase(quantity)

    sentence = f"{determiner.capitalize()} {noun} {adverb} {verb} {prepositional_phrase}."
    return sentence

main()