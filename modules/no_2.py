import streamlit as st


class Choice:
    def __init__(self):
        self.A = "既存のPythonライブラリで、レポートからテキストを抽出し、抽出されたテキストからPHIを識別する。"
        self.B = "Amazon Textractでレポートからテキストを抽出する。Amazon SageMakerで、抽出されたテキストからPHIを識別する。"
        self.C = "Amazon Textractでレボートからテキストを抽出する。Amazon Comprehend Medicalで、抽出されたテキストからPHIを識別する。"
        self.D = "Amazon Rekognitionでレポートからテキストを抽出する。Amazon Comprehend Medicalで、抽出されたテキストからPHIを識別する。"
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

    st.write("### 問題２")
    st.write(
        """
        ある病院は最近、Amazon API GatewayとAWS LambdaでRESTful APIをデプロイしました。  
        病院はAPI GatewayとLambdaで、PDF形式とJPEG形式のレポートをアップロードしています。  
        病院は、Lambdaコードを変更して、保護された医療情報 (PHI) を識別する必要があります。  
        運用上のオーバーヘッドが最も少なく、これらの要件を満たすソリューションはどれですか？  
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
                Amazon Textractは、スキャンされたドキュメントからテキスト、手書きの文字、データを自動抽出する機械学習サービスです。  
                サポートする形式はPDFまたはJPEGです。  
                また、Amazon Comprehend Medicalで保護された医療情報(PHI)を識別することが可能となります。\n
                ・選択肢Aは不適切です。  
                Pythonライブラリを使用した場合は、アプリケーションの運用が必要なため運用上のオーバーヘッドが増えてしまいます。\n
                ・選択肢Cは不適切です。  
                Amazon SageMakerはあらゆるユースケース向けの機械学習(ML)モデルを構築、トレーニング、デプロイするサービスです。  
                ただし、本サービスの要件を満たすには医療用に特化した学習をさせる必要があり、運用上のオーバーヘッドが増えてしまいます。\n
                ・選択肢Dは不適切です。  
                Amazon Rekognitionがサポートしている形式は、JPEGとPNGのみです。  
                PDF形式は未サポートのため、要件を満たすことが出来ません。\n
            """
        )
