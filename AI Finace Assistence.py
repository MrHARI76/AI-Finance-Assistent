import ollama
def financial_data():
    print("\nGive the Financial Data")
    revenue=float(input("Enter Your Revenue:₹"))
    expenses=float(input("Enter your Expenses:₹"))
    assets=float(input("Enter your Assets:₹"))
    liabilities=float(input("Enter your Liabilities:₹"))
    return revenue,expenses,assets,liabilities
def calculate(revenue,expenses,assets,liabilities):
    profit=revenue-expenses
    if revenue>0:
        profit_margin=(profit/revenue)*100
        expense_margin=(expenses/revenue)*100
    else:
        profit_margin=0
        expense_margin=0
    
    if assets>0:
        debt_ratio=(liabilities/assets)*100
    else:
        debt_ratio=0
    net_worth=assets-liabilities
    return profit,profit_margin,expense_margin,debt_ratio,net_worth
def display_report(profit,profit_margin,expense_margin,debt_ratio,net_worth):
    print("\n"+"="*25)
    print("     FININCIAL REPORT")
    print("="*50)
    print(f"Profit:₹{profit:,.2f}")
    print(f"Profit_Margin:₹{profit_margin:,.2f}")
    print(f"Expense_Margin:₹{expense_margin:,.2f}")
    print(f"Debt Ratio:₹{debt_ratio:,.2f}")
    print(f"Net Worth:₹{net_worth:,.2f}")

def ai_analyse(revenue,expenses,assets,liabilities,profit,profit_margin,expense_margin,debt_ratio,net_worth):

    prompt=f"""
    Analyze the foloowing fianancial infromation
    Revenue:₹{revenue:,.2f}
    Expenses:₹{expenses:,.2f}
    Assets:₹{assets:,.2f}
    Liabilities:₹{liabilities:,.2f}

    Calculated Analysis
    
    Profit:₹{profit:,.2f}
    Profit Mergin:₹{profit_margin:,.2f}
    Expense Margin:₹{expense_margin:,.2f}
    Debt Ratio:₹{debt_ratio:,.2f} 
    Net Worth:₹{net_worth:,.2f}

    Give The Analysis
    Include
    1. Overall Financial Health
    2. Important Observation
    3. Explanation of Financial Ration
    4. Suggestions
    
    Use Simple language
    Do not provide risky involvement advice
"""
    responses=ollama.chat(model="llama3.2:3b",
                          messages=[
                              {
                                  "role":"user",
                                  "content":prompt
                              }
                          ])
    return responses["message"]["content"]

def main():
    print("="*25)
    print("    AI ASSISTENT")
    print("="*25)
    print("\nWelcome")
    print("I can analyze your Financial Detail and provide Valuable Insights")
    revenue,expenses,assets,liabilities=financial_data()
    profit,profit_margin,expense_margin,debt_ratio,net_worth=calculate(revenue,expenses,assets,liabilities)
    display_report(profit,profit_margin,expense_margin,debt_ratio,net_worth)
    print("\n"+"="*25)
    print("  AI INSIGHTS")
    print("="*25)
    analysis=ai_analyse(revenue,expenses,assets,liabilities,profit,profit_margin,expense_margin,debt_ratio,net_worth)
    print(analysis)
    print("\n Thank you for using AI Financial Assistent")

if __name__=="__main__":
    main()




    







    
