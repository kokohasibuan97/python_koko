data = {
    'name': 'Mikasa Ackerman',
}
print(data)

data = {
    **data,'occupation':'Paradise Survey Corps',
}
print(data)

data = {
    'id':'U0001'
    **data,
    'gender':'female'
}
print(data)