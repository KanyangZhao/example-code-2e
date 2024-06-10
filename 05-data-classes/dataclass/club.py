from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
    #field 用于指定字段的默认值和其他属性

