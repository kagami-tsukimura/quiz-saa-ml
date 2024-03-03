import streamlit as st


class Choice:
    def __init__(self):
        self.A = "ファイルを分析S3バケットにコピーするLambda関数を作成する。分析S3バケットのS3イベント通知を作成する。イベント通知の送信先としてLambdaおよびSageMakerパイプラインを設定する。"
        self.B = "ファイルを分析S3バケットにコピーするLambda関数を作成する。イベント通知をAmazon EventBridgeに送信するように分析S3バケットを設定する。EventBridgeでObjectCreatedルールを構成する。ルールのターゲットとしてLambdaおよびSageMakerパイプラインを設定する。"
        self.C = "S3バケット間のS3レプリケーションを設定する。分析S3バケットのS3イベント通知を作成する。イベント通知の送信先としてLambdaおよびSageMakerパイプラインを設定する。"
        self.D = "S3バケット間のS3レプリケーションを設定する。イベント通知をAmazon EventBridgeに送信するように分析S3バケットを設定する。EventBridgeでObjectCreatedルールを構成する。ルールのターゲットとしてLambdaおよびSageMakerパイプラインを設定する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>1. Amazon SageMaker</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-SageMaker_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題１")
st.write(
    """
    レポートチームは、Amazon S3バケットで毎日ファイルを受け取ります。  
    Amazon QuickSight で使用するために、毎日同時にこの初期S3バケットから分析S3バケットにファイルを手動でコピーします。  
    追加のチームが、より大きなサイズのファイルを最初のS3バケットに送信し始めています。  
    レポートチームは、ファイルが最初のS3バケットに入ると、自動的に分析S3バケットに移動したいと考えています。  
    また、AWS Lambda関数を使用して、コピーされたデータにパターンマッチングを実行することも望んでいます。  
    さらに、データファイルをAmazon SageMaker Pipelinesに送信したいと考えています。  
    これらの要件を最小の運用オーバーヘッドで満たすために、ソリューションアーキテクトは何をすべきでしょうか?  
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
            ・選択肢AとCは不適切です。  
            Lambda関数はファイルのコピー処理にのみ使用され、パターンマッチングやSageMakerパイプラインへのデータ送信には対応できません。  
            S3レプリケーションはファイルのコピーのみを行い、Lambda関数やSageMakerパイプラインとの連携はできません。\n
            ・選択肢BとDは適切ですが、Dの方が運用オーバーヘッドが小さいため適切です。  
            EventBridgeを使用することで、S3バケットにファイルが追加された際にLambda関数とSageMakerパイプラインを同時に起動できます。  
            DはLambda関数とSageMakerパイプラインを個別に設定する必要がなく、設定と管理がよりシンプルになります。
        """
    )
