# btcarb

Bitcoin Futures arbitrage trading bot that connects to Phemex and Bitmex futures exchanges.

<h1>How it works:</h1>
Every 5 seconds, the bot fetches bids and asks from 2 different exchanges. The bot will find opportunities where the cross-exchange bid ask spread is at least 2 standard deviations larger than the mean spread. The bot will enter a position with limit orders earning a market maker rebate, and wait for the spread to return to normal. Once the spread has returned to normal, the bot will exit with more limit orders earning even more rebates. This bot takes advantage of market making incentives and market inefficiencies between exchanges.

Test mode lets you to switch between real, and testnet api keys.

Live logging in terminal allows you to watch the bot in action, and CSV logging allows you to code indicators and gives the bot a memory of past price action.

Functions have been abstracted to allow trading logic loop to be easy to understand


TO ADD IN FUTURE:

Trailing limit orders (Currently working on)

Indicators based on CSV logs

Implement async and await, websockets



