import numpy as np


class Norm:
    def __init__(self, x, norm='batch'):
        self.x = x
        self.norm = norm

    def fit(self):

        if self.norm == 'batch':
            return self.batch_norm()
        elif self.norm == 'layer':
            return self.layer_norm()

    def transform(self):
        x = self.x
        m, s = self.fit()
        return (x - m) / s

    def fit_transform(self):
        x = self.x
        m, s = self.fit(norm=self.norm)
        return (x - m) / s

    def batch_norm(self):
        x = self.x
        m = x.mean(axis=0)
        s = x.std(axis=0)
        return m, s

    def layer_norm(self):
        x = self.x
        m = x.mean(axis=1)
        s = x.std(axis=1)
        return m, s


x = np.random.rand(10, 2)
norm = Norm(x)
x = norm.fit_transform(norm='layer')

