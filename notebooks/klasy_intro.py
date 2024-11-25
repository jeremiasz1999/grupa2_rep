# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
class A: 

    static_attr = 7 

    def __init__(self, attr = 50):
        self.attr = attr

    def f(self):
        print('Welcome A')

class B(A):

    def g(self):
        print('Welcome B')

class C(B):

    def __init__(self, attr=50):
        super().__init__(attr)
        print(f'Created object C = {attr}')

    def f(self, x):
        print(f'Hello {x}. Welcome C')

    def h(self):
        print('Welcome C')


# %%
obj_c = C()

# %%
obj_c.__init__()

# %%
obj_c

# %%
obj_c.attr

# %%
obj_c = C(777)

# %%
obj_c.attr

# %%
obj_c.f('Roman')
