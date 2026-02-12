from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

from preprocessing import load_and_prepare_data
from model import build_model

(
    X_train_scaled,
    X_val_scaled,
    y_reg_train_log,
    y_reg_val_log,
    y_cls_train,
    y_cls_val,
    scaler,
    class_map,
    X_val,
    y_reg_val,
) = load_and_prepare_data()

model = build_model(X_train_scaled.shape[1])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss={
        "price_output": "mse",
        "class_output": "sparse_categorical_crossentropy"
    },
    loss_weights={
        "price_output": 0.7,
        "class_output": 0.3
    },
    metrics={
        "price_output": ["mae"],
        "class_output": ["accuracy"]
    }
)

early_stop = EarlyStopping(
    monitor="val_price_output_mae",
    patience=15,
    restore_best_weights=True,
    mode="min"
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=5,
    min_lr=1e-6
)

history = model.fit(
    X_train_scaled,
    {
        "price_output": y_reg_train_log,
        "class_output": y_cls_train
    },
    validation_data=(
        X_val_scaled,
        {
            "price_output": y_reg_val_log,
            "class_output": y_cls_val
        }
    ),
    epochs=100,
    batch_size=64,
    callbacks=[early_stop, reduce_lr],
    verbose=1
)

model.save("house_price_multitask.keras")
