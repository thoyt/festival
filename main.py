import os
import subprocess

cwd = os.getcwd()
infile_name = 'in.wav'
outfile_name = 'out.wav'

with open(infile_name, 'wb') as f:
    subprocess.call([
        'docker','run',
        '-v', '{}:/deploy'.format(cwd),
#        '-v', '{}/voices:/usr/share/festival/voices/english/'.format(cwd),
        '--rm',
        'festival',
        '/usr/bin/text2wave',
        '-mode', 'singing',
        '/deploy/xml/doremi.xml',
    ], stdout=f)

subprocess.call(['sox', '--ignore-length',
    infile_name,
    outfile_name,
    'reverb',
])
