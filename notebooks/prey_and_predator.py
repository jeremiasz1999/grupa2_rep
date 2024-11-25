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
    def f(self):
        print('I am in class A')

class B(A):
     def f(self):
         super().f()
         print('I am in class B')
    
class C(A):
     def f(self):
         super().f()
         print('I am in class C')

class D(B, C):
    def f(self):
        super().f()
        print('I am in class D')


# %%
obj_a = A()

# %%
obj_a.f()

# %%
obj_b = B()

# %%
obj_b.f()

# %%
obj_d = D()

# %%
obj_d.f()

# %%
D.__mro__

# %%
