import epidoc
import geodesy


# TODO test with 057-059
# dateline text from parsing EpiDocXML
epidoc_fname = "canonical-latinLit/data/phi0474/phi056/phi0474.phi056.perseus-lat1.xml"
parser = epidoc.EpiDocXMLParser(epidoc_fname)
# get a dictionary mapping known locations to lat/long
geodetic_fname = "input/loc_to_geodetic.csv"
loc_to_geodetic = geodesy.loc_to_geodetic(geodetic_fname)
