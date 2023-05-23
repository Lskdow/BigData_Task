#Python에서의 주요 GC 매커니즘
#Python객체의 Reference Count는 객체가 참조될 때마다 증가하고, 참조가 해제될 때 감소한다. 그런 방식으로 Reference Count가 0이 되는 경우, 객체의 메모리 할당이 해제된다.

#Reference Count 확인
import sys

a = 'hello'  #객체를 변수 a에 할당 = 참조 1
sys.getrefcount(a)  #a가 함수에 전달 = 참조 2
#console에 sys.getrefcont(a) 입력할 경우 2 출력

#Cyclic Reference의 경우 memory leak이 발생하게 됨
#두 객체가 서로를 참고할 경우, 하나를 삭제하여도 객체의 카운트가 항상 1이 됨

#아래의 코드가 memory leak이 발생하는 경우의 코드

import ctypes


class Object(ctypes.Structure):
  _fields_ = [("refcnt", ctypes.c_long)]


data1 = {}
data2 = {}
data1['_data2'] = data2
data2['_data1'] = data1

obj_address = id(data1)
print(obj_address)

del data1, data2
print(Object.from_address(obj_address).refcnt)

#del로 객체를 삭제했음에도 reference count가 1이 나옴.
