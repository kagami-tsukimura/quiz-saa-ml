import streamlit as st


class Choice:
    def __init__(self):
        self.A = "AWS Lambda関数を作成し、Kendraを使用して特定のキーワードに対する検索をトリガーします。Lambda関数がKendraの結果を取得し、アプリケーションに結果を返します。"
        self.B = "Kendraの検索エンドポイントを直接アプリケーションに統合し、ユーザーがアプリケーション内でキーワード検索を行えるようにします。"
        self.C = "Kendraを使用してカスタム検索アプリケーションを作成し、検索結果をアプリケーション内で表示します。"
        self.D = "AWS CloudFrontを使用してKendraの検索結果をキャッシュし、アプリケーションからの検索リクエストに対して高速な応答を提供します。"
        self.choices = [self.A, self.B, self.C, self.D]

    def get_choices(self):
        return self.choices


st.markdown("<h1 style='text-align: center;'>AWS SAA</h1>", unsafe_allow_html=True)
col1, col2 = st.columns((8, 2))

col1.write("")
col1.markdown(
    "<h2 style='text-align: center;'>8. Amazon Kendra</h2>", unsafe_allow_html=True
)
col2.image("images/Arch_Amazon-Kendra_64.png")

_ = [st.write("") for _ in range(5)]

choice = Choice()

st.write("### 問題８")
st.write(
    """
    ある企業は、大量のドキュメントと情報が格納されたナレッジベースを持っています。  
    ユーザーがこのナレッジベース内の情報を簡単かつ迅速に検索できるようにしたいです。  
    企業では、特定のキーワードに関連する文書を検索するためのカスタムアプリケーションを開発しています。  
    ユーザーがアプリケーションを使用してキーワードを検索すると、関連する文書が表示されるようにしたいと考えています。  
    これらの要件を満たし、運用オーバーヘッドを最小限に抑えたソリューションはどれでしょうか？  
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
            Kendraを使用してカスタム検索アプリケーションを作成することが適切です。  
            カスタムアプリケーションを作成することでユーザー体験を完全に制御でき、必要に応じて検索結果の整形やカスタマイズが可能です。  
            直接Kendraを呼び出し、Lambda関数を介さないことで、冗長性が減りパフォーマンスが向上します。\n
            ・選択肢Aは不適切です。  
            Lambda関数を使用して検索をトリガーすることは可能ですが、ユーザーがアプリケーションに検索ワードを入力するごとにLambda関数が呼び出されるため、冗長であり効率が低いです。  
            また、Lambda関数はKendraの検索結果をアプリケーションに返すため、Lambda関数の実行時間やコストが発生します。\n
            ・選択肢Bは不適切です。  
            Kendraの検索結果を直接アプリケーションに統合することは可能ですが、ユーザー体験のカスタマイズに柔軟性が制限されます。
            アプリケーションが直接Kendraにアクセスする場合、検索結果の整形やフィルタリングなどをカスタマイズに制限が発生します。\n
            ・選択肢Dは不適切です。  
            AWS CloudFrontはコンテンツのキャッシュと高速化に使用されます。  
            Kendraの検索結果は動的であり、検索キーワードによって結果が変わるためキャッシュが有効に機能しません。  
            また、直接Kendraを呼び出せるため、CloudFrontを経由する必要性はありません。\n
        """
    )
