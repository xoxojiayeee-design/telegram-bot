from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 TOKEN (example - sensitive hai, reset karna better)
TOKEN = "8682636613:AAEIx1MREF4gTjVN7_y6GPCND6y9PQaEkKc"

# ---------------- MAIN MENU ----------------
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("ABOUT US🚩", callback_data="about")],
        [InlineKeyboardButton("JACKING FILES🤙", callback_data="files")],
        [InlineKeyboardButton("IP REFRESH💋", callback_data="refresh")],
        [InlineKeyboardButton("INTERNATIONAL NUMBER😘", callback_data="number")],
        [InlineKeyboardButton("FREE FOLLOWER WEBSITE😛", callback_data="followers")],
        [InlineKeyboardButton("5L 4L🥀", callback_data="money")]
    ])

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 WELCOME MENU", reply_markup=main_menu())

# ---------------- BUTTON HANDLER ----------------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    try:
        await query.answer()
    except:
        return

    data = query.data

    if data == "back":
        await query.edit_message_text("🔥 MAIN MENU", reply_markup=main_menu())
        return

    if data == "about":
        text = """TEAM ANONYMOUS 🚩

WE ARE A TEAM...
WE ARE A SHADOW SYSTEM ☠️

SILENCE IS OUR LANGUAGE.
FEAR IS OUR PRESENCE.

SINCE 2021."""
    
    elif data == "files":
        text = "📂 FILES SECTION"

    elif data == "refresh":
        text = "🔄 IP REFRESH DONE"

    elif data == "number":
        text = "📞 INTERNATIONAL NUMBER SECTION"

    elif data == "followers":
        text = "📊 FREE FOLLOWER WEBSITE"

    elif data == "money":
        text = "💰 5L / 4L SECTION"

    else:
        text = "❌ INVALID OPTION"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 BACK", callback_data="back")]
    ])

    await query.edit_message_text(text, reply_markup=keyboard)

# ---------------- APP SETUP ----------------
app = (
    ApplicationBuilder()
    .token(TOKEN)
    .connect_timeout(60)
    .read_timeout(60)
    .build()
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()