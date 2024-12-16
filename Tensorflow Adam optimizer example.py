import tensorflow as tf

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu"),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer=optimizer,
            loss="mean_squared_error",
            metrics=["accuracy"])

model.fit(x_train, y_train, epochs=10, batch_siz=32)