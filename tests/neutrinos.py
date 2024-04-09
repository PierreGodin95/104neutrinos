#!/usr/bin/env python3
import math
import sys

def aritmeticmean(recValue, mean, newValue):
    recValue = float(recValue)
    mean = float(mean)
    newValue = float(newValue)
    values = recValue * mean + newValue
    recValue += 1
    result = values / recValue
    return result

def rootmean(nbValue, root_mean, newValue):
    nbValue = float(nbValue)
    root_mean = float(root_mean)
    newValue = float(newValue)
    values = (nbValue * root_mean)**2
    nbValue += 1
    result = math.sqrt(1 / nbValue * (values + newValue))
    return result

def harmomean(nbValue, mean, newValue):
    nbValue = float(nbValue)
    mean = float(mean)
    newValue = float(newValue)
    a = nbValue / mean
    a += 1 / newValue
    nbValue += 1
    result = nbValue / a
    return result

def stand_deviation(sd, armean, new_value, nb_values):
    nb_values = float(nb_values)
    armean = float(armean)
    new_value = float(new_value)
    sd = float(sd)
    aritmetic = aritmeticmean(nb_values, armean, new_value)
    variance = sd**2
    variance *= (nb_values)
    variance += (new_value - aritmetic)**2
    variance /= (nb_values + 1)
    new_deviation = math.sqrt(variance)
    return(new_deviation)

def create_rootmean(armean, sd):
    rootmean = math.sqrt((armean**2 + sd**2))
    return(rootmean)
