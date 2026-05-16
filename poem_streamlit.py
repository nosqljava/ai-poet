from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
import streamlit as st
import os

# load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.title("_AI 시인_  :sunglasses:")
title = st.text_input("시의 주제를 입력하세요", "봄비")
st.write("시의주제는 ", title)
if st.button("시 작성"):
    with st.spinner("Wait for it..."):
       #모델생성 
       model = init_chat_model(
        "gpt-4o-mini",
        # Kwargs passed to the model:
        temperature=0.7,
        timeout=30,
        max_tokens=1000,
        api_key=api_key
        )
       #프롬프트 생성
       prompt = ChatPromptTemplate.from_messages([
        ('system','You are a helpful assistant'),
        ('user',"{input}")
      ])
       # output, chain 실행 
       chain = prompt | model | StrOutputParser()
       # 결과값 출력
       response = chain.invoke({"input":title+"에 대한 시를 작성해줘"})
       st.write(response)
