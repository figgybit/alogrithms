import random


# ret = vector1.vector2
def inner_product(vector1, vector2):
    return sum(vector1[i]*vector2[i] for i in range(0, len(vector1)))

# ret = value*vector1 + vector2
def dot_product_add(value, vector1, vector2):
    return [vector1[i]*value + vector2[i] for i in range(0, len(vector1))]


def cross_product(Ax, Ay, Bx, By, Cx, Cy):
   return (Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax)


def perceptron_train(training_set, label, learning_rate = 1.0):
    num = len(training_set)
    if num == 0:
        raise "the training set is empty"
    if len(label) != num:
        raise "the number of training sample is not the same with labels"
    for sample in training_set:
        sample.append(1)
    dim = len(training_set[0])
    model = [0] * dim
    x = 0
    while True:
        error_count = 0
        for i in range(0, num):
            # print 'ITERATION - {0}'.format(x)
            if label[i]*inner_product(model, training_set[i]) <= 0:
                x += 1
                model = dot_product_add(label[i]*learning_rate, training_set[i], model)
                error_count = error_count + 1
        if error_count == 0:
            return model, x


def perceptron_predict(test_set, model, threshold = 0):
    prediction = []
    for sample in test_set:
        sample.append(1)
        if inner_product(sample, model) > threshold:
            prediction.append(1)
        else:
            prediction.append(-1)
    return prediction



def generate_training_points(N):
   # training_set = [[.3,.3], [.4,.3], [.1,.1], [.2,.1]]
   # label = [1, 1, -1, -1]
   # y = mx + b
   # create a line
   xy1 = (random.uniform(-1, 1), random.uniform(-1, 1))
   xy2 = (random.uniform(-1, 1), random.uniform(-1, 1))
   # y - y1 = m(x - x1)
   x1, y1 = xy1
   x2, y2 = xy2
   m = (y1 - y2) / (x1 - x2)
   # y - y1 = m * (x - x1)
   # y = mx - mx1 + y1
   b = -(m*x1) + y1
   # gather training data
   processing = True
   while processing:
      training_set = []
      label = []
      for x in range(N):
         xy3 = (random.uniform(-1, 1), random.uniform(-1, 1))
         x3, y3 = xy3
         training_set.append([x3,y3])
         cp = cross_product(x1, y1, x2, y2, x3, y3)
         if cp < 0:
            label.append(-1)
         elif cp > 0:
            label.append(1)
      if len(label) == N:
         processing = False
   return (xy1,xy2), training_set, label


def generate_test_points(f, M):
   # test_set = [[.5,.5], [.1,.1]]
   xy1, xy2 = f
   x1, y1 = xy1
   x2, y2 = xy2
   processing = True
   while processing:
      test_set = []
      label = []
      for x in range(M):
         xy3 = (random.uniform(-1, 1), random.uniform(-1, 1))
         x3, y3 = xy3
         test_set.append([x3,y3])
         cp = cross_product(x1, y1, x2, y2, x3, y3)
         if cp < 0:
            label.append(-1)
         elif cp > 0:
            label.append(1)
      if len(label) == M:
         processing = False
   return test_set, label


ites = []
errors = []
for x in range(0, 1000):
   x
   f, training_set, label = generate_training_points(100)
   model, x = perceptron_train(training_set, label)
   ites.append(x)
   test_set, test_label = generate_test_points(f, 1000)
   prediction = perceptron_predict(test_set, model)
   error = 0
   for f, b in zip(test_label, prediction):
      if f != b:
         error += 1
   errors.append(float(error)/float(1000))





sum(ites)/len(ites)
sum(errors)/len(errors)

