import random

def monte_carlo_hedge_simulation(iterations=10000):
    """
    Монте Карло симулация на футболен хедж с АДАПТИВНА СТРАТЕГИЯ
    """
    print("🎰 MONTE CARLO ХЕДЖ СИМУЛАЦИЯ (АДАПТИВНА СТРАТЕГИЯ)")
    print("=" * 80)

    # Входни данни
    coef = [float(x) for x in input("Въведете коефициенти (1 X 2): ").split()]
    bets = [float(x) for x in input("Въведете залози (1 X 2): ").split()]

    total_income = sum(bets)

    print(f"\n📊 ВХОДНИ ДАННИ:")
    print(f"1: {bets[0]:_} лв @ {coef[0]:_} → Плащане: {bets[0] * coef[0]:_.0f} лв")
    print(f"X: {bets[1]:_} лв @ {coef[1]:_} → Плащане: {bets[1] * coef[1]:_.0f} лв")
    print(f"2: {bets[2]:_} лв @ {coef[2]:_} → Плащане: {bets[2] * coef[2]:_.0f} лв")
    print(f"Общ приход: {total_income:_} лв")
    print("=" * 80)

    wins = 0
    break_even = 0
    losses = 0
    total_profit = 0
    results = []
    strategy_counts = {"ВИСОК КОЕФИЦИЕНТ": 0, "ЛИПСА НА ИЗЯВЕН ФАВОРИТ": 0}

    print(f"\n🔄 Стартиране на {iterations} итерации...")

    for i in range(iterations):
        # Хеджиращи коефициенти (2% дисконт)
        hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]
        payouts = [bets[i] * coef[i] for i in range(3)]

        # СТЪПКА 1: ИЗБОР НА СТРАТЕГИЯ (като във втория код)
        max_coef = max(coef)
        min_payout = min(payouts)
        min_payout_index = payouts.index(min_payout)

        if max_coef >= 4:
            # СТРАТЕГИЯ 1: Базирана на най-висок коефициент
            highest_coef_index = coef.index(max_coef)
            cash = payouts[highest_coef_index]
            strategy_name = "ВИСОК КОЕФИЦИЕНТ"
            base_index = highest_coef_index
            strategy_counts["ВИСОК КОЕФИЦИЕНТ"] += 1
        else:
            # СТРАТЕГИЯ 2: Базирана на липса на изявен фаворит
            cash = min_payout
            strategy_name = "ЛИПСА НА ИЗЯВЕН ФАВОРИТ"
            base_index = min_payout_index
            strategy_counts["ЛИПСА НА ИЗЯВЕН ФАВОРИТ"] += 1

        excess = total_income - cash

        # СТЪПКА 2: Изчисляване на дефицитите
        deficits = []
        for j in range(3):
            if j != base_index:
                deficit = payouts[j] - cash
                deficits.append((j, deficit))

        # СТЪПКА 3: ПОКРИВАНЕ НА ДЕФИЦИТИТЕ С ТОЧНИ СУМИ
        hedge_amounts = [0, 0, 0]
        remaining_excess = excess

        for j, deficit in deficits:
            hedge_amount = deficit / hedge_coefs[j]
            if hedge_amount <= remaining_excess:
                hedge_amounts[j] = hedge_amount
                remaining_excess -= hedge_amount

        # СТЪПКА 4: Разпределяне на оставащия излишък
        if remaining_excess > 0:
            other_outcomes = [i for i in range(3) if i != base_index]
            sum_other_coef = hedge_coefs[other_outcomes[0]] + hedge_coefs[other_outcomes[1]]
            base_amount = remaining_excess / sum_other_coef

            for j in other_outcomes:
                other_coef = hedge_coefs[[x for x in other_outcomes if x != j][0]]
                additional_hedge = other_coef * base_amount
                hedge_amounts[j] += additional_hedge

        # СТЪПКА 5: Изчисляване на резултата за случаен изход
        total_hedge = sum(hedge_amounts)
        final_cash = total_income - total_hedge

        # Случаен изход от мача
        random_outcome = random.randint(0, 2)
        payout = payouts[random_outcome]
        hedge_income = hedge_amounts[random_outcome] * hedge_coefs[random_outcome]

        result = final_cash + hedge_income - payout
        results.append(result)

        # Класификация на резултатите
        if result > 100:  # ✅ ПЕЧАЛБА (с реалистичен праг)
            wins += 1
        elif result >= -100:  # ✅ BREAK-EVEN (малка загуба/печалба)
            break_even += 1
        else:  # ❌ ЗАГУБА
            losses += 1
        
        total_profit += result

    # Статистика
    avg_profit = total_profit / iterations
    win_rate = (wins / iterations) * 100
    break_even_rate = (break_even / iterations) * 100
    loss_rate = (losses / iterations) * 100

    print(f"\n📊 РЕЗУЛТАТИ ОТ {iterations} ИТЕРАЦИИ:")
    print("=" * 50)
    print(f"✅ Печеливши ситуации: {wins} ({win_rate:.1f}%)")
    print(f"⚖️  Break-even ситуации: {break_even} ({break_even_rate:.1f}%)")
    print(f"❌ Загубени ситуации: {losses} ({loss_rate:.1f}%)")
    print(f"💰 Средна печалба: {avg_profit:_.0f} лв")
    print(f"📈 Обща печалба: {total_profit:_.0f} лв")

    # Статистика за стратегиите
    print(f"\n🎯 СТРАТЕГИИ:")
    for strategy, count in strategy_counts.items():
        percentage = (count / iterations) * 100
        print(f"   {strategy}: {count} пъти ({percentage:.1f}%)")

    # Детайлна статистика
    max_profit = max(results)
    min_profit = min(results)
    positive_profits = [r for r in results if r > 100]
    avg_positive = sum(positive_profits) / len(positive_profits) if positive_profits else 0

    print(f"\n📈 ДЕТАЙЛНА СТАТИСТИКА:")
    print(f"   Макс. печалба: {max_profit:_.0f} лв")
    print(f"   Мин. резултат: {min_profit:_.0f} лв")
    print(f"   Средна печалба при печеливши ситуации: {avg_positive:_.0f} лв")
    
    # Анализ на ефективността
    if wins + break_even > 0:
        success_rate = ((wins + break_even) / iterations) * 100
        print(f"   📊 Успешни операции (печалба/break-even): {success_rate:.1f}%")

    # Препоръки
    print(f"\n💡 ПРЕПОРЪКИ:")
    if win_rate > 70:
        print("   🎉 Отлична стратегия! Висок процент на печалби.")
    elif win_rate > 50:
        print("   👍 Добра стратегия. Стабилни резултати.")
    else:
        print("   ⚠️  Стратегията има висок риск. Препоръчително е тестване с различни коефициенти.")
    
    if loss_rate < 5:
        print("   🛡️  Ниск риск - рядко загуби.")
    elif loss_rate < 15:
        print("   ⚖️  Умерен риск - приемлив брой загуби.")
    else:
        print("   🚨 Висок риск - чести загуби.")

# Стартиране на симулацията
if __name__ == "__main__":
    try:
        iterations = int(input("Въведете брой итерации (по подразбиране 10000): ") or "10000")
        monte_carlo_hedge_simulation(iterations)
    except ValueError:
        print("Невалиден брой итерации. Стартиране с 10000...")
        monte_carlo_hedge_simulation()
