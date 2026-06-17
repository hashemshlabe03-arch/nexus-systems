import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تفعيل تسجيل البيانات لمراقبة الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# 1. أمر البداية /start (يحتوي على الأقسام القابلة للطي والترحيب الفخم)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = """
<b>🌐 مرحباً بك في NEXUS CORE SYSTEMS | الواجهة الذكية v10.0</b>

نحن لا نقدم وعوداً نظرية؛ بل نعيد هندسة "منطق العمل" لقطاعك عبر حلول برميوم سحابية مستقرة.

<tg-spoiler title="🎯 اضغط هنا لقراءة أهداف ومميزات المنظومة">
• <b>تصفير الهدر التشغيلي:</b> القضاء على الأخطاء البشرية في جدولة المواعيد والحجوزات.
• <b>الاستجابة الفوتونية:</b> ردود سريعة للغاية (0.4 ثانية) لفرز العملاء الساخنين على مدار الساعة.
• <b>بروتوكول الثقة الرقمية:</b> نمنح المنشآت المؤهلة فترة تشغيل تجريبية مجانية بالكامل لمدة 14 يوماً (Beta-Test).
</tg-spoiler>

💡 <i>استخدم الأمر /packages ليعرض لك البوت جدول الخدمات والاستثمار بالمسطرة والقلم.</i>
"""
    await update.message.reply_text(text=welcome_text, parse_mode='HTML')

# 2. أمر الباقات /packages (يحاكي تماماً جداول @richtextdemobot)
async def packages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    table_text = """
<b>📊 جدول البنى التحتية والاستثمار المتاح:</b>

<tg-table>
  <tg-table-row>
    <tg-table-cell><b>🛡️ نوع المنظومة</b></tg-table-cell>
    <tg-table-cell><b>⚡ كفاءة الرد</b></tg-table-cell>
    <tg-table-cell><b>💰 الاستثمار</b></tg-table-cell>
  </tg-table-row>
  <tg-table-row>
    <tg-table-cell>Nexus السحابي</tg-table-cell>
    <tg-table-cell>0.4 ثانية</tg-table-cell>
    <tg-table-cell>Beta (مجاني)</tg-table-cell>
  </tg-table-row>
  <tg-table-row>
    <tg-table-cell>تطبيق مصغر TMA</tg-table-cell>
    <tg-table-cell>فوري تفاعلي</tg-table-cell>
    <tg-table-cell>حسب الطلب</tg-table-cell>
  </tg-table-row>
  <tg-table-row>
    <tg-table-cell>أتمتة خطوط الربط</tg-table-cell>
    <tg-table-cell>مزامنة كاملة</tg-table-cell>
    <tg-table-cell>تواصل معنا</tg-table-cell>
  </tg-table-row>
</tg-table>

⚙️ <i>المنظومة متكاملة وتدعم كافة القطاعات والأملاك الخاصة النخبوية بالخليج.</i>
"""
    await update.message.reply_text(text=table_text, parse_mode='HTML')

def main() -> None:
    # ⚠️ استبدل TOKEN_HERE بمفتاح البوت الفعلي الذي أخذته من BotFather
    TOKEN = "8015018837:AAFV-canikedHmY3Ysj3bY59L2eUYv7yOLE"
    
    # بناء التطبيق
    application = Application.builder().token(TOKEN).build()

    # ربط الأوامر بالدوال
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("packages", packages))

    # تشغيل البوت واستقبال التحديثات
    application.run_polling()

if __name__ == '__main__':
    main()
