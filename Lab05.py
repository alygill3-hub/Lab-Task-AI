
import math

minimax_count = 0
pruning_count = 0

def minimax(depth, index, is_max, scores, max_depth):
    global minimax_count

    if depth == max_depth:
        minimax_count += 1
        return scores[index]

    if is_max:
        left = minimax(depth + 1, index * 2, False, scores, max_depth)
        right = minimax(depth + 1, index * 2 + 1, False, scores, max_depth)
        return max(left, right)
    else:
        left = minimax(depth + 1, index * 2, True, scores, max_depth)
        right = minimax(depth + 1, index * 2 + 1, True, scores, max_depth)
        return min(left, right)


def alphabeta(depth, index, is_max, scores, max_depth, alpha, beta):
    global pruning_count

    if depth == max_depth:
        pruning_count += 1
        return scores[index]

    if is_max:
        best = float('-inf')

        for child in range(2):
            result = alphabeta(
                depth + 1, index * 2 + child,
                False, scores, max_depth, alpha, beta
            )

            best = max(best, result)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for child in range(2):
            result = alphabeta(
                depth + 1, index * 2 + child,
                True, scores, max_depth, alpha, beta
            )

            best = min(best, result)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


test_cases = [
    [3, 5, 2, 9, 3, 5, 2, 9],
    [5, 3, 9, 2, 5, 3, 9, 2],
    [2, 9, 3, 5, 2, 9, 3, 5],
    [4, 4, 4, 4, 4, 4, 4, 4]
]

for scores in test_cases:
    minimax_count = 0
    pruning_count = 0

    max_depth = int(math.log2(len(scores)))

    print("Input Scores:", scores)

    result1 = minimax(0, 0, True, scores, max_depth)
    print("Minimax Result:", result1)
    print("Minimax Leaves Checked:", minimax_count)

    result2 = alphabeta(
        0, 0, True, scores, max_depth,
        float('-inf'), float('inf')
    )

    print("Alpha-Beta Result:", result2)
    print("Alpha-Beta Leaves Checked:", pruning_count)
    print("-" * 35)
