import streamlit as st
import openai
from streamlit_chat import message

# تعيين مفتاح API الخاص بـ OpenAI
openai.api_key = st.secrets["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"
                            ]

def api_calling(prompt, score):
    context = "You are an expert in mathematics. "
    if score < 80:
        context += "The user needs advice on improving their mathematical skills. "
    prompt = context + prompt
    completions = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return completions.choices[0].text.strip()

def calculate_score(questions, answers):
    # احتساب النقاط - يمكن تخصيص هذا بناءً على استجابات الطالب
    # يمكنك تعديل النقاط حسب ما تراه مناسبًا
    # في هذا المثال، سيتم احتساب النقاط بناءً على عدد الأسئلة التي تمت الإجابة عليها
    total_questions = len(questions)
    total_correct_answers = sum(1 for ans in answers if ans)  # حساب عدد الإجابات الصحيحة
    percentage_correct = (total_correct_answers / total_questions) * 100
    return percentage_correct

st.title("Math Expert Chat")

# بدء الدردشة
with st.form("chat_form"):
    st.header("Ask your math questions:")
    questions = st.text_area("Write your math questions here:", height=200)
    submitted = st.form_submit_button("Submit")

if submitted:
    # تقييم الأسئلة واستدعاء النصائح
    questions_list = questions.split("\n")
    score = calculate_score(questions_list, [])
    advice = api_calling(questions, score)
    st.header("Expert's Advice:")
    st.write(advice)
