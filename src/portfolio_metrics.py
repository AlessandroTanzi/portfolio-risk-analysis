import pandas as pd
import numpy as np


def calculate_returns(prices):
    """
    Calculate daily percentage returns from price data.
    """
    returns = prices.pct_change()
    returns = returns.dropna()
    return returns


def calculate_cumulative_returns(returns):
    """
    Calculate cumulative returns from daily returns.
    """
    cumulative_returns = (1 + returns).cumprod()
    return cumulative_returns


def calculate_portfolio_returns(returns, weights):
    """
    Calculate portfolio returns using asset returns and portfolio weights.
    """
    portfolio_returns = returns.dot(weights)
    return portfolio_returns


def calculate_volatility(returns):
    """
    Calculate annualized volatility.
    """
    volatility = returns.std() * np.sqrt(252)
    return volatility


def calculate_sharpe_ratio(portfolio_returns, risk_free_rate=0):
    """
    Calculate annualized Sharpe Ratio.
    """
    excess_returns = portfolio_returns - risk_free_rate / 252
    sharpe_ratio = (excess_returns.mean() / excess_returns.std()) * np.sqrt(252)
    return sharpe_ratio


def calculate_drawdown(cumulative_returns):
    """
    Calculate drawdown from cumulative returns.
    """
    running_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns / running_max) - 1
    return drawdown
