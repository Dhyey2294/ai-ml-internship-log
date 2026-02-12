from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout, BatchNormalization
from tensorflow.keras.regularizers import l2


def build_model(input_dim):
    inputs = Input(shape=(input_dim,))

    x = Dense(256, activation="relu", kernel_regularizer=l2(0.001))(inputs)
    x = BatchNormalization()(x)
    x = Dropout(0.4)(x)

    x = Dense(128, activation="relu", kernel_regularizer=l2(0.001))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.3)(x)

    x = Dense(64, activation="relu", kernel_regularizer=l2(0.001))(x)
    x = BatchNormalization()(x)
    x = Dropout(0.2)(x)

    price_output = Dense(1, name="price_output")(x)
    class_output = Dense(3, activation="softmax", name="class_output")(x)

    return Model(inputs, [price_output, class_output])
