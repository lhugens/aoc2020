import numpy as np

numbers = np.loadtxt("input.txt").astype(int)

tensor = numbers[:,None] + numbers

where = np.where(tensor == 2020)[0]

print(numbers[where[0]]*numbers[where[1]])

tensor3 = numbers[:, None, None] + tensor

indices = np.array(np.where(tensor3[:, :, :] == 2020)).transpose()

i, j, k = indices[0]

print(numbers[i]*numbers[j]*numbers[k])


