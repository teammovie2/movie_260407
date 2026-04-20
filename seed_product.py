from pybo import db
from pybo.models import Product


def seed_products():
    products = [
        {"id": 1, "Productname": "일반 관람권(2D)", "Producttype": "티켓", "Productprice": 18000, "stock": 1000,
         "Productdescription": "일반 관람권(2D) 1매", "Productimage_url": "/static/img/redticket.png", "Productlimit": 10, "Productdate": "온라인관람권 24 개월"},

        {"id": 2, "Productname": "VIP 관람권", "Producttype": "티켓", "Productprice": 50000, "stock": 1000,
         "Productdescription": "VIP 관람권 1매", "Productimage_url": "/static/img/blackticket.png", "Productlimit": 2, "Productdate": "온라인관람권 24 개월"},

        {"id": 3, "Productname": "BEST COMBO 교환권", "Producttype": "스낵", "Productprice": 14500, "stock": 1000,
         "Productdescription": "반반콤보 or 싱글스낵콤보 중 택 1", "Productimage_url": "/static/img/BEST COMBO 교환권.png", "Productlimit": 10, "Productdate": "스위트샵 상품권 24 개월"},

        {"id": 4, "Productname": "SINGLE COMBO 교환권", "Producttype": "스낵", "Productprice": 10000, "stock": 1000,
         "Productdescription": "싱글커피/내맘대로콤보 중 택 1", "Productimage_url": "/static/img/SINGLE COMBO 교환권.png", "Productlimit": 10, "Productdate": "스위트샵 상품권 24 개월"},

        {"id": 5, "Productname": "SNACKS 교환권", "Producttype": "스낵", "Productprice": 6500, "stock": 1000,
         "Productdescription": "콜팝치킨/소떡소떡(뿌링클, 맵스터) 중 택 1", "Productimage_url": "/static/img/SNACKS 교환권.png", "Productlimit": 10, "Productdate": "스위트샵 상품권 24 개월"},

        {"id": 6, "Productname": "팝콘(L) 교환권", "Producttype": "스낵", "Productprice": 8500, "stock": 1000,
         "Productdescription": "고소/달달한 빅사이즈 팝콘", "Productimage_url": "/static/img/popcorn_L.png", "Productlimit": 10, "Productdate": "스위트샵 상품권 24 개월"},

        {"id": 7, "Productname": "팝콘(M) 교환권", "Producttype": "스낵", "Productprice": 7500, "stock": 1000,
         "Productdescription": "고소/달달한 기본사이즈 팝콘", "Productimage_url": "/static/img/popcorn_M.png", "Productlimit": 10, "Productdate": "스위트샵 상품권 24 개월"},

        {"id": 8, "Productname": "셀프 탄산 교환권", "Producttype": "스낵", "Productprice": 4000, "stock": 1000,
         "Productdescription": "시원하고 청량감 MAX!", "Productimage_url": "/static/img/drink_L.png", "Productlimit": 10, "Productdate": "스위트샵 상품권 24 개월"},

        {"id": 9, "Productname": "귀멸의 칼날 랜덤 홀로그램 캔뱃지 교환권", "Producttype": "굿즈", "Productprice": 9900, "stock": 1000,
         "Productdescription": "홀로그램 캔뱃지", "Productimage_url": "/static/img/ds_holographic_buttonbadge.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 10, "Productname": "귀멸의 칼날 랜덤 포토캬라 캔뱃지 교환권", "Producttype": "굿즈", "Productprice": 9900, "stock": 1000,
         "Productdescription": "캐릭터 캔뱃지", "Productimage_url": "/static/img/ds_character_buttonbadge.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 11, "Productname": "귀멸의 칼날 랜덤 그래픽 캔뱃지 교환권", "Producttype": "굿즈", "Productprice": 9900, "stock": 1000,
         "Productdescription": "그래픽 캔뱃지", "Productimage_url": "/static/img/ds_graphic_buttonbadge.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},
    
        {"id": 12, "Productname": "진격의 거인 아크릴 예거 키홀더 교환권", "Producttype": "굿즈", "Productprice": 22500, "stock": 1000,
         "Productdescription": "진격의 거인 아크릴 키홀더", "Productimage_url": "/static/img/jin_eren.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 13, "Productname": "진격의 거인 아크릴 미카사 키홀더 교환권", "Producttype": "굿즈", "Productprice": 22500, "stock": 1000,
         "Productdescription": "진격의 거인 VIVID 아크릴 키홀더", "Productimage_url": "/static/img/jin_mikasa.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 14, "Productname": "진격의 거인 아크릴 리바이 키홀더 교환권", "Producttype": "굿즈", "Productprice": 22500, "stock": 1000,
         "Productdescription": "진격의 거인 VIVID 아크릴 키홀더", "Productimage_url": "/static/img/jin_levi.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 15, "Productname": "체인소 맨 덴지 아크릴스탠드 교환권", "Producttype": "굿즈", "Productprice": 30000, "stock": 1000,
         "Productdescription": "체인소 맨 아크릴스탠드", "Productimage_url": "/static/img/chain_denji.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 16, "Productname": "체인소 맨 마키마 아크릴스탠드 교환권", "Producttype": "굿즈", "Productprice": 30000, "stock": 1000,
         "Productdescription": "체인소 맨 아크릴스탠드", "Productimage_url": "/static/img/chain_makima.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"},

        {"id": 17, "Productname": "체인소 맨 레제 아크릴스탠드 교환권", "Producttype": "굿즈", "Productprice": 30000, "stock": 1000,
         "Productdescription": "체인소 맨 아크릴스탠드", "Productimage_url": "/static/img/chain_reje.jpg", "Productlimit": 3, "Productdate": "스위트샵 상품권 3 개월"}
    ]

    for p in products:
        db.session.add(Product(**p))

    db.session.commit()