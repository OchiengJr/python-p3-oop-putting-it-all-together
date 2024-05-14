def pytest_itemcollected(item):
    """
    Customize the display name of collected test items in pytest.
    
    This hook modifies the node ID of each test item based on the
    class-level and method-level docstrings, or their names if
    docstrings are not present.
    
    Args:
        item (pytest.Item): The collected test item.
    """
    # Get the parent (class) object and the node (test function) object
    par = getattr(item.parent, 'obj', None)
    node = getattr(item, 'obj', None)

    # Retrieve the class-level docstring or class name
    if par:
        pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    else:
        pref = ""

    # Retrieve the function-level docstring or function name
    if node:
        suf = node.__doc__.strip() if node.__doc__ else node.__name__
    else:
        suf = ""

    # Update the node ID with the formatted string if either prefix or suffix is available
    if pref or suf:
        item._nodeid = ' '.join(filter(None, [pref, suf]))

