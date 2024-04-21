def find_winner(filename: str)->str:
    """
    Function to determine the winner of the presidential election.

    Arguments:
    filename(str): The name of the file with voting data.

    Returns:
    str: The name of the winner or a message indicating that a third round of voting is required.
    """
    results = {}
    with open(filename, 'r') as file:
        for line in file:
            division_line = line.strip()
            part = division_line.split()

            candidate = part[0]
            votes = int(part[1])
            # print(candidate, votes)
            if candidate in results:
                results[candidate] += votes
            else:
                results[candidate] = votes
            # print(results)

    max_votes = max(results.values())
    winner = [candidate for candidate, votes in results.items() if votes == max_votes]
    # print(results)

    if len(winner) > 1:
        return 'A third round of voting is required'
    else:
        return f'Winner: {winner[0]}'

print(find_winner('Hw6/input.txt'))
