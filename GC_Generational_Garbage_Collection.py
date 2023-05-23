#Generational Garbage Collection
#Cyclic Reference 문제를 해결하기 위한 GC 기법
#GC는 파이썬의 모든 객체를 수집함. 객체의 수가 임계값을 넘을 경우, 즉시 GC를 수행함.
#이때 첫 세대가 시작되고, 생존한 객체는 다음 세대로 넘어감. GC는 총 3개의 세대를 소유하고 있음
#개발자가 임계값을 설정할 수 있음. 개발자가 설정한 임계값을 넘어가기 전까진 모든 객체들이 메모리에 살아있음.
import gc
import ctypes

#수집된 Garbage 개수 표현
print(f"Collected {gc.collect()} objects")


class Object(ctypes.Structure):
  _fields_ = [("refcnt", ctypes.c_long)]


data1 = {}
data2 = {}
data1['_data2'] = data2
data2['_data1'] = data1

print(f"Collected {gc.collect()} objects")

obj_address = id(data1)

del data1, data2
print(f"Collected {gc.collect()} objects")

print(Object.from_address(obj_address).refcnt)

#Generational GC는 Cyclic Reference를 해결할 수는 있으나, 프로그램을 완전히 중지하고 GC를 실행해야 함.
#Generational GC를 많이 수행할수록 프로그램의 성능은 낮아지게 됨.