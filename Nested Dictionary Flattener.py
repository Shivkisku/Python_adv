def flatten_dictionary(d, parent_key='', sep='.'):
    flattened = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            # Recursively flatten nested dictionaries
            flattened.update(flatten_dictionary(value, new_key, sep=sep))
        else:
            flattened[new_key] = value

    return flattened

# Example usage:
nested_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

flattened_dict = flatten_dictionary(nested_dict)
print(flattened_dict)
