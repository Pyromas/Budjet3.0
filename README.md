# Budget Tracker Telegram Bot

This is a Telegram bot for tracking your budget. It allows you to add incomes and expenses, view your transaction history, and manage your financial data easily through Telegram commands.

## Features

- **/start**: Get a welcome message and a brief description of available commands.
- **/add_income <amount> <category>**: Add a new income entry with a specific amount and category.
- **/add_expense <amount> <category>**: Add a new expense entry with a specific amount and category.
- **/summary**: Display the total income, total expenses, and the current balance.
- **/reset**: Reset all transaction data to start fresh.
- **/show_transactions**: Show a list of all recorded transactions.
- **/delete_last**: Delete the last recorded transaction.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `python-telegram-bot` library
- `pandas` library

### Installation

1. Clone this repository or download the code.
2. Install the required libraries using pip:
   ```bash
   pip install python-telegram-bot pandas
   TOKEN = 'YOUR_BOT_TOKEN_HERE'
   Save the file.

Running the Bot
Run the bot using the following command:

bash
Копировать код
python your_bot_file.py
Replace your_bot_file.py with the actual file name containing your bot code.

Usage
Commands
/start: Use this command to start the bot and get information about its functionality.
/add_income <amount> <category>: Adds income to your transaction list. Example: /add_income 500 salary.
/add_expense <amount> <category>: Adds an expense to your transaction list. Example: /add_expense 200 groceries.
/summary: Shows the total income, total expenses, and the current balance.
/reset: Resets the transaction data, clearing all records.
/show_transactions: Displays a list of all the transactions you've entered.
/delete_last: Removes the last recorded transaction.
Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request with your changes.
