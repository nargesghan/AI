def tally(rows):
    countries={}
    result=['Team                           | MP |  W |  D |  L |  P',]
    for com in rows:
        first, second, match_result = com.split(';')
        if match_result=="win":
            countries.setdefault(first,[]).append("win")
            countries.setdefault(second,[]).append("loss")
        elif match_result=="loss":
            countries.setdefault(first,[]).append("loss")
            countries.setdefault(second,[]).append("win")
        else:  # it's a draw
            countries.setdefault(first,[]).append("draw")
            countries.setdefault(second,[]).append("draw")

    # Create a list of tuples (number of points, country) for sorting
    sorting_list = [(countries[country].count('win')*3 + countries[country].count('draw'), country) for country in countries]
    # Sort the list by number of wins (descending) and then by country name (ascending)
    sorted_countries = sorted(sorting_list, key=lambda x: (-x[0], x[1]))

    for wins, country in sorted_countries:
        MP=len(countries[country])
        W=countries[country].count('win')
        L=countries[country].count('loss')
        D=countries[country].count('draw')
        P=W*3+D
        result.append(f'{country.ljust(31)}|  {MP} |  {W} |  {D} |  {L} | {P:2}')  

    return result
