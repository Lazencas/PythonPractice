class thaiPakage:
    def detail(self):
        print("태국 패키지 3박5일")
        print("호놀ㄹ롤롤")

if __name__ == "__main__": #모듈이 작동 가능한지 테스트 할 수 있다.
    print("thai 모듈을 직접 실행합니다")
    print("이 문장은 모듈을 직접 실행할 떄만 실행돼요")
    trip_to = thaiPakage()
    trip_to.detail()
else:
    print("외부에서 호출할때 나오는 구문")
