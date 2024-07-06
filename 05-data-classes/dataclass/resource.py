"""
Media resource description class with subset of the Dublin Core fields.

Default field values:

    >>> r = Resource('0')
    >>> r  # doctest: +NORMALIZE_WHITESPACE
    Resource(identifier='0', title='<untitled>', creators=[], date=None,
    type=<ResourceType.BOOK: 1>, description='', language='', subjects=[])

A complete resource record:
# tag::DOCTEST[]

    >>> description = 'Improving the design of existing code'
    >>> book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
    ...     ['Martin Fowler', 'Kent Beck'], date(2018, 11, 19),
    ...     ResourceType.BOOK, description, 'EN',
    ...     ['computer programming', 'OOP'])
    >>> book  # doctest: +NORMALIZE_WHITESPACE
    Resource(identifier='978-0-13-475759-9', title='Refactoring, 2nd Edition',
    creators=['Martin Fowler', 'Kent Beck'], date=datetime.date(2018, 11, 19),
    type=<ResourceType.BOOK: 1>, description='Improving the design of existing code',
    language='EN', subjects=['computer programming', 'OOP'])

# end::DOCTEST[]
"""

# tag::DATACLASS[]
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum, auto
import datetime
#from datetime import date


'''
Enum 是 Python 中的一个类,用于定义枚举(enumerations),
枚举是具有命名成员的集合。每个成员都有一个名称和一个值。
枚举在需要定义一组相关常量时非常有用，如一组状态、一组选项等。
'''

class ResourceType(Enum):  # <1> #使用 auto() 可以自动为枚举成员分配值。
    BOOK = auto()
    EBOOK = auto()
    VIDEO = auto()


@dataclass
class Resource:
    """Media resource description."""
    identifier: str                                    # <2>
    title: str = '<untitled>'                          # <3>
    creators: list[str] = field(default_factory=list)
    date: Optional[datetime.date] = None                        # <4>
    type: ResourceType = ResourceType.BOOK             # <5>
    description: str = ''
    language: str = ''
    subjects: list[str] = field(default_factory=list)
# end::DATACLASS[]


from typing import TypedDict
class ResourceDict(TypedDict):
    identifier: str
    title: str
    creators: list[str]
    date: Optional[datetime.date]
    type: ResourceType
    description: str
    language: str
    subjects: list[str]


if __name__ == '__main__':
    r = Resource('0')
    description = 'Improving the design of existing code'
    book = Resource('978-0-13-475759-9', 'Refactoring, 2nd Edition',
                    ['Martin Fowler', 'Kent Beck'], datetime.date(2018, 11, 19),
                    ResourceType.BOOK, description,
                    'EN', ['computer programming', 'OOP'])
    print(book)
    book_dict: ResourceDict = {
        'identifier': '978-0-13-475759-9',
        'title': 'Refactoring, 2nd Edition',
        'creators': ['Martin Fowler', 'Kent Beck'],
        'date': datetime.date(2018, 11, 19),
        'type': ResourceType.BOOK,
        'description': 'Improving the design of existing code',
        'language': 'EN',
        'subjects': ['computer programming', 'OOP']}
    book2 = Resource(**book_dict)
    print(book == book2)
