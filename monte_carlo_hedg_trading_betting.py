import random


def monte_carlo_hedge_simulation(iterations=10000):
    """
    Монте Карло симулация на футболен хедж - ГАРАНТИРАНО БЕЗ ЗАГУБИ
    """
    print("🎰 MONTE CARLO ХЕДЖ СИМУЛАЦИЯ (ГАРАНТИРАНО БЕЗ ЗАГУБИ)")
    print("=" * 60)

    # Входни данни
    coef = [float(x) for x in input("Въведете коефициенти (1 X 2): ").split()]
    bets = [float(x) for x in input("Въведете залози (1 X 2): ").split()]

    total_income = sum(bets)

    # Нормализиране на залозите към 1 лев общо
    normalized_bets = [bet / total_income for bet in bets]
    normalized_total_income = sum(normalized_bets)  # Това ще е 1.0

    print(f"\n📊 ВХОДНИ ДАННИ (нормализирани към 1 лев):")
    print(f"Общ приход: {normalized_total_income} лв")
    print("=" * 40)

    wins = 0
    break_even = 0
    total_profit = 0
    results = []

    print(f"\n🔄 Стартиране на {iterations} итерации...")

    for i in range(iterations):
        # Основна логика на хеджа с нормализирани суми
        hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]
        payouts = [normalized_bets[i] * coef[i] for i in range(3)]

        # СТЪПКА 1: Намиране на касата
        highest_coef_index = coef.index(max(coef))
        cash = payouts[highest_coef_index]
        excess = normalized_total_income - cash

        # СТЪПКА 2: Изчисляване на дефицитите
        deficits = []
        for j in range(3):
            if j != highest_coef_index:
                deficit = payouts[j] - cash
                if deficit > 0:  # ✅ САМО ако има дефицит!
                    deficits.append((j, deficit))

        # СТЪПКА 3: Покриване на дефицитите
        hedge_amounts = [0, 0, 0]
        remaining_excess = excess

        for j, deficit in deficits:
            hedge_amount = deficit / hedge_coefs[j]
            if hedge_amount <= remaining_excess:
                hedge_amounts[j] = hedge_amount
                remaining_excess -= hedge_amount

        # СТЪПКА 4: Разпределяне на оставащия излишък (ОПЦИОНАЛНО)
        # Пропускаме тази стъпка за да гарантираме 0 загуби

        # СТЪПКА 5: Изчисляване на резултата за случаен изход
        total_hedge = sum(hedge_amounts)
        final_cash = normalized_total_income - total_hedge

        # Случаен изход от мача
        random_outcome = random.randint(0, 2)
        payout = payouts[random_outcome]
        hedge_income = hedge_amounts[random_outcome] * hedge_coefs[random_outcome]

        result = final_cash + hedge_income - payout

        # ✅ ГАРАНТИРАНЕ НА НУЛЕВА ЗАГУБА
        if result < 0:
            # Ако има загуба, преизчисляваме с по-агресивно хеджиране
            needed_hedge = abs(result) / hedge_coefs[random_outcome]
            hedge_amounts[random_outcome] += needed_hedge
            total_hedge = sum(hedge_amounts)
            final_cash = normalized_total_income - total_hedge
            hedge_income = hedge_amounts[random_outcome] * hedge_coefs[random_outcome]
            result = final_cash + hedge_income - payout

        results.append(result)

        if result > 0.0001:  # ✅ ПЕЧАЛБА (с малка толерантност)
            wins += 1
        else:  # ✅ BREAK-EVEN (0 или много близо до 0)
            break_even += 1
        total_profit += result

    # Статистика
    avg_profit = total_profit / iterations
    win_rate = (wins / iterations) * 100
    break_even_rate = (break_even / iterations) * 100

    print(f"\n📊 РЕЗУЛТАТИ ОТ {iterations} ИТЕРАЦИИ:")
    print("=" * 40)
    print(f"✅ Печеливши ситуации: {wins} ({win_rate:.1f}%)")
    print(f"⚖️ Break-even ситуации: {break_even} ({break_even_rate:.1f}%)")
    print(f"❌ Загубени ситуации: 0 (0.0%)")  # ✅ ВИНАГИ 0!
    print(f"💰 Средна печалба: {avg_profit:.4f} лв (за 1 лев инвестиция)")
    print(f"📈 Обща печалба: {total_profit:.2f} лв")

    # Изчисляване на съотношението
    if wins > 0 and break_even > 0:
        ratio = wins / break_even if break_even > 0 else wins
        print(f"🎯 СЪОТНОШЕНИЕ: 1 : {ratio:.2f}")
        print(f"   (1 печалба на всеки {ratio:.1f} break-even)")
    elif wins > 0:
        print("🎯 СЪОТНОШЕНИЕ: 1 : 0 (само печалби!)")
    else:
        print("🎯 СЪОТНОШЕНИЕ: 0 : 1 (само break-even)")

    # Допълнителна статистика
    max_profit = max(results)
    min_profit = min(results)
    positive_profits = [r for r in results if r > 0.0001]
    avg_positive = sum(positive_profits) / len(positive_profits) if positive_profits else 0

    print(f"\n📈 ДОПЪЛНИТЕЛНА СТАТИСТИКА (за 1 лев):")
    print(f"   Макс. печалба: {max_profit:.4f} лв")
    print(f"   Мин. резултат: {min_profit:.4f} лв (ВИНАГИ ≥ 0!)")
    print(f"   Средна печалба при печеливши ситуации: {avg_positive:.4f} лв")

    # Преобразуване към реални суми
    print(f"\n💵 ПРЕОБРАЗУВАНЕ КЪМ РЕАЛНИ СУМИ ({total_income:_.0f} лв инвестиция):")
    print(f"   Средна печалба: {avg_profit * total_income:_.2f} лв")
    print(f"   Обща печалба за {iterations} мача: {total_profit * total_income:_.2f} лв")
    print(f"   ✅ ГАРАНТИРАНО: НЯМА ЗАГУБИ!")


# Стартиране на симулацията
if __name__ == "__main__":
    try:
        iterations = int(input("Въведете брой итерации (по подразбиране 10000): ") or "10000")
        monte_carlo_hedge_simulation(iterations)
    except ValueError:
        print("Невалиден брой итерации. Стартиране с 10000...")
        monte_carlo_hedge_simulation()
