import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon Comprehendで不適切なコンテンツを検出します。信頼性の低い予測には人間によるレビューを使用します。"
        self.B = "Amazon Rekognitionで不適切なコンテンツを検出します。信頼性の低い予測には人間によるレビューを使用します。"
        self.C = "Amazon SageMakerで不適切なコンテンツを検出します。Amazon SageMaker Ground Truthで、信頼性の低い予測にラベルを付けます。"
        self.D = "AWS Fargateでカスタム機械学習モデルをデプロイし、不適切なコンテンツを検出します。Amazon SageMaker Ground Truthで、信頼性の低い予測にラベルを付けます。"
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

    st.write("### 問題４")
    st.write(
        """
        ある会社が人気のソーシャルメディアWebサイトを運営しています。  
        このWebサイトでは、ユーザーは画像をアップロードして他のユーザーと共有することができます。  
        同社は、画像に不適切なコンテンツが含まれていないことを確認したいと考えています。  
        同社は開発労力を最小限に抑えるソリューションを必要としています。  
        これらの要件を満たすために、ソリューションアーキテクトは何をすべきでしょうか？  
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
                Amazon Rekognitionは画像分析サービスであり、不適切なコンテンツ検出機能を備えています。  
                また、信頼性の低い予測には人間によるレビューを使用することで、開発労力を抑えたソリューションとなります。\n
                ・選択肢Aは不適切です。  
                Amazon Comprehendは機械学習を使用してテキスト内の感情分析、キーフレーズ抽出、インサイト抽出ができる自然言語処理(NLP)のサービスです。  
                画像の不適切なコンテンツを検出する機能は備えていません。\n
                ・選択肢Cは不適切です。  
                Amazon SageMakerはあらゆるユースケース向けの機械学習(ML)モデルを構築、トレーニング、デプロイするサービスです。  
                また、Amazon SageMaker Ground Truthは、フルマネージドでデータにラベル付けできるサービスです。  
                ただし、Amazon Rekognitionを用いる場合と比べ、画像分析用の学習をさせる必要があり、開発労力は増加します。\n
                ・選択肢Dは不適切です。  
                AWS Fargate はサーバー管理が不要なコンテナ実行サービスです。  
                カスタム機械学習モデルをデプロイして、画像の不適切なコンテンツ検出を行うことができます。  
                ただし、Fargateはコンテナ実行に特化したサービスであり、モデル構築や学習には適していないため、開発労力は増加します。\n
            """
        )
