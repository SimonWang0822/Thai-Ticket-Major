# Thai Ticket Major Bot

This program is designed to automate the process of buying tickets from Thai Ticket Major

## Legal Notice & Disclaimer

It's important to understand the legal aspects of using this tool. Using a bot to buy tickets is legal in Thailand, as there are no specific laws prohibiting the use of automated programs for this purpose. However, please be aware that reselling tickets for profit is illegal and can result in legal action. This bot is intended for personal use and is not designed for commercial ticket scalping. Use it responsibly and at your own risk.

## Prerequisites

The only essential library required for this bot is Selenium. 

To install it, run the following command in your terminal:

```bash
pip install selenium
```

## Recent Anti-Bot Measures

Thai Ticket Major has recently implemented several new security measures to prevent automated ticket purchases. This bot has not been developed to handle these challenges.

Text-based CAPTCHA: A new Text-based CAPTCHA has been added to the ticket purchasing process after the queue. I have integrated an OCR library but have not yet implemented the code. If encountered, you have to write your own code. 

Randomized Queue Questions: After passing the initial queue, the website now presents a random question to verify you are not a bot. For example, it might ask you to identify an event venue from a list of three options.

To handle this, you can either integrate an AI model to analyze the question and choose the correct answer, or, you can create your own database of known questions and answers to allow the bot to choose the correct option automatically.
