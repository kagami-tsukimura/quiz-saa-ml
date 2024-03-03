import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon Transcribeで音声記録をテキストに変換する。変換されたテキストに対してAmazon Translateで日本語と中国語を英話に翻訳する。Amazon Comprehendでテキストに対して感情分析を実施する。"
        self.B = "Amazon Comprehendで音声記録をテキストに変換する。変換されたテキストに対してAmazon Translateで日本語と中国語を英語に翻訳する。Amazon Lexでテキストに対して感情分析を実施する。"
        self.C = "Amazon Comprehendで音声記録をテキストに変換する。変換されたテキストに対してAmazon Translateで日本語と中国語を英語に翻訳する。Amazon Pollyでテキストに対して感情分析を実施する。"
        self.D = "Amazon Transcribeで音声記録をテキストに変換する。変換されたテキストに対してAmazon Translateで日本語と中国語を英語に翻訳する。Amazon Pollyでテキストに対して感情分析を実施する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>4. Amazon Polly</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Polly_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題４")
st.write(
    """
    ある会社はAWSにホストされたECサイトを運用しており、コールセンターシステムによる顧客対応も実施しています。  
    顧客は世界中におり、英語と日本語と中国語の対応が必須です。  
    同社は顧客満足度をあげるためにコールセンターの音声記録を分析することにしました。  
    以下のように音声記録を解析する必要があります。

    ・音声記録をテキストに変換する。  

    ・日本語と中国語もすべて英語に変換する。  

    ・テキスト内容の感情分析を実施する。  

    しかし、自社の要員で機械学習モデルを生成して対応するためのリソースが不足しています。  
    どのようにデータを解析すればよいでしょうか？  
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
            Amazon Transcribeで音声記録をテキストに変換します。  
            アップロードされた音声を読み込むことで、その内容をテキストへと変換することができます。  
            日本語と中国語もすべて英語に翻訳するために、音声記録から変換後のテキストにAmazon Translateを適用し、日本語テキストと中国語テキストを英語に翻訳します。  
            Amazon Translateは様々な言語に適用して、特定の言語に変換することができます。  
            Amazon Comprehendで英語テキストへの感情分析を実施します。  
            Amazon Comprehendは機械学習を使用してテキスト内の感情分析、キーフレーズ抽出、インサイト抽出ができる自然言語処理(NLP)のサービスです。  
            これで感情分析レポートを作成することができます。\n
            ・選択肢Bは不適切です。  
            Amazon Comprehendを利用して音声記録をテキストに変換することはできません。  
            また、Amazon Lexを利用してテキスト内容の感情分析を実施できません。  
            Amazon LexはAlexaに利用されている音声言語対話AIサービスです。\n
            ・選択肢Cは不適切です。  
            Amazon Comprehendを利用して音声記録をテキストに変換することはできません。  
            また、Amazon Pollyを利用してテキストに対して感情分析を実施することはできません。  
            Amazon Pollyは人間の声のような音声を合成する音声生成AIサービスです。\n
            ・選択肢Dは不適切です。  
            Amazon Pollyを利用してテキストに対して感情分析を実施することはできません。  
        """
    )
