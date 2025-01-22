from typing import NewType

UserId = NewType('UserId', int)

id1 = UserId(1234)
id2 = UserId(5678)

print(id1 + id2) # um int