import os
from datetime import datetime

# Defina sua data de nascimento
birth_date = datetime(2005, 8, 15)

# Calcule a idade
today = datetime.today()
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Atualize o README.md
with open('README.md', 'r') as file:
    content = file.read()

# Substitua a idade no conteúdo
new_content = content.replace(f'tenho {age - 1} anos', f'tenho {age} anos')

# Escreva de volta no README.md
with open('README.md', 'w') as file:
    file.write(new_content)
