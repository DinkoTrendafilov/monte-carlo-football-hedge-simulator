# 🎰 Monte Carlo Hedge Simulator for Football Betting

This project demonstrates a **Monte Carlo simulation approach** for modeling a **hedge strategy** in football (soccer) betting.  
It helps estimate profitability, win/loss ratios, and expected returns when placing multiple bets on different outcomes (1, X, 2).

---

## 🧠 Concept

In betting markets, hedging is a risk management technique used to **minimize potential losses** by placing bets on multiple outcomes of the same event.  
This simulator uses **Monte Carlo methods** to simulate thousands of random match outcomes and analyze the financial performance of a given hedge structure.

---

## ⚙️ How It Works

1. **User Input**:
   - Betting odds for each outcome (1, X, 2)
   - Amounts wagered on each outcome

2. **Normalization**:
   - All bets are scaled to a total investment of **1 unit** (e.g., 1 BGN) for fair comparison.

3. **Simulation**:
   - Random match outcomes are generated across *N* iterations (default = 10,000).
   - The algorithm calculates payouts, hedging amounts, and total returns.

4. **Output Metrics**:
   - ✅ Win rate (%)
   - ❌ Loss rate (%)
   - 💰 Average profit/loss per iteration
   - 🎯 Profit-to-loss ratio
   - 📈 Maximum and minimum profits
   - 💵 Scaled results for the actual investment

---

## 🧩 Example

```bash
🎰 MONTE CARLO ХЕДЖ СИМУЛАЦИЯ (НОРМАЛИЗИРАНА)
============================================

Enter odds (1 X 2): 2.1 3.3 3.8  
Enter bets (1 X 2): 50 30 20  
Enter number of iterations: 10000
Output Example:

yaml
Копиране на код
✅ Winning Scenarios: 6152 (61.5%)
❌ Losing Scenarios: 3848 (38.5%)
💰 Avg. Profit/Loss: +0.0421 (per 1 BGN invested)
🎯 Ratio: 1 : 1.60
📈 Max Profit: +0.1124 | Min: -0.0893
📊 Key Idea
The simulation mimics thousands of possible match outcomes to evaluate the stability and profitability of a hedging strategy.

It can be used to:

Optimize bet allocation between outcomes

Evaluate hedge efficiency under different odds

Compare multiple betting systems

💡 Future Enhancements
Add variable odds distributions (e.g., changing line movements)

Integrate real market data from football APIs

Create visualizations for profit distributions

Extend to multi-match portfolio hedging

🧰 Tech Stack
Python 3.x

Random (standard library)

Monte Carlo methodology

Pure math (no external dependencies)


