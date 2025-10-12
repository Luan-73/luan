import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
import numpy as np
import time
st.title("🎧 Ứng dụng giải trí và sức khỏe")



menu = st.selectbox("Chọn chức năng mà bạn muốn dùng: ",["🎤 MV yêu thích", "💤 Dự đoán giờ ngủ", "📰 Đọc báo","Giá vàng", "Kiểm tra sức khoẻ","Nhịp tim","Bước đi","Uống nước","Kiểm tra tính cách theo DISC","Nhân tướng học","Nhắc nhở nghỉ ngơi và tập thể dục","Ứng dụng theo dõi sức khoẻ nâng cao"])
if menu == '🎤 MV yêu thích':
    st.sidebar.title("🎶 Danh sách nghệ sĩ")
    selected_artist = st.sidebar.radio("Chọn nghệ sĩ:", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP"])

    videos = {
        "Đen Vâu": [
            ("Bữa ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
            ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
            ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
            ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM")
        ],
        "Hà Anh Tuấn": [
            ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
            ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
            ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
            ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")
        ],
        "Sơn Tùng M-TP": [
            ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
            ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
            ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
            ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
        ]
    }
    st.header(f"Các bài hát của {selected_artist} 🎵")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
elif menu == '💤 Dự đoán giờ ngủ':
    st.header("🔮 Dự đoán giờ ngủ mỗi đêm")
    x = [
            [10, 1, 8],
            [20, 5, 6],
            [25, 8, 3],
            [30, 6, 5],
            [35, 2, 9],
            [40, 4, 3]
        ]
    y = [10, 8, 6, 7, 9.5, 9]
    model = LinearRegression()
    model.fit(x, y)
    st.write("Nhập thông tin cá nhân:")
    age = st.number_input("Tuổi của bạn", min_value=5, max_value=100, value=25)
    activity = st.slider("Mức độ hoạt động thể chất (1 = ít, 10 = rất nhiều)", 1, 10, 5)
    screen_time = st.number_input("Thời gian dùng màn hình mỗi ngày (giờ)", min_value=0, max_value=24, value=6)

    if st.button("💤 Dự đoán ngay"):
        input_data = [[age, activity, screen_time]]
        result = model.predict(input_data)[0]
        st.success(f"Bạn nên ngủ khoảng {result:.1f} giờ mỗi đêm")

        if result < 6.5:
            st.warning("😴 Có thể bạn cần nghỉ ngơi nhiều hơn để cải thiện sức khỏe.")
        elif result > 9:
            st.info("😅 Có thể bạn đang vận động nhiều – ngủ bù hợp lý nhé.")
        else:
            st.success("✅ Lượng ngủ lý tưởng! Hãy giữ thói quen tốt nhé.")
elif menu == '📰 Đọc báo':
    st.header("Tin tức mới nhất trên VnExpress")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
elif menu == 'Giá vàng':
    st.header("Cập nhật giá vàng từ Vietnamnet")
    feet = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feet.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
    if gold_news:
        for entry in gold_news[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.info("Không tìm thấy tin tức về giá vàng.")
elif menu == 'Kiểm tra sức khoẻ':
    st.header("Kiểm tra chỉ số BMI của bạn ")
    can_nang = st.number_input("Nhập cân nặng của bạn (kg)", min_value=10.0,max_value=200.0,value=60.0,step=0.1)
    chieu_cao = st.number_input("Nhập chiều cao của bạn (m)",min_value=1.0,max_value=2.5,value=1.7,step=0.01)
    if st.button("Tính BMI"):
        bmi =   can_nang/(chieu_cao ** 2)
        st.success(f"chỉ số bmi của bạn là: {bmi: .2f}")
        if bmi < 18.5:
            st.warning("Bạn đang thiếu cân, nên ăn uống đầy đủ và dinh dưỡng hơn.")
        elif 18.5 <= bmi < 25:
            st.info("Bạn có cân nặng bình thường. Hãy tiếp tục duy trì lối sống lành mạnh.")
        elif 25 <= bmi < 30:
            st.warning("Bạn đang thừa cân. Nên cân đối chế độ ăn và tập thể dục.")
        else:
            st.error("Bạn đang béo phì. Nên gặp chuyên gia dinh dưỡng hoặc bác sĩ để được tư vấn.")
elif menu == 'Nhịp tim':
    st.header("Kiểm tra nhịp tim xem có nên gặp bác sĩ không ")
    x = np.array([
        # Trẻ em
        [100, 2, 12],
        [95, 4, 15],
        [90, 6, 18],
        [85, 9, 20],
        [80, 12, 25],

        # Người lớn
        [75, 20, 50],
        [72, 30, 65],
        [70, 40, 70],
        [68, 50, 75],
        [66, 58, 78],

        # Người cao tuổi
        [70, 65, 70],
        [75, 70, 68],
        [80, 75, 65],
        [85, 80, 60],
        [90, 85, 58],
    ])
    y = np.array([
        # Trẻ em - rủi ro thấp đến vừa
        1.2, 1.3, 1.5, 1.6, 1.7,

        # Người lớn - rủi ro trung bình
        2.0, 2.3, 2.7, 3.0, 3.2,

        # Người cao tuổi - rủi ro cao dần
        3.5, 3.8, 4.0, 4.3, 4.6
    ])
    model = LinearRegression()
    model.fit(x,y)
    st.subheader("Nhập thông tin sức khoẻ ")
    
    hr = st.number_input("Nhịp tim (bm) ", min_value=40,max_value=200,value=75)
    age = st.number_input("Tuổi ",min_value=1,max_value=120,value=30)
    weight = st.number_input("Cân Nặng (kg) ",min_value=10.0,max_value=200.0,value=60.0)
    if st.button("Kiểm tra sức khoẻ"):
        score = model.predict([[hr,age,weight]])[0]
        st.success(f"chỉ số rủi ro: **{score: .2f}**")
        if age<13:
            safe_threshold = 1.5
        elif age<60:
            safe_threshold = 2.0
        else: 
            safe_threshold = 2.5
        if score < safe_threshold:
            st.info("Bạn khoẻ mạnh và không cần đi bác sĩ ")
        elif score <(safe_threshold + 1):
            st.warning("Cần theo dõi thêm, hãy nghỉ ngơi và kiểm tra lại sau ")
        elif score <(safe_threshold + 2):
            st.warning("Có dấu hiệu bất thường cần hỏi thêm ý kiến bác sĩ ")
        else:
            st.error("Rủi ro cao, nên gặp bác sĩ càng sớm càng tốt")  
elif menu == 'Bước đi': 
    st.header("Kiểm tra số bước đi nên đi mỗi ngày")
    st.title("Bạn nên đi bao nhiêu bước mỗi ngày?")
    age2 = st.number_input("Nhập tuổi của bạn:", min_value=0.0, max_value=130.0, value=18.0, step=1.0)
    if st.button("Kiểm tra số bước"):
        if age2 < 18:
            st.info("Bạn nên đi **12000-15000 bước** mỗi ngày.")
        elif 18 <=age2 <= 39:
            st.info(" + Bạn nên đi **8000-10000 bước** mỗi ngày.")
        elif 40 <= age2 <= 64:
            st.warning("Bạn nên đi **7000-9000 bước** mỗi ngày.")
        elif age2 > 64:
            st.warning("Bạn nên đi **6000-8000 bước** mỗi ngày.")
        else:
            st.error("A Có lỗi xảy ra. Vui lòng kiểm tra lại thông tin.")
elif menu == 'Uống nước':
    st.header("Lượng nước uống khuyến nghị mỗi ngày")
    st.title("Bạn nên uống bao nhiêu lít nước mỗi ngày?")
    age3 = st.number_input("Nhập tuổi của bạn:", min_value=0.0, max_value=120.0, value=18.0, step=1.0)
    if st.button("Kiểm tra số lít nước khuyến nghị"):
        if age3 < 4:
            st.info("Bạn nên uống **1.3 lít nước** mỗi ngày.")
        elif 4<= age3 <=8:
            st.info("Bạn nên uống **1.7 lít nước** mỗi ngày.")
        elif 9<= age3 <=13:
            st.info("Bạn nên uống **2.1-2.4 lít nước** mỗi ngày.")
        elif 14<= age3 <=18:
            st.info("Bạn nên uống **2.3-3.3 lít nước** mỗi ngày.")
        elif 19<= age3 <=50:
            st.warning("Bạn nên uống **2.7 lít nước(nữ)/3.3 lít nước(nam)** mỗi ngày.")
        else:
            st.error("Bạn nên uống **2.5-3.0 lít nước** mỗi ngày tuỳ vào sức khoẻ và hoạt động.")
elif menu == 'Kiểm tra tính cách theo DISC':
    st.header("Kiểm tra tính cách theo DISC")
    st.markdown("Chọn một mô tả đúng nhất và một mô tả ít đúng nhất trong từng nhóm")
    groups = [
        {
            "D": "Tôi quyết đoán và thích kiểm soát",
            "I": "Tôi thích thân thiện và nói chuyện dễ dàng",
            "S": "Tôi kiên nhẫn và đáng tin cậy",
            "C": "Tôi chính xác và có hệ thống",
        },
        {
            "D": "Tôi thích thử thách và hành động nhanh",
            "I": "Tôi tràn đầy năng lượng và lạc quan",
            "S": "Tôi ổn định và hỗ trợ người khác",
            "C": "Tôi làm việc theo quy tắc rõ ràng",
        },
        {
            "D": "Tôi thích kiểm soát kết quả",
            "I": "Tôi thích được công nhận",
            "S": "Tôi ưu tiên sự hài hoà",
            "C": "Tôi chú ý đến việc chi tiết và phân tích",
        }
    ]
    scores = {"D": 0, "I":0, "S": 0, "C": 0 }
    for idx , group in enumerate(groups):
        st.markdown(f"### nhóm {idx + 1}")
        options = list(group.values())
        keys = list(group.keys())
        most = st.radio("Mô tả đúng nhất với bạn ", options, key = f"most_{idx}")
        least = st.radio("Mô tả ít đúng nhất với bạn ", options, key=f"least_{idx}")
        for key, val in group.items():
            if val == most:
                scores[key] += 1
            if val == least:
                scores[key] -= 1
    if st.button("Xem kết quả DISC "):
        st.header(" Kết quả của bạn ")
        max_type = max(scores, key = scores.get)

        for style, score in scores.items():
            st.write(f"{style}: {score} điểm ")
        st.markdown(f"Tính nổi bật nhất của bạn là: {max_type}**")
        descriptions = {
            "D": "Quyết đoán, định hướng kết quả và thích kiểm soát",
            "I": "Giao tiếp tốt, tràn đầy năng lượng và truyền cảm hứng",
            "S": "Kiên nhẫn, đáng tin cậy và hỗ trợ người khác",
            "C": "Chính xác, tuân thủ quy trình và thích phân tích logic"
        } 
        st.info(descriptions[max_type])
        st.markdown("----")
        st.markdown("Mô tả chi tiết các nhóm DISC")
        st.markdown("""
            - **D (Dominance)**: Người lãnh đạo, chủ động, thích cạnh tranh. Ví dụ: CEO, nhà sáng lập.  
            - **I (Influence)**: Người truyền cảm hứng, thích giao tiếp, có sức hút. Ví dụ: người làm marketing, diễn giả.  
            - **S (Steadiness)**: Người hỗ trợ, trung thành, kiên nhẫn. Ví dụ: giáo viên, điều dưỡng.  
            - **C (Conscientiousness)**: Người phân tích, tỉ mỉ, theo quy trình. Ví dụ: kế toán, kỹ sư.
        """)
        st.caption("Đây chỉ là bài tham khảo về chỉ số DISC")
elif menu == "Nhân tướng học":
    st.header("Phân tích tướng mặt theo ngũ hành")
    st.markdown("Chọn các đặc điểm bạn cảm thấy đúng với gương mặt của mình")
    st.subheader("Đôi mắt")
    eyes_good = st.multiselect("Đặc điểm tốt về đôi mắt: ",[
        "Mắt sáng và có thần (Tư duy nhanh nhạy, có năng lực tích cực)",
        "Mắt dài và đều (tầm nhìn chiến lược và có nội tâm sâu sắc)",
        "Mắt cười (dễ gần, thân thiện và giao tiếp tốt)"
    ])
    eyes_bad = st.multiselect("Đặc điểm chưa tốt về mắt: ",[
        "Mắt lờ đờ, thiêu thần (thiếu sinh khí và mệt mỏi)",
        "Mắt không cân xứng (thiếu cân bằng và cảm giác nhìn yếu)",
        "Tròng trắng lẫn tròng đen (dễ gặp bất ổn, tâm lý dao động)"
    ])
    st.subheader("Mũi")
    nose_good = st.multiselect("Đặc điểm tốt về mũi: ", [
        "Mũi cao thẳng và đầy đặn (tài vận tốt lập nghiệp dễ dàng)",
        "Cánh mũi dày, đều (Biết giữ tiền và quản lý tài chính tốt)",
        "Đầu mũi tròn đầy (Ham học hỏi, lòng bao dung, nhân hậu)"
    ])
    nose_bad = st.multiselect("Đặc điểm chưa tốt về mũi: ", [
        "Mũi lệch (tính cách thiếu ổn định)",
        "Mũi hếch (khó giữ tài sản, hay tiêu xài)",
        "Cánh mũi mỏng (tài chính bấp bênh)"
    ])
    st.subheader("Trán")
    forehead_good = st.multiselect("Đặc điểm tốt về trán: ", [
        "Trán cao và rộng (Thông minh, tư duy logic)",
        "Trán đầy đặn, trơn láng (sự nghiệp tốt, thuận lợi)",
        "Không có nếp nhăn sớm (suy nghĩ tích cực ổn định)"
    ])
    forehead_bad = st.multiselect("Đặc điểm chưa tốt về trán: ",[
        "Trán thấp và hẹp (tầm nhìn hạn chế)",
        "Trán nghiêng (thiếu kiên định)",
        "Trán lõm (dễ bị chi phối thiếu quyết đoán)"
    ])
    st.subheader("Tai")
    ears_good = st.multiselect("Đặc điểm tốt về tai: ", [
        "Tai đầy, vành rõ (sức khoẻ tốt, có phúc khí)",
        "Dái tai dày (hậu vận vững vàng)",
        "Tai cao hơn chân mày (tư duy tốt, trí tuệ sáng)"
    ])
    ears_bad = st.multiselect("Đặc điểm chưa tốt về tai: ", [
        "Tai mỏng như giấy (yếu vận, dễ bị ảnh hưởng)",
        "Tai vểnh ra bên ngoài (nóng bỏng, bốc đồng)",
        "Tai thấp hơn lông mày (thiếu tư duy chiến lược)"
    ])
elif menu == "Nhắc nhở nghỉ ngơi và tập thể dục":
    st.subheader("Nhắc nhở nghỉ ngơi và tập thể dục")
    minutes = st.number_input("Nhập số phút làm việc: ",min_value=1,step=1,value=1)
    if st.button("Bắt đầu đếm ngược"):
        st.info(f"Bắt đầu đếm ngược {minutes} phút")
        my_bar = st.progress(0)
        total_seconds = minutes * 60
        for sec in range(total_seconds):
            percent = int(((sec+1)/total_seconds)*100)
            my_bar.progress(percent)
            time.sleep(1)
        st.success("Hết giờ rồi! Hãy đứng dậy nghỉ ngơi và tập vài động tác nhé!")
        audio_file = open("alarm.mp3","rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes,format="audio/mp3",start_time=0)
elif menu == "Ứng dụng theo dõi sức khoẻ nâng cao":
    st.set_page_config(page_title="Ứng dụng Sức Khoẻ Nâng Cao",layout="centered")
    st.title("Ứng dụng Theo Dõi Sức Khoẻ Nâng Cao")
    st.header("Nhập thông tin cá nhân")
    name = st.text_input("Họ và tên:")
    age = st.number_input("Tuổi:",min_value=0,max_value=120,step=1)
    gender = st.radio("Giới tính:",("Nam","Nữ"))
    height = st.number_input("Chiều cao (cm):",min_value=50.0,max_value=250.0,step = 0.1)
    weight = st.number_input("Cân nặng (kg):",min_value=10.0,max_value=250.0,step = 0.1)
    activity_level= st.selectbox("Mức độ hoạt động thể chất:",[
        "Ít vận động",
        "Vận động nhẹ (1-3 buổi/tuần)",
        "Vận động vừa (3-5 buổi/tuần)",
        "Vận động nhiều (6-7 buổi/tuần)",
        "Vận động rất nhiều (2 lần/ngày)"
    ])
    if st.button("Phân tích sức khoẻ"):
        if height>0 and weight>0:
            height_m = height/100
            bmi = weight/(height_m**2)
            if gender == "Nam":
                bmr = 10*weight+6.25*height-5*age+5
            else:
                bmr = 10*weight+6.25*height-5*age-161
            activity_factors = {
                "Ít vận động": 1.2,
                "Vận động nhẹ (1-3 buổi/tuần)":1.375,
                "Vận động vừa (3-5 buổi/tuần)":1.55,
                "Vận động nhiều (6-7 buổi/tuần)":1.725,
                "Vận động rất nhiều (2 lần/ngày)":1.9
            }
            activity_factor = activity_factors[activity_level]
            tdee = bmr * activity_factor
            water_intake = weight *35/1000
            st.subheader("Kết quả phân tích")
            st.write(f"**Chào {name}!**")
            st.write(f"**Chỉ số BMI:** '{bmi:.2f}'")
            st.write(f"**BMR(Tỷ lệ trao đổi chất cơ bản):** '{bmr:.0f}' kcal/ngày")
            st.write(f"**TDEE(Năng lượng tiêu hao mỗi ngày):** '{tdee:.0f}' kcal/ngày")
            st.write(f"**Lượng nước nên uống mỗi ngày:** '{water_intake:.0f}' lít")
            st.markdown("### Đánh giá chỉ số BMI:")
            if bmi<18.5:
                st.warning("Bạn đang thiếu cân. Hãy tăng dinh dưỡng.")
            elif 18.5 <= bmi <24.9:
                st.success("Bạn có cân nặng bình thường. Duy trì chế độ sống lành mạnh!")
            elif 25<=bmi<29.9:
                st.warning("Bạn đang thừa cân. Hãy cân bằng lại chế độ ăn và hoạt động")
            else:
                st.error("Bạn đang béo phì. Cần tham khảo chuyên gia để cải thiện sức khoẻ")
            
            st.markdown("### Gợi ý chế độ ăn (Theo mục tiêu):")
            col1,col2 = st.columns(2)
            with col1:
                st.info("**Duy trì cân nặng:**")
                st.write(f"- Ăn khoảng '{tdee:.0f}' kcal/ngày")
            with col2:
                st.info("**Giảm cân nhẹ:**")
                st.write(f"- Ăn khoảng '{tdee-300:.0f}' kcal/ngày")
            st.markdown("### Gợi ý thực đơn mẫu:")
            st.markdown("""
            - **Sáng:** Trứng luộc, bánh mì nguyên cám, trái cây
            - **Trưa** Cơm gạo lứt, ức gà, rau luộc, canh
            - **Tối** Salad rau xanh, cá hấp, trái cây ít ngọt
            - **Snack:** Hạt khô,sữa chua ít đường
             """)
st.header("Theo dõi sức khoẻ về nhịp tim")
sys = st.number_input("Huyết áp tâm thu(mmhg): ",min_value=50, max_value = 250,step=1)
dia = st.number_input("Huyết áp tâm trương(mmhg)",min_value=30,max_value=150,step=1)
heart_rate = st.number_input("Nhịp tim khi nghỉ ngơi(bpm): ",min_value=30,max_value=200,step=1)
if st.button("Phân tích tim mạch:"):
    st.subheader("Kết quả phân tích tim mạch")
    if sys<90 or dia<60:
        st.warning("Huyết áp thấp")
    elif 90<= sys <= 120 and 60<=dia<=80:
        st.success("Huyết áp bình thường")
    elif 120<=sys<=139 and 80<=dia<=89:
        st.warning("Tiền huyết áp")
    elif 140<=sys<=159 or 90<=dia<=99:
        st.error("Tăng huyết áp độ 1") 
    elif 160<=sys<=179 or 100<=dia<=109:
        st.error("Tăng huyết áp độ 2")
    else:
        st.error("Tăng huyết áp độ 3")         
    if heart_rate <60:
        st.warning("Nhịp tim chậm")
    elif 60<=heart_rate<=100:
        st.success("Nhịp tim bình thường")
    else:
        st.success("Nhịp tim cao")
    # ==========================
    # 📖 Lý thuyết nhịp tim theo độ tuổi
    # ==========================
    st.markdown("### 📖 Nhịp tim theo độ tuổi")
    st.markdown("""
    - Công thức nhịp tim tối đa: 220 - tuổi  
    - Vùng tập luyện hiệu quả: *50% - 85% nhịp tim tối đa*

    | Tuổi | Tối đa (bpm) | 50-85% (bpm) |
    |------|--------------|--------------|
    | 20   | 200          | 100 - 170    |
    | 30   | 190          | 95 - 162     |
    | 40   | 180          | 90 - 153     |
    | 50   | 170          | 85 - 145     |
    | 60   | 160          | 80 - 136     |
    | 70   | 150          | 75 - 128     |
    """)
# 📖 Lý thuyết nhịp tim theo độ tuổi
    # ==========================
    st.markdown("### 📖 Nhịp tim theo độ tuổi")
    st.markdown("""
    - Công thức nhịp tim tối đa: `220 - tuổi`  
    - Vùng tập luyện hiệu quả: **50% - 85% nhịp tim tối đa**
    | Tuổi | Tối đa (bpm) | 50-85% (bpm) |
    |------|--------------|--------------|
    | 20   | 200          | 100 - 170    |
    | 30   | 190          | 95 - 162     |
    | 40   | 180          | 90 - 153     |
    | 50   | 170          | 85 - 145     |
    | 60   | 160          | 80 - 136     |
    | 70   | 150          | 75 - 128     |
    """)
    st.header("Phát triển chiều cao")

    if  age > 0:
        st.subheader("Phân tích tiềm năng phát triển chiều cao")
        if gender == "Nam":
            max_growth_age = 21
        else:
            max_growth_age = 19
        if age >= max_growth_age:
            st.info("""Ở độ tuổi hiện tại, khả năng tăng chiều cao tự nhiên gần như là không còn. 
                    Bạn nên tập luyện và bổ sung dinh dưỡng để giữ vóc dáng cân đối.
                    """)
        else:
            remaining_years = max_growth_age - age
            st.write(f"Bạn vẫn còn khoảng {remaining_years} năm để phát triển chiều cao tối ưu.")
            if activity_level == "Ít vận động":
                growth_potential  = "Thấp"
                st.warning("Mức độ vận động thấp có thể làm hạn chế phát triển chiều cao. Hãy cố gắng vận động nhiều hơn mỗi ngày.")
            elif activity_level == ["Vận động nhẹ (1-3 buổi/tuần)", "Vận động vừa (3-5 buổi/tuần)"]:
                growth_potential  = "Trung bình"
                st.info("Mức độ vận động khá tốt, bạn nên bổ sung thêm các bài tập kéo dãn hoặc thể thao ngoài trời để tối ưu phát triển.")
            else:
                growth_potential = "cao"
                st.success("Rất tốt! Mức độ vận động cao giúp kích thích hormone tăng trưởng, hỗ trợ phát triển chiều cao tối đa.")
            
            st.markdown(f"Tiềm năng phát triển chiều cao của bạn: {growth_potential}")
            st.markdown("Gợi ý phát triển chiều cao tối đa")
            with st.expander("Chế độ dinh dưỡng nên bổ sung"):
                st.markdown("""
                    -**Protein:** Thịt nạc, cá, trứng, đậu phụ
                    -**Canxi:** Sữa, phô mai, sữa chua, cá hồi, rau xanh đậm 
                    -**Vitamin D:** Phơi nắng 15-20 phút hoặc ăn trứng, cá
                    -**Kẽm và Magie:** Có trong hải sản, các loại hạt, đậu, ngũ cốc nguyên hạt
                    -**Tránh:** Nước ngọt có gas, đồ ăn nhanh, đồ chiên rán nhiều mỡ
""")
            with st.expander("Bài tập hỗ trợ phát triển chiều cao"):
                st.markdown(""""
                    -**Tập hàng ngày:** Bơi lội, nhảy dây, bóng rổ, đu xà, yoga kéo giãn
                    -**Buổi sáng:** Kéo dãn cơ thể, vươn vai, hít thở sâu ngoài trời
                    -**Thói quen:** Giữ lưng thẳng khi ngồi và đứng, tránh gù lưng
                            """)





