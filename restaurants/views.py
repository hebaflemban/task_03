from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        'my_list' : [{'restaurant_name':'Lazeez' , "food_type": 'Mediterranean cuisine'},
                     {'restaurant_name':'Laguna' , "food_type": 'Chinese cuisine'},
                     {'restaurant_name':'Aroma' , "food_type": 'Italian cuisine'},

        ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        'my_object' : { 'restaurant_name':'Lazeez' ,
                        'food_type': 'Mediterranean cuisine',
                        'Operating Hours' : ' All week 4:00 PM - 10:00 PM',
                        'Adress' : '1821 Haight St \nSan Francisco, CA 94117',
                        'Phone' : '(415) 751-1970',
                        'Affordability' : '$',
                        'Rating' : '4.5',
                        'Reviews' : {'Daniel B.':'A perfect place which looks ordinary from outside but has really amazing vibes and good feel to it',
                                     'lyn m.':'Drinks are funny and creative, such as my personal favorite, the Bitchin Camaro Dr. Pepper and Sailor Jerry'
                                     },
                        'Menue' : {'Tater Tots ':'$3',
                                    'Nachos ':'$4'}


        }

    }
    return render(request, 'detail.html', context)
