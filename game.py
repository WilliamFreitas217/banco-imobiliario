import random


def erase_all_properties(player, table):
    """
    Erases the name of the player of all his properties
    :param player: Player being deleted
    :param table: table of the game
    """
    for p in table:
        if p.owner and p.owner.persona == player.persona:
            table[table.index(p)].vacate()


def game(table, properties_qnt, players, original_order):
    """
    Function that will run the game
    :param table: game table
    :param properties_qnt: how many properties there will be on the table
    :param players: Players that will be playing
    :param original_order: Original order of players
    :return: rounds spent, winner
    """
    rounds = 0
    while len(players) > 1 and rounds < 1000:
        for player in players:
            dice = random.randint(1, 6)
            player.rounds_played += dice
            table_field = player.rounds_played % properties_qnt

            if table_field == 0:
                player.cash += 100

            if not table[table_field].owner:
                bought = player.buy_property(table[table_field])
                table[table_field].owner = player if bought else None
            else:
                players[players.index(table[table_field].owner)].cash += table[table_field].rent
                player.cash -= table[table_field].rent

            if player.cash < 0:
                erase_all_properties(player, table)
                players.pop(players.index(player))
        rounds += 1

    sorted_winner_list = sorted(players, key=lambda p: p.cash)
    winner = sorted_winner_list[-1]

    tie = [winner]
    for w in sorted_winner_list:
        if w.persona != winner.persona and w.cash == winner.cash:
            tie.append(w)
    tie_verification = sorted([original_order.index(w.persona) for w in tie])[0]

    return rounds, next(p for p in tie if p.persona == original_order[tie_verification]).persona
