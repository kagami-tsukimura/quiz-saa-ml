import streamlit as st


class Choice:
    def __init__(self):
        self.A = (
            "Amazon Textractで抽出したデータをAmazon Comprehendに取り込んで分析する。"
        )
        self.B = "Amazon Textractで抽出したデータをAmazon Athenaに取り込んで分析する。"
        self.C = (
            "Amazon Comprehendで抽出したデータをAmazon Athenaに取り込んで分析する。"
        )
        self.D = (
            "Amazon Comprehendで抽出したデータをAmazon Textractに取り込んて分析する。"
        )
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>10. Amazon Textract</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Textract_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題１０")
st.write(
    """
    あるメディア企業は、自社のニュースサイトを運営しています。  
    開発チームはニュースレポートの分析を依頼されました。  
    その際は、機械学習機能を利用してニュースレポートを処理して、ニュースレポートの内容と書き込みコメントに対するインサイトを抽出することが必要です。  
    これらの要件を満たすことができるソリューションはどれでしょうか？  
    """
)

answer = st.radio("", choice.get_choices())
st.write("")
_, col_check = st.columns((8, 2))

if col_check.button("チェック"):
    if answer == choice.get_choices()[0]:
        st.success("正解！")
    else:
        st.error("不正解...")

    st.write("### 解説")
    st.write(
        """
            ・選択肢Aは適切です。  
            ニュースサイトのような文字情報を分析する際は、Amazon Textractを利用して文字データを抽出すること求められます。  
            そして抽出された文字データを分析するためにAmazon Comprehendを利用することで、ニュースレポートの内容と書き込みコメントに対するインサイトを抽出することができます。\n
            ・選択肢BとCは不適切です。  
            Amazon AthenaはAmazon S3に保存されたデータに対して、SQLクエリを実行することができる機能です。  
            ドキュメント情報の解析には利用できません。\n
            ・選択肢Dは不適切です。  
            Amazon Comprehendはドキュメントから文字データを抽出することができません。  
            Amazon Comprehendは文字情報から価値あるインサイトを導き出し、理解することができる言語識別AIサービスです。\n
        """
    )
