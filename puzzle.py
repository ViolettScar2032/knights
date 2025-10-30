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
    # A is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # A’s statement: "I am both a knight and a knave"
    Implication(AKnight, And(AKnight, AKnave)),   # If A is a knight, statement is true
    Implication(AKnave, Not(And(AKnight, AKnave))) # If A is a knave, statement is false
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B are either knights or knaves, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A says "We are both knaves"
    Implication(AKnight, And(AKnave, BKnave)),      # If A is a knight, statement is true
    Implication(AKnave, Not(And(AKnave, BKnave)))   # If A is a knave, statement is false
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B can’t be both knight and knave
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A says "We are the same kind"
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),

    # B says "We are of different kinds"
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))
)

# Puzzle 3
knowledge3 = And(
    # Each character is either a knight or knave
    Or(AKnight, AKnave), Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave), Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave), Not(And(CKnight, CKnave)),

    # A's ambiguous statement
    Or(AKnight, AKnave),

    # B says "A said 'I am a knave'"
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),

    # B says "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


# def main():
#     symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
#     puzzles = [
#         ("Puzzle 0", knowledge0),
#         ("Puzzle 1", knowledge1),
#         ("Puzzle 2", knowledge2),
#         ("Puzzle 3", knowledge3)
#     ]
#     for puzzle, knowledge in puzzles:
#         print(puzzle)
#         if len(knowledge.conjuncts) == 0:
#             print("    Not yet implemented.")
#         else:
#             for symbol in symbols:
#                 if model_check(knowledge, symbol):
#                     print(f"    {symbol}")

def main():
    puzzles = [
        ("Puzzle 0", [("A", AKnight, AKnave)], knowledge0),
        ("Puzzle 1", [("A", AKnight, AKnave), ("B", BKnight, BKnave)], knowledge1),
        ("Puzzle 2", [("A", AKnight, AKnave), ("B", BKnight, BKnave)], knowledge2),
        ("Puzzle 3", [("A", AKnight, AKnave), ("B", BKnight, BKnave), ("C", CKnight, CKnave)], knowledge3)
    ]

    for puzzle_name, characters, knowledge in puzzles:
        print(puzzle_name)
        for name, knight, knave in characters:
            if model_check(knowledge, knight):
                print(f"    {name} is a Knight")
            elif model_check(knowledge, knave):
                print(f"    {name} is a Knave")



if __name__ == "__main__":
    main()
