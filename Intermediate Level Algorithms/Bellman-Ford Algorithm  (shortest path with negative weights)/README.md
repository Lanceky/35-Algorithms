Bellman-Ford Algorithm: Handling Negative Weights in Shortest Paths
1. Core Concept

Bellman-Ford is a single-source shortest path algorithm that works with negative edge weights (unlike Dijkstra's). It can also detect negative weight cycles, making it valuable for financial arbitrage and risk analysis systems.
Key Features

    Works with negative weights

    Detects negative cycles

    Time Complexity: O(VE) (slower than Dijkstra but more versatile)

    Space Complexity: O(V)

Problem Statement

Imagine you're booking flights where:

    Airports = Nodes (A, B, C, D)

    Flights = Edges with costs (some routes offer layover cash incentives at certain airports)

    Goal: Find the cheapest route from your origin to all other airports

Flight Network:

A → B: $200  
A → C: $500  
B → C: -$50 (layover incentive: airline pays you $50 to connect via B)  
C → D: $300  
D → B: -$100 (layover incentive at D)

Why Negative Weights?

    The "-$50" for B→C means:
    "If you connect through B, the airline discounts your next flight by $50"

    This could represent:

        Airline subsidies for using less popular hubs

        Loyalty rewards for specific routes

        Government incentives to promote tourism at certain airports

Step-by-Step Cost Calculation (Bellman-Ford)

    Initial Costs from A:
    A: $0, B: ∞, C: ∞, D: ∞

    First Pass:

        A→B: $200

        A→C: $500

        B→C: $200 (A→B) + (-$50) = $150 (cheaper than direct A→C!)

        C→D: $150 (A→B→C) + $300 = $450

        D→B: $450 (A→B→C→D) + (-$100) = $350 (but B is already $200 → no update)

    Final Cheapest Flights from A:

    A: $0  
    B: $200 (A→B)  
    C: $150 (A→B→C with $50 discount)  
    D: $450 (A→B→C→D)

Negative Cycle Detection

If we had:

B → C: -$200  
C → B: -$200

This would create a "free money loop" (B→C→B→C...), which Bellman-Ford would detect as invalid.