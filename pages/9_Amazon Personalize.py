import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon S3バケットに製品属性データを保存し、Amazon Personalizeデータセットグループにそのバケットを追加する。"
        self.B = "Amazon DynamoDBテーブルに製品属性データを保存し、Amazon Personalizeデータセットグループにそのテーブルを追加する。"
        self.C = "Amazon Relational Database Service(RDS)インスタンスに製品属性データを保存し、Amazon PersonalizeデータセットグループにそのRDSインスタンスを追加する。"
        self.D = "Amazon Redshiftデータウェアハウスに製品属性データを保存し、Amazon Personalizeデータセットグループにそのデータウェアハウスを追加する。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>9. Amazon Personalize</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Personalize_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題９")
st.write(
    """
    小売業者は、Amazon Personalizeを使用して顧客にパーソナライズされた商品レコメンデーションシステムを提供しています。  
    レコメンデーションの精度を向上させるために、小売業者は顧客の行動データに加えて、製品の属性データも活用したいと考えています。  
    この要件を満たすために、小売業者はどのようなアクションを実行する必要がありますか？  
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
            Amazon Personalizeは、Amazon S3バケットに保存されたデータセットを使用することができます。  
            製品属性データは、CSV 形式などの構造化データ形式で保存する必要があります。\n
            ・選択肢Bは不適切です。  
            Amazon DynamoDBは、キーバリューストアであり、ドキュメントや関係データの保存には適していません。  
            製品属性データは複数の属性を持つ複雑なデータ構造であるため、DynamoDBには適していません。\n
            ・選択肢Cは不適切です。  
            Amazon RDSは、リレーショナルデータベースサービスであり、スキーマ定義が必要です。  
            製品属性データの構造が頻繁に変更される場合、RDSは適していません。\n
            ・選択肢Dは不適切です。  
            Amazon Redshiftは、データウェアハウスサービスであり、大量のデータを分析するために使用されます。\n
        """
    )
