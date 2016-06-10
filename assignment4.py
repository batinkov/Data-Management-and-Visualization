#!/usr/bin/env python3

import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt


mean_martian_radius = 3389.5 # Mean radius of the planet Mars in [km]


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
    print('Study of the distribution of craters over the Martian surface - Assignment 4')
    print_delimiter()

    # Load the raw data but only select the colums that are relevant for the study.
    craters = pandas.read_csv('marscrater_pds.csv', usecols=['LATITUDE_CIRCLE_IMAGE', 'LONGITUDE_CIRCLE_IMAGE', 'DIAM_CIRCLE_IMAGE'], low_memory=False) # load the data from the csv file

    # Filter the craters that have diameter larger than 200km. They are relatively small group and won't be taken into account in the study.
    craters = craters[(craters['DIAM_CIRCLE_IMAGE'] <= 200)]

    # Print some general info about the crater data
    print('The number of observations is {} and the number of variables is {}.'.format(len(craters), len(craters.columns)))
    print_delimiter()


    # This part of the code examines the latitude variable.
    latitude_bins = [-90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90,] # define the latitude bins

    # Define the corresponding latitude labels.
    latitude_labels = ['-90 to -80', '-80 to -70', '-70 to -60', '-60 to -50', '-50 to -40', '-40 to -30', '-30 to -20', '-20 to -10', '-10 to 0',
                       '0 to 10', '10 to 20', '20 to 30', '30 to 40', '40 to 50', '50 to 60', '60 to 70', '70 to 80', '80 to 90', ]

    # Calculate the latitude bins and include them in the craters data-set
    latitude_craters = pandas.cut(craters['LATITUDE_CIRCLE_IMAGE'], latitude_bins, labels=latitude_labels)
    craters['latitude_categories'] = pandas.cut(craters['LATITUDE_CIRCLE_IMAGE'], latitude_bins, labels=latitude_labels)

    del latitude_bins, latitude_labels, latitude_craters # delete the unnecessary variables

    print('Martian craters latitude frequency distribution [COUNTS]. The craters are organized into bins. Each bin includes the count of craters from 10° angle:', end='\n')
    print(craters['latitude_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters latitude frequency distribution [PERCENTAGE]. The craters are organized into bins. Each bin includes craters percentage from 10° angle:', end='\n')
    print(100 * (craters['latitude_categories'].value_counts(sort=False, normalize=True)), end='\n')

    seaborn.countplot(x='latitude_categories', data=craters, color='#4c72b0')
    plt.xlabel('Latitide categories')
    plt.ylabel('Number of craters per category')
    plt.title('Latitide crater distribution over the Martian surfaces')
    plt.show()

    print_delimiter()



    # This part of the code examines the longitude variable.
    longitude_bins = [-180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180] # define the longitude bins

    # Define the corresponding longitude labels.
    longitude_labels = ['-180 to -160', '-160 to -140', '-140 to -120', '-120 to -100', '-100 to -80', '-80 to -60', '-60 to -40', '-40 to -20', '-20 to 0',
                        '0 to 20', '20 to 40', '40 to 60', '60 to 80', '80 to 100', '100 to 120', '120 to 140', '140 to 160', '160 to 180', ]

    # Calculate the longitude bins and include them in the crater data-set
    longitude_craters = pandas.cut(craters['LONGITUDE_CIRCLE_IMAGE'], longitude_bins, labels=longitude_labels)
    craters['longitude_categories'] = pandas.cut(craters['LONGITUDE_CIRCLE_IMAGE'], longitude_bins, labels=longitude_labels)

    del longitude_bins, longitude_labels, longitude_craters # delete the unnecessary variables

    print('Martian craters longitude frequency distribution [COUNTS]. The craters are organized into bins. Each bin includes the count of craters from 20° angle:', end='\n')
    print(craters['longitude_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters longitude frequency distribution [PERCENTAGE]. The craters are organized into bins. Each bin includes craters percentage from 20° angle:', end='\n')
    print(100 * (craters['longitude_categories'].value_counts(sort=False, normalize=True)), end='\n')

    seaborn.countplot(x='longitude_categories', data=craters, color='#4c72b0')
    plt.xlabel('Longitude categories')
    plt.ylabel('Number of craters per category')
    plt.title('Longitude crater distribution over the Martian surfaces')
    plt.show()

    print_delimiter()



    # This part of the code examines the diameter variable.
    diameter_bins = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] # define the diameter bins

    # Define the corresponding diameter labels.
    diameter_labels = ['1 to 10', '10 to 20', '20 to 30', '30 to 40', '40 to 50', '50 to 60', '60 to 70', '70 to 80', '80 to 90', '90 to 100',
                       '100 to 110', '110 to 120', '120 to 130', '130 to 140', '140 to 150', '150 to 160', '160 to 170', '170 to 180', '180 to 190', '190 to 200', ]

    # Calculate the diameter bins and include them in the crater data-set
    diameter_craters = pandas.cut(craters['DIAM_CIRCLE_IMAGE'], diameter_bins, labels=diameter_labels)
    craters['diameter_categories'] = pandas.cut(craters['DIAM_CIRCLE_IMAGE'], diameter_bins, labels=diameter_labels)

    del diameter_bins, diameter_labels, diameter_craters # delete the unnecessary variables

    print('Martian craters diameter frequency distribution [COUNTS]. The craters are organized into bins:')
    print(craters['diameter_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters diameter frequency distribution [PERCENTAGE]. The craters are organized into bins:', end='\n')
    print(100 * (craters['diameter_categories'].value_counts(sort=False, normalize=True)), end='\n')

    seaborn.countplot(x='diameter_categories', data=craters, color='#4c72b0')
    plt.xlabel('Diameter categories')
    plt.ylabel('Number of craters per category')
    plt.title('Diameter distribution of Martian craters')
    plt.show()

    print_delimiter()


    # This part of the code examines the diameter variable but in a different bin configuration.
    diameter_bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 200] # define the diameter bins

    # Define the corresponding diameter labels.
    diameter_labels = ['1 to 2', '2 to 3', '3 to 4', '4 to 5', '5 to 6', '6 to 7', '7 to 8', '8 to 9', '9 to 10', '10 to 200', ]

    # Calculate the diameter bins and include them in the crater data-set
    diameter_craters = pandas.cut(craters['DIAM_CIRCLE_IMAGE'], diameter_bins, labels=diameter_labels)
    craters['diameter_categories'] = pandas.cut(craters['DIAM_CIRCLE_IMAGE'], diameter_bins, labels=diameter_labels)

    del diameter_bins, diameter_labels, diameter_craters # delete the unnecessary variables

    print('Martian craters diameter frequency distribution [COUNTS]. The craters are organized into bins:')
    print(craters['diameter_categories'].value_counts(sort=False), end='\n\n')

    print('Martian craters diameter frequency distribution [PERCENTAGE]. The craters are organized into bins:', end='\n')
    print(100 * (craters['diameter_categories'].value_counts(sort=False, normalize=True)), end='\n')

    seaborn.countplot(x='diameter_categories', data=craters, color='#4c72b0')
    plt.xlabel('Diameter categories')
    plt.ylabel('Number of craters per category')
    plt.title('Diameter distribution of Martian craters')
    plt.show()

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

    print('''Martian craters latitude distribution normalized per square km.
             The index of the DataFrame is the latitude category.
             The column "number_of_craters" shows the total number of craters per latitude category.
             The column "surface_area" shows the area [km^2] of the corresponding latitude category.
             The column "number_of_craters_normalized" shows the number of craters per square kilometer for each latitude category.
          ''')
    print(craters_distribution)

    craters_distribution['number_of_craters_normalized'].plot(kind='bar')
    plt.xlabel('Latitude categories')
    plt.ylabel('Normalized number of craters (craters per square km)')
    plt.title('Normalized Martian craters latitude distribution')
    plt.show()

    print_delimiter()



    # Study how the crater diameter depends on the latitude
    latitude_groups = craters.groupby('latitude_categories')

    crater_diameter_latitude_distribution = pandas.DataFrame(columns=['observations', 'mean', 'median'])

    for index in craters_distribution.index:
        observations = len(latitude_groups.get_group(index)['DIAM_CIRCLE_IMAGE'])
        mean = latitude_groups.get_group(index)['DIAM_CIRCLE_IMAGE'].mean()
        median = latitude_groups.get_group(index)['DIAM_CIRCLE_IMAGE'].median()
        crater_diameter_latitude_distribution.loc[index] = [observations, mean, median]

    crater_diameter_latitude_distribution['mean'].plot(kind='bar')
    plt.xlabel('Latitude categories')
    plt.ylabel('Mean diameter as a function of the latitude')
    plt.title('Martian craters mean diameter as a function of the latitude')
    plt.show()

    crater_diameter_latitude_distribution['median'].plot(kind='bar')
    plt.xlabel('Latitude categories')
    plt.ylabel('Median diameter as a function of the latitude')
    plt.title('Martian craters median diameter as a function of the latitude')
    plt.show()


    # Study the properties of the crater diameters of the individual latitude categories
    for index in craters_distribution.index:
        print(latitude_groups.get_group(index)['diameter_categories'].describe())
        latitude_groups.get_group(index)['diameter_categories'].value_counts(sort=False).plot('bar')
        plt.xlabel('Latitude group: {}'.format(index))
        plt.ylabel('Number of craters per category')
        plt.title('Martian craters diameter distribution for latitude category {}'.format(index))
        plt.show()

