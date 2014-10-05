''' Constants for shared use
'''
from troposphere.constants import AP_NORTHEAST_1, AP_NORTHEAST_1A, \
    AP_NORTHEAST_1B, AP_NORTHEAST_1C, AP_SOUTHEAST_1, AP_SOUTHEAST_1A, \
    AP_SOUTHEAST_1B, AP_SOUTHEAST_2, AP_SOUTHEAST_2A, AP_SOUTHEAST_2B,\
    EU_WEST_1, EU_WEST_1A, EU_WEST_1B, EU_WEST_1C, SA_EAST_1, SA_EAST_1A, \
    SA_EAST_1B, US_EAST_1, US_EAST_1A, US_EAST_1B, US_EAST_1C, US_EAST_1D, \
    US_EAST_1E, US_WEST_1, US_WEST_1A, US_WEST_1B, US_WEST_1C, US_WEST_2, \
    US_WEST_2A, US_WEST_2B, US_WEST_2C

REGION_AZ_MAP = 'RegionAZMap'

REGION_AZ_MAPPINGS = {
            AP_NORTHEAST_1: {
                'A': AP_NORTHEAST_1A,
                'B': AP_NORTHEAST_1B,
                'C': AP_NORTHEAST_1C
            },
            AP_SOUTHEAST_1: {
                'A': AP_SOUTHEAST_1A,
                'B': AP_SOUTHEAST_1B
            },
            AP_SOUTHEAST_2: {
                'A': AP_SOUTHEAST_2A,
                'B': AP_SOUTHEAST_2B
            },
            EU_WEST_1: {
                'A': EU_WEST_1A,
                'B': EU_WEST_1B,
                'C': EU_WEST_1C,
            },
            SA_EAST_1: {
                'A': SA_EAST_1A,
                'B': SA_EAST_1B
            },
            US_EAST_1: {
                'A': US_EAST_1A,
                'B': US_EAST_1B,
                'C': US_EAST_1C,
                'D': US_EAST_1D,
                'E': US_EAST_1E
            },
            US_WEST_1: {
                'A': US_WEST_1A,
                'B': US_WEST_1B,
                'C': US_WEST_1C
            },
            US_WEST_2: {
                'A': US_WEST_2A,
                'B': US_WEST_2B,
                'C': US_WEST_2C
            }
        }