import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon Pollyでチャットポットを作成する。チャットボットのメッセージ内でAmazon Rekognitionでアップロードされた修理箇所の写真から修理内容の識別を行う。"
        self.B = "Amazon Pollyでチャットボットを作成する。チャットボットのメッセージ内でAmazon SageMakerで画像識別モデルを生成して、アップロードされた修理箇所の写真から修理内容の識別を行う。"
        self.C = "Amazon Lexでチャットポットを作成する。チャットボットのメッセージ内でAmazon Rekognitionでアップロードされた修理箇所の写真から修理内容の識別を行う。"
        self.D = "Amazon Lexでチャットボットを作成する。チャットボットのメッセージ内でAmazon SageMakerで画像識別モデルを生成して、アップロードされた修理箇所の写真から修理内容の識別を行う。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>5. Amazon Lex</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Lex_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題５")
st.write(
    """
    ある会社は自動車修理システムを構築しています。  
    自動車修理時の見積もりをアプリケーションで簡易に実施するために、チャットボットを利用する予定です。  
    あなたはソリューションアーキテクトとして、チャットボットを利用した対話システムの構築を検討しています。  
    チャットボットとのやり取りで、画像認識を利用した修理内容の把握も必要となります。  
    AWSではAI機能を提供しているため、技術選定することにしました。  
    しかし同社ではAIモデルを生成するリソースが不足しています。  
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
            ・選択肢Cは適切です。  
            Amazon Lexは、音声やテキストを使用して、任意のアプリケーションにチャットボットを構築するサービスです。  
            音声のテキスト変換には自動音声認識(ASR)、テキストの意図認識には自然言語理解(NLU)という高度な深層学習機能が使用できるため、リアルな会話を実現するアプリケーションを開発できます。  
            Amazon Rekognitionで、アップロードされた修理箇所の写真から修理内容の識別を行うことができます。  
            Amazon RekognitionはAI知識がないエンジニアであっても容易に画像分析と動画分析をアプリケーションを構築できる画像識別AIです。  
            Rekognition APIに画像または動画を与えるだけで、このサービスが対象物、人、テキスト、シーン、アクティビティ、それに不適切なコンテンツまで検出します。\n
            ・選択肢AとDは不適切です。  
            Amazon Pollyは、文章をリアルな音声に変換するサービスです。  
            発話できるアプリケーションを作成できますが、チャットボット機能は有していません。\n
            ・選択肢Bは不適切です。  
            Amazon SageMakerは開発者とデータサイエンティストに機械学習モデルを迅速に構築、トレーニング、デプロイするためのAI開発環境を提供するプラットフォームです。  
            同社はAIモデルを生成するリソースが不足しているため、Amazon SageMakerを利用してAIモデルを構成することができません。  
            したがって、Amazon Rekognitionを利用する方が最適です。  
        """
    )
