import os
import openai
openai.organization = "org-AkUlB4dvZZooqXvZou0iX5ty"
openai.api_key = ("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")
x = openai.Model.list()
print(x)