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

# %% [markdown]
# # Typowanie zmiennych w Pythonie

# %% [markdown]
# ## Typy zmiennych

# %% [markdown]
# ## Typowanie statyczne

# %% [markdown]
# ## Typowanie dynamiczne

# %% [markdown]
# ## Dodawanie typów zmiennych do funkcji

# %%
"""Dodawanie Type Hints do funkcji"""

def headline(text, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


# %%
# ! pip install mypy

# %%
print(headline("python type checking"))

# %%
print(headline("python type checking", align=False))

# %%
print(headline("python type checking", align="center"))

# %%

# %%
"""Ponownie wykorzystujemy funckje headline, ale teraz deklarujemy domyślną wartość drugiej zmiennej jako False"""

def headline_2(text, centred: bool = False) -> str:
    if not centred:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


# %%
print(headline_2("python type checking", centred=True))

# %%

# %% [markdown]
# ## Wady i zalety typowania zmiennych

# %% [markdown]
# ## Type Annotations or Type comments

# %% [markdown]
# # Deck of cards

# %%
