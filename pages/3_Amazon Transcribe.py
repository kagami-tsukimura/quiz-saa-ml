import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon Kinesis PIIリダクション機能を有効にして、Amazon Kinesis Video Streamsを使用して音声ファイルを処理する。Amazon Kinesis Data Firehoseにより、出力結果をS3バケットに保存する。"
        self.B = "Amazon Kinesis Video Streamsを使用して音声ファイルを処理して、音声ファイルをS3バケットに保存する。S3イベント通知によってAWS Lambda関数を呼び出してPIIリダクション機能を有効にしたAmazon Textractタスクを開始し、通話音声を分析する。"
        self.C = "Amazon Transcribe PIIリダクション機能を有効にして、AmazonTranscribeの文字起こしジョブを設定する。音声ファイルがS3バケットにアップロードされたらAWS Lambda関数を呼び出して文字起こしジョブを実行する。出力結果をS3バケットに保存する。"
        self.D = "Amazon Kinesis PIIリダクション機能を有効にして、Amazon Kinesis Video Streamsを使用して音声ファイルを処理する。 Amazon EventBridgeを使用して、音声ファイルがS3バケットにアップロードされたときにジョブを開始する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>3. Amazon Transcribe</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Transcribe_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題３")
st.write(
    """
    ある会社は、AWS上に構築されたコールセンターシステムの運用をしています。  
    あなたはソリューションアーキテクトとして、コールセンターシステムの音声データを利用した分析用アプリケーションを構築しようとしています。  
    このアプリケーションは、音声通話を録音し、その音声ファイルをAmazon S3バケットに保存してからテキストを抽出します。  
    個人情報保護の観点から、顧客個人を特定できる情報をテキストから削除することが必要です。  
    これらの要件を満たすソリューションはどれでしょうか？
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
            ・選択肢AとBとDは不適切です。  
            Amazon Kinesis PIIリダクション機能というものはありません。  
            また、Amazon Kinesis Video Streamsは音声ファイルの文字起こしには利用できません。  
            ・選択肢Cは適切です。  
            音声ファイルからテキストを抽出する際に、顧客個人を特定できる情報を削除するには、Amazon Transcribe PIIリダクション機能を利用します。  
            PIIリダクション機能を有効にして、Amazon Transcribeの文字起こしジョブを設定することで、自動的に顧客個人を特定できる情報を削除することが可能です。  
            PIIとは個人を識別できる情報を指します。  
            Amazon Transcribe PIIリダクション機能はAmazon Transcribeが個人情報を識別して、自動的にPIIを隠蔽してくれます。  
            Lambda関数からAmazon Transcribeジョブを呼び出して、音声ファイルからテキスト抽出する簡易アプリケーションを開発します。  
            それをAmazon S3イベント通知機能に連携することで、音声ファイルがS3バケットにアップロードされたイベントをトリガーにLambda関数が呼び出され、Amazon Transcribeジョブを実行し、出力結果をS3バケットに保存することが可能となります。
        """
    )
