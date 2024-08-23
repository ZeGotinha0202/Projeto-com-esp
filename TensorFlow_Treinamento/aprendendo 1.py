import tensorflow as tf

#frase = tf.constant('Ola mundo')

#print(frase.numpy().decode('UTF-8'))
#print(frase)

a = tf.constant(5)
b = tf.constant(3)
c = tf.constant(2)

d = tf.multiply(a,b)
e = tf.add(b,c)
f = tf.subtract(d,e)
g = tf.divide(d,e)

nan = g.numpy()
saida = f.numpy()
print(saida, nan)