# import travel.thai
# trip_to = travel.thai.thaiPakage()
# trip_to.detail()

#하나의 디렉토리에 여러 모듈을 가져다놓은게 패키지

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import * # init에서 __all__ 설정을 해줘야 실행되나? 공개해줘야한다는데
# #trip_to = vietnam.VietnamPackage()
# trip_to = thai.thaiPakage()
# trip_to.detail()

import inspect
import random

from travel import thai
print(inspect.getfile(random)) #이렇게 모듈의 위치 확인 가능
print(inspect.getfile(thai))

