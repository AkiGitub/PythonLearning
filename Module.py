import package.subPackage1.config as mx
import platform as plt
from package.subPackage1.config import person1

print(mx.getData(2)) #4
print(mx.person1['age']) #36
print(plt.system()) #windows
print(plt.machine()) #AMD64
print(plt.version()) #AMD64
print(plt.python_compiler()) #AMD64

print(person1['name'])
print(dir(mx))
