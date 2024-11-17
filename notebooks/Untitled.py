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
# # Typowanie zmiennnych w Pythonie

# %% [markdown]
# ## Typy zmiennych

# %% [markdown]
# ## Typowanie statyczne

# %% [markdown]
# ## Typowanie dynamiczne i duck typing

# %% [markdown]
# ## Dodawanie typów zmiennych do funkcji

# %%
# Dodwanie type hints do funkcji:

# %%
def headline(text: str, align: bool = True) -> str: #text str informuje mypy że zmienna text powinna być typu str, a align typu bool
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


# %%

# %%
print(headline("python type checking"))
print(headline("use mypy","center"))

# %%
print(headline("python type checking"))
print(headline("use mypy", False))

# %% [markdown]
# ## Wady i zalety typowania zmiennych

# %% [markdown]
# ## Type Annotations or Type comments

# %% [markdown]
# # Deck of Cards

# %%
