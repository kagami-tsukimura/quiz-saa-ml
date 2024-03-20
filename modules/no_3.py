import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon Textract APIを呼び出すAWS Lambda関数を作成する。Lambda関数が実行するAmazon Textractがドキュメントをテキストに変換する。"
        self.B = "デジタル化した文書をAmazon S3バケットにアップロードし、Amazon S3イベント通知でLambda関数を実行する。"
        self.C = "Amazon Comprehend Medicalを使用して、テキストから健康診断デ一タを抽出する。"
        self.D = "Amazon Rekognition APIを呼び出すAWS Lambda関数を作成する。Lambda関数が実行するAmazon Rekognitionがドキュメントをテキストに変換する。"
        self.E = "Amazon Transcribeを使用して、テキストから健康診断データを抽出する。"
        self.F = "Lambda関数URLを組み込んだAmazon S3静的ウェブサイトを横築する。このサイトからPDFファイルの読み込み処理を実施する。"
        self.choices = [self.A, self.B, self.C, self.D, self.E, self.F]
        self.symbols = ["A", "B", "C", "D", "E", "F"]

    def get_choices(self):
        return self.choices

    def get_symbols(self):
        return self.symbols


def main():

    st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)

    st.write("")
    st.markdown(
        "<h2 style='text-align: center;'>総合問題</h2>",
        unsafe_allow_html=True,
    )

    _ = [st.write("") for _ in range(5)]

    choice = Choice()

    st.write("### 問題３")
    st.write(
        """
        ある企業は、AWSを利用して従業員の人事文書を保存するためのソリューションを構築しています。  
        文書によっては手書きの古い文書も存在するため、古い手書き文書は一旦デジタル化してから保存することが必要です。  
        同社では福利厚生の一環として、従業員の健康管理を実施する健康管理アプリケーションを導入しています。  
        あなたはソリューションアーキテクトとして、これらのドキュメントをテキスト化してから健康診断に関する情報のみを抽出して健康管理アプリケーションに保存することが求められています。  
        また、このソリューションでは、スケーラビリティと運用効率を最大化する必要があります。  
        この要件に適したソリューションの組み合わせはどれでしょうか？（3つ選択）  
        """
    )

    [st.write("") for _ in range(3)]
    for symbol, choice_text in zip(choice.get_symbols(), choice.get_choices()):
        st.write(f"{symbol}. {choice_text}\n\n")
    answers = st.multiselect(
        "", choice.get_symbols(), placeholder="3つ選択してください"
    )
    st.write("")
    _, col_check = st.columns((8, 2))

    if col_check.button("チェック"):
        if set(answers) == {
            choice.get_symbols()[0],
            choice.get_symbols()[2],
            choice.get_symbols()[5],
        }:
            st.success("正解！")
        else:
            st.error("不正解...")

        st.write("### 解説")
        st.write(
            """
                ・選択肢Aは適切です。  
                Amazon Textractは光学文字認識(OCR)で、PDFなどのスキャンしたドキュメント、フォーム、表からテキストデータを自動的に抽出するサービスです。  
                Lambda関数からAmazon Textract APIを呼び出し、サーバレスに文書のデジタル処理を実行することができます。\n
                ・選択肢Cは適切です。  
                デジタルデータから特定の医療データを抽出する際は、Amazon Comprehend Medicalを使用します。  
                Amazon Comprehend Medical は、デジタルデータから構造化されていない臨床テキスト内の有用な情報を検出して返すサービスです。\n
                ・選択肢Fは適切です。  
                Lambda関数URLを組み込んだAmazon S3静的ウェブサイトを構築して、サイトからPDFファイルの読み込み処理を実施します。  
                手書き文書をPDF化した後、Amazon TextractでOCR処理を実施します。  
                その際は、必要となる簡易なアプリケーションをLambda関数URLを組み込んだAmazon S3静的ウェブサイトで実現します。\n
                ・選択肢Bは不適切です。  
                ドキュメントをAmazon S3バケットにアップロードする際に、Amazon S3イベント通知を利用してLambda関数を実行することはできます。  
                しかしながら、今回は人事文書をデジタル化した後にAmazon S3バケットに保存することになり、OCR処理前に保存が発生して手順がおかしくなります。\n
                ・選択肢Dは不適切です。  
                Amazon Rekognition APIがサポートしている形式は、JPEGとPNGのみです。  
                PDF形式は未サポートのため、要件を満たすことが出来ません。\n
                ・選択肢Eは不適切です。  
                Amazon Transcribeは音声をテキストに変換する音声認識の技術を用いたサービスです。  
                Amazon Transcribeを使用して、テキストから健康診断データを抽出することはできません。\n
            """
        )
