import random

def monte_carlo_hedge_simulation(iterations=10000):
    """
    Monte Carlo simulation of football hedge with ADAPTIVE STRATEGY
    """
    print("MONTE CARLO HEDGE SIMULATION (ADAPTIVE STRATEGY)")
    print("=" * 80)

    # Input data
    coef = [float(x) for x in input("Enter odds (1 X 2): ").split()]
    bets = [float(x) for x in input("Enter bets (1 X 2): ").split()]

    total_income = sum(bets)

    print(f"\nINPUT DATA:")
    print(f"1: {bets[0]:_} at {coef[0]:_} → Payout: {bets[0] * coef[0]:_.0f}")
    print(f"X: {bets[1]:_} at {coef[1]:_} → Payout: {bets[1] * coef[1]:_.0f}")
    print(f"2: {bets[2]:_} at {coef[2]:_} → Payout: {bets[2] * coef[2]:_.0f}")
    print(f"Total income: {total_income:_}")
    print("=" * 80)

    wins = 0
    break_even = 0
    losses = 0
    total_profit = 0
    results = []
    strategy_counts = {"HIGH ODDS": 0, "NO CLEAR FAVORITE": 0}

    print(f"\nStarting {iterations} iterations...")

    for i in range(iterations):
        # Hedging odds (2% discount)
        hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]
        payouts = [bets[i] * coef[i] for i in range(3)]

        # STEP 1: STRATEGY SELECTION (as in the second code)
        max_coef = max(coef)
        min_payout = min(payouts)
        min_payout_index = payouts.index(min_payout)

        if max_coef >= 4:
            # STRATEGY 1: Based on highest odds
            highest_coef_index = coef.index(max_coef)
            cash = payouts[highest_coef_index]
            strategy_name = "HIGH ODDS"
            base_index = highest_coef_index
            strategy_counts["HIGH ODDS"] += 1
        else:
            # STRATEGY 2: Based on no clear favorite
            cash = min_payout
            strategy_name = "NO CLEAR FAVORITE"
            base_index = min_payout_index
            strategy_counts["NO CLEAR FAVORITE"] += 1

        excess = total_income - cash

        # STEP 2: Calculate deficits
        deficits = []
        for j in range(3):
            if j != base_index:
                deficit = payouts[j] - cash
                deficits.append((j, deficit))

        # STEP 3: COVER DEFICITS WITH EXACT AMOUNTS
        hedge_amounts = [0, 0, 0]
        remaining_excess = excess

        for j, deficit in deficits:
            hedge_amount = deficit / hedge_coefs[j]
            if hedge_amount <= remaining_excess:
                hedge_amounts[j] = hedge_amount
                remaining_excess -= hedge_amount

        # STEP 4: Distribute remaining excess
        if remaining_excess > 0:
            other_outcomes = [i for i in range(3) if i != base_index]
            sum_other_coef = hedge_coefs[other_outcomes[0]] + hedge_coefs[other_outcomes[1]]
            base_amount = remaining_excess / sum_other_coef

            for j in other_outcomes:
                other_coef = hedge_coefs[[x for x in other_outcomes if x != j][0]]
                additional_hedge = other_coef * base_amount
                hedge_amounts[j] += additional_hedge

        # STEP 5: Calculate result for random outcome
        total_hedge = sum(hedge_amounts)
        final_cash = total_income - total_hedge

        # Random match outcome
        random_outcome = random.randint(0, 2)
        payout = payouts[random_outcome]
        hedge_income = hedge_amounts[random_outcome] * hedge_coefs[random_outcome]

        result = final_cash + hedge_income - payout
        results.append(result)

        # Result classification
        if result > 100:  # WIN (with realistic threshold)
            wins += 1
        elif result >= -100:  # BREAK-EVEN (small loss/profit)
            break_even += 1
        else:  # LOSS
            losses += 1
        
        total_profit += result

    # Statistics
    avg_profit = total_profit / iterations
    win_rate = (wins / iterations) * 100
    break_even_rate = (break_even / iterations) * 100
    loss_rate = (losses / iterations) * 100

    print(f"\nRESULTS FROM {iterations} ITERATIONS:")
    print("=" * 50)
    print(f"Winning situations: {wins} ({win_rate:.1f}%)")
    print(f"Break-even situations: {break_even} ({break_even_rate:.1f}%)")
    print(f"Losing situations: {losses} ({loss_rate:.1f}%)")
    print(f"Average profit: {avg_profit:_.0f}")
    print(f"Total profit: {total_profit:_.0f}")

    # Strategy statistics
    print(f"\nSTRATEGIES:")
    for strategy, count in strategy_counts.items():
        percentage = (count / iterations) * 100
        print(f"   {strategy}: {count} times ({percentage:.1f}%)")

    # Detailed statistics
    max_profit = max(results)
    min_profit = min(results)
    positive_profits = [r for r in results if r > 100]
    avg_positive = sum(positive_profits) / len(positive_profits) if positive_profits else 0

    print(f"\nDETAILED STATISTICS:")
    print(f"   Max profit: {max_profit:_.0f}")
    print(f"   Min result: {min_profit:_.0f}")
    print(f"   Average profit in winning situations: {avg_positive:_.0f}")
    
    # Effectiveness analysis
    if wins + break_even > 0:
        success_rate = ((wins + break_even) / iterations) * 100
        print(f"   Successful operations (profit/break-even): {success_rate:.1f}%")

    # Recommendations
    print(f"\nRECOMMENDATIONS:")
    if win_rate > 70:
        print("   Excellent strategy! High win percentage.")
    elif win_rate > 50:
        print("   Good strategy. Stable results.")
    else:
        print("   Strategy has high risk. Recommended to test with different odds.")
    
    if loss_rate < 5:
        print("   Low risk - rare losses.")
    elif loss_rate < 15:
        print("   Moderate risk - acceptable number of losses.")
    else:
        print("   High risk - frequent losses.")

# Start simulation
if __name__ == "__main__":
    try:
        iterations = int(input("Enter number of iterations (default 10000): ") or "10000")
        monte_carlo_hedge_simulation(iterations)
    except ValueError:
        print("Invalid number of iterations. Starting with 10000...")
        monte_carlo_hedge_simulation()
