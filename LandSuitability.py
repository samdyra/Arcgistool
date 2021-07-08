# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Created on: 2021-07-08 23:39:44.00000
# Made by Dwiputra Sam Mulia
# Land Suitability Analysis using Fuzzy Logic
# Description: Visit my linkedin profile https://www.linkedin.com/in/dwiputra-sam-mulia-1b9b1a200/ reccommend my skills if u want to :)
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments & Local variables:

Roads_Fuzzy = ""
Distance_from_Roads__Euclidean_distance_ = arcpy.GetParameterAsText(8)
Roads_Membership_type = arcpy.GetParameterAsText(2)
if Roads_Membership_type == '#' or not Roads_Membership_type:
    Roads_Membership_type = "SMALL  #  5" # provide a default value if unspecified

LULC_Fuzzy = ""
LULC__Fixed_values_from_1___0_ = arcpy.GetParameterAsText(12)
LULC_Membership_type = arcpy.GetParameterAsText(15)
if LULC_Membership_type == '#' or not LULC_Membership_type:
    LULC_Membership_type = "LINEAR  #   # " # provide a default value if unspecified

River_Fuzzy = ""
Distance_from_Rivers__Euclidean_Distance_ = arcpy.GetParameterAsText(9)
River_Memership_Type = arcpy.GetParameterAsText(3)
if River_Memership_Type == '#' or not River_Memership_Type:
    River_Memership_Type = "MSSMALL 1 1" # provide a default value if unspecified

Slope_Fuzzy = ""
Slope__Percentage_ = arcpy.GetParameterAsText(10)
Slope_Membership_type = arcpy.GetParameterAsText(4)
if Slope_Membership_type == '#' or not Slope_Membership_type:
    Slope_Membership_type = "SMALL  #  5" # provide a default value if unspecified

SAVI_Fuzzy = ""
SAVI____1___1_ = arcpy.GetParameterAsText(13)
SAVI_Membership_type = arcpy.GetParameterAsText(16)
if SAVI_Membership_type == '#' or not SAVI_Membership_type:
    SAVI_Membership_type = "LARGE  #  5" # provide a default value if unspecified

RainRate_Fuzzy = ""
Rain_Rate__mm_year_ = arcpy.GetParameterAsText(0)
RR_Membership_Type = arcpy.GetParameterAsText(1)
if RR_Membership_Type == '#' or not RR_Membership_Type:
    RR_Membership_Type = "GAUSSIAN  #  0,1" # provide a default value if unspecified

Temperature_Fuzzy = ""
Temperature_C_ = arcpy.GetParameterAsText(11)
Temp_Membership_Type = arcpy.GetParameterAsText(14)
if Temp_Membership_Type == '#' or not Temp_Membership_Type:
    Temp_Membership_Type = "NEAR  #  0,1" # provide a default value if unspecified


Land_Suitability = arcpy.GetParameterAsText(5)
Extent = arcpy.GetParameterAsText(6)
Overlay_type = arcpy.GetParameterAsText(7)
if Overlay_type == '#' or not Overlay_type:
    Overlay_type = "AND" # provide a default value if unspecified


# Process: Fuzzy Membership (4)
arcpy.gp.FuzzyMembership_sa(Distance_from_Roads__Euclidean_distance_, Roads_Fuzzy, Roads_Membership_type, "NONE")

# Process: Fuzzy Membership (2)
arcpy.gp.FuzzyMembership_sa(LULC__Fixed_values_from_1___0_, LULC_Fuzzy, LULC_Membership_type, "NONE")

# Process: Fuzzy Membership (6)
arcpy.gp.FuzzyMembership_sa(Distance_from_Rivers__Euclidean_Distance_, River_Fuzzy, River_Memership_Type, "NONE")

# Process: Fuzzy Membership (7)
arcpy.gp.FuzzyMembership_sa(Slope__Percentage_, Slope_Fuzzy, Slope_Membership_type, "NONE")

# Process: Fuzzy Membership
arcpy.gp.FuzzyMembership_sa(SAVI____1___1_, SAVI_Fuzzy, SAVI_Membership_type, "NONE")

# Process: Fuzzy Membership (3)
arcpy.gp.FuzzyMembership_sa(Rain_Rate__mm_year_, RainRate_Fuzzy, RR_Membership_Type, "NONE")

# Process: Fuzzy Membership (5)
arcpy.gp.FuzzyMembership_sa(Temperature_C_, Temperature_Fuzzy, Temp_Membership_Type, "NONE")

# Process: Fuzzy Overlay
tempEnvironment0 = arcpy.env.extent
arcpy.env.extent = Extent
arcpy.gp.FuzzyOverlay_sa("'';'';'';'';'';'';''", Land_Suitability, Overlay_type, "0,9")
arcpy.env.extent = tempEnvironment0

