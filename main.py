import streamlit as st
from PIL import Image
import time

st.title('Streamlit 超入門')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption='sample', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text, 'です。'

condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンディション', condition

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)

#st.bar_chart(df)
#API Reference display chartsで確認

#st.write(df, width=100, height=100) #writeは引数が使えない
#st.dataframe(df.style.highlight_max(axis=0)) #dataframeは引数が使える
#st.table(df.style.highlight_max(axis=0)) #tableは静的な表を作成したいときに使える
#詳しくデータ表示を見たい人は公式ドキュメント->API Reference
