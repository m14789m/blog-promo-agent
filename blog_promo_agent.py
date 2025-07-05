
import streamlit as st
import openai

st.set_page_config(page_title="وكيل ترويج المدونة", layout="centered")

st.title("🚀 وكيل ترويج ذكي لمدونتك")
st.markdown("اكتب معلومات التدوينة وسننشئ لك منشورًا ترويجيًا احترافيًا تلقائيًا باستخدام الذكاء الاصطناعي.")

# إدخال المستخدم
title = st.text_input("📝 عنوان التدوينة")
url = st.text_input("🔗 رابط التدوينة")
category = st.text_input("📁 الفئة (مثلاً: وظائف، دورات، تطوير ذات...)")

# مفتاح OpenAI - يتم جلبه من secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

if st.button("✨ أنشئ الترويج تلقائيًا"):
    if not title or not url or not category:
        st.warning("يرجى تعبئة جميع الحقول أولاً.")
    else:
        with st.spinner("جاري إنشاء المحتوى الترويجي..."):
            prompt = f"""
أنت مساعد تسويق ذكي. أنشئ منشورًا ترويجيًا لتدوينة جديدة في مدونة سعودية عن "{category}".
العنوان: {title}
الرابط: {url}

النتائج المطلوبة:
1. وصف ترويجي احترافي (3-5 أسطر)
2. منشور مناسب لتويتر أو فيسبوك
3. هاشتاغات مقترحة
4. Meta Description للسيو
5. كلمات مفتاحية (SEO)

اكتب بالعربية الفصحى، بنبرة مشوقة ومحترفة، موجهة لجمهور سعودي.
"""

            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "أنت مساعد ذكي في التسويق."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=800
            )

            result = response.choices[0].message.content
            st.success("✅ تم إنشاء المحتوى الترويجي بنجاح!")
            st.markdown(result)
