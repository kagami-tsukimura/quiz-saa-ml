import streamlit as st


class Choice:
    def __init__(self):
        self.A = "既存のPythonライブラリを使用してレポートからテキストを抽出し、抽出されたテキストからPHIを識別します。"
        self.B = "Amazon Textractを使用してレポートからテキストを抽出します。Amazon SageMakerを使用して、抽出されたテキストからPHIを識別します。"
        self.C = "Amazon Textractを使用してレポートからテキストを抽出します。Amazon Comprehend Medicalを使用して、抽出されたテキストからPHIを特定します。"
        self.D = "Amazon Rekognitionを使用してレポートからテキストを抽出します。Amazon Comprehend Medicalを使用して、抽出されたテキストからPHIを識別します。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>5. Amazon Lex</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Comprehend_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題６")
st.write(
    """
    ある病院は最近、API GatewayとLambdaを使用してRESTful API をデプロイしました。  
    病院はAPI GatewayとLambdaを使用して、PDF 形式とJPEG形式のレポートをアップロードします。  
    レポート内の保護医療情報(PHI)を特定するためにLambdaコードを変更する必要があります。  
    運用オーバーヘッドを最小限に抑えながらこれらの要件を満たすソリューションはどれですか？
    """
)

answer = st.radio("", choice.get_choices())
st.write("")
_, col_check = st.columns((8, 2))

if col_check.button("チェック"):
    if answer == choice.get_choices()[2]:
        st.success("正解！")
    else:
        st.error("不正解...")

    st.write("### 解説")
    st.write(
        """
            ・選択肢Cは適切です。  
            Amazon TextractはPDFや画像からテキストを抽出するサービスです。  
            Amazon Textractでレポートからテキストを抽出し、Amazon Comprehend Medicalで医療情報(PHI)を特定します。\n
            ・選択肢AとBは不適切です。  
            既存のPythonライブラリやAmazon SageMakerを使用する場合、運用オーバーヘッドを最小限に抑える要件を満たせません。\n
            ・選択肢Dは不適切です。  
            Amazon Rekognitionは深層学習技術を使用して画像や動画を分析するサービスです。  
            Amazon Rekognitionを使用してレポートからテキストを抽出することはできません。\n
        """
    )
