
from datetime import datetime
from pybo import create_app, db
from pybo.models import Faq


def insert_test_data(n=10):
    """테스트용 질문 데이터 n개 생성"""
    app = create_app()  # Flask 컨텍스트 가 필요
    with app.app_context():
        kinds = ["영화관 이용", "할인혜택", "멤버십", "관람권", "예매", "영화관 이용", "할인혜택", "멤버십", "관람권", "예매"]
        questions = ['굿즈 상영기준은 어떻게 되나요?', '청소년 할인 혜택 기준은 어떻게 되나요?', '포인트 소멸은 어떻게 이뤄지나요?', '특별관 전용 관람권이 따로 있나요?', '영화 관람시간대 중 조조는 언제인가요?', '굿즈 상영기준은 어떻게 되나요?', '청소년 할인 혜택 기준은 어떻게 되나요?', '포인트 소멸은 어떻게 이뤄지나요?', '특별관 전용 관람권이 따로 있나요?', '영화 관람시간대 중 조조는 언제인가요?']

        for i in range(n):
            q = Faq(
                kind=kinds[i],
                question = questions[i],
                create_date = datetime.now()
            )
            db.session.add(q)
        db.session.commit()
        print(f"{n}개의 테스트 데이터가 생성되었습니다.")

if __name__ == '__main__':
    insert_test_data()