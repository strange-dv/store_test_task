# store_test_task
Test task


*The project is just a basic data structure for applications<br>and simple endpoints to retrieve the records created, which was the main goal of the task*

### Categories endpoint:
`/categories/`<br>
(Can be used with /?name= url kwarg to define the start category)<br>
Example response:
```json
{
  "name": "First",
  "subordinate_categories": [
  {
    "name": "Second",
    "subordinate_categories": [
    {
      "name": "Third",
      "subordinate_categories": [],
      "superior_category": {
      "name": "Second"
      }
    }
    ],
    ]
    "superior_category": {
                "name": "First"
            }
        },
        {
            "name": "Second2",
            "subordinate_categories": [],
            "superior_category": {
                "name": "First"
            }
        }
    ],
    "superior_category": null
}
```

### Products endpoint:
`/products/`<br>
Example response:
```json
[
    {
        "name": "Product1",
        "category": {
            "name": "Second8"
        }
    },
    {
        "name": "Product2",
        "category": {
            "name": "Third"
        }
    }
]
```