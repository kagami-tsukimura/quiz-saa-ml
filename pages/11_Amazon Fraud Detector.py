import streamlit as st


class Choice:
    def __init__(self):
        self.A = "独自に不正検出の機械学習モデルを開発する。"
        self.B = "Amazon Personalizeで顧客の行動に基づき不正な注文を検知する。"
        self.C = "Amazon Macieで個人情報漏洩のリスクを検知する。"
        self.D = "Amazon Fraud Detectorで顧客の行動に基づいて不正な注文を検知する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>11. Amazon Fraud Detector</h2>",
    unsafe_allow_html=True,
)
col2.image("images/Arch_Amazon-Fraud-Detector_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題１１")
st.write(
    """
    Eコマース企業は、高い精度で不正な注文を検知するシステムを構築しようとしています。  
    機械学習の知見者はおらず、予算の都合上コストも抑えなければなりません。  
    なお、過去の顧客の購入履歴や閲覧履歴、デバイス情報などはデータソースとして利用可能です。  
    これらの要件を満たすソリューションはどれでしょうか？  
    """
)

answer = st.radio("", choice.get_choices())
st.write("")
_, col_check = st.columns((8, 2))

if col_check.button("チェック"):
    if answer == choice.get_choices()[3]:
        st.success("正解！")
    else:
        st.error("不正解...")

    st.write("### 解説")
    st.write(
        """
            ・選択肢Dは適切です。  
            Amazon Fraud Detectorは、過去の通信ログなどから不正アクセスを検出するサービスです。  
            機械学習の知見がなくとも、フルマネージドで簡単に不正検知システムを構築できます。  
            導入コストも比較的低く、予算を抑えることができます。  
            さらに、不正検知に特化しており、高い精度が期待できます。\n
            ・選択肢Aは不適切です。  
            Eコマース企業には機械学習の知見者がいないため、独自の機械学習モデルを作成できません。  
            また、独自で作成するには開発コストや運用コストがAWS Fraud Detectorを利用する場合より高くなるため、コストを抑える要件からも外れます。\n
            ・選択肢Bは不適切です。  
            Amazon Personalizeは、顧客の行動データに基づいて、個々の顧客に合わせたレコメンデーションを提供するサービスです。  
            不正な注文を検知する要件に適したサービスではありません。\n
            ・選択肢Cは不適切です。  
            Eコマース企業には機械学習の知見者がいないため、独自の機械学習モデルを作成できません。  
            また、コストを抑える要件からも外れます。\n
        """
    )
