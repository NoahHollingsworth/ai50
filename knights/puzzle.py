from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Biconditional(AKnave, Not(AKnight)), #A can only be a knave if it is not a knight
    Biconditional(And(AKnight, AKnave), AKnight) #If "I am both a knight and a knave." is true, A is a knight
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Biconditional(AKnave, Not(AKnight)), #A can only be a knave if it is not a knight
    Biconditional(BKnave, Not(BKnight)), #B can only be a knave if it is not a knight
    Biconditional(And(AKnave, BKnave), AKnight) #A and B can only be knaves if A is telling the truth (must be a knight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Biconditional(AKnave, Not(AKnight)), #A can only be a knave if it is not a knight
    Biconditional(BKnave, Not(BKnight)), #B can only be a knave if it is not a knight
    Implication(AKnight, BKnight), #If A is telling the truth, they must both be knights (the reverse is not necessarily true)
    Biconditional(BKnight, AKnave) #If B is telling the truth, it must be a knight, and A must be a knave

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Biconditional(AKnave, Not(AKnight)), #A can only be a knave if it is not a knight
    Biconditional(BKnave, Not(BKnight)), #B can only be a knave if it is not a knight
    Biconditional(CKnave, Not(CKnight)), #C can only be a knave if it is not a knight
    
    Biconditional(AKnight, CKnight), #if A is a knight, then C is a knight because it told the truth
    Biconditional(BKnight, CKnave), #If B is a knight, C is a knave is true
    Biconditional(BKnave, CKnight), #If B is a knave, then C is a knave is false 
    Implication(AKnight, BKnave), #If A is a knight, then be B must be a knave
    Implication(BKnight, Biconditional(AKnight, AKnave)) #If B is a knight, A must have said it's a knave, and told the truth
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
