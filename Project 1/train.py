def lSVM(X=None, y=None, flag=False):
    model = SVC(kernel='linear')
    if flag:
        return model
    else:
        return model.fit(X, y)

# this file is used for training the model
