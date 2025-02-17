# import theater_module

# theater_module.price(3) # 3명에서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명 조조 할인 가격
# theater_module.price_soldier(5) # 5명 군인인

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# # from
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# # price_soldier(5)

from theater_module import price_soldier as price
price(5) # 군인 할인 가격격