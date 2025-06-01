import streamlit as st
st.title('Nghệ sĩ âm nhạc yêu thích')
col1,col2 = st.columns(2)
col3,col4 = st.columns([2,1])
with col1:
    b1 = st.button('Kanye West')
    with st.form('Kanye West'):
        options = ['có','không']
        option = st.multiselect('Bạn thích nghệ sĩ này chứ?',options)
        submitted = st.form_submit_button('Chọn')
        if submitted:
            if len(option) == 0:
                st.write('Bạn chưa cho ý kiến')
            else:
                st.write('Cảm ơn bạn đã cho ý kiến!')    
with col2:
    b2 = st.button('Kendrick Lamar')
    with st.form('Kendrick Lamar'):
        options = ['có','không']
        option = st.multiselect('Bạn thích nghệ sĩ này chứ?',options)
        submitted = st.form_submit_button('Chọn')
        if submitted:
            if len(option) == 0:
                st.write('Bạn chưa cho ý kiến')
            else:
                st.write('Cảm ơn bạn đã cho ý kiến!')    
if b1:
    with col3:
        st.title('Bài hát yêu thích')
        st.write('Gone')
        #audio = open('Gone.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('All of the lights')
        #audio = open('All Of The Lights.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Blood on the leaves')
        #audio = open('Blood On The Leaves.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Family business')
        #audio = open('Family Business.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Saint Pablo')
        #audio = open('Saint Pablo.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Ghost town')
        #audio = open('Ghost Town.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Paranoid')
        #audio = open('Paranoid.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Otis')
        #audio = open('Otis.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Diamonds From Sierra Leone (Remix)')
        #audio = open('Diamonds From Sierra Leone (Remix).mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Runaway')
        #audio = open('Runaway.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Homecoming')
        #audio = open('Homecoming.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Slow Jamz')
        #audio = open('Slow Jamz.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('All Falls Down')
        #audio = open('All Falls Down.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('We Major')
        #audio = open('We Major.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('I Wonder')
        #audio = open('I wonder.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('RoboCop')
        #audio = open('RoboCop.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Devil In A New Dress')
        #audio = open('Devil In A New Dress.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Niggas In Paris')
        #audio = open('Nias In Paris.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Bound 2')
        #audio = open('Bound 2.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('No More Parties In LA')
        #audio = open('No More Parties In LA.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Come To Life')
        #audio = open('Come To Life.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        st.title('MV yêu thích')
        video = 'https://www.youtube.com/watch?v=gG_dA32oH44'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=BBAtAM7vtgc'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=BoEKWtgJQAU'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=8kyWDhB_QeI'
        st.video(video, format='video/mp4')
    with col4:
        image = 'https://i8.amplience.net/i/naras/kanye-west_MI0005472981-MN0000361014'
        st.image(image,caption='Kanye West')
        st.write('Họ và tên: Kanye West')
        st.write('Nghệ danh:Ye')
        st.write('Kanye West là một trong những nghệ sĩ có ảnh hưởng lớn nhất trong ngành âm nhạc hiện đại. Anh nổi bật với phong cách sản xuất độc đáo và khả năng kết hợp các thể loại như hip hop, rap, và nhạc điện tử. Các album nổi tiếng của anh như The College Dropout, Graduation, 808s & Heartbreak, và My Beautiful Dark Twisted Fantasy đều được đánh giá cao về sự sáng tạo và cách tân âm nhạc.Kanye đã giành được 24 giải Grammy và là một trong những nghệ sĩ thành công nhất trong lịch sử giải thưởng này')
if b2:
    with col3:
        st.title('Bài hát yêu thích')
        st.write('Barbed Wire')
        #audio = open('Barbed Wire.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Hol Up')
        #audio = open('Hol Up.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Keisha Song (Her Pain)')
        #audio = open('Keisha Song (Her Pain).mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Hiiipower')
        #audio = open('Hiiipower.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Swimming Pools (Drank)')
        #audio = open('Swimming Pools (Drank).mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Sing About Me, Im Dying Of Thirst')
        #audio = open('Sing About Me, Im Dying Of Thirst.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('The Recipe')
        #audio = open('The Recipe.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('These Walls')
        #audio = open('These Walls.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Alright')
        #audio = open('Alright.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('i')
        #audio = open('i.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('untitled 07  levitate')
        #audio = open('untitled 07  levitate.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('PRIDE')
        #audio = open('PRIDE.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('ELEMENT')
        #audio = open('ELEMENT.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('XXX')
        #audio = open('XXX.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Die Hard')
        #audio = open('Die Hard.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Father Time')
        #audio = open('Father Time.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('Rich Spirit')
        #audio = open('Rich Spirit.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('luther')
        #audio = open('luther.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('heart pt 6')
        #audio = open('heart pt 6.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        #st.write('gloria')
        #audio = open('gloria.mp3','rb')
        #st.audio(audio,format='audio/mp3')
        st.title('MV yêu thích')
        video = 'https://www.youtube.com/watch?v=8-ejyHzz3XE'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=GF8aaTu2kg0'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=Z-48u_uWMHY'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=drV0QatqbRU'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=tvTRZJ-4EyI'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=glaG64Ao7sM'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=ox7RsX1Ee34'
        st.video(video, format='video/mp4')
        video = 'https://www.youtube.com/watch?v=H58vbez_m4E'
        st.video(video, format='video/mp4')
    with col4:
        image = 'data:image/jpeg;base64,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'
        st.image(image,caption='Kendrick Lamar')
        st.write('Họ và tên: Kendrick Lamar Duckworth')
        st.write('Nghệ danh:Kendrick Lamar(K.DOT)')
        st.write('Kendrick Lamar là một rapper, nhạc sĩ và nhà sản xuất âm nhạc người Mỹ, nổi tiếng với những bài hát mang tính xã hội cao và phản ánh thực trạng cuộc sống. Anh đã giành nhiều giải thưởng lớn, bao gồm giải Grammy, và được công nhận là một trong những nghệ sĩ hip-hop xuất sắc nhất thế giới. Âm nhạc của Kendrick Lamar kết hợp nhiều thể loại, từ rap đến jazz và funk, với lời bài hát sâu sắc và thông điệp mạnh mẽ về sự bất công và đấu tranh xã hội.')

        

        
        
        
        
        



