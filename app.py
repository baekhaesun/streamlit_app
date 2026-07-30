import streamlit as st
import random

st.set_page_config(
    page_title="🌈 MBTI 진로 탐험소",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#ffe29f,#ffa99f,#ff719a,#7afcff);
background-size:400% 400%;
animation:bg 12s ease infinite;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.big{
font-size:55px;
font-weight:bold;
text-align:center;
color:white;
text-shadow:3px 3px 8px black;
}

.sub{
font-size:24px;
text-align:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big'>🌈✨ MBTI 진로 탐험소 ✨🚀</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>🎉 나에게 딱 맞는 직업을 찾아보자! 🎉</div>", unsafe_allow_html=True)

st.write("")

jobs={
"INTJ":{"emoji":"🧠👑","jobs":["AI 개발자 🤖","과학자 🔬","의사 🩺","대학교수 🎓","변리사 📚","데이터 분석가 📊"],"feature":"논리적이고 전략적이에요 🧠","study":"혼자 깊이 공부하는 것을 좋아해요 📚","env":"조용한 연구실 🔬"},
"INTP":{"emoji":"💡🧪","jobs":["프로그래머 💻","게임개발자 🎮","연구원 🔬","발명가 ⚙️","수학자 ➗"],"feature":"창의적인 아이디어가 넘쳐요 💡","study":"궁금한 것을 끝까지 탐구해요 🔍","env":"자유로운 연구환경 🌎"},
"ENTJ":{"emoji":"👔🚀","jobs":["CEO 🏢","기업가 💼","판사 ⚖️","프로젝트매니저 📋","변호사 👨‍⚖️"],"feature":"리더십 최고! 👑","study":"목표를 정하면 끝까지 해요 🎯","env":"도전적인 회사 🚀"},
"ENTP":{"emoji":"🎉💥","jobs":["유튜버 📹","광고기획자 📢","기업가 💰","마케터 📈","PD 🎬"],"feature":"아이디어 뱅크 💡","study":"토론하면서 배우는 것을 좋아해요 🗣️","env":"창의적인 사무실 🎨"},
"INFJ":{"emoji":"💖🌸","jobs":["상담사 😊","교사 🍎","작가 ✍️","심리학자 🧠","사회복지사 ❤️"],"feature":"따뜻하고 배려심이 많아요 🥰","study":"의미를 찾으며 공부해요 📖","env":"사람을 돕는 공간 🤝"},
"INFP":{"emoji":"🌷🎨","jobs":["웹툰작가 🎨","소설가 📚","음악가 🎵","디자이너 🖌️","일러스트레이터 🌈"],"feature":"감성이 풍부해요 🌸","study":"자신이 좋아하는 분야에 몰입해요 💕","env":"자유로운 작업실 🏡"},
"ENFJ":{"emoji":"🥳❤️","jobs":["교사 👨‍🏫","강사 🎤","정치인 🏛️","HR담당자 👥","상담사 😊"],"feature":"사람들을 잘 이끌어요 🌟","study":"함께 공부하는 것을 좋아해요 🤝","env":"활기찬 조직 🏢"},
"ENFP":{"emoji":"🎈🌈","jobs":["배우 🎭","MC 🎤","크리에이터 📱","광고기획자 📢","여행작가 ✈️"],"feature":"에너지가 넘쳐요 ⚡","study":"재미있게 배우는 것을 좋아해요 🎲","env":"자유로운 분위기 🎉"},
"ISTJ":{"emoji":"📚✅","jobs":["공무원 🏢","회계사 💰","군인 🪖","은행원 🏦","품질관리 👷"],"feature":"성실하고 책임감이 강해요 👍","study":"계획적으로 공부해요 📅","env":"안정적인 조직 🏢"},
"ISFJ":{"emoji":"🌼💛","jobs":["간호사 🩺","교사 🍎","사회복지사 ❤️","사서 📚","행정직 🗂️"],"feature":"친절하고 헌신적이에요 🤗","study":"차근차근 반복학습 📖","env":"따뜻한 직장 🏡"},
"ESTJ":{"emoji":"👮💼","jobs":["경찰 👮","군인 🪖","관리자 📋","공무원 🏢","은행장 🏦"],"feature":"체계적이고 리더십이 있어요 👑","study":"목표 중심으로 공부해요 🎯","env":"규칙이 있는 조직 📋"},
"ESFJ":{"emoji":"🥰🎁","jobs":["간호사 🩺","승무원 ✈️","교사 🍎","호텔리어 🏨","상담사 😊"],"feature":"사교성이 좋아요 😄","study":"친구들과 함께 공부해요 👭","env":"사람이 많은 곳 🏫"},
"ISTP":{"emoji":"🛠️🚗","jobs":["파일럿 ✈️","정비사 🔧","엔지니어 ⚙️","소방관 🚒","드론전문가 🚁"],"feature":"문제 해결 능력이 뛰어나요 🔥","study":"실습을 좋아해요 🔨","env":"현장 중심 🏗️"},
"ISFP":{"emoji":"🎨🌼","jobs":["플로리스트 🌸","사진작가 📸","디자이너 🎨","요리사 👨‍🍳","패션디자이너 👗"],"feature":"예술 감각이 뛰어나요 ✨","study":"직접 만들면서 배워요 🖌️","env":"감성적인 공간 🌺"},
"ESTP":{"emoji":"🏎️🔥","jobs":["기업가 💼","운동선수 ⚽","영업전문가 💰","경찰 👮","파일럿 ✈️"],"feature":"행동력이 최고예요 🚀","study":"직접 경험하며 배워요 🎯","env":"역동적인 환경 🌎"},
"ESFP":{"emoji":"🎤🎊","jobs":["가수 🎵","배우 🎬","유튜버 📹","MC 🎤","승무원 ✈️"],"feature":"분위기 메이커 😍","study":"즐겁게 배우는 스타일 🎉","env":"사람이 많은 곳 🌈"}
}

mbti = st.selectbox("🌟 MBTI를 선택하세요", list(jobs.keys()))

if st.button("🚀 진로 추천 받기"):
    st.balloons()

    info = jobs[mbti]

    st.header(f"{info['emoji']} {mbti}")

    st.progress(random.randint(85,100))

    st.success("💖 성격 특징\n\n"+info["feature"])
    st.info("📚 공부 스타일\n\n"+info["study"])
    st.warning("🏢 잘 맞는 환경\n\n"+info["env"])

    st.subheader("💼 추천 직업")

    for job in info["jobs"]:
        st.markdown(f"### ⭐ {job}")

    st.snow()

st.divider()

st.markdown(
"""
<center>

# 🌈 꿈을 향해 도전하세요! 🚀

🎓💖✨🌈🚀📚🎉🏆

</center>
""",
unsafe_allow_html=True
)
