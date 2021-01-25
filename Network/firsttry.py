def sigmoid(x):
    e = 2.7
    return 1 / (1 + pow(e, -x))

num_inputs = 2
inputs     = [1,0]
number_h   = 2

weights_input = [0.45, 0.75, -0.12, 0.13]
weights_hidden = [1.5, -2.3]
ideal = []

E = 0
Emax = 1e-6
for i in range(num_inputs):
    for j in range(num_inputs):
        ideal.append(i ^ j)
#print(ideal)
print("Training: ", "\n")
while True:
    for i in range(number_h):
        for j in range(number_h):
            tmp       = inputs[i] * w1[i]
            h1_input  = h1_input + tmp
            h1_output = sigmoid(h1_input)
            tmp       = inputs[i] *
    print(h1_output)
    break
    