#!/usr/bin/env python3

import pandas
import numpy


mean_martian_radius = 3389.5 # Mean radius of the planet Mars in [km]


# TODO: use me
def calculate_bins(data_set, variable, user_bins, user_labels, new_variable):
    # Calculate the latitude bins and include them in the craters data-set
    data_set = pandas.cut(data_set[variable], user_bins, labels=user_labels)
    data_set[new_variable] = pandas.cut(data_set[variable], user_bins, labels=user_labels)


def print_delimiter(ch='#', count=40):
    print('')
    print(count * (ch + ' '))
    print('')


def calculate_surface_10angles(radius):
    '''
    https://en.wikipedia.org/wiki/Spherical_cap
    '''

    angles = [10, 20, 30, 40, 50, 60, 70, 80, 90] # in degrees
    angles = map(lambda x: (numpy.pi*x)/180, angles) # in radians
    areas = []

    for angle in angles:
        area = 2*numpy.pi*radius*radius*(1 - numpy.cos(angle)) # calculate the area
        area -= sum(areas) # correct area so it corresponds only to the 10 degree ring
        areas.append(area) # add the area to the list

    return areas


if __name__ == '__main__':
    print_delimiter()
    print('Study of the distribution of craters over the Martian surface - Assignment 3')
    print_delimiter()


    craters = pandas.read_csv('marscrater_pds.csv', low_memory=False) # load the data from the csv file

    # Filter the raw data and select only the colums that are relevant for the study.
    craters = craters.filter(['CRATER_ID', 'CRATER_NAME', 'LATITUDE_CIRCLE_IMAGE', 'LONGITUDE_CIRCLE_IMAGE', 'DIAM_CIRCLE_IMAGE'])

    # Filter the craters that have diameter larger than 200km. They are relatively small group and won't be taken into account in the study.
    craters = craters[(craters['DIAM_CIRCLE_IMAGE'] <= 200)]

    # Print some general info about the crater data
    print('The number of observations is {0} and the number of variables is {1}.'.format(len(craters), len(craters.columns)))
    print_delimiter()


    # This part of the code examines the latitude variable.
    latitude_bins = [-90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90,] # define the latitude bins

    # Define the corresponding latitude labels.
    latitude_labels = [ '-90 < latitude <= -80',
                        '-80 < latitude <= -70',
                        '-70 < latitude <= -60',
                        '-60 < latitude <= -50',
                        '-50 < latitude <= -40',
                        '-40 < latitude <= -30',
                        '-30 < latitude <= -20',
                        '-20 < latitude <= -10',
                        '-10 < latitude <=   0',
                        '  0 < latitude <=  10',
                        ' 10 < latitude <=  20',
                        ' 20 < latitude <=  30',
                        ' 30 < latitude <=  40',
                        ' 40 < latitude <=  50',
                        ' 50 < latitude <=  60',
                        ' 60 < latitude <=  70',
                        ' 70 < latitude <=  80',
                        ' 80 < latitude <=  90',
                      ]

    # Calculate the latitude bins and include them in the craters data-set
    latitude_craters = pandas.cut(craters['LATITUDE_CIRCLE_IMAGE'], latitude_bins, labels=latitude_labels)
    craters['latitude_categories'] = pandas.cut(craters['LATITUDE_CIRCLE_IMAGE'], latitude_bins, labels=latitude_labels)

    del latitude_bins, latitude_labels, latitude_craters # delete the unnecessary variables

    print('Martian craters latitude frequency distribution [COUNTS]. The craters are organized into bins. Each bin includes the count of craters from 10° angle:', end='\n')
    print(craters['latitude_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters latitude frequency distribution [PERCENTAGE]. The craters are organized into bins. Each bin includes craters percentage from 10° angle:', end='\n')
    print(100 * (craters['latitude_categories'].value_counts(sort=False, normalize=True)), end='\n')
    print_delimiter()



    # This part of the code examines the longitude variable.
    longitude_bins = [-180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180] # define the longitude bins

    # Define the corresponding longitude labels.
    longitude_labels = [ '-180 < longitude <= -160',
                         '-160 < longitude <= -140',
                         '-140 < longitude <= -120',
                         '-120 < longitude <= -100',
                         '-100 < longitude <=  -80',
                         ' -80 < longitude <=  -60',
                         ' -60 < longitude <=  -40',
                         ' -40 < longitude <=  -20',
                         ' -20 < longitude <=    0',
                         '   0 < longitude <=   20',
                         '  20 < longitude <=   40',
                         '  40 < longitude <=   60',
                         '  60 < longitude <=   80',
                         '  80 < longitude <=  100',
                         ' 100 < longitude <=  120',
                         ' 120 < longitude <=  140',
                         ' 140 < longitude <=  160',
                         ' 160 < longitude <=  180',
                       ]

    # Calculate the longitude bins and include them in the crater data-set
    longitude_craters = pandas.cut(craters['LONGITUDE_CIRCLE_IMAGE'], longitude_bins, labels=longitude_labels)
    craters['longitude_categories'] = pandas.cut(craters['LONGITUDE_CIRCLE_IMAGE'], longitude_bins, labels=longitude_labels)

    del longitude_bins, longitude_labels, longitude_craters # delete the unnecessary variables

    print('Martian craters longitude frequency distribution [COUNTS]. The craters are organized into bins. Each bin includes the count of craters from 20° angle:', end='\n')
    print(craters['longitude_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters longitude frequency distribution [PERCENTAGE]. The craters are organized into bins. Each bin includes craters percentage from 20° angle:', end='\n')
    print(100 * (craters['longitude_categories'].value_counts(sort=False, normalize=True)), end='\n')
    print_delimiter()



    # This part of the code examines the diameter variable.
    diameter_bins = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] # define the diameter bins

    # Define the corresponding diameter labels.
    diameter_labels = [ '  1 < diameter <=  10',
                        ' 10 < diameter <=  20',
                        ' 20 < diameter <=  30',
                        ' 30 < diameter <=  40',
                        ' 40 < diameter <=  50',
                        ' 50 < diameter <=  60',
                        ' 60 < diameter <=  70',
                        ' 70 < diameter <=  80',
                        ' 80 < diameter <=  90',
                        ' 90 < diameter <= 100',
                        '100 < diameter <= 110',
                        '110 < diameter <= 120',
                        '120 < diameter <= 130',
                        '130 < diameter <= 140',
                        '140 < diameter <= 150',
                        '150 < diameter <= 160',
                        '160 < diameter <= 170',
                        '170 < diameter <= 180',
                        '180 < diameter <= 190',
                        '190 < diameter <= 200',
                      ]

    # Calculate the diameter bins and include them in the crater data-set
    diameter_craters = pandas.cut(craters['DIAM_CIRCLE_IMAGE'], diameter_bins, labels=diameter_labels)
    craters['diameter_categories'] = pandas.cut(craters['DIAM_CIRCLE_IMAGE'], diameter_bins, labels=diameter_labels)

    del diameter_bins, diameter_labels, diameter_craters # delete the unnecessary variables

    print('Martian craters diameter frequency distribution [COUNTS]. The craters are organized into bins:')
    print(craters['diameter_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters diameter frequency distribution [PERCENTAGE]. The craters are organized into bins:', end='\n')
    print(100 * (craters['diameter_categories'].value_counts(sort=False, normalize=True)), end='\n')
    print_delimiter()


    # study the normalized craters' distribution over the Martian sufrace
    craters_distribution = pandas.DataFrame(craters['latitude_categories'].value_counts(sort=False)) # create a new DataFrame that includes the number of craters in every latitude category
    craters_distribution.columns = ['number_of_craters'] # set better name for the column

    surface_10angles = calculate_surface_10angles(mean_martian_radius) # these are the surfaces for the latitude categories for the Northern Hemisphere
    surface_10angles.extend(reversed(surface_10angles)) # add the surfaces for the latitude categories for the Southern Hemisphere as well

    craters_distribution['surface_area'] = surface_10angles # add the surfece areas for the individual latitude categories

    del surface_10angles # delete the unnecessary variables

    # calculate the normalized crater distribution (number of acaters per square kilometer)
    craters_distribution['number_of_craters_normalized'] = craters_distribution['number_of_craters'] / craters_distribution['surface_area']

    print('''Martian craters latitude distribution. The index of the DataFrame is the latitude category.
             The column "number_of_craters" shows the total number of craters per latitude category.
             The column "surface_area" shows the area [km^2] of the corresponding latitude category.
             The column "number_of_craters_normalized" shows the number of craters per square kilometer for each latitude category.''')
    print(craters_distribution)
    print_delimiter()

