from jinja2 import Template
from colourterm import tform
import sys

def get_template(filename):
    try:
        with open(filename, 'r') as infile:
            return infile.read()
    except:
        print("\r"+tform("Incorrect template file.", "FAIL"))
        print("Template must adhere to Jinja2 format")
        sys.exit()

#------------------------------------------------------------------------------

def store_script(filename, script):
    with open(filename, 'w') as outfile:
        outfile.write(script)

#------------------------------------------------------------------------------

def startup(config):
    print(tform("Starting program",'HEADER'))
    print("Fetching template")
    template = get_template(config)
    print(tform("Program running",'OKGREEN'))

    return template

#------------------------------------------------------------------------------

def shutdown(logs):
    print(tform("Halting program",'WARNING'))

    #store_log('tank_sim.log', logs)

    print(tform("Program ended", 'OKGREEN'))


#------------------------------------------------------------------------------

def main():
    if(len(sys.argv) < 2):
        print("\r"+tform("Incorrect usage.", "FAIL"))
        print("eg: sim.py <script_template>")
        sys.exit()

    templateName = str(sys.argv[1])

    pyPlate = startup(templateName)

    args = {'cycleCount': 100000,
            'tankSize': 1000
            }

    try:
        print("- Applying template")
        t = Template(pyPlate)
        script = t.render(args)
        print("- ...")
        print("- Success")
    except:
        print("! Templating failed")

    store_script("test.py", script)

    shutdown("logs")

#------------------------------------------------------------------------------

main()

#------------------------------------------------------------------------------