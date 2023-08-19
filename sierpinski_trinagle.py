# def move_tower(n, source, auxiliary, target):
#     if n == 1:
#         print(f"Move disc {n} from {source} to {target}")
#     else:
#         move_tower(n - 1, source, target, auxiliary)
#         print(f"Move disc {n} from {source} to {target}")
#         move_tower(n - 1, auxiliary, source, target)

# n = 3
# source_peg = 'A'
# auxiliary_peg = 'B'
# target_peg = 'C'

# initial_state = "A" * n
# final_state = "C" * n

# print(f"Move the tower from {initial_state} to {final_state}:\n")
# move_tower(n, source_peg, auxiliary_peg, target_peg)

def hanoi_sierpinski(n, source, auxiliary, target):
    moves = []
    
    def move_disc(from_peg, to_peg):
        moves.append((from_peg, to_peg))
    
    if n > 0:
        # Step 1: Move n-1 discs from source to auxiliary peg using the target peg as auxiliary.
        moves.extend(hanoi_sierpinski(n-1, source, target, auxiliary))

        # Step 2: Move the nth disc from source to target peg.
        move_disc(source, target)

        # Step 3: Move the n-1 discs from auxiliary peg to target peg using the source peg as auxiliary.
        moves.extend(hanoi_sierpinski(n-1, auxiliary, source, target))
    
    return moves

# Call the function to generate all permutations
all_permutations = []

# Iterate through all possible starting configurations of pegs A, B, and C
for start_config in [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]:
    moves = hanoi_sierpinski(3, *start_config)
    all_permutations.append(moves)

# Print all permutations
for i, permutation in enumerate(all_permutations):
    print(f"Permutation {i + 1}:")
    for move in permutation:
        print(f"Move disc from Peg {move[0]} to Peg {move[1]}")
    print()


