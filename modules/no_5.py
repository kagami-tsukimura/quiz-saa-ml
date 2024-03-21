import streamlit as st


class Choice:
    def __init__(self):
        self.A = "Amazon RDSでデータベースを構築する。"
        self.B = "Amazon DynamoDBでデータベースを構築する。"
        self.C = "Amazon Auroraでデータベースを構築する。"
        self.D = "Amazon EC2インスタンス上にデータベースを構築する。"
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

    st.write("### 問題５")
    st.write(
        """
        ある企業は、AWS上にデータベースを構築するための要件を確認しています。  
        データベースに利用するサーバーのOS設定を自社が管理することが要件となっています。  
        ソリューションアーキテクトは、最適なデータベースを設定するためのAWSサービスを選択することになりました。  
        この要件を満たすデータベース構築方法はどれでしょうか？  
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
                ・選択肢Dは適切です。  
                自社でOS設定などのデータベースのインフラ環境を管理するためには、EC2インスタンスを使用してDBを構築することが必要です。  
                EC2インスタンスを用いることで、ゲストサーバーOSやデータベースをユーザー側で完全に制御することができます。\n
                ・選択肢AとBとCは不適切です。  
                RDS、DynamoDB、Auroraはマネージド型サービスのため、データベースを構成するOS設定などを自社で管理できません。\n
                なお、AWSが提供するサービスは、マネージド型とアンマネージド型があります。  
                Amazon RDSのようなAWS側がほとんどの運用管理を実施するものがマネージド型です。  
                Amazon EC2のように物理サーバーはAWS側で管理し、ソフトウェア構成以降はユーザー側が運用管理を実施するものがアンマネージド型です。\n
            """
        )
