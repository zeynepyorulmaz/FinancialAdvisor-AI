# Stock Analysis Agent

AI-powered stock analysis tool combining real-time market data with GPT-4 insights.

## Features

- Real-time stock data fetching via yfinance
- AI-generated market analysis using OpenAI's GPT-4
- Key metrics calculation (price changes, volume analysis)
- Automated trading recommendations

## Requirements

```
openai
yfinance
```

## Setup

1. Install dependencies:
```bash
pip install openai yfinance
```

2. Set up your OpenAI API key:
```python
api_key = 'your-openai-api-key'
```

## Usage

```python
from stock_analysis_agent import StockAnalysisAgent

# Initialize agent
agent = StockAnalysisAgent(api_key='your-openai-api-key')

# Analyze a stock
symbol = "NVDA"
stock_data = agent.get_stock_data(symbol)
analysis = agent.generate_analysis(symbol, stock_data)
```

## API Reference

### StockAnalysisAgent

#### get_stock_data(symbol, period='1mo')
Fetches stock metrics including:
- Current price
- Price change percentage
- Average volume
- Period high/low

#### generate_analysis(symbol, stock_data)
Provides AI-generated analysis with:
- Price trend analysis
- Volume pattern insights
- Buy/hold/sell recommendation
- Supporting rationale

