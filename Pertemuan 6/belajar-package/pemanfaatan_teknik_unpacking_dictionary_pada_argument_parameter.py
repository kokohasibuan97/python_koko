def show_biography(id,name,occupation,gender):
    print(f"id:{id}")
    print(f"name:{name}")
    print(f"occupation:{occupation}")
    print(f"gender:{gender}")

data1 = {
    'id': 'U0001',
    'gender': 'female',
    'name': 'Mikasa Ackerman',
    'occupation': 'Paradise Survey Corps'
}
show_biography(**data1)

data2 = {
    'gender':'female',
    'name':'Mikasa Ackerman',
    'occupation':'Paradise Survey Corps',
}