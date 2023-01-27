person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
         }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if("skills" in person):
    mid = len(person["skills"]) // 2
    print(person["skills"][mid])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if(("skills" in person) and ("Python" in person["skills"])):
    print(person["skills"])

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!
frontend = ["JavaScript", "React"]
backend = ["Node", "Python", "MongoDB"]
fullstack= ["React", "Node", "MongoDB"]
msg = "unknown title"
if("skills" in person):
    skills = person["skills"] 
    if all(skill in skills for skill in frontend):
        msg = 'He is a front end developer'
    if all(skill in skills for skill in backend):    
        msg = 'He is a backend developer'
    if all(skill in skills for skill in fullstack):   
       msg = 'He is a fullstack developer'
    print(msg)  
else:
    print("No skills found")    
