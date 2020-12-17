#!/usr/bin/python3
# this is a smith configuration file

# override the default folders
# DOCDIR = ["documentation", "web"]

# set the font name and description
APPNAME = 'JapaSansOriya'
FAMILY = APPNAME
DESC_SHORT = "Font for the Oriya script"

# Get version and authorship information from Regular UFO (canonical metadata); must be first function call:
getufoinfo('source/masters/' + FAMILY + '-Thin' + '.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
# ftmlTest('tools/ftml-smith.xsl')

generated = 'generated/'

# set up the build parameters from the designspace file(s)
dspace = 'Design'
dspace = ''

designspace('source/' + FAMILY + dspace + '.designspace',
    target = process('${DS:FILENAME_BASE}.ttf',
        cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/instances/${DS:FILENAME_BASE}.ufo'])
    ),
    opentype = fea(generated + '${DS:FILENAME_BASE}.fea',
        mapfile = generated + '${DS:FILENAME_BASE}.map',
        master = 'source/opentype/master.feax',
        make_params = '',
        params = '',
        ),
    ap = 'generated/' + '${DS:FILENAME_BASE}.xml',
    # woff = woff('web/${DS:FILENAME_BASE}.woff', params='-v ' + VERSION + ' -m ../source/${DS:FAMILYNAME}-WOFF-metadata.xml'),
    script = ['ory2'],
    pdf = fret(params='-oi')
)
