def ogip_dictionary_image():
    """
    for a given OGIP file type of image,
    returns a dictionary giving the keywords recommended or required for the image to be a useful/valid OGIP image
    An asterisk (*) as the final character of a keyword indicates that the keyword root can have multiple values,
    for example: MJDREF (MJDREFI + MJDREFF), E_MIN1...E_MINn, etc
    Other Special Characters:
        a "+" is used if values are tied - if one appears the others need to appear ("MJDREFI + MJDREFF")
        a "|" separates names which can be used as alternates ("MJDREF | MJDREFI + MJDREFF")
        Square brackets "[ ]" mark required keyword values "HDUCLASS[OGIP]"

    @param extname:
    @return:
    """
    """
    this function returns the  required and optional keywords and columns
    as defined by
    The FITS IMAGE Extension
        http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=1994A%26AS..105...53P&db_key=AST&high=3db47576cf06148
    Representations of World Coordinates in FITS
        http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=2002A%26A...395.1061G&db_key=AST&high=3db47576cf06933
    Representations of Celestial Coordinates in FITS
        http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=2002A%26A...395.1077C&db_key=AST&high=3db47576cf06933
    """
    global status
    global REPORT

    """
    FOR A FITS IMAGE HEADER:
    """
    """
    Define REQUIRED Keywords for SPECTRUM TABLE
    """

    """
    Define recommended Keywords
    """
    optkeys = ['TELESCOP', 'INSTRUME']
    optkeys.append('FILTER')
    optkeys.append('EXPOSURE')
    optkeys.append('HDUCLASS[OGIP]')  # OGIP is the allowed keyword value
    optkeys.append('HDUCLAS1[IMAGE]')  # IMAGE is the allowed keyword value
    #
    # HDUCLAS3 = PREDICTED can be used only if HDUCLAS2 = PRF, etc for TOTAL AND NET
    #
    optkeys.append('HDUCLAS2[TOTAL|NET|EXPOSURE|DETMAP|BKG|GENERIC|PRF (HDUCLAS3[PREDICTED|TOTAL|NET])| VIGNETTING]')

    optkeys = ['DETNAM']
    optkeys.append('RA-OBJ')
    optkeys.append('DEC-OBJ')
    optkeys.append('DATE-OBS')
    optkeys.append('DATE-END')
    optkeys.append('TIME-OBS') # time-obs can be included in date-obs
    optkeys.append('TIME-END') # time-end can be included in date-end
    optkeys.append('CREATOR')
    optkeys.append('ONTIME')
    optkeys.append('TIMEZERO|TIMEZERI+TIMEZERF')  # can be given as single keyword or integer + fraction; either ok
    optkeys.append('TSTART|TSTARTI+TSTARTF')  # can be given as single keyword or integer + fraction; either ok
    optkeys.append('TSTOP|TSTOPI+TSTOPF')  # can be given as single keyword or integer + fraction; either ok
    optkeys.append('TIMESYS')
    optkeys.append('TIMEUNIT')
    optkeys.append('TIMEREF')

    optkeys.append('OBJECT')
    optkeys.append('AUTHOR')



    image = {'KEYWORDS':{'REQUIRED':reqkeys,'RECOMMENDED':optkeys}, 'COLUMNS':{'REQUIRED':reqcols,'RECOMMENDED':optcols}}

    """
    FOR GTI TABLE (OPTIONAL)
    """
    """
    Define Required Keywords FOR GTI TABLE
    """
    reqkeys = ['TELESCOP', 'INSTRUME']
    """
    Define optional Keywords
    """
    optkeys = ['DETNAM', 'FILTER']
    optkeys.append('FILTER')
    optkeys.append('RA*')
    optkeys.append('DEC*')
    optkeys.append('TIMEZERO|TIMEZERI+TIMEZERF')  # can be given as single keyword or integer + fraction; either ok
    optkeys.append('TSTART|TSTARTI+TSTARTF')  # can be given as single keyword or integer + fraction; either ok
    optkeys.append('TSTOP|TSTOPI+TSTARTF')  # can be given as single keyword or integer + fraction; either ok
    optkeys.append('TIMESYS')
    optkeys.append('TIMEUNIT')
    optkeys = ['DATE-OBS']
    optkeys.append('DATE-END')
    optkeys.append('ONTIME')
    optkeys=['HDUCLASS[OGIP]']
    optkeys.append('HDUCLAS1[GTI]')

    """
    Define Required Columns
    """
    reqcols = ['START', 'STOP']
    """
    Define Optional Columns
    """
    optcols = ['TIMEDEL']

    gti={'KEYWORDS':{'REQUIRED':reqkeys,'RECOMMENDED':optkeys}, 'COLUMNS':{'REQUIRED':reqcols,'RECOMMENDED':optcols}}

    extns={'REQUIRED':['IMAGE'], 'OPTIONAL':['GTI']}
    #
    # create structure for IMAGE file
    #
    ogip = {'EXTENSIONS':extns, 
            'IMAGE':image,
            'GTI':gti,
            'REFERENCE':'FITS Support office',
            'REFURL':'http://fits.gsfc.nasa.gov/fits_documentation.html',
            'REFTITLE':'FITS Image Extensions and Coordinate Systems'}
    return ogip


