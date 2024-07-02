import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門!')

'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
text = st.text_input('あなたの趣味を教えてください')

st.write('コンディション: ', condition)
st.write('あなたの趣味は、', text, 'です。')

left_column, right_column = st.columns(2)
button = left_column.button('カラム二文字を表示')
if button:
    right_column.write('ここはカラムです')


expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')



option = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1, 11))
)
st.write('あなたの好きな数字は、', option, 'です')


st.write('チェックボックス')
if st.checkbox('show image'):
    st.write('Display Image')
    img = Image.open('yuzu.JPG')
    st.image(img, caption='yuzu', use_column_width=True)


df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.table(df.style.highlight_max(axis=0))
st.dataframe(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)



"""
# テスト用の文字列
### 小タイトル

``` python
import streamlit as st
import numpy as np
import pandas as pd
```
"""