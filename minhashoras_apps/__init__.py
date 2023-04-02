__api_version__ = '0.1.0'

__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __api_version__.replace('-', '.', 1).split('.')
    ]
)
