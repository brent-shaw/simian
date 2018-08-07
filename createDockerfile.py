base_image = 'python:2.7'
working_dir = '/app'
installs = 'pip install -r requirements.txt'
exposed_port = '502'
scripy_interpret = 'python'
script_file = 'client.py'

dockerfile_lines = ['FROM '+base_image+'\n',
                    'WORKDIR '+working_dir+'\n',
                    'ADD . '+working_dir+'\n',
                    'RUN '+installs+'\n',
                    'EXPOSE '+exposed_port+'\n',
                    'CMD ["'+scripy_interpret+'", "'+script_file+'"]']

def createFileName(base, port, script):
    filename = []
    filename += base.split(':')[0]
    filename += '_'
    filename += port
    filename += script.split('.')[0]

def createDockerfile(contents):
    with open('Dockerfile', 'w') as the_file:
        for line in contents:
            the_file.write(line)

def createRequirementsFile(reqs):
    with open('Dockerfile', 'w') as the_file:
        for req in reqs:
            the_file.write(req)

createDockerfile(dockerfile_lines)
