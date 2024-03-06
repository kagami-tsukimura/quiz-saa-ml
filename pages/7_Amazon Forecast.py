import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon SageMakerエンドポイントを作成して、Amazon S3パケットにある過去のデータでモデルをトレーニングする。関数URL付きのAWS Lambda関数を設定して、SageMakerモデルで予測を行う。"
        self.B = "Amazon SageMakerモデルをデプロイして、Amazon s3バケットにある過去のデータでモデルをトレーニングする。関数URL付きのAWS Lambda関数を設定して、 SageMakerモデルで予測を行う。"
        self.C = "Amazon S3バケットにある過去のデータを使用して、Amazon Forecast予測モデルをトレーニングする。Amazon Forecast予測モデルを使用する関数URL付きのAWS Lambda関数を設定して、予測を行う。"
        self.D = "Amazon S3バケットにある過去のデータを使用して、Amazon Forecast予測モデルをトレーニングする。Amazon Forecast予測モデルを使用するAmazonSageMakerモデルをデプロイして、予測を行う。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>7. Amazon Forecast</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Forecast_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題７")
st.write(
    """
    ある会社は、ユーザーの身体データを収集する健康管理機能を有した腕時計を開発しています。  
    このソリューションでは、Amazon S3バケットに保存されているデータを使用して健康管理に関する予測モデルを作成する必要があります。  
    マネージドサービスを利用して機械学習のトレーニングと予測を行いたいと考えており、予測モデルはURL形式で呼び出せる必要があります。  
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
            Amazon Forecastは予測モデルを生成できるマネージド型サービスです。  
            Amazon ForecastはAmazon S3バケット内のデータを読み込んで予測モデルの学習と予測実行が可能です。  
            また、AWS Lambda関数を利用してその予測モデルを実行するアプリケーションを開発することもできます。  
            関数URL付きのAWS Lambda関数を利用することで、API Gatewayなしに予測モデルをURL形式で呼び出すことができます。\n
            ・選択肢AとBとDは不適切です。  
            Amazon SageMakerは機械学習モデルをユーザーがコーディングできる機械学習プラットフォームサービスです。  
            マネージド型サービスのAmazon Forecastと異なり、一からモデルを構成する知見が必要となります。\n
        """
    )
