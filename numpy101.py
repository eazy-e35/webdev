import numpy as np

print(np.zeros(10));

print(np.ones(10));

print(np.ones(10) * 5);

print('------------- -------------------------');

print(np.arange(10,51));

print('------------- -------------------------');

print(np.arange(10,51,2));

mat = np.array([[0,1,2],[3,4,5],[6,7,8]]);

iden = np.eye(3);
print(iden);
print('------------- -------------------------');

print(mat);

print('------------- -------------------------');
print(np.random.rand(2));
