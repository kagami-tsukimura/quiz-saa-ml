import streamlit as st


class Choice:
    def __init__(self):
        self.A = "EC2インスタンスからRekognition APlを呼び出し、JSONフォーマットで情報を取得する。取得した画像をS3バケットに保存して、エンドユーザー側の端末に表示させるプロセスを実装する。"
        self.B = "Lambda関数からRekognition APIを呼び出し、JSONフォーマットで情報を取得する。取得した画像をS3バケットに保存して、エンドユーザー側の端末に表示させるプロセスを実装する。"
        self.C = "Lambda関数からRekognition APIを呼び出し、JSONフォーマットで情報を取得する。取得した画像をDynamoDBに保存して、エンドユーザー側の端末に表示させるプロセスを実装する。"
        self.D = "EC2インスタンスからRekognition APIを呼び出し、JSONフォーマットで情報を取得する。取得した画像をDynamoDBに保存して、エンドユーザー側の端末に表示させるプロセスを実装する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>2. Amazon Rekognition</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Rekognition_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題２")
st.write(
    """
    ある企業は動物画像検索アプリを開発しています。  
    このアプリケーションでは、ユーザーが動物写真をアップロードすることで、類似した動物を画像検索できます。  
    一連の写真をアップロードして、特定の画像が利用された時間を検索することもできます。  
    開発チームはアプリケーションの開発を迅速に実施するために、マネージド型のAWSサービスを利用して構築したいと考えています。  
    この要件を実装するのにコスト最適で容易なソリューションはどれでしょうか？
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
            ・選択肢AとDは不適切です。  
            コスト最適で容易なソリューションという要件からEC2インスタンスではなく、Lambdaによるサーバレスアプリケーションを優先します。\n
            ・選択肢Cは不適切です。  
            DynamoDBはNoSQLデータベースであり、ドキュメント型としてJSON形式のデータは扱えますが、画像を保存することはできません。\n
            ・選択肢Bは適切です。  
            Lambda関数からRekognition APIを呼び出すことで、低コストなサーバレスな画像識別アプリケーションを構築することができます。
        """
    )
