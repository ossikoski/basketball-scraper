from scraper import Scraper


def get_fantasy_points(stats, player):
    fantasy_max = 0
    for position in range(1, 6):
        if position == 1:
            fantasy = stats[player][-1] + 2*stats[player][1]
        if position == 2:
            fantasy = stats[player][-1] + 3*stats[player][5]
            if fantasy > fantasy_max:
                fantasy_max = fantasy
                best_position = position
        if position == 3:
            fantasy = stats[player][-1] + 2*stats[player][0]
            if fantasy > fantasy_max:
                fantasy_max = fantasy
                best_position = position
        if position == 4:
            fantasy = stats[player][-1] + 2*stats[player][3]
            if fantasy > fantasy_max:
                fantasy_max = fantasy
                best_position = position
        if position == 5:
            fantasy = stats[player][-1] + 2*stats[player][4]
            if fantasy > fantasy_max:
                fantasy_max = fantasy
                best_position = position

    return fantasy_max, best_position
        
    
def main():
    s = Scraper()
    price_data = s.get_prices()
    stats = s.stats()
    print(stats)

if __name__ == '__main__':
    main()