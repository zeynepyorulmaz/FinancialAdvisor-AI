import yfinance as yf
from openai import OpenAI



class StockAnalysisAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_stock_data(self, symbol, period='1mo'):
        """Fetch stock data using yfinance"""
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        current_price = hist['Close'][-1]

        # Calculate key metrics
        price_change = ((current_price - hist['Close'][0]) / hist['Close'][0]) * 100
        avg_volume = hist['Volume'].mean()

        return {
            'current_price': current_price,
            'price_change': price_change,
            'avg_volume': avg_volume,
            'high': hist['High'].max(),
            'low': hist['Low'].min()
        }

    def generate_analysis(self, symbol, stock_data):
        """Generate verbal recommendation using OpenAI"""
        prompt = f"""
        As a stock market expert, analyze the following data for {symbol}:
        - Current Price: ${stock_data['current_price']:.2f}
        - Price Change: {stock_data['price_change']:.2f}%
        - Average Volume: {stock_data['avg_volume']:,.0f}
        - 30-day High: ${stock_data['high']:.2f}
        - 30-day Low: ${stock_data['low']:.2f}

        Provide a concise analysis and recommendation. Consider:
        1. Price trends
        2. Volume patterns
        3. Clear buy/hold/sell recommendation
        4. Key reasons for the recommendation
        """

        response = self.client.chat.completions.create(
            model="gpt-4",  # or gpt-3.5-turbo depending on your needs
            messages=[
                {"role": "system", "content": "You are a experienced stock market analyst."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content


def main():
    # Replace with your OpenAI API key
    api_key = 'yourkeyhere'

    # Initialize the agent
    agent = StockAnalysisAgent(api_key)

    # Example usage
    symbol = "NVDA"  # Example stock symbol
    try:
        # Get stock data
        stock_data = agent.get_stock_data(symbol)

        # Generate analysis
        analysis = agent.generate_analysis(symbol, stock_data)

        print(f"\nAnalysis for {symbol}:")
        print(analysis)

    except Exception as e:
        print(f"Error analyzing {symbol}: {str(e)}")


if __name__ == "__main__":
    main()
