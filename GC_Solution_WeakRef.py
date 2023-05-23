#weakref 사용
#Reference Count를 늘리지 않는 Reference 방법.
#Cyclic Reference를 피할 수 있음
import weakref


class wf:

  def __init__(self):
    self.data = 1


#서로 참조
a = wf()
b = a

a = None
print(b)  #b는 여전히 a를 참조하고 있음

a = wf()
b = weakref.ref(a)  #a를 weakref로 참조
a = None  #a삭제
print(b)  #dead로 b가 더 이상 참조하지 않음을 알 수 있음
