import theater_module
theater_module.price(3) #3명이서 영화보러 갈때 가격
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv  #원래이름은 기니까 별명
mv.price(2)
mv.price_soldier(3)

from theater_module import * #제일 짧음. 이거 쓰는게 좋겟네
price(3)
price_morning(4)
price_soldier(2)

from theater_module import price, price_morning #내가 필요한 함수만 명시
price(2)
price_morning(4)
price_soldier(2)