# Digital-and-Algorithmic-Marketing

### Group project: Recommending restaurants for groups

### Members

Li Liu 

Suresh Govindaraj 

Xi Zhao

### Model

A group of people wanted to have an amazing restaurant dining experience in Las Vegas. Some of them were attracted by a French restaurant 30 min away. Some of them thought the nearby sushi place was good enough. They opened Yelp and set the filters. But it didn't help them decide because the app showed each of them very different results.

Here comes our system. We want to help them decide which ones work best for them all.

Using our utility maximization framework, our system recommends the restaurants that will most likely maximize their total utilities.

Suppose we have three people: A, B, C are choosing from N restaurants (R indicates restaurants factors).

For each restaurant i (i=1...N), each person would have a utility for i: $$u_A(R_i)$$, $u_B(R_i)$, $u_C(R_i)$

We need to have a match function for predicting the total utilities from eating at this restaurant, such that $m_{R_i}(A,B,C) = U_{i}(u(R_i), R_i, Weights, Preferences)$

Our core algorithm will account for the following factors:

* Each restaurant has a baseline utility for the group (Think of $\beta_0$). We use machine learning to predict this utility by using the existing _**Yelp reviews data**_.

Then we will use _**users' input data**_ to adjust the baseline utility based on the groups' preferences and consensus ($\sum_k(\prod_m(p_m*w_m)X_k)$): 

* People have different voting weights (Ex. parents make the final decision instead of kids)

* People have own preferences (Ex. not important at all, neutral, very important)

* People care about others. The total utility depends on others' preference. If A knows B and C hate pizza, the utility for A to choose a pizza place will be lower than the case if A dining alone. 

When A, B, C open the system, they will be asked to choose their preferences for distance and cuisine types. If the factor is not important for A at all, the $p_{A}=0.1$. If the factor is neutral for A, the $p_{A}=0.5$. If the factor is very important for A, the $p_{A}=1$. Also, they have different voting weights w, $w_A, w_b, w_C$, and $w_A+w_b+w_C=1$, 

Generally, suppose we have M (m=1...M) people to choose from N (i=1...N) restaurants and the system asks them to answer K (k=1...K) questions:

$$U_{i} = \beta_0 + \beta_1X_1+ \beta_2X_2+...+\beta_kX_k+\epsilon$$
$$\hat{U_{i}}= \hat{f}(Restaurant Reputations, Weekend, Group...) + \sum_k(\prod_m(p_m*w_m)X_k)$$

Then we have scores for all restaurants from i=1 to N. We can sort them and recommend the top ones for the group.
