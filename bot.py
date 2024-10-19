import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import pandas as pd


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


transactions = pd.DataFrame(columns=["type", "amount", "category"])

async def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение, когда бот запускается."""
    await update.message.reply_text(
        "Привет! Я бот для отслеживания бюджета. Используй /add_income для добавления дохода, "
        "/add_expense для добавления расхода, /summary для получения итогов, "
        "/reset для сброса данных, /show_transactions для отображения всех транзакций, "
        "и /delete_last для удаления последней транзакции."
    )

async def add_income(update: Update, context: CallbackContext) -> None:
    """Добавляет доход."""
    try:
        amount = float(context.args[0])
        category = context.args[1]
        global transactions
        transactions = pd.concat([transactions, pd.DataFrame({"type": ["income"], "amount": [amount], "category": [category]})], ignore_index=True)
        await update.message.reply_text(f"Доход в размере {amount} руб. добавлен в категорию {category}.")
    except (IndexError, ValueError):
        await update.message.reply_text("Используй команду так: /add_income <сумма> <категория>")

async def add_expense(update: Update, context: CallbackContext) -> None:
    """Добавляет расход."""
    try:
        amount = float(context.args[0])
        category = context.args[1]
        global transactions
        transactions = pd.concat([transactions, pd.DataFrame({"type": ["expense"], "amount": [amount], "category": [category]})], ignore_index=True)
        await update.message.reply_text(f"Расход в размере {amount} руб. добавлен в категорию {category}.")
    except (IndexError, ValueError):
        await update.message.reply_text("Используй команду так: /add_expense <сумма> <категория>")

async def summary(update: Update, context: CallbackContext) -> None:
    """Отправляет итоговые данные о бюджете."""
    global transactions
    income_total = transactions[transactions["type"] == "income"]["amount"].sum()
    expense_total = transactions[transactions["type"] == "expense"]["amount"].sum()
    balance = income_total - expense_total

    summary_message = (
        f"Общий доход: {income_total} руб.\n"
        f"Общие расходы: {expense_total} руб.\n"
        f"Текущий баланс: {balance} руб."
    )
    await update.message.reply_text(summary_message)

async def reset(update: Update, context: CallbackContext) -> None:
    """Сбрасывает все данные транзакций."""
    global transactions
    transactions = pd.DataFrame(columns=["type", "amount", "category"])
    await update.message.reply_text("Все данные транзакций сброшены.")

async def show_transactions(update: Update, context: CallbackContext) -> None:
    """Отображает все транзакции."""
    global transactions
    if transactions.empty:
        await update.message.reply_text("Нет записанных транзакций.")
    else:
        transaction_list = transactions.to_string(index=False)
        await update.message.reply_text(f"Текущие транзакции:\n{transaction_list}")

async def delete_last(update: Update, context: CallbackContext) -> None:
    """Удаляет последнюю транзакцию."""
    global transactions
    if transactions.empty:
        await update.message.reply_text("Нет транзакций для удаления.")
    else:
        last_transaction = transactions.iloc[-1]
        transactions = transactions.iloc[:-1]
        await update.message.reply_text(
            f"Последняя транзакция удалена:\nТип: {last_transaction['type']}, "
            f"Сумма: {last_transaction['amount']}, Категория: {last_transaction['category']}"
        )

def main() -> None:
    """Запускает бота."""
    TOKEN = ''  # Замените 'ВАШ_ТОКЕН_ЗДЕСЬ' на токен вашего бота

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add_income", add_income))
    application.add_handler(CommandHandler("add_expense", add_expense))
    application.add_handler(CommandHandler("summary", summary))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(CommandHandler("show_transactions", show_transactions))
    application.add_handler(CommandHandler("delete_last", delete_last))

    
    application.run_polling()

if __name__ == '__main__':
    main()
    main()
