# Json Differentiator
## Install Dependencies:
>`pip install -r requirements.txt`
## Usage:
>`python main.py`
```
Old Files Path >> `<enter old directory path>`  
New Files Path >> `<enter new directory path>`  
5 differences in 1.json saved to `<old directory path>\diff\<filename>.json`
```
## Example:
#### Old File
```json
{
    "fruit": "Apple",
    "size": {
        "height": "small",
        "weight": "medium"
    },
    "color": "Red"
}
```
#### New File
```json
{
    "fruit": "Banana",
    "size": {
        "height": "long",
        "weight": "medium"
    },
    "color": "Red"
}
```
#### Difference File
```json
{
    "root['fruit']": {
        "new_value": "Banana",
        "old_value": "Apple"
    },
    "root['size']['height']": {
        "new_value": "long",
        "old_value": "small"
    }
}
```