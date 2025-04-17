#!/usr/bin/python3
# this is a smith configuration file

# command line options
opts = preprocess_args(
    {'opt' : '-r'} # only build the regular weight
)

# override the default folders
DOCDIR = ["documentation", "web"]
TESTDIR = ['tests', '../font-japa-sans-oriya-private/tests']

# set the font name and description
APPNAME = 'JapaSansOriya'
FAMILY = APPNAME
DESC_SHORT = "Font for the Oriya script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Thin' + '.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

generated = 'generated/'

# set up the build parameters from the designspace file(s)
dspace = 'Design'
dspace = ''

cmds = [
    cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/instances/${DS:FILENAME_BASE}.ufo']),
    cmd('gftools fix-nonhinting -q --no-backup ${DEP} ${TGT}'),
    ]

designspace('source/' + FAMILY + dspace + '.designspace',
    target = process('${DS:FILENAME_BASE}.ttf', *cmds),
    instanceparams = '-W',
    instances = ['Japa Sans Oriya Regular'] if '-r' in opts else None,
    opentype = fea(generated + '${DS:FILENAME_BASE}.fea',
        mapfile = generated + '${DS:FILENAME_BASE}.map',
        master = 'source/opentype/master.feax',
        make_params = '',
        params = '',
        ),
    ap = 'generated/' + '${DS:FILENAME_BASE}.xml',
    version = VERSION,
    woff = woff('web/${DS:FILENAME_BASE}',
        metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
    script = ['ory2'],
    pdf = fret(params='-oi')
)
