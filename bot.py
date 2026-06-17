import logging
import asyncio
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تفعيل تسجيل البيانات لمراقبة الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# 1. أمر الترحيب /start
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

# 2. أمر الباقات /packages
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

# --- خدعة الويب لإرضاء سيرفر Render ومنع خطأ 127 ---
def run_dummy_server():
    # المنصة تطلب تشغيل منفذ رقم 10000 تلقائياً لخدمات الويب
    port = 10000
    handler = SimpleHTTPRequestHandler
    with TCPServer(("", port), handler) as httpd:
        logging.info(f"Dummy web server running on port {port}")
        httpd.serve_forever()

def main() -> None:
    # تشغيل السيرفر الوهمي في خلفية منفصلة تماماً
    web_thread = Thread(target=run_dummy_server, daemon=True)
    web_thread.start()

    # ⚠️ ضع التوكن الخاص بك هنا بالملي
    TOKEN = "8015018837:AAFV-canikedHmY3Ysj3bY59L2eUYv7yOLE"
    
    # بناء وتوصيل البوت تلقائياً بالـ API
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("packages", packages))

    # تشغيل البوت بنظام الاستطلاع المستمر
    application.run_polling()

if __name__ == '__main__':
    main()
