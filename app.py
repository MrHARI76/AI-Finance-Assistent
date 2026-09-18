import streamlit as st
import ollama


st.title("💰 AI Financial Assistant")

st.write("Analyze your financial data and get AI-powered insights.")


st.header("Financial Information")

revenue = st.number_input(
    "Annual Revenue (₹)",
    min_value=0.0
)

expenses = st.number_input(
    "Annual Expenses (₹)",
    min_value=0.0
)

assets = st.number_input(
    "Total Assets (₹)",
    min_value=0.0
)

liabilities = st.number_input(
    "Total Liabilities (₹)",
    min_value=0.0
)


if st.button("Analyze Financial Data"):

    profit = revenue - expenses

    if revenue > 0:
        profit_margin = (profit / revenue) * 100
        expense_margin = (expenses / revenue) * 100
    else:
        profit_margin = 0
        expense_margin = 0

    if assets > 0:
        debt_ratio = (liabilities / assets) * 100
    else:
        debt_ratio = 0

    net_worth = assets - liabilities


    st.header("Financial Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Profit", f"₹{profit:,.2f}")

    with col2:
        st.metric("Profit Margin", f"{profit_margin:.2f}%")

    with col3:
        st.metric("Expense Ratio", f"{expense_margin:.2f}%")


    col4, col5 = st.columns(2)

    with col4:
        st.metric("Debt Ratio", f"{debt_ratio:.2f}%")

    with col5:
        st.metric("Net Worth", f"₹{net_worth:,.2f}")


    st.header("🤖 AI Insights")

    prompt = f"""
    You are an AI Financial Assistant.

    Analyze the following financial information:

    Revenue: ₹{revenue:,.2f}
    Expenses: ₹{expenses:,.2f}
    Assets: ₹{assets:,.2f}
    Liabilities: ₹{liabilities:,.2f}

    Financial Metrics:

    Profit: ₹{profit:,.2f}
    Profit Margin: {profit_margin:.2f}%
    Expense Ratio: {expense_margin:.2f}%
    Debt-to-Asset Ratio: {debt_ratio:.2f}%
    Net Worth: ₹{net_worth:,.2f}

    Please provide:

    1. Overall financial analysis
    2. Important observations
    3. Explanation of the financial ratios
    4. Three practical suggestions

    Use simple language.
    This is for educational purposes.
    """


    with st.spinner("AI is analyzing your financial data..."):

        try:

            response = ollama.chat(
                model="llama3.2:3b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.write(response["message"]["content"])

        except Exception as e:

            st.error(
                "Ollama is not running. Please start Ollama and try again."
            )