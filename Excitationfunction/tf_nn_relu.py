"""tf.nn.relu(features, name = None)
解释：这个函数的作用是计算激活函数relu，即max(features, 0)。
所有负数都会归一化为0，所以的正值保留为原值不变
使用例子："""

import tensorflow as tf

a = tf.constant([-1.0, 2.0])
with tf.Session() as sess:
    b = tf.nn.relu(a)
    print(sess.run(b))
"""输入参数：
  ● features: 一个Tensor。数据类型必须是：float32，float64，int32，int64，uint8，int16，int8。
  ● name: （可选）为这个操作取一个名字。
输出参数：
  ● 一个Tensor，数据类型和features相同。"""
