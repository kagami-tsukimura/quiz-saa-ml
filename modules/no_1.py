import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon Rekognitionで複数の話者を識別し、トランスクリプトファイルをAmazon S3に保存する。Amazon Textractでトランスクリプトを解析する。"
        self.B = "Amazon Transcribeで複数の話者を識別し、トランスクリプトファイルをAmazon S3に保存する。Amazon Athenaでトランスクリプトを解析する。"
        self.C = "Amazon Translateで複数の話者を識別し、トランスクリプトをAmazon Redshiftに保存する。SQLクエリでトランスクリプトを解析する。"
        self.D = "Amazon Pollyで複数の話者を識別し、トランスクリプトをAmazon S3に保存する。Amazon Comprehendでトランスクリプトを解析する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


def main():

    st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)

    st.write("")
    st.markdown(
        "<h2 style='text-align: center;'>総合問題</h2>",
        unsafe_allow_html=True,
    )

    _ = [st.write("") for _ in range(5)]

    choice = Choice()

    st.write("### 問題１")
    st.write(
        """
        テレマーケティング企業では、AWS上でコールセンターのシステム構築を検討しています。  
        同社では、複数の話者を識別した精度の高いトランスクリプトを生成するソリューションが必要です。  
        また、ビジネスパターン把握のために、これらのトランスクリプトを解析したいと考えています。  
        トランスクリプトは監査に対応するため、7年間保存する必要があります。  
        これらの要件を満たすことができるソリューションはどれでしょうか？  
        """
    )

    answer = st.radio("", choice.get_choices())
    st.write("")
    _, col_check = st.columns((8, 2))

    if col_check.button("チェック"):
        if answer == choice.get_choices()[1]:
            st.success("正解！")
        else:
            st.error("不正解...")

        st.write("### 解説")
        st.write(
            """
                ・選択肢Bは適切です。  
                Amazon Transcribeは音声をテキストに変換するサーピスで、複数話者の識別が可能です。  
                トランスクリプトファイルはAmazon S3に保存でき、S3上に長期保存を行います。  
                また、Amazon Athenaでトランスクリプトの解析を行うことが可能です。  
                AthenaはS3に保存されたデータに対してSQLクエリを実行することができるため、ビジネスパターンの分析に適しています。\n
                ・選択肢Aは不適切です。  
                Amazon Rekognitionは主に画像や動画分析に用いられ、音声識別やトランスクリプト生成のためのサービスではありません。  
                また、Amazon Textractは主に印刷されたテキストや手書きのテキストを認識するためのサービスで、トランスクリプトの解析には向いていません。\n
                ・選択肢Cは不適切です。  
                Amazon Translateは翻訳サービスであり、復数話者の識別やトランスクリプト生成のためのサービスではありません。  
                また、Amazon Redshiftはデータウェアハウスサービスで、大量の構造化テークの長期保存には適していますが、テキストデータの保存には適していません。\n
                ・選択肢Dは不適切です。  
                Amazon Pollyはテキストを自然な音声に変換するサービスであり、話者の識別やトランスクリプト生成はサポートしていません。\n
            """
        )
