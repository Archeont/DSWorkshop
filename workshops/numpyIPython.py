import numpy as np
from timeit import timeit


arr = np.random.randn(1000000)
# indexing
# agregate functions

timeit("arr.max()", setup="import numpy as np; arr=np.random.randn(1000000)", number=1000)
timeit("max(lista)", setup="import numpy as np; arr=np.random.randn(1000000); lista = list(arr)", number=1000)

# vectorization

timeit("arr = arr + 5", setup="import numpy as np; arr=np.random.randn(1000000)", number=10)
timeit("lista = [x + 5 for x in lista]", setup="import numpy as np; arr=np.random.randn(1000000); lista = list(arr)", number=10)

# boolean indexing
arr[np.logical_and((arr > 2) , (arr < 3))]
arr[(arr > 2) & (arr < 3)]