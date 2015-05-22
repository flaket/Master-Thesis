X_train, X_test, y_train, y_test
    = cross_validation
        .train_test_split(X, y, test_size=0.25, random_state=r.randint(0, len(X)))