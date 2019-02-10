import os
import subprocess

cwd = os.getcwd()
infile_name = 'in.wav'
outfile_name = 'out.wav'

def generate(source='doremi'):
    with open(infile_name, 'wb') as f:
        subprocess.call([
            'docker','run',
            '-v', '{}:/deploy'.format(cwd),
            '--rm',
            'festival',
            '/usr/bin/text2wave',
            '-mode', 'singing',
            '/deploy/xml/{}.xml'.format(source),
        ], stdout=f)

    subprocess.call(['sox', '--ignore-length',
        infile_name,
        outfile_name,
        'reverb',
    ])

if __name__ == "__main__":
    generate()