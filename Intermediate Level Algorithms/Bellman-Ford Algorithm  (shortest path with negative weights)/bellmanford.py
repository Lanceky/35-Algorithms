def find_cheapest_flights(flights, origin):
    prices = {airport: float('inf') for airport in flights}
    prices[origin] = 0

    # Relax edges
    for _ in range(len(flights) - 1):
        for airport in flights:
            for destination, cost in flights[airport].items():
                if prices[airport] + cost < prices[destination]:
                    prices[destination] = prices[airport] + cost

    # Check for negative cycles (impossible pricing loops)
    for airport in flights:
        for destination, cost in flights[airport].items():
            if prices[airport] + cost < prices[destination]:
                return "Error: Impossible flight pricing (negative cycle detected)"

    return prices


# Flight network with layover incentives
flights = {
    'A': {'B': 200, 'C': 500},
    'B': {'C': -50},  # $50 discount for connecting via B
    'C': {'D': 300},
    'D': {'B': -100}  # $100 discount for returning to B from D
}

print(find_cheapest_flights(flights, 'A'))