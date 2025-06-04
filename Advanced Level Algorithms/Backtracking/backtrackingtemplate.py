def backtrack(candidate):
    if is_complete(candidate):
        output(candidate)
        return

    for next_candidate in generate_candidates(candidate):
        if is_valid(next_candidate):
            make_move(next_candidate)  # Modify state
            backtrack(next_candidate)  # Recurse
            undo_move(next_candidate)  # Backtrack (undo)