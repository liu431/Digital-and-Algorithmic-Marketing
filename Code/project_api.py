#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Created on March 21 2020

@author: LI LIU, SURESH GOVINDARAJ, XI ZHAO
"""
import numpy as np
import pandas as pd
import sys


# In[10]:


def recommend_restaurant(latitude, longitude):
    XX = pd.read_csv("user_features.csv")
    restaurants = pd.read_csv("restaurants.csv")
    
    loc = [float(latitude), float(longitude)]
    restaurants['distance'] = np.sqrt((restaurants['latitude'] - loc[0])**2 + (restaurants['longitude'] - loc[1])**2)
    restaurants['distance_walking'] = abs(restaurants['latitude'] - loc[0]) + abs(restaurants['longitude'] - loc[1])
    restaurants['walking_minutes'] = restaurants['distance_walking']*10


    def similarity(restaurants, **kwargs):
        score = 0

        for feature in kwargs:
            score += (restaurants[feature]-kwargs[feature])**2

        return score

    restaurants['similarity'] = restaurants.apply(similarity, popular = 1, gender = 0.33, 
                                              weekend = 1, vegan = 1, kid = 1, group = 1, Ameri = 0.33,
                                              Europ = 0.67, SouAM = 0.33, Asian = 0.67, Indian = 0.67, 
                                              Chinese = 0.67, MidEas = 0.33, Drinks = 0.33, axis=1)
    
    restaurants['utility_reweighted'] = restaurants['utility']/restaurants['similarity']
    
    rank = restaurants.sort_values(by='utility_reweighted', ascending = False)[['name', 'address', 'similarity',
                                                                    'utility_reweighted', 'distance',
                                                                            'walking_minutes']].head(10)
    rank.index = pd.Index([int(i) for i in np.linspace(1, 10, 10)])
    
    print(rank)
    return rank.round(2)


# In[11]:


if __name__ == "__main__": 

    recommend_restaurant(float(sys.argv[1]), float(sys.argv[1]))

