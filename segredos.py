import secrets
import string as s
from secrets import SystemRandom as Sr

print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k= 25)))

#fiz igual do curso, muito maneiro
