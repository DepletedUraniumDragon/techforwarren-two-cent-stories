import json


def get_submissions(event, context):
    submissions = {"people": [
        {
            "id": 0,
            "firstName": "Frankie",
            "debt": 5000,
            "story": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ultricies, urna at egestas blandit, lectus ipsum bibendum sem, sit amet tincidunt nibh tortor ut elit. Donec luctus hendrerit odio vitae finibus. Cras auctor blandit justo, quis consectetur velit lobortis sed. Curabitur eget iaculis diam. Nullam semper, nisi quis auctor vestibulum, odio libero tempus est, at condimentum turpis nisi sed arcu. Nullam congue velit ac nibh laoreet, eu convallis tellus mollis. Ut suscipit leo sed augue aliquam vestibulum. Morbi mauris lorem, molestie vitae justo eu, auctor eleifend purus. Ut cursus velit molestie convallis ultricies. Mauris rutrum interdum ante, eget auctor tortor elementum eu. Nullam non efficitur enim. Suspendisse commodo orci a eros pharetra egestas. Pellentesque luctus posuere tellus in pharetra.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ultricies, urna at egestas blandit, lectus ipsum bibendum sem, sit amet tincidunt nibh tortor ut elit. Donec luctus hendrerit odio vitae finibus. Cras auctor blandit justo, quis consectetur velit lobortis sed. Curabitur eget iaculis diam. Nullam semper, nisi quis auctor vestibulum, odio libero tempus est, at condimentum turpis nisi sed arcu. Nullam congue velit ac nibh laoreet, eu convallis tellus mollis. Ut suscipit leo sed augue aliquam vestibulum. Morbi mauris lorem, molestie vitae justo eu, auctor eleifend purus. Ut cursus velit molestie convallis ultricies. Mauris rutrum interdum ante, eget auctor tortor elementum eu. Nullam non efficitur enim. Suspendisse commodo orci a eros pharetra egestas. Pellentesque luctus posuere tellus in pharetra."
        }, {
            "id": 1,
            "firstName": "Jason",
            "debt": 150000,
            "story": "Aliquam porta consequat mollis. Pellentesque tristique elementum libero sed auctor. In hac habitasse platea dictumst. Morbi consectetur massa arcu, eu sodales tellus tincidunt sed. In hac habitasse platea dictumst. Mauris id lacus consequat, pellentesque orci vitae, egestas ante. In bibendum scelerisque nunc ac posuere. Duis ut nunc id ipsum tincidunt luctus sed at sapien."
        }, {
            "id": 2,
            "firstName": "Amy",
            "debt": 30000,
            "story": ""
        }, {
            "id": 3,
            "firstName": "Jess",
            "debt": 1000,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus,sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 4,
            "firstName": "Colton",
            "debt": 45000,
            "story": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ultricies, urna at egestas blandit, lectus ipsum bibendum sem, sit amet tincidunt nibh toscipit leo sed augue aliquam vestibulum. Morbi mauris lorem, molestie vitae justo eu, auctor eleifend purus. Ut cursus velit molestie convallis ultricies. Mauris rutrum interdum ante, eget auctor tortor elementum eu. Nullam non efficitur enim. Suspendisse commodo orci a eros pharetra egestas. Pellentesque luctus posuere tellus in pharetra."
        }, {
            "id": 5,
            "firstName": "Sandra",
            "debt": 135000,
            "story": "Aliquam porta consequat mollis. Pellentesque tristique elementum libero sed auctor. In hac habitasse platea dictumst. Morbi consectetur massa arcu, eu sodales tellus tincidunt sed. In hac habitasse platea dictumst. Mauris id lacus consequat, pellentesque orci vitae, egestas ante. In bibendum scelerisque nunc ac posuere. Duis ut nunc id ipsum tincidunt luctus sed at sapien."
        }, {
            "id": 6,
            "firstName": "Joe",
            "debt": 37000,
            "story": ""
        }, {
            "id": 7,
            "firstName": "Linda",
            "debt": 123000,
            "story": "Pellt consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 8,
            "firstName": "Terrence",
            "debt": 52000,
            "story": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ultricies, urna at egestas blandit, lectus ipsum bibendum sem, sit amet tincidunt nibh tortor ut elit. Donec luctus hendrerit odio vitae finibus. Cras auctor blandit justo, quis consectetur velit lobortis sed. Curabitur eget iaculis diam. Nullam semper, nisia."
        }, {
            "id": 9,
            "firstName": "Jane",
            "debt": 150000,
            "story": "Aliquam porta consequat mollis. Pellentesque tristique elementum libero sed auctor. In hac habitasse platea dictumst. Morbi consectetur massa arcu, eu sodales tellus tincidunt sed. In hac habitasse platea dictumst. Mauris id lacus consequat, pellentesque orci vitae, egestas ante. In bibendum scelerisque nunc ac posuere. Duis ut nunc id ipsum tincidunt luctus sed at sapien."
        }, {
            "id": 10,
            "firstName": "Nora",
            "debt": 507793,
            "story": ""
        }, {
            "id": 11,
            "firstName": "Wallace",
            "debt": 13000,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 12,
            "firstName": "Amber",
            "debt": 296746,
            "story": ""
        }, {
            "id": 13,
            "firstName": "Jenelle",
            "debt": 100560,
            "story": "Pellentesque consdales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 14,
            "firstName": "Emmerson",
            "debt": 100003,
            "story": "Pellentesque consecteti. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 15,
            "firstName": "Mindy",
            "debt": 70581,
            "story": "esque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursfaucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 16,
            "firstName": "Dion",
            "debt": 994290,
            "story": ""
        }, {
            "id": 17,
            "firstName": "Linnaea",
            "debt": 94493,
            "story": ""
        }, {
            "id": 18,
            "firstName": "Sherry",
            "debt": 338987,
            "story": ""
        }, {
            "id": 19,
            "firstName": "Anthony",
            "debt": 7436,
            "story": ""
        }, {
            "id": 20,
            "firstName": "Jonelle",
            "debt": 26104,
            "story": ""
        }, {
            "id": 21,
            "firstName": "Jess",
            "debt": 68796,
            "story": ""
        }, {
            "id": 22,
            "firstName": "Gladwin",
            "debt": 36899,
            "story": "s dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 23,
            "firstName": "Ginnie",
            "debt": 46260,
            "story": ""
        }, {
            "id": 24,
            "firstName": "Celinda",
            "debt": 84046,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 25,
            "firstName": "Kate",
            "debt": 1759,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 26,
            "firstName": "Ron",
            "debt": 16278,
            "story": ""
        }, {
            "id": 27,
            "firstName": "Ember",
            "debt": 54719,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 28,
            "firstName": "Tatianna",
            "debt": 26902,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eg"
        }, {
            "id": 29,
            "firstName": "Giselle",
            "debt": 55871,
            "story": ""
        }, {
            "id": 30,
            "firstName": "Laurence",
            "debt": 25735,
            "story": "Lodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 31,
            "firstName": "Ashley",
            "debt": 12796,
            "story": ""
        }, {
            "id": 32,
            "firstName": "Steve",
            "debt": 36899,
            "story": "s dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 33,
            "firstName": "Albert",
            "debt": 22260,
            "story": ""
        }, {
            "id": 34,
            "firstName": "Ry",
            "debt": 84054,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 35,
            "firstName": "Katlyn",
            "debt": 24539,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 36,
            "firstName": "Robert",
            "debt": 16278,
            "story": ""
        }, {
            "id": 37,
            "firstName": "Chase",
            "debt": 13259,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 38,
            "firstName": "Tristin",
            "debt": 69032,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eg"
        }, {
            "id": 39,
            "firstName": "Sam",
            "debt": 5171,
            "story": ""
        }, {
            "id": 40,
            "firstName": "Chad",
            "debt": 5000,
            "story": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ultricies, urna at egestas blandit, lectus ipsum bibendum sem, sit amet tincidunt nibh tortor ut elit. Donec luctus hendrerit odio vitae finibus. Cras auctor blandit justo, quis consectetur velit lobortis sed. Curabitur eget iaculis diam. Nullam semper, nisi quis auctor vestibulum, odio libero tempus est, at condimentum turpis nisi sed arcu. Nullam congue velit ac nibh laoreet, eu convallis tellus mollis. Ut suscipit leo sed augue aliquam vestibulum. Morbi mauris lorem, molestie vitae justo eu, auctor eleifend purus. Ut cursus velit molestie convallis ultricies. Mauris rutrum interdum ante, eget auctor tortor elementum eu. Nullam non efficitur enim. Suspendisse commodo orci a eros pharetra egestas. Pellentesque luctus posuere tellus in pharetra."
        }, {
            "id": 41,
            "firstName": "August",
            "debt": 150000,
            "story": "Aliquam porta consequat mollis. Pellentesque tristique elementum libero sed auctor. In hac habitasse platea dictumst. Morbi consectetur massa arcu, eu sodales tellus tincidunt sed. In  tincidunt luctus sed at sapien."
        }, {
            "id": 42,
            "firstName": "Ben",
            "debt": 30000,
            "story": ""
        }, {
            "id": 43,
            "firstName": "Lyndi",
            "debt": 1000,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet odio dles mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 44,
            "firstName": "Chantelle",
            "debt": 45000,
            "story": ""
        }, {
            "id": 45,
            "firstName": "Michael",
            "debt": 135000,
            "story": ""
        }, {
            "id": 46,
            "firstName": "Sheree",
            "debt": 37000,
            "story": ""
        }, {
            "id": 47,
            "firstName": "Janice",
            "debt": 123000,
            "story": ""
        }, {
            "id": 48,
            "firstName": "Vere",
            "debt": 52000,
            "story": ""
        }, {
            "id": 49,
            "firstName": "Nita",
            "debt": 150000,
            "story": "Aliquam porta consequat mollis. Pellentesque tristique elementum libero sed auctor. In hac habitasse platea dictumst. Morbi consectetur massa arcu, eu sodales tellus tincidunt sed. In hac habitasse platea dictumst. Mauris id lacus consequat, pellentesque orci vitae, egestas ante. In bibendum scelerisque nunc ac posuere. Duis ut nunc id ipsum tincidunt luctus sed at sapien."
        }, {
            "id": 50,
            "firstName": "Annabeth",
            "debt": 507793,
            "story": ""
        }, {
            "id": 51,
            "firstName": "Jaylah",
            "debt": 150000,
            "story": ""
        }, {
            "id": 52,
            "firstName": "Ricky",
            "debt": 30000,
            "story": ""
        }, {
            "id": 53,
            "firstName": "Everly",
            "debt": 1000,
            "story": "Pellet risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 54,
            "firstName": "Digby",
            "debt": 45000,
            "story": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ultricies, urna at egestas blandit, lectus ipsum bibendum sem, sit amet tincidunt nibh tortor ut elit. Donec luo sed augue aliquam vestibulum. Morbi mauris lorem, molestie vitae justo eu, auctor eleifend purus. Ut cursus velit molestie convallis ultricies. Mauris rutrum interdum ante, eget auctor tortor elementum eu. Nullam non efficitur enim. Suspendisse commodo orci a eros pharetra egestas. Pellentesque luctus posuere tellus in pharetra."
        }, {
            "id": 55,
            "firstName": "Jen",
            "debt": 135000,
            "story": ""
        }, {
            "id": 56,
            "firstName": "Finn",
            "debt": 37000,
            "story": ""
        }, {
            "id": 57,
            "firstName": "Isiah",
            "debt": 123000,
            "story": "Pellentesque consectetur venenatis semper. Sed viverra, massa nec molestie dignissim, neque felis vestibulum lacus, a porttitor orci sem et purus. In accumsan, augue in imperdiet consectetur, urna libero iaculis est, eget pellentesque ex lacus eget eros. Suspendisse tempor, velit quis cursus consequat, felis enim placerat risus, malesuada dictum odio dui vitae libero. Maecenas a dolor arcu. Ut egestas egestas ex, semper efficitur turpis lobortis eget. Duis augue enim, malesuada id nibh sit amet, viverra sodales mi. Proin non erat ac lacus laoreet faucibus quis at mi. Donec pellentesque lacus dui, eu mattis velit egestas quis. Phasellus sodales nisl quis tellus sodales, nec bibendum ante pulvinar. Phasellus aliquam nunc porttitor orci venenatis, vel bibendum purus sodales."
        }, {
            "id": 58,
            "firstName": "Byron",
            "debt": 52000,
            "story": ""
        }, {
            "id": 59,
            "firstName": "Claribel",
            "debt": 150000,
            "story": ""
        }, {
            "id": 60,
            "firstName": "Ryan",
            "debt": 507793,
            "story": "asdf"
        }
    ]}

    return {
        "statusCode": 200,
        "body": json.dumps(submissions)
    }


def hello(event, context):
    body = {
        "message": "We did it!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "headers": {'x-custom-header': 'My Header Value'},
        # "body": json.dumps(body)
        "body": json.dumps(body)
    }

    return response


def goodbye(event, context):
    response = {
        "statusCode": 200,
        "headers": {'x-custom-header': 'My Header Value'},
        # "body": json.dumps(body)
        "body": json.dumps("goodbye")
    }

    return response
